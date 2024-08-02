import os

def convert_md_to_txt(source_folder):
    for filename in os.listdir(source_folder):
        if filename.endswith('.md'):
            md_file_path = os.path.join(source_folder, filename)
            txt_filename = filename.replace('.md', '.txt')
            txt_file_path = os.path.join(source_folder, txt_filename)

            # Read the content of the .md file
            with open(md_file_path, 'r', encoding='utf-8') as md_file:
                content = md_file.read()

            # Write the content to a new .txt file
            with open(txt_file_path, 'w', encoding='utf-8') as txt_file:
                txt_file.write(content)

            print(f"Created {txt_filename} from {filename}")

if __name__ == "__main__":
    source_folder = '.'  # Current directory
    convert_md_to_txt(source_folder)
