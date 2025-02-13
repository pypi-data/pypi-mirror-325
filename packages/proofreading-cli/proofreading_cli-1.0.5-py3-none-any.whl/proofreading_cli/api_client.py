import json
import os
from http import HTTPStatus
from typing import Dict

import pandas as pd
import requests
from proofreading_cli.config import Config
from proofreading_cli.constants import GC_API_KEY_ENV, GREEN, RED, RESET
from proofreading_cli.mapper import map_hit_item
from tenacity import retry, stop_after_attempt, wait_fixed


class ApiClient:
    def __init__(self, config: Config, debug: bool):
        self.endpoint = config.proofreading.api.hit
        self.api_key = os.getenv(GC_API_KEY_ENV)
        self.headers = {
            "accept": "text/plain",
        }
        self.timeout = config.proofreading.api.timeout
        self.page_size = config.proofreading.api.page_size
        self.debug = debug

    @retry(
        stop=stop_after_attempt(2),
        wait=wait_fixed(1),
    )
    def get_hits_by_date(self, params: Dict[str, str]) -> pd.DataFrame:
        page_index = 0
        all_hits = []

        while True:
            request_params = {
                "Paging.PageIndex": page_index,
                "Paging.PageSize": self.page_size,
                "HitFilters.ProofreadingStatuses": params["statuses"],
                "HitFilters.IsSubmitted": params["is-submitted"],
                "HitDateFilters.DateTimeType": params["date-type"],
                "HitDateFilters.StartDate": params["start-date"],
                "HitDateFilters.EndDate": params["end-date"],
                "apikey": self.api_key,
            }

            if self.debug:
                print(f"{GREEN}\nRequest Parameters:")
                print(f"{GREEN}{json.dumps(request_params, indent=4)}{RESET}")

            try:
                response = requests.get(
                    f"{self.endpoint}/get-by-date-range",
                    headers=self.headers,
                    params=request_params,
                    timeout=self.timeout,
                )

                if response.status_code == HTTPStatus.OK:
                    hits = response.json().get("items", [])
                    if not hits:
                        break

                    all_hits.extend(map_hit_item(item) for item in hits)
                else:
                    response.raise_for_status()

            except requests.exceptions.Timeout:
                print(
                    f"\n{RED}Request timed out for page_index={page_index}! Skipping this page.{RESET}"
                )
            except requests.exceptions.ConnectionError:
                print(
                    f"\n{RED}Connection error occurred for page_index={page_index}! Skipping this page.{RESET}"
                )
            except requests.exceptions.RequestException as e:
                print(
                    f"\n{RED}Request error for page_index={page_index}: {e}! Skipping this page.{RESET}"
                )
            except (ValueError, KeyError, TypeError) as e:
                print(
                    f"\n{RED}Response parsing error for page_index={page_index}: {e}! Skipping this page.{RESET}"
                )

            finally:
                page_index += 1

        return pd.DataFrame(all_hits)

    @retry(
        stop=stop_after_attempt(2),
        wait=wait_fixed(1),
    )
    def get_hits_by_page(self, params: Dict[str, str]) -> pd.DataFrame:
        params = {
            "Paging.PageIndex": params["page_index"],
            "Paging.PageSize": params["page_size"],
            "HitFilters.ProofreadingStatuses": params["statuses"],
            "HitFilters.IsSubmitted": params["is_submited"],
            "apikey": self.api_key,
        }

        try:
            response = requests.get(
                self.endpoint,
                headers=self.headers,
                params=params,
                timeout=self.timeout,
            )

            if response.status_code == HTTPStatus.OK:
                hits = response.json().get("items", [])
                data = [map_hit_item(item) for item in hits]
                return pd.DataFrame(data)
            else:
                response.raise_for_status()

        except requests.exceptions.Timeout:
            print(f"Request timed out while fetching hits with params {params}.")
            raise

        except requests.exceptions.ConnectionError:
            print("Connection error occurred while fetching hits.")
            raise

        except requests.exceptions.RequestException as e:
            print(f"Request error: {e}.")
            raise

        except (ValueError, KeyError, TypeError) as e:
            print(f"Response parsing error: {e}.")
            raise
