from unittest.mock import MagicMock

import pytest

from httptest.utils.validate import Base, param_id


class DummyResponse:
	def __init__(self, status_code=200, json_data=None, elapsed_seconds=0.1):
		self.response = MagicMock()
		self.response.status_code = status_code
		self.response.json.return_value = json_data
		self.response.elapsed.total_seconds.return_value = elapsed_seconds


@pytest.fixture
def base():
	return Base()


def test_validate_status_code(base):
	base.response = DummyResponse(status_code=201)
	base.validate(status_code=201)


def test_validate_positive(base):
	base.response = DummyResponse(status_code=200)
	base.validate(case="positive")


def test_validate_negative(base):
	base.response = DummyResponse(status_code=404)
	base.validate(case="negative")


def test_validate_empty_with_lookup_key(base):
	base.response = DummyResponse(status_code=200, json_data={"items": []})
	base.validate(case="empty", lookup_key="items")


def test_validate_empty_without_lookup_key(base):
	base.response = DummyResponse(status_code=200, json_data=[])
	base.validate(case="empty")


def test_validate_value_min(base):
	base.response = DummyResponse(status_code=200)
	base.validate(case="value", filter_type="min", filter_value=5, filter_list=[5, 6, 7])


def test_validate_value_max(base):
	base.response = DummyResponse(status_code=200)
	base.validate(case="value", filter_type="max", filter_value=7, filter_list=[5, 6, 7])


def test_validate_value_equal(base):
	base.response = DummyResponse(status_code=200)
	base.validate(case="value", filter_type="equal", filter_value=3, filter_list=[3, 3, 3])


def test_validate_value_subset_single(base):
	base.response = DummyResponse(status_code=200)
	base.validate(case="value", filter_type="subset", filter_value=2, filter_list=[1, 2, 3])


def test_validate_performance(base):
	base.response = DummyResponse(status_code=200, elapsed_seconds=0.5)
	base.validate(case="performance", allowed_seconds=1)


def test_validate_invalid_case(base):
	base.response = DummyResponse(status_code=200)
	with pytest.raises(ValueError, match="Invalid case"):
		base.validate(case="invalid")


def test_validate_value_missing_filter_value(base):
	base.response = DummyResponse(status_code=200)
	with pytest.raises(ValueError, match="filter_value must be provided"):
		base.validate(case="value", filter_type="min", filter_list=[1, 2, 3])


def test_param_id_iso8601():
	param = {"start": "2024-06-01T12:34:56Z"}
	assert param_id(param) == "start_ISO8601"


def test_param_id_yyyy_mm_dd():
	param = {"date": "2024-06-01"}
	assert param_id(param) == "date_YYYY-MM-DD"


def test_param_id_regular_string():
	param = {"foo": "bar"}
	assert param_id(param) == "foo_bar"


def test_param_id_int_value():
	param = {"num": 42}
	assert param_id(param) == "num_42"


def test_param_id_multiple_keys():
	param = {"date": "2024-06-01", "id": 7}
	assert param_id(param) == "date_YYYY-MM-DD_id_7"


def test_param_id_mixed_types():
	param = {"start": "2024-06-01T12:34:56Z", "count": 3, "desc": "test"}
	assert param_id(param) == "start_ISO8601_count_3_desc_test"
