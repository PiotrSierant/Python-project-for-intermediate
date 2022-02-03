class Person:

    def __init__(self, name, phone_number, address=None, email=None):

        self.name = name
        self.phone_number = phone_number
        self.address = address
        self.email = email

    def __str__(self):
        return '''
        Name:         {}
        Phone number: {}
        Address:      {}
        Email :       {}
        '''.format(self.name, self.phone_number, self.address, self.email)

    def lastName(self):
        return 'LastName: {}'.format(self.name.split()[-1])


nickname1 = Person(
    'Peter Sierant',
    '828231283',
    'Zalesie 44',
    'piotr.sierant96@gmail.com',
)

nickname2 = Person(
    'Antoni Sierant',
    '828132832',
    'Zalesie 44',
    'piotr.sierant96@gmail.com',
)

nickname3 = Person(
    'Sergiej Sierant',
    '828131283',
    'Zalesie 44',
    'piotr.sierant96@gmail.com',
)

nickname4 = Person(
    'Łukasz Sierant',
    '828131282',
    'Zalesie 44',
    'piotr.sierant96@gmail.com',
)
