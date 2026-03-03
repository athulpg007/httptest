import pytest

from httptest.endpoints.the_internet import (
	GetBasicAuth,
	GetStatusCode,
)
from httptest.utils.validate import Base, param_id
from params.the_internet import (
	get_basic_auth_negative_params,
	get_basic_auth_params,
	get_status_code_params,
)


class TestGetStatusCode(Base):
	@pytest.mark.parametrize("params", get_status_code_params, ids=param_id)
	def test_get_status_code(self, params):
		self.response = GetStatusCode(**params)
		self.validate(status_code=params["status_code"])


class TestGetBasicAuth(Base):
	@pytest.mark.parametrize("params", get_basic_auth_params, ids=param_id)
	def test_get_basic_auth_success(self, params):
		self.response = GetBasicAuth(**params)
		self.validate(status_code=200)

	@pytest.mark.parametrize("params", get_basic_auth_negative_params, ids=param_id)
	def test_get_basic_auth_failure(self, params):
		self.response = GetBasicAuth(**params)
		self.validate(status_code=401)
