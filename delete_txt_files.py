import os

def delete_all_txt_files(source_folder):
    for root, dirs, files in os.walk(source_folder):
        for filename in files:
            if filename.endswith('.txt'):
                txt_file_path = os.path.join(root, filename)
                os.remove(txt_file_path)
                print(f"Deleted {filename} from {root}")

if __name__ == "__main__":
    source_folder = '.'  # Current directory
    delete_all_txt_files(source_folder)
