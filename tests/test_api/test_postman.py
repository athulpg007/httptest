import pytest

from httptest.endpoints.postman import (
	GetRequest,
	PostRequest,
	PostRequestWithFile,
)
from httptest.utils.validate import Base, param_id
from params.postman import (
	get_request_params,
	post_request_params,
	post_request_with_file_params,
)


class TestGetRequest(Base):
	@pytest.mark.parametrize("params", get_request_params, ids=param_id)
	def test_get_request(self, params):
		self.response = GetRequest(params=params)
		self.validate()

	def test_get_request_performance(self):
		self.response = GetRequest()
		self.validate(case="performance", allowed_seconds=3)


class TestPostRequest(Base):
	@pytest.mark.parametrize("data", post_request_params, ids=param_id)
	def test_post_request(self, data):
		self.response = PostRequest(data)
		self.validate()


class TestPostRequestWithFile(Base):
	@pytest.mark.parametrize("params", post_request_with_file_params, ids=param_id)
	def test_post_request_with_file(self, params):
		self.response = PostRequestWithFile(**params)
		self.validate()
