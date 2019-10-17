import json
import unittest
import requests
from parameterized import parameterized

import app
from api.Login_api import Login


def MyJson():
    list1 = []
    with open(app.URl + "/date/data.json", "r", encoding="utf-8") as f:
        msg = json.load(f)
        for i in msg.values():
            list1.append((i.get("username"),
                          i.get("password"),
                          i.get("verify_code"),
                          i.get("status"),
                          i.get("msg")))
    print(list1)
    return list1


class TPShopLogin(unittest.TestCase):
    def setUp(self):
        self.session = requests.Session()
        self.login = Login()

    def tearDown(self):
        self.session.close()

    @parameterized.expand(MyJson())
    def testLogin(self, name, pwd, code,status,msg):
        self.login.get_code(self.session)
        response = self.login.get_login(self.session, name, pwd, code)
        s = response.json().get("status")
        m = response.json().get("msg")

        self.assertEqual(status,s)
        self.assertIn(msg,m)


