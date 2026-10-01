import hashlib
password_hash = hashlib.md5(b'secret_password').hexdigest()
