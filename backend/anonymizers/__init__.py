from .masking import apply_masking
from .pseudonymization import apply_pseudonymization
from .generalization import apply_generalization
from .perturbation import apply_perturbation
from .aggregation import apply_aggregation
import json

def anonymize_column(df, column, method, extra_data=None):
    if method == "masking":
        return apply_masking(df, column)
    elif method == "pseudonymization":
        return apply_pseudonymization(df, column)
    elif method == "generalization":
        gen_map = json.loads(extra_data) if extra_data else {}
        return apply_generalization(df, column, gen_map)
    elif method == "perturbation":
        return apply_perturbation(df, column)
    elif method == "aggregation":
        return apply_aggregation(df, column)
    else:
        return df
