# benchmarks/memory_usage.py
import psutil, os

def measure_memory_usage(func, *args, **kwargs):
    process = psutil.Process(os.getpid())
    mem_before = process.memory_info().rss / (1024 * 1024)  # en MiB
    result = func(*args, **kwargs)
    mem_after = process.memory_info().rss / (1024 * 1024)
    return result, mem_after - mem_before
