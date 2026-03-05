import pytest

from httptest.endpoints.postman import (
	GetRequest,
)
from httptest.utils.validate import Base, param_id
from params.postman import (
	get_request_params,
)


class TestGetRequest(Base):
	@pytest.mark.parametrize("params", get_request_params, ids=param_id)
	def test_get_request(self, params):
		self.response = GetRequest(params=params)
		self.validate()

	def test_get_request_performance(self):
		self.response = GetRequest()
		self.validate(case="performance", allowed_seconds=3)
