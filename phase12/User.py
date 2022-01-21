import rsa
class User:
    def __init__(self, username,email, pwd):
        self.username = username
        self.email = email
        self.pwd = pwd
        self.rsa_public, self.rsa_private = rsa.newkeys(512)
