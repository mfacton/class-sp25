from datetime import datetime

def read_file(filepath):
    try:
        with open(filepath, "r") as file:
            return file.read().strip()
    except FileNotFoundError:
        print(f"Warning: {filepath} not found")
        return ""

def process_folders(folders, file_name):
    content = []
    for folder in folders:
        file_content = read_file(f"{folder}/{file_name}")
        if file_content:
            content.append(f"### {folder}\n\n" + file_content)
    return "\n\n".join(content)

def generate():
    folders = ["2.001", "21m.361", "6.230", "6.250", "6.300"]
    categories = ["grading.md", "dates.md"]
    template_file = "template.md"
    output_file = "README.md"
    
    template_content = read_file(template_file)
    if not template_content:
        return
    
    for category in categories:
        category_content = process_folders(folders, category)
        template_content = template_content.replace(f"<!--{category}-->", category_content)
    
    with open(output_file, "w") as file:
        file.write(template_content.strip() + "\n")

if __name__ == "__main__":
    generate()

