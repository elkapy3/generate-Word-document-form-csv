import csv
from docx import Document
import os

# Define the function to create a Word document
def create_word_doc(name, amount, output_dir):
    document = Document()
    content = f"Hello, my name is {name} and I have {amount}. I am happy to be here and to see you all."

    document.add_paragraph(content)
    file_path = os.path.join(output_dir, f"{name}.docx")
    document.save(file_path)

# Main function to read CSV and create Word documents
def generate_docs_from_csv(csv_file, output_dir):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    with open(csv_file, newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            name = row['name']
            amount = row['amount']
            create_word_doc(name, amount, output_dir)

# Define paths
csv_file = "data.csv"  # Replace with your CSV file path
output_dir = "output_docs"  # Directory to save Word documents

# Execute the function
generate_docs_from_csv(csv_file, output_dir)