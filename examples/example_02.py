"""
Example 02: Fetching a single post from https://jsonplaceholder.typicode.com
"""


from httptest.endpoints.jsonplaceholder import GetPost

post = GetPost(post_id=1)
print(f"{post.url}: {post.response.status_code}")
print(f"Content: {post.response.content}")
