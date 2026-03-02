"""
Example load test script.

This script can run load test on any API endpoint using concurrent requests.
You can choose the endpoint, parameters, concurrency level, and duration of the test.

"""

from load_test import run_load_test

from httptest.endpoints.jsonplaceholder import GetPost
from params.jsonplaceholder import get_post_params

if __name__ == "__main__":
	run_load_test(endpoint=GetPost, params_list=get_post_params, concurrency=5, duration=5)
