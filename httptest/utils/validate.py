"""
Module for validating API responses in tests.
"""


def param_id(param: dict) -> str:
	"""Create descriptive IDs for pytest fixtures based on parameter key-value pairs."""
	result = []
	for k, v in param.items():
		if isinstance(v, str) and "T" in v and v.endswith("Z") and len(v) > 15:
			result.append(f"{k}_ISO8601")
		elif isinstance(v, str) and len(v) == 10 and v[4] == "-" and v[7] == "-":  # Check for YYYY-MM-DD format
			result.append(f"{k}_YYYY-MM-DD")
		else:
			result.append(f"{k}_{v}")
	return "_".join(result)


class Base:
	response = None  # response object, will be set in each test class

	def _validate_positive(self) -> None:
		assert self.response.response.status_code == 200, (
			f"Expected a 200 OK response, got {self.response.response.status_code}."
		)

	def _validate_negative(self) -> None:
		assert str(self.response.response.status_code)[0] == "4", (
			f"Expected a 4XX error, got {self.response.response.status_code}."
		)

	def _validate_empty(self, lookup_key: str | None = None) -> None:
		assert self.response.response.status_code == 200, (
			f"Expected a 200 OK response, got {self.response.response.status_code}."
		)
		if lookup_key:
			assert self.response.response.json()[lookup_key] == []
		else:
			assert self.response.response.json() == []

	def _validate_value(self, filter_type: str, filter_value: str | float, filter_list: list[str | float]) -> None:
		assert self.response.response.status_code == 200, (
			f"Expected a 200 OK response, got {self.response.response.status_code}."
		)
		assert filter_type, "Filter min, max, or equal must be provided for 'value' case."
		if not filter_value:
			raise ValueError("filter_value must be provided for 'value' case.")

		if filter_type == "min":
			assert all(value >= filter_value for value in filter_list), (
				f"Expected all values in {filter_list} to be "
				f"greater than or equal to {filter_value}.\n"
				f"Filter value: {filter_value}, found minimum value: {min(filter_list)}."
			)
		elif filter_type == "max":
			assert all(value <= filter_value for value in filter_list), (
				f"Expected all values in {filter_list} to be "
				f"less than or equal to {filter_value}.\n"
				f"Filter value: {filter_value}, found maximum value: {max(filter_list)}."
			)
		elif filter_type == "equal":
			assert all(value == filter_value for value in filter_list), (
				f"Expected all values in {filter_list} to be equal to {filter_value}."
			)
		elif filter_type == "subset":
			if isinstance(filter_value, list):
				assert set(filter_value).issubset(set(filter_list)), (
					f"Expected {filter_value} to be a subset of {filter_list}."
				)
			else:
				assert filter_value in filter_list, f"Expected {filter_value} to be in {filter_list}."

	def _validate_performance(self, allowed_seconds: float) -> None:
		if not allowed_seconds:
			raise ValueError("allowed_seconds must be provided for 'performance' case.")
		response_time = self.response.response.elapsed.total_seconds()
		assert response_time < allowed_seconds, (
			f"Expected response time <= {allowed_seconds} seconds, response took {response_time} seconds."
		)

	def validate(
		self,
		case: str = "positive",
		status_code: int | None = None,
		lookup_key: str | None = None,
		filter_type: str = None,
		filter_value: int | float | str | list[str] | None = None,
		filter_list: list[int] | list[float] | list[str] | None = None,
		allowed_seconds: int | None = None,
	) -> None:
		valid_cases = ["positive", "negative", "empty", "value", "performance"]
		if case not in valid_cases:
			raise ValueError(f"Invalid case. Must be one of {valid_cases}.")

		assert self.response is not None, "The 'response' object is not set by the test before validate() is called."

		if status_code is not None:
			assert self.response.response.status_code == status_code, (
				f"Expected status code {status_code}, got {self.response.response.status_code}."
			)
			return # If status code is specified, we only validate that and skip other checks

		if case == "positive":
			self._validate_positive()
		elif case == "negative":
			self._validate_negative()
		elif case == "empty":
			self._validate_empty(lookup_key)
		elif case == "value":
			self._validate_value(filter_type, filter_value, filter_list)
		elif case == "performance":
			self._validate_performance(allowed_seconds)
