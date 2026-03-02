import datetime
import re
import unittest

import pytest

from httptest.utils.timedif import TimeDif


class TestTimeDif(unittest.TestCase):
	def test_default_now(self):
		td = TimeDif()
		now = datetime.datetime.now(datetime.UTC)
		assert abs(td.now.timestamp() - now.timestamp()) <= 2

	def test_day_offset(self):
		td = TimeDif(day_offset=2)
		expected = datetime.datetime.now(datetime.UTC) + datetime.timedelta(days=2)
		assert abs(td.now.timestamp() - expected.timestamp()) <= 2

	def test_hour_minute_second_offset(self):
		td = TimeDif(hour_offset=1, minute_offset=30, second_offset=15)
		expected = datetime.datetime.now(datetime.UTC) + datetime.timedelta(hours=1, minutes=30, seconds=15)
		assert abs(td.now.timestamp() - expected.timestamp()) <= 2

	def test_microsecond_offset(self):
		td = TimeDif(microsecond_offset=500)
		expected = datetime.datetime.now(datetime.UTC) + datetime.timedelta(microseconds=500)
		assert abs(td.now.timestamp() - expected.timestamp()) <= 2

	def test_iso_format(self):
		td = TimeDif()
		iso = td.iso()
		assert re.match(r"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z", iso)

	def test_iso_format_microseconds(self):
		td = TimeDif()
		iso = td.iso(microseconds=True)
		assert re.match(r"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\.\d+Z", iso)

	def test_date(self):
		td = TimeDif()
		date = td.date()
		assert re.match(r"\d{4}-\d{2}-\d{2}", date)

	def test_parse_timestamp(self):
		ts = "2024-01-01T12:00:00Z"
		dt = TimeDif.parse_timestamp(ts)
		assert dt == datetime.datetime(2024, 1, 1, 12, 0, 0, tzinfo=datetime.UTC)

	def test_init_with_timestamp(self):
		ts = "2024-01-01T12:00:00Z"
		td = TimeDif(timestamp=ts)
		assert td.now == datetime.datetime(2024, 1, 1, 12, 0, 0, tzinfo=datetime.UTC)

	def test_invalid_timestamp(self):
		with pytest.raises(ValueError, match="Could not parse timestamp"):
			TimeDif.parse_timestamp("invalid-timestamp")


if __name__ == "__main__":
	unittest.main()
