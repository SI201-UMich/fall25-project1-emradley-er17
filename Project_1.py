# PROJECT 1 CHECKPOINT
# Name of Dataset: Sample Superstore Dataset
# Columns: Ship Mode, Category, Sub Category State, Region, Sales, Quantity, Profit 
# Calculations: 
#   1. What is the average profit in the East?
#   2. What percentage of office supplies were shipped by first class?
#   3. What percentage of the phones sold in California have a higher number of sales than 300? 
#   4. What is the average quantity in each region?
# Function Decomposition Diagram:
# Names of Collaboratoros: Ella Kim


import kagglehub

# Download latest version
path = kagglehub.dataset_download("bravehart101/sample-supermarket-dataset")

print("Path to dataset files:", path)
