import hashlib
AWS_SECRET_KEY = 'AKIAIOSFODNN7EXAMPLEkey12345'
password_hash = hashlib.md5(b'secret_password').hexdigest()
