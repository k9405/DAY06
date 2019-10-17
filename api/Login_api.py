import app


class Login:
    def get_code(self, session):
        return session.get(app.login_URL + "index.php?m=Home&c=User&a=verify")

    def get_login(self, session, username, password, code):
        MyDate = {"username": username,
                  "password": password,
                  "verify_code": code}
        return session.post(app.login_URL + "index.php?m=Home&c=User&a=do_login", data=MyDate)
