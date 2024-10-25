import random


def generate_phone_number():
    return f"+7{random.randint(100, 999)}{random.randint(100, 999)}{random.randint(10, 99)}{random.randint(10, 99)}"


