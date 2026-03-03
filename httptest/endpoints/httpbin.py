"""Endpoints from httpbin project https://httpbin.org/."""

from httptest.endpoint import Endpoint

BASE_URL = "https://httpbin.org"


class GetStatus(Endpoint):
	"""
	Endpoint for fetching a specific status code from httpbin API.
	"""

	def __init__(self, status_code: int) -> None:
		self.url = f"{BASE_URL}/status/{status_code}"
		self.response = self.get(url=self.url)


class GetBasicAuth(Endpoint):
	"""
	Endpoint for fetching basic auth status from httpbin API.
	"""

	def __init__(self, username: str, password: str) -> None:
		self.url = f"{BASE_URL}/basic-auth/{username}/{password}"
		self.response = self.get(url=self.url, auth=(username, password))
