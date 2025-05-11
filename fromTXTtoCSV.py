import csv

def convert_txt_to_csv(txt_file_path):
    # Read the text file
    with open(txt_file_path, 'r') as txt_file:
        lines = txt_file.readlines()
    
    # Create a new CSV file path
    new_csv_path = txt_file_path.rsplit('.', 1)[0] + '.csv'
    
    # Write to CSV file
    with open(new_csv_path, 'w', newline='') as csv_file:
        writer = csv.writer(csv_file)
        
        # Assuming each line is separated by spaces or tabs (adjust as needed)
        for line in lines:
            # Split each line by space (or tab, or another delimiter) and write as a new row in CSV
            writer.writerow(line.strip().split())
    
    print(f"Text file has been converted to CSV and saved as: {new_csv_path}")

# Example usage
txt_file_path = "bibliography.bib" # Correct path
convert_txt_to_csv(txt_file_path)
