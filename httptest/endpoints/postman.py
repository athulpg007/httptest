from httptest.endpoint import Endpoint

BASE_URL = "https://postman-echo.com"


class GetRequest(Endpoint):
	"""
	Endpoint for sending a GET request to Postman Echo API.
	"""

	def __init__(self, params: dict = None) -> None:
		self.url = f"{BASE_URL}/get"
		self.response = self.get(url=self.url, params=params)


class PostRequest(Endpoint):
	"""
	Endpoint for sending a POST request to Postman Echo API.
	"""

	def __init__(self, data: dict = None) -> None:
		self.url = f"{BASE_URL}/post"
		self.response = self.post(url=self.url, data=data)


class PostRequestWithFile(Endpoint):
	"""
	Endpoint for sending a POST request with a file to Postman Echo API.
	"""

	def __init__(self, file: bytes = None) -> None:
		self.url = f"{BASE_URL}/post"
		self.files = None
		if file:
			with open(file, "rb") as f:
				self.files = {"file": f.read()}
		self.response = self.post(url=self.url, files=self.files)
