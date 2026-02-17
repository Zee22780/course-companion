import pdfplumber
import sys

def extract_pages(pdf_path: str) -> list[dict]:
    """
    Extract text from each page in a PDF file.
    
    Returns a list of chunks, each with:
    - text: the page content
    - locator: page number
    - source_file: original filename
    """

    chunks = []

    with pdfplumber.open(pdf_path) as pdf:
        for page_num, page in enumerate(pdf.pages, start=1):
            page_text = page.extract_text()

            # Only include pages that have content
            if page_text and page_text.strip():
                chunks.append({
                    "text": page_text.strip(),
                    "locator": f"Page {page_num}",
                    "source_file": pdf_path
                })
    return chunks


def main():
    if len(sys.argv) < 2:
        print("Usage: python poc_parse_pdf.py <path_to_pdf>")
        sys.exit(1)

    pdf_path = sys.argv[1]
    print(f"\n{'='*60}")
    print(f"Parsing: {pdf_path}")
    print(f"{'='*60}\n")

    chunks = extract_pages(pdf_path)

    print(f"Found {len(chunks)} pages with content:\n")

    for chunk in chunks:
        print(f"---{chunk['locator']} ---")
        print(chunk['text'])
        print()

    print(f"{'='*60}")
    print(f"Total chunks: {len(chunks)}")
    print(f"Ready for Step 2: embedding these chunks")
    print(f"{'='*60}")

if __name__ == "__main__":
    main()