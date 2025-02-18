import unittest
from datetime import datetime
from user_assignment import User
from user_service import UserService
from userUtil import UserUtil

class TestUser(unittest.TestCase):
    def setUp(self):
        # Setting up a sample user for testing
        self.user = User(
            user_id=25189808,
            name="Aiturgan",
            surname="Kanybekova",
            email="aiturgan.kanybekova@example.com",
            password="Secure@123",
            birthday=datetime(2005, 9, 2)
        )

    def test_get_details(self):
        # Test the get_details method
        expected_details = "User ID: 25189808, Name: Aiturgan Kanybekova, Email: aiturgan.kanybekova@example.com, Birthday: 2005-09-02"
        self.assertEqual(self.user.get_details(), expected_details)

    def test_get_age(self):
        # Test the get_age method
        expected_age = 2025 - 2005  
        self.assertEqual(self.user.get_age(), expected_age)

    def test_user_id(self):
        # Test the user_id attribute
        self.assertEqual(self.user.user_id, 25189808)

    def test_name(self):
        # Test the name attribute
        self.assertEqual(self.user.name, "Aiturgan")

    def test_surname(self):
        # Test the surname attribute
        self.assertEqual(self.user.surname, "Kanybekova")

    def test_email(self):
        # Test the email attribute
        self.assertEqual(self.user.email, "aiturgan.kanybekova@example.com")

    def test_birthday(self):
        # Test the birthday attribute
        self.assertEqual(self.user.birthday, datetime(2005, 9, 2))

class TestUserService(unittest.TestCase):
    def setUp(self):
        self.user = User(250000004, "Bob", "Miller", "bob.miller@example.com", "Secure@123", datetime(2000, 8, 25))
        UserService.add_user(self.user)

    def test_add_user(self):
        self.assertIn(self.user.user_id, UserService.users)

    def test_find_user(self):
        found_user = UserService.find_user(250000004)
        self.assertIsNotNone(found_user)
        self.assertEqual(found_user.name, "Bob")

    def test_delete_user(self):
        UserService.delete_user(250000004)
        self.assertIsNone(UserService.find_user(250000004))

    def test_get_number(self):
        self.assertEqual(UserService.get_number(), 1)

class TestUserUtil(unittest.TestCase):

    def test_generate_user_id(self):
        # Test that generate_user_id() produces a valid user ID
        user_id = UserUtil.generate_user_id()
        user_id_str = str(user_id)

        # Check if the user_id starts with the current year (e.g., "24" for 2024)
        self.assertTrue(user_id_str.startswith(str(datetime.now().year)[2:]))
        # Check if the user_id is exactly 8 digits long, because string starts from 0
        self.assertEqual(len(user_id_str), 8)

    def test_generate_password(self):
        # Test that generate_password() produces a password that meets the requirements
        password = UserUtil.generate_password()
        self.assertGreaterEqual(len(password), 8)  # Check for minimum length
        self.assertTrue(any(c.isupper() for c in password))  # At least 1 uppercase letter
        self.assertTrue(any(c.islower() for c in password))  # At least 1 lowercase letter
        self.assertTrue(any(c.isdigit() for c in password))  # At least 1 digit

    def test_is_strong_password(self):
        # Test valid strong password
        strong_password = "Valid@123"
        self.assertTrue(UserUtil.is_strong_password(strong_password))
        
        # Test invalid weak password
        weak_password = "weakpass"
        self.assertFalse(UserUtil.is_strong_password(weak_password))

    def test_generate_email(self):
        # Test generate_email() method
        name = "Aiturgan"
        surname = "Kanybekova"
        domain = "example.com"
        email = UserUtil.generate_email(name, surname, domain)
        self.assertEqual(email, "aiturgan.kanybekova@example.com")

    def test_validate_email(self):
        # Test valid email
        valid_email = "valid.email@example.com"
        self.assertTrue(UserUtil.validate_email(valid_email))
        
        # Test invalid email without "@"
        invalid_email1 = "invalid-email.com"
        self.assertFalse(UserUtil.validate_email(invalid_email1))
        
        # Test invalid email without domain
        invalid_email2 = "invalid@.com"
        self.assertFalse(UserUtil.validate_email(invalid_email2))
if __name__ == "__main__":
    unittest.main()
        