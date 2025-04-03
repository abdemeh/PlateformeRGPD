import pandas as pd
import numpy as np
from faker import Faker
import random
import os

# Initialisation de Faker et des seeds pour la reproductibilité
fake = Faker("fr_FR")
Faker.seed(42)
np.random.seed(42)
random.seed(42)

def generate_dataset(n):
    """Génère un dataset synthétique de n lignes."""
    departments = ['RH', 'Informatique', 'Finance', 'Marketing', 'Production']
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
    return pd.DataFrame(data)

# Liste des tailles de dataset à générer
sizes = [10000, 100000, 1000000]

for size in sizes:
    df = generate_dataset(size)
    output_path = f"dataset_example_{size}.csv"
    df.to_csv(output_path, index=False)
    print(f"Dataset généré avec succès : {os.path.abspath(output_path)}")
