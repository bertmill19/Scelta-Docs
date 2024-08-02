import os

def convert_md_to_txt(source_folder):
    for root, dirs, files in os.walk(source_folder):
        for filename in files:
            if filename.endswith('.md'):
                md_file_path = os.path.join(root, filename)
                
                # Read the content of the .md file
                with open(md_file_path, 'r', encoding='utf-8') as md_file:
                    content = md_file.read()
                    
                # Create the .txt file and write the content
                txt_filename = filename.replace('.md', '.txt')
                txt_file_path = os.path.join(root, txt_filename)
                
                with open(txt_file_path, 'w', encoding='utf-8') as txt_file:
                    txt_file.write(content)
                
                print(f"Converted {filename} to {txt_filename} in {root}")

if __name__ == "__main__":
    source_folder = '.'  # Current directory
    convert_md_to_txt(source_folder)
