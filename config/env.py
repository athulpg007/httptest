"""
Set up environment variables and configurations for the application.
"""

import os

TEMP_FILE_DIR = "./tmp"  # Temporary file directory for downloaded files.

# option to add more headers to the request
ADD_MORE_HEADERS = os.environ.get("ADD_MORE_HEADERS", "False").lower() == "true"

# specify additional headers in the format "key1:value1,key2:value2"
ADDITIONAL_HEADERS = os.environ.get("ADDITIONAL_HEADERS", None)
