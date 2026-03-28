import unittest
from unittest.mock import Mock, patch

import pytest
from utils import percentile

from tests.test_load.load_test import make_request, run_load_test


def test_percentile_empty():
	assert percentile([], 50) is None


def test_percentile_single_value():
	assert percentile([42], 50) == 42


def test_percentile_typical():
	data = [1, 2, 3, 4, 5]
	assert percentile(data, 0) == 1
	assert percentile(data, 50) == 3
	assert percentile(data, 100) == 5


def test_percentile_float_percent():
	data = [10, 20, 30, 40]
	assert pytest.approx(percentile(data, 25), 0.01) == 17.5
	assert pytest.approx(percentile(data, 75), 0.01) == 32.5


def test_percentile_unsorted():
	data = [5, 1, 3, 2, 4]
	assert percentile(data, 50) == 3


def test_percentile_non_integer():
	data = [1, 2, 3]
	assert pytest.approx(percentile(data, 33.3), 0.01) == 1.666


class TestLoad(unittest.TestCase):
	def test_make_request(self):
		# Mock response object
		mock_response = Mock()
		mock_response.response.request.url = "http://test/api"
		mock_response.response.status_code = 200

		# Mock endpoint to return the mock response
		mock_endpoint = Mock(return_value=mock_response)
		params = {}

		url, status, elapsed = make_request(mock_endpoint, params)

		assert url == "http://test/api"
		assert status == 200
		assert isinstance(elapsed, float)

	@patch("tests.test_load.load_test.make_request")
	def test_run_load_test_basic(self, mock_make_request):
		# Mock make_request to return a successful response
		mock_make_request.return_value = ("http://test/api", 200, 1)
		mock_endpoint = Mock()
		params_list = [{}]
		concurrency = 1
		duration = 0.1  # 10  millisecond

		# Run the load test (output will print, but we just check it runs)
		run_load_test(mock_endpoint, params_list, concurrency, duration)

		# Ensure make_request was called at least once
		assert mock_make_request.called
