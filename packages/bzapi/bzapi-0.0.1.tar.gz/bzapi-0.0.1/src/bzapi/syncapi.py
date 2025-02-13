import json
from datetime import datetime, timedelta
from functools import lru_cache
from typing import Callable

import jwt
import requests


class BaseApi(object):
    def __init__(self, auth_header_supplier: Callable[[], str]):
        self.auth_header_supplier = auth_header_supplier

    def _headers(self):
        return {"Authorization": self.auth_header_supplier()}


class BzApi(BaseApi):

    def __init__(
        self,
        auth_header_supplier: Callable[[], str],
        base_url=None,
    ):
        super().__init__(auth_header_supplier)
        self.base_url = base_url or "https://flow.boltzbit.com/bz-api"
        self.files_url = f"{self.base_url}/v1/files"
        self.streamed_chat_queries_url = f"{self.base_url}/v1/ai/streamed-chat-queries"

    def create_file(self, data, filename, params=None):
        params = params or {}
        r = requests.get(f"{self.files_url}", headers=self._headers(), params=params)
        r.raise_for_status()
        return r.json()

    def list_files(self, params=None):
        r = requests.get(f"{self.files_url}", headers=self._headers(), params=params)
        r.raise_for_status()
        return r.json()

    def fetch_file(self, file_id):
        r = requests.get(f"{self.files_url}/{file_id}", headers=self._headers())
        r.raise_for_status()
        return r.json()

    def streamed_chat_queries(self, body):
        resp = requests.post(
            self.streamed_chat_queries_url,
            json=body,
            headers=self._headers(),
            stream=True,
        )
        resp.raise_for_status()
        try:
            for line in resp.iter_lines():
                if line:
                    # SSE format: "data: {json_data}\n\n"
                    line = line.decode("utf-8")
                    if line.startswith("data: "):
                        data = line[6:]  # Remove "data: " prefix
                        yield json.loads(data)
        finally:
            resp.close()
