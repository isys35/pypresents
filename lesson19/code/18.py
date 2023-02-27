c1 = Customer(
    first_name = 'Dmitriy',
    last_name = 'Yatsenko',
    username = 'Moseend',
    email = 'moseend@mail.com'
)

c2 = Customer(
    first_name = 'Valeriy',
    last_name = 'Golyshkin',
    username = 'Fortioneaks',
    email = 'fortioneaks@gmail.com'
)

print(c1.first_name, c2.last_name)

session.add(c1)
session.add(c2)

print(session.new)

session.commit()