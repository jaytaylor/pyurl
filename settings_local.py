# Begin Pyurl-specific configuration

SITE_BASE_URL = 'http://pyurl.us'

MAX_PATH_LEN = 2068

MIN_HASH_LEN = 2
MAX_HASH_LEN = 8

MAX_HASH_COLLISIONS_ALLOWED = 10

VALIDATE_TARGET_LINKS = True

# Allow users to request a custom hash code?
#ALLOW_CUSTOM_HASH = False
ALLOW_CUSTOM_HASH = True

# If True, then hash requests exceeding the MAX_HASH_LEN will be truncated.
# If False, then hash requests exceeding the MAX_HASH_LEN will be ignored.
TRUNC_LONG_HASH_REQUESTS = True

VALID_HASH_CHARS = 'a-zA-Z0-9'

PREVIEW_WIDTH = 320
#PREVIEW_HEIGHT = 480

# End Pyurl-specific configuration
