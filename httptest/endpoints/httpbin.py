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


class GetHeaders(Endpoint):
	"""
	Endpoint for fetching request headers from httpbin API.
	"""

	def __init__(self) -> None:
		self.url = f"{BASE_URL}/headers"
		self.response = self.get(url=self.url)


class GetIP(Endpoint):
	"""
	Endpoint for fetching client's IP address from httpbin API.
	"""

	def __init__(self) -> None:
		self.url = f"{BASE_URL}/ip"
		self.response = self.get(url=self.url)


class GetUserAgent(Endpoint):
	"""
	Endpoint for fetching client's user agent from httpbin API.
	"""

	def __init__(self) -> None:
		self.url = f"{BASE_URL}/user-agent"
		self.response = self.get(url=self.url)


class GetBase64(Endpoint):
	"""
	Endpoint for fetching base64 encoded data from httpbin API.
	"""

	def __init__(self, data: str) -> None:
		self.url = f"{BASE_URL}/base64/{data}"
		self.response = self.get(url=self.url)


class GetBytes(Endpoint):
	"""
	Endpoint for fetching a specific number of random bytes from httpbin API.
	"""

	def __init__(self, n: int) -> None:
		self.url = f"{BASE_URL}/bytes/{n}"
		self.response = self.get(url=self.url)


class GetStreamBytes(Endpoint):
	"""
	Endpoint for fetching a specific number of random bytes as a stream from httpbin API.
	"""

	def __init__(self, n: int) -> None:
		self.url = f"{BASE_URL}/stream-bytes/{n}"
		self.response = self.get(url=self.url)


class GetStream(Endpoint):
	"""
	Endpoint for fetching a stream of JSON objects from httpbin API.
	"""

	def __init__(self, n: int) -> None:
		self.url = f"{BASE_URL}/stream/{n}"
		self.response = self.get(url=self.url)


class GetDelay(Endpoint):
	"""
	Endpoint for fetching a delayed response from httpbin API.
	"""

	def __init__(self, delay: int) -> None:
		self.url = f"{BASE_URL}/delay/{delay}"
		self.response = self.get(url=self.url)


class GetUUID(Endpoint):
	"""
	Endpoint for fetching a random UUID from httpbin API.
	"""

	def __init__(self) -> None:
		self.url = f"{BASE_URL}/uuid"
		self.response = self.get(url=self.url)
