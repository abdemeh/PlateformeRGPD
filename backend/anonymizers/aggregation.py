def apply_aggregation(df, column):
    def aggregate(value):
        try:
            num = float(value)
            return int(num // 10 * 10)  # Regroupe par tranches de 10
        except:
            return value

    df[column] = df[column].apply(aggregate)
    return df
