import csv

def read_csv_and_create_dict(file_path, key_column, value_column):
    # Initialize an empty dictionary of lists
    key_value_dict = {}
    
    # Open the CSV file
    with open(file_path, mode='r', newline='') as csv_file:
        # Create a csv.DictReader object
        csv_reader = csv.DictReader(csv_file)
        
        # Loop through each row in the CSV file
        for row in csv_reader:
            # Convert key and value to uppercase
            key = row[key_column].upper()
            value = row[value_column].toUpperCase()
            
            # If the key is already in the dictionary, append the value to the list
            if key in key_value_dict:
                key_value_dict[key].append(value)
            else:
                # Otherwise, create a new list for the key
                key_value_dict[key] = [value]
    
    return key_value_dict

# Specify the path to the CSV file
csv_file_path = 'your_file.csv'

# Specify the key and value column names
key_column_name = 'KeyColumn'
value_column_name = 'ValueColumn'

# Call the function and print the resulting dictionary
result_dict = read_csv_and_create_dict(csv_file_path, key_column_name, value_column_name)
print(result_dict)
