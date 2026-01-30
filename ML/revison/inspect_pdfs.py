
import os
from pypdf import PdfReader

pdf_files = [
    "/Users/ml/Downloads/zzm/ML/revison/Revision_worksheet_part2 - Solutions.pdf",
    "/Users/ml/Downloads/zzm/ML/revison/com4509_part1_revision_solutions.pdf"
]

for pdf_path in pdf_files:
    print(f"--- Extracting from {os.path.basename(pdf_path)} ---")
    try:
        reader = PdfReader(pdf_path)
        for i, page in enumerate(reader.pages):
            text = page.extract_text()
            print(f"Page {i+1}:")
            print(text)
            print("-" * 20)
    except Exception as e:
        print(f"Error extracting {pdf_path}: {e}")
