from httptest.endpoint import Endpoint

BASE_URL = "https://echo.zuplo.io"


class GetRequest(Endpoint):
	"""
	Endpoint for sending a GET request to Zuplo Echo API.
	"""

	def __init__(self, params: dict = None) -> None:
		self.url = f"{BASE_URL}/get"
		self.response = self.get(url=self.url, params=params)
