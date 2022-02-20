from faker import Faker


class TestData:
    def __init__(self):
        fake = Faker()
        self.email = fake.email()
        self.gender = "male"
        self.last_name = fake.last_name()
        self.password = "password123"
        self.birthdate = "1980-02-28"
        self.address = fake.address()
        self.city = fake.city()
        self.postal_code = fake.postalcode()
        self.state = fake.state()
        self.phone = "123342123"
        self.alias = "My home"