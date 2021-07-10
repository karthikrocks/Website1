try:
    from app import app
    import unittest
except Exception as e:
    print("Some Modules are missing : {}".format(e))


class FlaskTestStatus(unittest.TestCase):
    def test_status_login(self):
        tester = app.test_client(self)
        response = tester.get("/login")
        status_code = response.status_code
        self.assertEqual(status_code, 405)

    def test_status_home(self):
        tester = app.test_client(self)
        response = tester.get("/home")
        status_code = response.status_code
        self.assertEqual(status_code, 200)

    def test_status_account(self):
        tester = app.test_client(self)
        response = tester.get("/details")
        status_code = response.status_code
        self.assertEqual(status_code, 302)

    def test_status_setup(self):
        tester = app.test_client(self)
        response = tester.get("/setup")
        status_code = response.status_code
        self.assertEqual(status_code, 302)

    def test_status_email_enter(self):
        tester = app.test_client(self)
        response = tester.get("/enter_email")
        status_code = response.status_code
        self.assertEqual(status_code, 200)

    def test_status_forgot_passwd(self):
        tester = app.test_client(self)
        response = tester.get("/forgot_password")
        status_code = response.status_code
        self.assertEqual(status_code, 302)

# TODO: class TestCases with unnitest. Tests all cases.

if __name__ == "__main__":
    unittest.main()
