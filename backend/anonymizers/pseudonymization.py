import hashlib

def apply_pseudonymization(df, column):
    def pseudonymize(value):
        value = str(value)
        return hashlib.sha256(value.encode('utf-8')).hexdigest()[:16]

    df[column] = df[column].apply(pseudonymize)
    return df
