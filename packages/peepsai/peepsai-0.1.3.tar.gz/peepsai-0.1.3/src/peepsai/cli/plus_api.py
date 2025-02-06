from os import getenv
from typing import Optional
from urllib.parse import urljoin

import requests

from peepsai.cli.version import get_peepsai_version


class PlusAPI:
    """
    This class exposes methods for working with the PeepsAI+ API.
    """

    TOOLS_RESOURCE = "/peepsai_plus/api/v1/tools"
    PEEPSS_RESOURCE = "/peepsai_plus/api/v1/peepz"

    def __init__(self, api_key: str) -> None:
        self.api_key = api_key
        self.headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
            "User-Agent": f"PeepsAI-CLI/{get_peepsai_version()}",
            "X-Peepsai-Version": get_peepsai_version(),
        }
        self.base_url = getenv("PEEPSAI_BASE_URL", "https://app.peepsai.io")

    def _make_request(self, method: str, endpoint: str, **kwargs) -> requests.Response:
        url = urljoin(self.base_url, endpoint)
        session = requests.Session()
        session.trust_env = False
        return session.request(method, url, headers=self.headers, **kwargs)

    def login_to_tool_repository(self):
        return self._make_request("POST", f"{self.TOOLS_RESOURCE}/login")

    def get_tool(self, handle: str):
        return self._make_request("GET", f"{self.TOOLS_RESOURCE}/{handle}")

    def publish_tool(
        self,
        handle: str,
        is_public: bool,
        version: str,
        description: Optional[str],
        encoded_file: str,
    ):
        params = {
            "handle": handle,
            "public": is_public,
            "version": version,
            "file": encoded_file,
            "description": description,
        }
        return self._make_request("POST", f"{self.TOOLS_RESOURCE}", json=params)

    def deploy_by_name(self, project_name: str) -> requests.Response:
        return self._make_request(
            "POST", f"{self.PEEPSS_RESOURCE}/by-name/{project_name}/deploy"
        )

    def deploy_by_uuid(self, uuid: str) -> requests.Response:
        return self._make_request("POST", f"{self.PEEPSS_RESOURCE}/{uuid}/deploy")

    def peeps_status_by_name(self, project_name: str) -> requests.Response:
        return self._make_request(
            "GET", f"{self.PEEPSS_RESOURCE}/by-name/{project_name}/status"
        )

    def peeps_status_by_uuid(self, uuid: str) -> requests.Response:
        return self._make_request("GET", f"{self.PEEPSS_RESOURCE}/{uuid}/status")

    def peeps_by_name(
        self, project_name: str, log_type: str = "deployment"
    ) -> requests.Response:
        return self._make_request(
            "GET", f"{self.PEEPSS_RESOURCE}/by-name/{project_name}/logs/{log_type}"
        )

    def peeps_by_uuid(
        self, uuid: str, log_type: str = "deployment"
    ) -> requests.Response:
        return self._make_request(
            "GET", f"{self.PEEPSS_RESOURCE}/{uuid}/logs/{log_type}"
        )

    def delete_peeps_by_name(self, project_name: str) -> requests.Response:
        return self._make_request(
            "DELETE", f"{self.PEEPSS_RESOURCE}/by-name/{project_name}"
        )

    def delete_peeps_by_uuid(self, uuid: str) -> requests.Response:
        return self._make_request("DELETE", f"{self.PEEPSS_RESOURCE}/{uuid}")

    def list_peepz(self) -> requests.Response:
        return self._make_request("GET", self.PEEPSS_RESOURCE)

    def create_peeps(self, payload) -> requests.Response:
        return self._make_request("POST", self.PEEPSS_RESOURCE, json=payload)
