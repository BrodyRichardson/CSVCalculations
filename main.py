import csv

def process_numbers(num1, num2):
    total = num1 + num2
    difference = num1 - num2
    product = num1 * num2
    quotient = num1 / num2
    return total, difference, product, quotient

with open("numbers.csv", "r") as f:
    reader = csv.reader(f)
    next(reader)  # skip the header row
    results = []
    for row in reader:
        num1, num2 = [float(cell) for cell in row]
        total, difference, product, quotient = process_numbers(num1, num2)
        results.append([total, difference, product, quotient])

with open("results.csv", "w", newline='') as f:
    writer = csv.writer(f)
    writer.writerow(["Sum", "Difference", "Product", "Quotient"])
    writer.writerows(results)