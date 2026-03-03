import pytest

from httptest.endpoints.httpbin import (
	GetBase64,
	GetBasicAuth,
	GetBytes,
	GetDelay,
	GetHeaders,
	GetIP,
	GetStatus,
	GetStream,
	GetStreamBytes,
	GetUserAgent,
	GetUUID,
)
from httptest.utils.validate import Base, param_id
from params.httpbin import (
	get_base64_params,
	get_basic_auth_params,
	get_bytes_params,
	get_bytes_stream_params,
	get_delay_params,
	get_status_params,
	get_stream_params,
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


class TestGetStreamBytes(Base):
	@pytest.mark.parametrize("params", get_bytes_stream_params, ids=param_id)
	def test_get_stream_bytes(self, params):
		self.response = GetStreamBytes(**params)
		self.validate(status_code=200)


class TestGetDelay(Base):
	@pytest.mark.parametrize("params", get_delay_params, ids=param_id)
	def test_get_delay(self, params):
		self.response = GetDelay(**params)
		self.validate(status_code=200)


class TestGetUUID(Base):
	def test_get_uuid(self):
		self.response = GetUUID()
		self.validate(status_code=200)


class TestGetStream(Base):
	@pytest.mark.parametrize("params", get_stream_params, ids=param_id)
	def test_get_stream(self, params):
		self.response = GetStream(**params)
		self.validate(status_code=200)
