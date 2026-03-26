# AGENTS.md

## Project Overview
`httptest` is a Python framework designed for writing parameterized tests for HTTP endpoints. It supports concurrent test execution within a Docker container. The framework's core revolves around the `Endpoint` class, which wraps the `requests` library and provides HTTP methods like `GET`, `POST`, `PUT`, `PATCH`, and `DELETE`.

### Key Components
- **Endpoints**: Defined as classes inheriting from `Endpoint`. Each endpoint represents an HTTP API with methods for interaction.
- **Parameterized Tests**: Test cases are parameterized using `pytest` and validated with utility functions.
- **Authentication**: Supports `BEARER_TOKEN` and `ACCESS_KEY_SECRET_KEY` authentication modes.
- **Concurrency**: Tests are optimized for I/O-bound operations and can utilize multiple CPU cores.

## Developer Workflows

### Setup
1. Clone the repository.
2. Create and activate a virtual environment:
   - Using `uv`:
     ```bash
     uv sync
     source .venv/bin/activate
     ```
   - Using `virtualenv`:
     ```bash
     python3 -m venv .venv
     source .venv/bin/activate
     pip install -r requirements.txt
     ```

### Running Tests
- Locally:
  ```bash
  pytest
  ```
- In Docker:
  ```bash
  docker compose up --build
  ```
  - Configure `NUM_CORES` in `.env` to control parallelism.

### Code Formatting and Linting
- Format and check code using `ruff`:
  ```bash
  ruff format
  ruff check
  ```

### Contribution Guidelines
- Maintain test coverage above 95%.
- Follow existing code style and conventions.
- Run tests locally or in Docker before submitting changes.

## Project-Specific Conventions

### Endpoint Definition
- Use the `Endpoint` class to define HTTP endpoints.
- Example:
  ```python
  from httptest.endpoint import Endpoint

  class GetPost(Endpoint):
      def __init__(self, post_id: int):
          self.url = f"https://example.com/posts/{post_id}"
          self.response = self.get(url=self.url)
  ```

### Parameterized Tests
- Define test parameters in `params/`.
- Example:
  ```python
  get_post_params = [
      {"post_id": 1},
      {"post_id": 2},
  ]
  ```
- Write tests using `pytest.mark.parametrize`:
  ```python
  @pytest.mark.parametrize("params", get_post_params)
  def test_get_post(self, params):
      response = GetPost(**params)
      assert response.status_code == 200
  ```

### Authentication
- Add authentication headers using `add_auth`:
  ```python
  self.add_auth(mode="BEARER_TOKEN")
  ```
- Ensure environment variables like `BEARER_TOKEN` are set.

## Key Files and Directories
- `httptest/endpoint.py`: Core `Endpoint` class.
- `httptest/endpoints/`: Predefined endpoints.
- `params/`: Parameter definitions for tests.
- `tests/`: Test cases organized by endpoint.
- `Dockerfile` and `docker-compose.yml`: Docker setup for running tests.

## External Dependencies
- **Python Libraries**: `requests`, `pytest`
- **Docker**: For containerized test execution.

## Notes for AI Agents
- Follow the patterns in `httptest/endpoints/` and `params/` for adding new endpoints and parameters.
- Use `tests/test_api/` as a reference for writing new tests.
- Ensure all contributions pass CI checks for formatting, linting, and test coverage.
