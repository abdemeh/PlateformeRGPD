import random

def apply_perturbation(df, column):
    def perturb(value):
        try:
            num = float(value)
            noise = random.uniform(-0.1, 0.1) * num  # +-10% bruit
            return round(num + noise, 2)
        except:
            return value

    df[column] = df[column].apply(perturb)
    return df
