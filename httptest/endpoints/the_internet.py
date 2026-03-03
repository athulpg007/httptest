"""Endpoints from the-internet project https://the-internet.herokuapp.com/."""

from httptest.endpoint import Endpoint

BASE_URL = "https://the-internet.herokuapp.com"


class GetStatusCode(Endpoint):
	"""
	Endpoint for fetching a specific status code from the-internet API.
	"""

	def __init__(self, status_code: int) -> None:
		self.url = f"{BASE_URL}/status_codes/{status_code}"
		self.response = self.get(url=self.url)


class GetBasicAuth(Endpoint):
	"""
	Endpoint for fetching basic auth status from the-internet API.
	"""

	def __init__(self, username: str, password: str) -> None:
		self.url = f"{BASE_URL}/basic_auth"
		self.response = self.get(url=self.url, auth=(username, password))
