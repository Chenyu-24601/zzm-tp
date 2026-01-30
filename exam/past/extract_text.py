
import os
import pypdf

def extract_text_from_pdf(pdf_path):
    try:
        reader = pypdf.PdfReader(pdf_path)
        text = ""
        for page in reader.pages:
            text += page.extract_text() + "\n"
        return text
    except Exception as e:
        return f"Error reading {pdf_path}: {e}"

def main():
    directory = "/Users/ml/Downloads/zzm/exam/past"
    files = [f for f in os.listdir(directory) if f.endswith(".pdf")]
    
    for f in files:
        path = os.path.join(directory, f)
        print(f"--- START OF {f} ---")
        print(extract_text_from_pdf(path))
        print(f"--- END OF {f} ---\n")

if __name__ == "__main__":
    main()
