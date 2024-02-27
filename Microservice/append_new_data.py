import json

def read_existing_data(txt_file_path):
    try:
        with open(txt_file_path, 'r') as txt_file:
            return txt_file.read()
    except FileNotFoundError:
        print("TXT file not found.")
        return ""

def append_new_data(json_file_path, txt_file_path):
    try:
        with open(json_file_path, 'r') as json_file:
            data = json.load(json_file)
    except FileNotFoundError:
        print("JSON file not found.")
        return
    
    existing_data = read_existing_data(txt_file_path)
    existing_entries = existing_data.strip().split('\n\n')  # Split existing data into individual entries
    
    try:
        with open(txt_file_path, 'a+') as txt_file:
            for entry in data:
                new_entry_str = ""
                for key, value in entry.items():
                    new_entry_str += f"{key}: {value}\n"
                if new_entry_str.strip() not in existing_entries:
                    txt_file.write(new_entry_str + "\n")  # Add the new entry with an empty line after
            print("New data appended successfully.")
    except FileNotFoundError:
        print("TXT file not found.")

def close_files(json_file, txt_file):
    with open(json_file_path, 'r') as json_file:
        json_file.close()
    with open(txt_file_path, 'a+') as txt_file:
        txt_file.close()

# example calling
if __name__ == "__main__":
    while True:
        json_file_path = input("Enter the path to the JSON file: ")
        txt_file_path = input("Enter the path to the TXT file: ")
        append_new_data(json_file_path, txt_file_path)

        choice = input("Do you want to append more data? (y/n): ")
        if choice.lower() != 'y':
            break

    confirm_close_files = input("Do you want to close the JSON and TXT files? (y/n): ")
    if confirm_close_files.lower() == 'y':
        close_files(json_file_path, txt_file_path)
