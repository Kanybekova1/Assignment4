import random
from datetime import datetime
import string
from random import sample
import re
# library re(regex) searches patterns, strings, performs matching operarions
class UserUtil:
    @staticmethod
    def generate_user_id():
        year_id = str(datetime.now().year)[-2:]
        rand_digits = random.randint(100000, 999999)
        return int(year_id + str(rand_digits))
    @staticmethod
    def generate_password():
        chars = string.ascii_letters + string.digits + "!@#$%^&*"
        password = "".join(random.choice(chars) for _ in range(10))
        return password if UserUtil.is_strong_password(password) else UserUtil.generate_password()

        
    @staticmethod
    def is_strong_password(password):
        if len(password) < 8:
            return False
        upper = any(char.isupper() for char in password)
        lower = any(char.islower() for char in password)
        digit = any(char.isdigit() for char in password)
        symbol = any(char in string.punctuation for char in password)
        return upper and lower and digit and symbol

    @staticmethod
    def generate_email(name,surname,domain):
        email = f"{name.lower()}.{surname.lower()}@{domain.lower()}"
        return email
    @staticmethod
    def validate_email(email):
        valid = re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', email)
        return valid is not None
