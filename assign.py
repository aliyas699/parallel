from concurrent.futures import ThreadPoolExecutor

# Define addition and subtraction functions
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

# Input values
a, b = 10, 5

# Using ThreadPoolExecutor for parallel execution
with ThreadPoolExecutor() as executor:
    future_add = executor.submit(add, a, b)
    future_subtract = executor.submit(subtract, a, b)
    
    # Get results
    result_add = future_add.result()
    result_subtract = future_subtract.result()

print(f"Addition Result: {result_add}")
print(f"Subtraction Result: {result_subtract}")
