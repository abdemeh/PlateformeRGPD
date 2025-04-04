# utils/visualization.py
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
import math
from matplotlib.colors import to_hex

plt.rcParams['font.family'] = ['Constantia', 'DejaVu Sans', 'Arial']

def plot_comparison(ax, metric_name, values, methods, colors):
    ax.bar(methods, values, color=colors, edgecolor='black')
    ax.set_xlabel("Method", fontsize=10)
    ax.set_ylabel(metric_name, fontsize=10)
    ax.set_title(metric_name, fontsize=12)
    ax.tick_params(axis='x', labelrotation=45, labelsize=9)
    for i, v in enumerate(values):
        try:
            text_value = f"{float(v):.2f}"
        except (ValueError, TypeError):
            text_value = str(v)
        ax.text(i, v, text_value, ha='center', va='bottom', fontsize=8)

def plot_all_benchmarks(benchmark_results):
    metrics = [m for m in list(next(iter(benchmark_results.values())).keys()) if m != "Scalability"]
    num_metrics = len(metrics)
    methods = list(benchmark_results.keys())
    
    colors = ['#003f5c', '#58508d', '#bc5090', '#ff6361', '#ffa600']
    
    cols = 5
    rows = math.ceil(num_metrics / cols)
    
    fig, axes = plt.subplots(rows, cols, figsize=(3 * cols, 4 * rows), squeeze=False)
    axes = axes.flatten()
    
    for i, metric in enumerate(metrics):
        values = [benchmark_results[m].get(metric, 0) for m in methods]
        plot_comparison(axes[i], metric, values, methods, colors)
    
    # Turn off any unused subplots
    for j in range(num_metrics, len(axes)):
        axes[j].axis('off')
    
    fig.suptitle("Benchmark Comparison for All Metrics", fontsize=16)
    plt.tight_layout(rect=[0, 0, 1, 0.95])
    plt.show()
