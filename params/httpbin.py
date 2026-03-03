get_status_params = [
	{"status_code": 200},
	{"status_code": 401},
	{"status_code": 404},
	{"status_code": 500},
]

get_basic_auth_params = [
	{"username": "user", "password": "passwd"},
]

get_base64_params = [
	{"data": "SGVsbG8sIFdvcmxkIQ=="},
	{"data": "SFRUUEJJTiBpcyBhd2Vzb21l"},
]

get_bytes_params = [
	{"n": 1},
	{"n": 2},
	{"n": 16},
	{"n": 64},
]

get_bytes_stream_params = [
	{"n": 1},
	{"n": 2},
	{"n": 16},
	{"n": 64},
]

get_stream_params = [
	{"n": 1},
	{"n": 2},
	{"n": 16},
	{"n": 64},
]

get_delay_params = [
	{"delay": 0},
	{"delay": 1},
]
