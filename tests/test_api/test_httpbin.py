import pytest

from httptest.endpoints.httpbin import (
	GetBasicAuth,
	GetStatus,
)
from httptest.utils.validate import Base, param_id
from params.httpbin import (
	get_basic_auth_params,
	get_status_params,
)


class TestGetStatus(Base):
	@pytest.mark.parametrize("params", get_status_params, ids=param_id)
	def test_get_status(self, params):
		self.response = GetStatus(**params)
		self.validate(status_code=params["status_code"])


class TestGetBasicAuth(Base):
	@pytest.mark.parametrize("params", get_basic_auth_params, ids=param_id)
	def test_get_basic_auth(self, params):
		self.response = GetBasicAuth(**params)
		self.validate(status_code=200)
