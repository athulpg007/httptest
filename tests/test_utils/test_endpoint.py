from unittest import mock

from httptest.endpoint import Endpoint


@mock.patch("httptest.endpoint.requests.get")
def test_get_method(mock_get):
	ep = Endpoint()
	ep.get("http://test", params={"a": 1})
	mock_get.assert_called_once()


def test_build_params_static():
	result = Endpoint.build_params(["a", "b"], [1, None])
	assert result == {"a": 1}


def test_generate_params_sets_params():
	ep = Endpoint()
	ep.param_keys = ["x", "y"]
	ep.param_values = [1, 2]
	ep.generate_params()
	assert ep.params == {"x": 1, "y": 2}
	ep.generate_params(data=True)
	assert ep.data == {"x": 1, "y": 2}


def test_retry_on_failure():
	ep = Endpoint()
	ep.response = mock.Mock()

	# test retry logic, simulate 500 failures
	ep.response.status_code = 500
	with mock.patch.object(ep, "get", return_value=mock.Mock(status_code=500)) as mock_get:
		result = ep.retry_on_failure(status_code=500, retry_delay=0.01, max_retries=3)
		assert result is False
		assert mock_get.call_count == 3  # Retries 3 times

	ep.response.status_code = 200
	with mock.patch.object(ep, "get", return_value=mock.Mock(status_code=200)) as mock_get:
		result = ep.retry_on_failure(status_code=200, retry_delay=0.01, max_retries=3)
		assert result is True
		assert mock_get.call_count == 1  # Succeeds on first retry
