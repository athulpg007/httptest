"""
Base class for making API requests.
"""

import logging
import os
from time import sleep

import requests

from config import env, settings

logging.basicConfig(level=logging.INFO)


class Endpoint:
	"""
	Base class for making API requests. All endpoints inherit from this base class.
	Provides methods for GET, PUT, POST, and DELETE requests.
	"""

	access_key = os.environ.get("API_ACCESS_KEY", None)
	secret_key = os.environ.get("API_SECRET_KEY", None)

	timeout = settings.REQUEST_TIMEOUT

	auth = False

	base_url = None
	headers = {}

	if env.ADD_MORE_HEADERS and env.ADDITIONAL_HEADERS is not None:
		additional_headers = env.ADDITIONAL_HEADERS.split(",")
		for header in additional_headers:
			key, value = header.split(":")
			headers[key.strip()] = value.strip()

	url = None
	param_keys = []
	param_values = []
	params = {}
	data = {}
	file = None
	response = None
	json = None

	def add_auth(self, mode: str = None) -> None:
		if mode == "BASIC_AUTH":
			assert self.access_key is not None, "API_ACCESS_KEY environment variable must be set for BASIC_AUTH mode."
			assert self.secret_key is not None, "API_SECRET_KEY environment variable must be set for BASIC_AUTH mode."
			self.headers = {
				"Authorization": "basic " + self.access_key + ":" + self.secret_key,
				"User-Agent": "custom-user-agent",
			}
		else:
			self.headers = {
				"User-Agent": "custom-user-agent",
			}

	@staticmethod
	def build_params(param_keys: list[str], param_values: list[str | float]) -> dict:
		"""
		Returns a dictionary of param_keys and param_values, excluding items where the value is None.
		"""
		return {k: v for k, v in zip(param_keys, param_values, strict=True) if v is not None}

	def generate_params(self, data: bool = False) -> None:
		"""
		Generates a dictionary of parameters from the param_keys and param_values lists.
		:param data: bool - If True, generates self.data; otherwise, generates self.params, default = False.
		:return: None
		"""
		if data:
			self.data = self.build_params(self.param_keys, self.param_values)
			return
		self.params = self.build_params(self.param_keys, self.param_values)

	def get(self, url: str, params: dict = None, data: dict = None) -> requests.Response:
		logging.info(f" GET: {url}")
		if params:
			logging.info(f"params: {params}")
		logging.info("")
		return requests.get(url=url, headers=self.headers, params=params, data=data, timeout=self.timeout)

	def put(
		self,
		url: str,
		params: dict = None,
		data: dict | str | bytes | None = None,
		files: dict = None,
		json: dict = None,
		cookies: dict = None,
	) -> requests.Response | None:
		logging.info(f" PUT: {url}")
		if data or json:
			logging.info(f"data: {self.data}")
		logging.info("")
		return requests.put(
			url=url,
			headers=self.headers,
			params=params,
			data=data,
			files=files,
			json=json,
			cookies=cookies,
			timeout=self.timeout,
		)

	def post(
		self,
		url: str,
		params: dict = None,
		data: dict | str | bytes | None = None,
		files: dict = None,
		json: dict = None,
		cookies: dict = None,
	) -> requests.Response | None:
		logging.info(f" POST: {url}")
		if data or json:
			logging.info(f"data: {self.data}")
		if files:
			logging.info(f"file: {self.file}")
		logging.info("")
		return requests.post(
			url=url,
			headers=self.headers,
			params=params,
			data=data,
			files=files,
			json=json,
			cookies=cookies,
			timeout=self.timeout,
		)

	def patch(
		self,
		url: str,
		params: dict = None,
		data: dict | str | bytes | None = None,
		files: dict = None,
		json: dict = None,
		cookies: dict = None,
	) -> requests.Response | None:
		logging.info(f" PATCH: {url}")
		if data or json:
			logging.info(f"data: {self.data}")
		if files:
			logging.info(f"file: {self.file}")
		logging.info("")
		return requests.patch(
			url=url,
			headers=self.headers,
			params=params,
			data=data,
			files=files,
			json=json,
			cookies=cookies,
			timeout=self.timeout,
		)

	def delete(
		self,
		url: str,
		params: dict = None,
		data: dict | str | None = None,
		json: dict | None = None,
		files: dict = None,
	) -> requests.Response | None:
		logging.info(f" DELETE: {url}")
		logging.info("")
		if data or json:
			logging.info(f"data: {self.data}")
		return requests.delete(
			url=url, headers=self.headers, params=params, data=data, json=json, files=files, timeout=self.timeout
		)

	def retry_on_failure(
		self,
		status_code: int,
		retry_delay: float | None = 2,
		max_retries: int | None = 3,
	) -> bool:
		"""
		Automatically retry GET request on failure for a known error, e.g. 500.
		Must be called after the self.response is set by an initial GET request.

		:param status_code: int, the status code to retry on
		:param retry_delay: float, delay between retries in seconds
		:param max_retries: int, maximum number of retries
		:return: bool, True if a successful response (status code 200) is received within max_retries, else False
		"""

		retries = 0
		assert self.response is not None, (
			"retry_on_failure() must be called after an initial GET request that sets self.response."
		)
		while self.response.status_code == status_code and retries < max_retries:
			retries += 1
			logging.warning(f"Received status code: {self.response.status_code}. Retrying {retries}/{max_retries}...")
			self.response = self.get(url=self.url, params=self.params)
			if self.response.status_code == 200:
				return True
			sleep(retry_delay)
		return False
