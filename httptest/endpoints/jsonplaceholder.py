from httptest.endpoints.endpoint import Endpoint

BASE_URL = "https://jsonplaceholder.typicode.com"


class GetPosts(Endpoint):
	"""
	Endpoint for fetching posts from JSONPlaceholder API.
	"""

	def __init__(self) -> None:
		self.url = f"{BASE_URL}/posts"
		self.response = self.get(url=self.url)


class GetPost(Endpoint):
	"""
	Endpoint for fetching a single post by ID from JSONPlaceholder API.
	"""

	def __init__(self, post_id: int) -> None:
		self.url = f"{BASE_URL}/posts/{post_id}"
		self.response = self.get(url=self.url)


class GetPostComments(Endpoint):
	"""
	Endpoint for fetching comments of a specific post from JSONPlaceholder API.
	"""

	def __init__(self, post_id: int) -> None:
		self.url = f"{BASE_URL}/posts/{post_id}/comments"
		self.response = self.get(url=self.url)


class CreatePost(Endpoint):
	"""
	Endpoint for creating a new post in JSONPlaceholder API.
	"""

	def __init__(self, title: str, body: str, user_id: int) -> None:
		self.url = f"{BASE_URL}/posts"
		self.data = {"title": title, "body": body, "userId": user_id}
		self.headers["Content-Type"] = "application/json"
		self.response = self.post(url=self.url, json=self.data)


class UpdatePost(Endpoint):
	"""
	Endpoint for updating an existing post in JSONPlaceholder API.
	"""

	def __init__(self, post_id: int, title: str, body: str, user_id: int) -> None:
		self.url = f"{BASE_URL}/posts/{post_id}"
		self.data = {"id": post_id, "title": title, "body": body, "userId": user_id}
		self.headers["Content-Type"] = "application/json"
		self.response = self.put(url=self.url, json=self.data)


class PatchPost(Endpoint):
	"""
	Endpoint for partially updating an existing post in JSONPlaceholder API.
	"""

	def __init__(self, post_id: int, title: str = None, body: str = None, user_id: int = None) -> None:
		self.url = f"{BASE_URL}/posts/{post_id}"
		self.data = {}
		if title is not None:
			self.data["title"] = title
		if body is not None:
			self.data["body"] = body
		if user_id is not None:
			self.data["userId"] = user_id
		self.headers["Content-Type"] = "application/json"
		self.response = self.patch(url=self.url, json=self.data)


class DeletePost(Endpoint):
	"""
	Endpoint for deleting a post in JSONPlaceholder API.
	"""

	def __init__(self, post_id: int) -> None:
		self.url = f"{BASE_URL}/posts/{post_id}"
		self.response = self.delete(url=self.url)
