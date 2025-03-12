import bcrypt

class Cryptor:
    def __init__(self):
        pass

    def enc_pw(self, pw):
        salt = bcrypt.gensalt()
        hashed_password = bcrypt.hashpw(pw.encode('utf-8'), salt)
        return hashed_password

    def check_pw(self, user_pw, server_pw):
        return bcrypt.checkpw(user_pw.encode('utf-8'), server_pw)


#ct = Cryptor()

#print(ct.pw_enc("1234"))