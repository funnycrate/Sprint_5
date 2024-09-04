import random as rd

class Helpers:
    @staticmethod
    def generate_email():
        return f"igor_radzeivskiy_13_{rd.randint(000, 999)}@gmail.com"

    @staticmethod
    def generate_password():
        return f'Password{rd.randint(000, 999)}'