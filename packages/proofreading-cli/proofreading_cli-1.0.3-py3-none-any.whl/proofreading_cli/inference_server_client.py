import json
import os
from concurrent.futures import ThreadPoolExecutor
from typing import Any, Tuple

import pandas as pd
import requests
from proofreading_cli.config import Config
from proofreading_cli.constants import (
    INFERENCE_SERVER_API_KEY,
    MODEL_VERSION_1,
    MODEL_VERSION_2,
)


class InferenceServerClient:
    def __init__(self, config: Config):
        self.model_1_endpoint = config.proofreading.inference.endpoint.model_1
        self.model_2_endpoint = config.proofreading.inference.endpoint.model_2
        self.api_key = os.getenv(INFERENCE_SERVER_API_KEY)
        self.headers = {
            "Content-Type": "application/json",
            "API-KEY": self.api_key,
        }
        self.timeout = config.proofreading.api.timeout

    def apply_inference(
        self, dataset: pd.DataFrame, model_types: Tuple[str]
    ) -> pd.DataFrame:
        model_endpoints = {
            MODEL_VERSION_1: self.model_1_endpoint,
            MODEL_VERSION_2: self.model_2_endpoint,
        }

        for model_type in model_types:
            if model_type not in model_endpoints:
                continue

            endpoint = model_endpoints[model_type]

            with ThreadPoolExecutor() as executor:
                responses = list(
                    executor.map(
                        lambda row: self.fetch_model_response(row, endpoint),
                        (dataset.iloc[i] for i in range(len(dataset))),
                    )
                )

            dataset[f"{model_type}_label"] = [
                res.get("label", None) for res in responses
            ]
            dataset[f"{model_type}_probability"] = [
                res.get("probability", None) for res in responses
            ]

        return dataset

    def get_exact_model_version(self, model: str) -> str:
        empty_data = {
            "body": "empty",
            "headline": "empty",
            "lectorate_search_term": "empty",
            "search_dimension_name": "empty",
        }

        if model == MODEL_VERSION_2:
            response = self.fetch_model_response(
                empty_data, endpoint=self.model_2_endpoint
            )

        else:
            response = self.fetch_model_response(
                empty_data, endpoint=self.model_1_endpoint
            )

        return response["model_version"]

    def fetch_model_response(self, row: pd.Series, endpoint: str) -> Any:
        data = {
            "body": row["body"],
            "headline": row["headline"] if row["headline"] != "" else " ",
            "search_term": row["lectorate_search_term"],
            "search_dimension": row["search_dimension_name"],
        }
        try:
            response = requests.post(
                endpoint,
                headers=self.headers,
                data=json.dumps(data),
                timeout=self.timeout,
            )
            response.raise_for_status()
            return response.json()
        except requests.exceptions.JSONDecodeError:
            print(f"Invalid JSON response from endpoint: {endpoint}")
            print(f"Response content: {response.text}")
            return {"error": "Invalid JSON response"}
        except requests.exceptions.RequestException as e:
            print(f"Request failed: {e}")
            print(f"Request data: {data}")
            raise
