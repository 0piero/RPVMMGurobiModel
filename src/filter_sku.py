import csv
import sys

def filter_rows_by_sku(file1, file2, output_file):
    # Step 1: Read SKUs from file1 into a set
    sku_set = set()
    with open(file1, 'r', newline='', encoding='utf-8') as f1:
        reader = csv.DictReader(f1)
        for row in reader:
            sku = row.get("SKU")
            if sku is not None:
                sku_set.add(sku)
    
    # Step 2: Read file2 and select rows whose SKU is in sku_set
    selected_rows = []
    with open(file2, 'r', newline='', encoding='utf-8') as f2:
        reader = csv.DictReader(f2)
        header = reader.fieldnames
        for row in reader:
            if row.get("SKU") in sku_set:
                selected_rows.append(row)
    
    # Step 3: Write the selected rows to the output CSV file
    with open(output_file, 'w', newline='', encoding='utf-8') as out:
        writer = csv.DictWriter(out, fieldnames=header)
        writer.writeheader()
        writer.writerows(selected_rows)
    
    print(f"Filtered rows written to '{output_file}'.")

if __name__ == '__main__':
    if len(sys.argv) != 4:
        print("Usage: python script.py file1.csv file2.csv output.csv")
        sys.exit(1)
    
    file1 = sys.argv[1]
    file2 = sys.argv[2]
    output_file = sys.argv[3]
    filter_rows_by_sku(file1, file2, output_file)
