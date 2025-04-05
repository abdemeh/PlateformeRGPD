# methods/masquage.py
def mask_column(series):
    # Replace all but the last 4 characters with "XXXX"
    return series.apply(lambda x: "XXXX" + str(x)[-4:] if len(str(x)) > 4 else "XXXX")
