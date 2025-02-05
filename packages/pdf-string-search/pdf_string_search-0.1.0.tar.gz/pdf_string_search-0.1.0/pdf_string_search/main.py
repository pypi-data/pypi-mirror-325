import os
import fitz  # PyMuPDF

def search_pdf_for_string(pdf_path, search_string):
    """
    Searches a PDF file for the given string.
    Returns True if found, False otherwise.
    """
    try:
        doc = fitz.open(pdf_path)
        for page_num in range(doc.page_count):
            page = doc.load_page(page_num)
            text = page.get_text("text")
            if search_string.lower() in text.lower():
                return True
    except Exception as e:
        print(f"Error reading {pdf_path}: {e}")
    return False

def process_files(txt_file_path, pdf_folder_path):
    """
    Processes the text file with search strings and checks each PDF for those strings.
    Creates separate output files for each search string.
    """
    if not os.path.exists(txt_file_path):
        print(f"Text file {txt_file_path} not found!")
        return

    if not os.path.isdir(pdf_folder_path):
        print(f"Folder {pdf_folder_path} not found!")
        return

    # Read strings from the text file
    with open(txt_file_path, 'r', encoding='utf-8') as txt_file:
        search_strings = [line.strip() for line in txt_file.readlines()]

    # Get output directory (same as the input TXT file location)
    output_dir = os.path.dirname(txt_file_path)

    for search_string in search_strings:
        safe_filename = "".join(c if c.isalnum() or c in (' ', '_') else "_" for c in search_string)
        output_file_path = os.path.join(output_dir, f"{safe_filename}_results.txt")

        found_pdfs = []
        for pdf_filename in os.listdir(pdf_folder_path):
            if pdf_filename.lower().endswith('.pdf'):
                pdf_path = os.path.join(pdf_folder_path, pdf_filename)
                if search_pdf_for_string(pdf_path, search_string):
                    found_pdfs.append(pdf_filename)

        # Write results for this search string
        with open(output_file_path, 'w', encoding='utf-8') as output_file:
            if found_pdfs:
                output_file.write("\n".join(found_pdfs) + "\n")
            else:
                output_file.write("No PDFs found containing this string.\n")

        print(f"Results saved to: {output_file_path}")

def main():
    txt_file_path = input("Enter the path to the text file with search strings: ")
    pdf_folder_path = input("Enter the path to the folder containing PDF files: ")
    process_files(txt_file_path, pdf_folder_path)

if __name__ == "__main__":
    main()