## httptest

A simple Python requests wrapper to write tests for HTTP endpoints.

## Setup Instructions
- Clone the repository.
- You can run the tests in two ways:
  - Using a local Python virtual environment (Supported Python versions: `3.12`, `3.13`, `3.14`).
  - Using Docker (recommended).

### Setup a local Python environment

- Using `uv`
  - `uv sync`
  - `source .venv/bin/activate`
- Using `Virtualenv`
  - `python3 -m venv .venv`
  - `source .venv/bin/activate`
  - `pip install -r requirements.txt`


### Use Docker (recommended)
- To run the tests in the Docker container, run:
```
docker-compose up --build
```

#### Additional configuration
By default, the tests will use all available CPU cores. To explicitly how many cores to use, set the desired `NUM_CORES` in the `.env` file. You can set the `NUM_CORES` to a higher value than the number of available cores. For example, if you have 2 cores and you set `NUM_CORES=16`, it will create 8 workers per CPU. This is possible because all tests are independent, and are primarily I/O bound (waiting for API responses) allowing multiple workers to run on a CPU. However, setting a very high number of workers may lead to diminishing returns due to context switching overhead. For 2 cores, a value between `16` is recommended.

To continously run the tests in a loop, for example to keep sending traffic, set the `restart` policy in the `docker-compose.yml` file to `unless-stopped` (default is `no` restart).

#### Additional header values
If you need to add additional header values to the requests, use these environment variables:
```
ADD_MORE_HEADERS=True
ADDITIONAL_HEADERS="key1:value1,key2:value2"
```
```
```

## Contributing
- Run `ruff check --fix` to format the code, and fix any problems.
- Make sure to run the tests locally before committing your changes.
- The PR checks enforce a minimum code coverage of 90%.
