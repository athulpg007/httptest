import pytest

from httptest.endpoints.httpbin import (
	GetBase64,
	GetBasicAuth,
	GetBytes,
	GetHeaders,
	GetIP,
	GetStatus,
	GetUserAgent,
)
from httptest.utils.validate import Base, param_id
from params.httpbin import (
	get_base64_params,
	get_basic_auth_params,
	get_bytes_params,
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


class TestGetHeaders(Base):
	def test_get_headers(self):
		self.response = GetHeaders()
		self.validate()


class TestGetIP(Base):
	def test_get_ip(self):
		self.response = GetIP()
		self.validate(status_code=200)


class TestGetUserAgent(Base):
	def test_get_user_agent(self):
		self.response = GetUserAgent()
		self.validate(status_code=200)


class TestGetBase64(Base):
	@pytest.mark.parametrize("params", get_base64_params, ids=param_id)
	def test_get_base64(self, params):
		self.response = GetBase64(**params)
		self.validate(status_code=200)


class TestGetBytes(Base):
	@pytest.mark.parametrize("params", get_bytes_params, ids=param_id)
	def test_get_bytes(self, params):
		self.response = GetBytes(**params)
		self.validate(status_code=200)
