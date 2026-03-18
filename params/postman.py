get_request_params = [
	{"foo1": "bar1", "foo2": "bar2"},
	{"param1": "value1", "param2": "value2", "param3": "value3"},
	{"search": "test", "limit": 10, "offset": 0},
	{"filter": "active", "sort": "asc", "page": 2},
	{"user": "john_doe", "age": 30, "country": "USA"},
	{"q": "python testing", "lang": "en", "results": 5},
	{"category": "books", "price_min": 10, "price_max": 50},
	{"status": "pending", "priority": "high", "assigned_to": "team_a"},
	{"type": "json", "format": "pretty", "indent": 4},
	{"key1": "value1", "key2": "value2", "key3": "value3", "key4": "value4"},
]

get_request_more_params = [{"post_id": x} for x in range(1, 201)]

post_request_params = [
	{"foo1": "bar1", "foo2": "bar2"},
	{"param1": "value1", "param2": "value2", "param3": "value3"},
	{"search": "test", "limit": 10, "offset": 0},
	{"filter": "active", "sort": "asc", "page": 2},
	{"user": "john_doe", "age": 30, "country": "USA"},
	{"q": "python testing", "lang": "en", "results": 5},
	{"category": "books", "price_min": 10, "price_max": 50},
	{"status": "pending", "priority": "high", "assigned_to": "team_a"},
	{"type": "json", "format": "pretty", "indent": 4},
	{"key1": "value1", "key2": "value2", "key3": "value3", "key4": "value4"},
]

post_request_more_params = [{"post_id": x} for x in range(1, 201)]

post_request_with_file_params = [
	{"file": "tmp/file.txt"},
]

get_response_headers_params = [
	{"foo1": "bar1", "foo2": "bar2"},
	{"param1": "value1", "param2": "value2", "param3": "value3"},
	{"search": "test", "limit": 10, "offset": 0},
	{"filter": "active", "sort": "asc", "page": 2},
	{"user": "john_doe", "age": 30, "country": "USA"},
	{"q": "python testing", "lang": "en", "results": 5},
	{"category": "books", "price_min": 10, "price_max": 50},
	{"status": "pending", "priority": "high", "assigned_to": "team_a"},
	{"type": "json", "format": "pretty", "indent": 4},
	{"key1": "value1", "key2": "value2", "key3": "value3", "key4": "value4"},
]
