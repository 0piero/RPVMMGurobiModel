import csv
import sys

def select_rows_for_n_unique_caixa_ids(input_file, output_file, n):
    groups = {}  # Dictionary to group rows by CAIXA_ID

    # Read the CSV and group rows by CAIXA_ID
    with open(input_file, 'r', newline='', encoding='utf-8') as infile:
        reader = csv.DictReader(infile)
        header = reader.fieldnames
        for row in reader:
            caixa_id = row["CAIXA_ID"]
            if caixa_id not in groups:
                groups[caixa_id] = []
            groups[caixa_id].append(row)
    
    # Select the first N unique CAIXA_ID values
    selected_caixa_ids = list(groups.keys())[:n]

    # Collect all rows from the selected CAIXA_ID groups
    selected_rows = []
    for caixa_id in selected_caixa_ids:
        selected_rows.extend(groups[caixa_id])
    
    # Write the selected rows to the output CSV
    with open(output_file, 'w', newline='', encoding='utf-8') as outfile:
        writer = csv.DictWriter(outfile, fieldnames=header)
        writer.writeheader()
        writer.writerows(selected_rows)
    
    print(f"Selected rows from {len(selected_caixa_ids)} unique CAIXA_ID values written to '{output_file}'.")

if __name__ == '__main__':
    if len(sys.argv) != 4:
        print("Usage: python script.py input.csv output.csv N")
        sys.exit(1)
    
    input_csv = sys.argv[1]
    output_csv = sys.argv[2]
    try:
        n = int(sys.argv[3])
    except ValueError:
        print("Error: N must be an integer.")
        sys.exit(1)
    
    select_rows_for_n_unique_caixa_ids(input_csv, output_csv, n)
