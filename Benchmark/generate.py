import pandas as pd
import numpy as np
from faker import Faker
import random
import os

fake = Faker("fr_FR")
Faker.seed(42)
np.random.seed(42)
random.seed(42)

# Nombre de lignes
n = 10000

# Départements simulés
departments = ['RH', 'Informatique', 'Finance', 'Marketing', 'Production']

# Génération du dataset
data = {
    "name": [fake.name() for _ in range(n)],
    "email": [fake.email() for _ in range(n)],
    "phone": [fake.phone_number() for _ in range(n)],
    "address": [fake.address().replace('\n', ', ') for _ in range(n)],
    "birth_date": [fake.date_of_birth(minimum_age=18, maximum_age=65) for _ in range(n)],
    "gender": [random.choice(['Male', 'Female']) for _ in range(n)],
    "department": [random.choice(departments) for _ in range(n)],
    "salary": np.round(np.random.normal(35000, 10000, size=n), 2),
    "credit_card": [fake.credit_card_number() for _ in range(n)],
}

df = pd.DataFrame(data)

# Sauvegarder en CSV
output_path = "dataset_example.csv"
df.to_csv(output_path, index=False)
print(f"Dataset généré avec succès : {os.path.abspath(output_path)}")
