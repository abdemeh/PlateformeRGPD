import os
import time
import psutil
import pandas as pd
import matplotlib.pyplot as plt

# Import anonymization methods
from methods import masquage, pseudonymisation, generalisation, perturbation, aggregation

# Import benchmark functions
from benchmarks import execution_time, memory_usage, information_loss, reversibility, re_identification, entropy_diversity, data_precision, scalability

# Import utils
from utils.json_exporter import save_benchmark_summary_json
from utils.dataset_loader import load_dataset
from benchmarks.information_loss import compute_information_loss
from utils.visualization import plot_all_benchmarks

# Define the directory where datasets are stored
DATASET_DIR = "datasets"
dataset_files = [f for f in os.listdir(DATASET_DIR) if f.endswith(".csv")]

# Create output folder for anonymized files
output_folder = "anonymized_datasets"
if not os.path.exists(output_folder):
    os.makedirs(output_folder)
    
print("Available datasets:")
for i, file in enumerate(dataset_files):
    print(f"{i+1}. {file}")

choice = input("Select dataset number: ").strip()
try:
    idx = int(choice) - 1
    selected_dataset = os.path.join(DATASET_DIR, dataset_files[idx])
except:
    print("Invalid choice, exiting.")
    exit()

# Load dataset
df = load_dataset(selected_dataset)
print(f"Loaded dataset with {len(df)} rows and {len(df.columns)} columns.")

# Define a dictionary of anonymization methods.
# Each method is a function that takes a DataFrame and returns a new DataFrame.
methods = {
    "masquage": lambda d: d.assign(credit_card = masquage.mask_column(d["credit_card"])),
    "pseudonymisation": lambda d: d.assign(name = pseudonymisation.pseudonymize_column(d["name"])),
    "generalisation": lambda d: d.assign(birth_date = generalisation.generalize_birth_date(d["birth_date"])),
    "perturbation": lambda d: d.assign(salary = perturbation.perturb_numeric(d["salary"], noise_level=0.1)),
    "aggregation": lambda d: d.assign(salary = aggregation.aggregate_numeric(d["salary"], bins=5))
}

# Benchmark function: runs a given anonymization method and returns benchmark metrics.
def run_benchmarks(method_name, anonymize_func, df):
    original_df = df.copy()
    
    # Measure execution time and memory usage
    process = psutil.Process(os.getpid())
    mem_before = process.memory_info().rss / (1024 * 1024)
    start_time = time.perf_counter()
    new_df = anonymize_func(df)
    end_time = time.perf_counter()
    mem_after = process.memory_info().rss / (1024 * 1024)
    exec_time = end_time - start_time
    mem_used = mem_after - mem_before
    
    # Choose appropriate column for comparison based on method
    if method_name == "masquage":
        orig = original_df["credit_card"]
        new = new_df["credit_card"]
    elif method_name == "pseudonymisation":
        orig = original_df["name"]
        new = new_df["name"]
    elif method_name == "generalisation":
        orig = original_df["birth_date"]
        new = new_df["birth_date"]
    elif method_name in ["perturbation", "aggregation"]:
        orig = original_df["salary"]
        new = new_df["salary"]
    else:
        orig = new = None
    
    # Calculate benchmark criteria
    info_loss = compute_information_loss(orig, new) if orig is not None else None
    # Appel de la nouvelle fonction de réversibilité (qui retourne un tuple)
    perc_rev, avg_sim = reversibility.compute_reversibility(orig, new, threshold=0.7) if orig is not None else (None, None)
    reid_risk = re_identification.compute_reidentification_risk(new) if new is not None else None
    ent_before = entropy_diversity.compute_entropy(orig) if orig is not None else None
    ent_after = entropy_diversity.compute_entropy(new) if new is not None else None
    unique_before = orig.nunique() if orig is not None else None
    unique_after = new.nunique() if new is not None else None
    precision = data_precision.compute_data_precision(orig, new)
    scale = scalability.evaluate_scalability(len(df))
    
    benchmarks = {
        "Execution Time (s)": round(exec_time, 4),
        "Memory Used (MiB)": round(mem_used, 4),
        "Avg Information Loss": round(info_loss, 2) if info_loss is not None else None,
        "Reversibility (%)": perc_rev,
        "Average Similarity (%)": round(avg_sim, 2) if avg_sim is not None else None,
        "Re-ID Risk (%)": round(reid_risk, 2) if reid_risk is not None else None,
        "Entropy Before": round(ent_before, 4) if ent_before is not None else None,
        "Entropy After": round(ent_after, 4) if ent_after is not None else None,
        "Unique Values Before": unique_before,
        "Unique Values After": unique_after,
        "Data Precision (%)": precision * 100,
        "Scalability": scale
    }
    return new_df, benchmarks

all_results = {}
benchmark_summary = {}

# Loop over each anonymization method, run the benchmarks, and save the anonymized dataset.
for method_name, func in methods.items():
    print(f"\nRunning method: {method_name}")
    new_df, metrics = run_benchmarks(method_name, func, df)
    
    # Build new file name based on original file name and method suffix
    base_filename = os.path.basename(selected_dataset)  # get file name without directory
    base, ext = os.path.splitext(base_filename)
    new_file = os.path.join(output_folder, f"{base}_{method_name}{ext}")
    
    # Save the anonymized dataset in the output folder
    new_df.to_csv(new_file, index=False)
    print(f"Anonymized dataset saved as: {os.path.abspath(new_file)}")
    
    all_results[method_name] = metrics
    benchmark_summary[method_name] = metrics

# Print benchmark results
print("\n=== Benchmark Summary ===")
for method, metrics in benchmark_summary.items():
    print(f"\nMethod: {method}")
    for k, v in metrics.items():
        print(f"  {k}: {v}")

# Export benchmark results to JSON
save_benchmark_summary_json(benchmark_summary)

# Visualize benchmark results
plot_all_benchmarks(benchmark_summary)


