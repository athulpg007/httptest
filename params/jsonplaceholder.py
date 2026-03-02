get_post_params = [
	{"post_id": 1},
	{"post_id": 2},
]

get_post_negative_params = [
	{"post_id": 0},
	{"post_id": -1},
	{"post_id": 101},
]

create_post_params = [
	{"title": "foo", "body": "bar", "user_id": 1},
	{"title": "Hello World", "body": "This is a test post.", "user_id": 2},
]

update_post_params = [
	{"post_id": 1, "title": "Updated Title", "body": "Updated body content.", "user_id": 1},
	{"post_id": 2, "title": "Another Update", "body": "More updated content.", "user_id": 2},
]

patch_post_params = [
	{"post_id": 1, "title": "Partially Updated Title"},
	{"post_id": 2, "body": "Partially updated body content."},
]

delete_post_params = [
	{"post_id": 1},
	{"post_id": 2},
]

delete_post_negative_params = [
	{"post_id": 0},
	{"post_id": -1},
	{"post_id": 101},
]
