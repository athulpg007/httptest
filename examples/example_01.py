"""
Example 01: Fetching posts from https://jsonplaceholder.typicode.com
"""

from httptest.endpoints.jsonplaceholder import GetPosts

posts = GetPosts()
print(f"{posts.url}: {posts.response.status_code}")
