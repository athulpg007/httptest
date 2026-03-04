import pytest

from httptest.endpoints.fakerapi import (
	GetAddress,
	GetProducts,
)
from httptest.utils.validate import Base, param_id
from params.fakerapi import (
	get_address_country_filter_params,
	get_address_params,
	get_products_max_price_params,
	get_products_min_price_params,
	get_products_params,
)


class TestGetAddress(Base):
	@pytest.mark.parametrize("params", get_address_params, ids=param_id)
	def test_get_address(self, params):
		self.response = GetAddress(**params)
		self.validate()

	@pytest.mark.parametrize("params", get_address_country_filter_params, ids=param_id)
	def test_get_address_country_filter(self, params):
		self.response = GetAddress(**params)
		filter_value = params["country_code"]
		filter_list = [item["country"] for item in self.response.response.json()["data"]]
		self.validate(filter_type="equal", filter_value=filter_value, filter_list=filter_list)


class TestGetProducts(Base):
	@pytest.mark.parametrize("params", get_products_params, ids=param_id)
	def test_get_products(self, params):
		self.response = GetProducts(**params)
		self.validate()

	@pytest.mark.parametrize("params", get_products_min_price_params, ids=param_id)
	def test_get_products_min_price_filter(self, params):
		self.response = GetProducts(**params)
		filter_value = params["price_min"]
		filter_list = [item["price"] for item in self.response.response.json()["data"]]
		self.validate(filter_type="min", filter_value=filter_value, filter_list=filter_list)

	@pytest.mark.parametrize("params", get_products_max_price_params, ids=param_id)
	def test_get_products_max_price_filter(self, params):
		self.response = GetProducts(**params)
		filter_value = params["price_max"]
		filter_list = [item["price"] for item in self.response.response.json()["data"]]
		self.validate(filter_type="max", filter_value=filter_value, filter_list=filter_list)
