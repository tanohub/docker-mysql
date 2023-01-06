import random
from faker import Faker


def generate(data_type):
    fake = Faker()

#https://faker.readthedocs.io/en/stable/providers.html

    datatype_dict = {
        "NAME": fake.first_name(),
        "SURNAME": fake.last_name(),
        "PHONE": fake.phone_number(),
        "EMAIL": fake.email(),
        "ADDRESS": fake.address(),
        "POSTAL_CODE": fake.postcode(),
        "REGION": fake.state(),
        "COUNTRY": fake.country(),
        "WORD": fake.word(),
        "TEXT": fake.text(),
        "NUMBER": fake.random_number(),
        "AMOUNT": round(random.random(), 2),
        "CURRENCY_CODE": fake.currency_code(),
        "ALPHA_NUMERIC": fake.bothify(text='??##?#?##?'),
        "UUID": fake.uuid4(),
        "UUID_WITHOUT_HYPHEN": str(fake.uuid4()).replace("-", ""),
        "DATE": fake.date(),
        "DATE_TIME": fake.date_time(),
        "BOOLEAN": fake.boolean(),
        "BIT": random.randint(0, 1),
        "UNIQUE_ID": fake.unique.bothify(text='##########'),
        "NULL": str('NULL')
    }

    return datatype_dict[data_type]
