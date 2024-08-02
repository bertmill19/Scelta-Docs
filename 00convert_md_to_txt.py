import os

def convert_md_to_txt(source_folder):
    for filename in os.listdir(source_folder):
        if filename.endswith('.md'):
            md_file_path = os.path.join(source_folder, filename)
            
            # Read the content of the .md file
            with open(md_file_path, 'r', encoding='utf-8') as md_file:
                content = md_file.read()
                
            # Create the .txt file and write the content
            txt_filename = filename.replace('.md', '.txt')
            txt_file_path = os.path.join(source_folder, txt_filename)
            
            with open(txt_file_path, 'w', encoding='utf-8') as txt_file:
                txt_file.write(content)
                
            # Remove the original .md file
            os.remove(md_file_path)
            
            print(f"Converted and removed {filename}")

if __name__ == "__main__":
    source_folder = '.'  # Current directory
    convert_md_to_txt(source_folder)
