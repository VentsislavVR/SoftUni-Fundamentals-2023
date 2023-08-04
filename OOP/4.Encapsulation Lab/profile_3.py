class Profile:
    def __init__(self, username: str, password: str):
        self.username = username
        self.password = password

    @property
    def username(self)->str:
        return self.__username

    @username.setter
    def username(self, value)->None:
        if len(value) < 5 or len(value) > 15:
            raise ValueError("The username must be between 5 and 15 characters.")
        self.__username = value

    @property
    def password(self)->str:
        return self.__password

    @password.setter
    def password(self, value:str)->None:
        is_length_valid = len(value) >= 8
        is_upper_case_presented = len([x for x in value if x.isupper()]) > 0
        is_digit_presented = len([x for x in value if x.isdigit()]) > 0

        if is_length_valid and is_digit_presented and is_upper_case_presented:
            self.__password = value
        else:
            raise ValueError("The password must be 8 or more characters with at least 1 digit and 1 uppercase letter.")

    def __str__(self)->str:
        return f'You have a profile with username: "{self.username}" and password: {"*" * len(self.__password)}'


import unittest


class Tests(unittest.TestCase):
    def test_invalid_password(self):
        with self.assertRaises(ValueError) as ve:
            self.profile = Profile('My_username', 'My-password')
        self.assertEqual(str(ve.exception),
                         "The password must be 8 or more characters with at least 1 digit and 1 uppercase letter.")

    def test_invalid_username(self):
        with self.assertRaises(ValueError) as ve:
            self.profile = Profile('Too_long_username', 'Any')
        self.assertEqual(str(ve.exception), "The username must be between 5 and 15 characters.")

    def test_correct_profile(self):
        self.profile = Profile("Username", "Passw0rd")
        self.assertEqual(str(self.profile), 'You have a profile with username: "Username" and password: ********')


if __name__ == "__main__":
    unittest.main()
