"""
Script to perform load testing on a given API endpoint using concurrent requests.
"""

import logging
import time
from concurrent.futures import ThreadPoolExecutor, as_completed

from utils import percentile

from httptest.utils.timedif import TimeDif


def make_request(endpoint, params: dict) -> tuple[str, int, float]:
	"""
	Make a single API request and return the URL, status code, and elapsed time.
	"""
	start = time.time()
	response = endpoint(**params)
	elapsed = time.time() - start
	return response.response.request.url, response.response.status_code, elapsed


def run_load_test(endpoint, params_list: list, concurrency: int, duration: int) -> None:
	"""
	Run a load test on the given endpoint with specified parameters, concurrency, and duration.

	:param endpoint:
	:param params_list:
	:param concurrency: number of concurrent threads
	:param duration: int, seconds
	:return:
	"""
	results = []
	elapsed_times = []
	failures = 0
	total = 0
	end_time = time.time() + duration
	start_time = time.time()
	with ThreadPoolExecutor(max_workers=concurrency) as executor:
		while time.time() < end_time:
			futures = [executor.submit(make_request, endpoint, params) for params in params_list]
			for future in as_completed(futures):
				url, status, elapsed = future.result()
				results.append((status, elapsed))
				elapsed_times.append(elapsed)
				total += 1
				if status != 200:
					failures += 1
				logging.info(
					f"{TimeDif().iso()} {url[:120]}{'...' if len(url) > 120 else ''}: {status}, elapsed: {elapsed:.2f}s"
				)

	total_time = time.time() - start_time
	if elapsed_times:
		p50 = percentile(elapsed_times, 50)
		p95 = percentile(elapsed_times, 95)
		p99 = percentile(elapsed_times, 99)
		logging.info("------------------------------")
		logging.info(f"Total requests  : {total}")
		logging.info(f"Total time      : {total_time:.2f}s")
		logging.info(f"RPS    : {total / total_time:.2f}")
		logging.info("------------------------------")
		logging.info(f"Median            : {p50:.2f}s")
		logging.info(f"95th percentile   : {p95:.2f}s")
		logging.info(f"99th percentile   : {p99:.2f}s")
		logging.info("------------------------------")
	logging.info(f"Failures: {failures} / {total} ({(failures / total * 100 if total else 0):.2f}%)")
