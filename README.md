# Dosa Restaurant Order Analysis

This project aims to help a Dosa restaurant improve its system for tracking customer orders by automating part of the process. The restaurant has been manually recording individual orders, and the goal of this project is to analyze the past orders and generate insights in the form of two JSON files.

## Project Overview

In this project, a Python script will be developed to:
- Read JSON-formatted order data from a file.
- Generate two new JSON files:
  - **`customers.json`**: Contains customer phone numbers and their corresponding names as key value pair.
  - **`items.json`**: Contains menu items, their prices, and the total number of times they’ve been ordered in nested format.

The project uses `example_orders.json` as sample data to work with, which mimics the actual data format that will be used for evaluation.

## How It Works

### Step 1: Data Input
The Python script reads a JSON file containing order data. The file name is provided as a command-line argument.

### Step 2: Customer Information Processing
The script extracts customer names and phone numbers, ensuring the phone numbers are correctly formatted, and then saves this data in the `customers.json` file.

### Step 3: Item Data Aggregation
The script collects information about each ordered item, including its price and the total number of orders. This data is saved in the `items.json` file.

---
## Requirements

- Python 3.x
- json module (standard library)

## Usage Instructions

### 1. Run the Python Script
Use the following command to run the script, replacing `example_orders.json` with your actual data file:

```bash
python order_analysis.py example_orders.json

