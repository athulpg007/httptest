import pytest

from httptest.endpoints.zuplo import (
	GetRequest,
)
from httptest.utils.validate import Base, param_id
from params.zuplo import (
	get_request_params,
)


class TestGetRequest(Base):
	@pytest.mark.parametrize("params", get_request_params, ids=param_id)
	def test_get_request(self, params):
		self.response = GetRequest(params=params)
		self.validate()
