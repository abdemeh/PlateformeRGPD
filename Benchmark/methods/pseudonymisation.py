# methods/pseudonymisation.py
import random

def pseudonymize_column(series):
    # Replace values with a pseudonym (e.g., "User" + random number)
    return series.apply(lambda x: "User" + str(random.randint(1000, 9999)))
