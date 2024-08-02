import os

def convert_md_to_txt(source_folder):
    for filename in os.listdir(source_folder):
        if filename.endswith('.md'):
            md_file_path = os.path.join(source_folder, filename)
            txt_filename = filename.replace('.md', '.txt')
            txt_file_path = os.path.join(source_folder, txt_filename)

            os.rename(md_file_path, txt_file_path)
            
            print(f"Renamed {filename} to {txt_filename}")

if __name__ == "__main__":
    source_folder = '.'  # Current directory
    convert_md_to_txt(source_folder)
