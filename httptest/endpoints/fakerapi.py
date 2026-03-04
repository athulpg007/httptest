"""Endpoints for the FakerAPI service."""

from httptest.endpoint import Endpoint

BASE_URL = "https://fakerapi.it/api/v2"


class GetAddress(Endpoint):
	"""
	Endpoint for fetching a random address from FakerAPI.
	"""

	def __init__(self, locale: str = None, quantity: int = None, country_code: str = None) -> None:
		"""
		:param locale: str
		:param quantity: int
		:param country_code: str
		"""
		self.locale = locale
		self.quantity = quantity
		self.country_code = country_code

		self.param_keys = ["_locale", "_quantity"]
		self.param_values = [self.locale, self.quantity]
		self.generate_params()

		self.url = f"{BASE_URL}/addresses"
		self.response = self.get(url=self.url, params=self.params)


class GetProducts(Endpoint):
	"""
	Endpoint for fetching a random product from FakerAPI.
	"""

	def __init__(
		self, locale: str = None, quantity: int = None, price_min: float = None, price_max: float = None
	) -> None:
		"""
		:param locale: str
		:param quantity: int
		"""
		self.locale = locale
		self.quantity = quantity
		self.price_min = price_min
		self.price_max = price_max

		self.param_keys = ["_locale", "_quantity", "_price_min", "_price_max"]
		self.param_values = [self.locale, self.quantity, self.price_min, self.price_max]
		self.generate_params()

		self.url = f"{BASE_URL}/products"
		self.response = self.get(url=self.url, params=self.params)
