import os

def delete_all_txt_files(source_folder):
    for filename in os.listdir(source_folder):
        if filename.endswith('.txt'):
            txt_file_path = os.path.join(source_folder, filename)
            os.remove(txt_file_path)
            print(f"Deleted {filename}")

if __name__ == "__main__":
    source_folder = '.'  # Current directory
    delete_all_txt_files(source_folder)