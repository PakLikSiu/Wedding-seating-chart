import csv
import json
import os

def build_seating_chart():
    csv_file = 'guests.csv'
    json_file = 'guests.json'
    
    if not os.path.exists(csv_file):
        print(f"Error: {csv_file} not found.")
        return

    guests = []
    
    # Read the CSV
    with open(csv_file, mode='r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            # Clean up any accidental whitespace
            name = row.get('Name', '').strip()
            table = row.get('Table', '').strip()
            
            if name and table:
                guests.append({"name": name, "table": table})
                
    # Write the JSON
    with open(json_file, mode='w', encoding='utf-8') as f:
        json.dump(guests, f, indent=2)
        
    print(f"Success! Built {json_file} with {len(guests)} guests.")

if __name__ == "__main__":
    build_seating_chart()
