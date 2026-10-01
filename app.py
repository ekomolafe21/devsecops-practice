import hashlib
password_hash = hashlib.sha256(b'secret_password').hexdigest()
