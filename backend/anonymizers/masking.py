def apply_masking(df, column):
    def mask_value(value):
        value = str(value)
        if '@' in value:  # Email
            local, domain = value.split('@')
            return local[0] + '*' * (len(local) - 1) + '@' + domain
        elif value.isdigit() and len(value) >= 6:  # Phone
            return value[:2] + '*' * (len(value) - 4) + value[-2:]
        else:  # Name or generic
            return value[0] + '*' * (len(value) - 1) if value else value

    df[column] = df[column].apply(mask_value)
    return df
