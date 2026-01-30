
import pypdf

files = [
    "/Users/ml/Downloads/zzm/Revision 1-6.pdf",
    "/Users/ml/Downloads/zzm/COM6115 (from week 7 to week 11).pdf"
]

for pdf_path in files:
    print(f"--- START OF {pdf_path} ---")
    try:
        reader = pypdf.PdfReader(pdf_path)
        for i, page in enumerate(reader.pages):
            text = page.extract_text()
            print(f"Page {i+1}:\n{text}\n")
    except Exception as e:
        print(f"Error reading {pdf_path}: {e}")
    print(f"--- END OF {pdf_path} ---\n")
