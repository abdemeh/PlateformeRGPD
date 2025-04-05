import json
import os

def save_benchmark_summary_json(benchmark_summary, filename="benchmark_summary.json"):
    with open(filename, "w") as f:
        json.dump(benchmark_summary, f, indent=4)
    print(f"Benchmark summary saved as: {os.path.abspath(filename)}")
