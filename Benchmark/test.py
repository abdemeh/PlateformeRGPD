from faker import Faker

fake = Faker("fr_FR")

print(fake.email())      # ex: amanda.garcia@gmail.com
print(fake.email())      # ex: john83@outlook.com
print(fake.email())      # ex: lisa.hall@live.com
print(fake.email())      # ex: taylor69@yahoo.com
print(fake.email())      # ex: james.white@gmail.com