import os
import re
from PyPDF2 import PdfMerger, PdfReader
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter


def natural_sort_key(s):
    """Generate a natural sort key for a string."""
    return [int(text) if text.isdigit() else text.lower() for text in re.split(r'(\d+)', s)]

def create_default_title_page(pdf_name, page_size, temp_file="temp_title_page.pdf"):
    """Create a beautified title page PDF with the file name and given page size."""
    c = canvas.Canvas(temp_file, pagesize=page_size)
    width, height = page_size
    
    # Draw a header line
    c.setStrokeColorRGB(0.2, 0.4, 0.6)  # Custom color for lines
    c.setLineWidth(2)
    c.line(50, height - 100, width - 50, height - 100)
    
    # Add the title text
    c.setFont("Helvetica-Bold", 24)
    c.setFillColorRGB(0.2, 0.4, 0.6)  # Custom color for text
    c.drawCentredString(width / 2, height - 150, f"Document: {pdf_name}")
    
    # Draw a footer line
    c.line(50, 100, width - 50, 100)
    
    # Save the title page
    c.save()
    return temp_file

def merge_pdfs_from_folder(directory, output_file_name="merged_output.pdf", is_title_page=False, output_file_path=None, create_title_page=create_default_title_page):
    """Merge all PDF files in a directory into one file with beautified title pages."""
    # Get a list of PDF files in the directory, sorted naturally
    pdf_files = sorted([f for f in os.listdir(directory) if f.endswith('.pdf')], key=natural_sort_key)

    if not pdf_files:
        raise Exception(f"No PDF files found in the directory: {os.path.abspath(directory)}. Please ensure the directory contains at least one PDF file to merge.")

    merger = PdfMerger()

    for pdf_file in pdf_files:
        pdf_path = os.path.join(directory, pdf_file)

        if is_title_page:
            # Determine the page size of the first page in the PDF
            reader = PdfReader(pdf_path)
            first_page = reader.pages[0]
            width, height = first_page.mediabox.upper_right
            page_size = (float(width), float(height))
            
            # Create a beautified title page with dynamic size
            title_page = create_title_page(pdf_file, page_size)
            with open(title_page, "rb") as temp_pdf:
                merger.append(PdfReader(temp_pdf))

        # Add the current PDF to the merger
        merger.append(pdf_path)

        # Remove the temporary title page
        os.remove(title_page)

    # Save the merged PDF back to the same directory
    if not output_file_path:
        output_file_path = os.path.join(directory, output_file_name)

    if os.path.exists(output_file_path):
        raise Exception(f"A file named '{output_file_name}' already exists at {output_file_path}. Please choose a different output file name or remove the existing file.")
    
    with open(output_file_path, "wb") as output_pdf:
        merger.write(output_pdf)

    return output_file_path



def merge_pdfs_from_paths(pdf_files, output_file_path, output_file_name="merged_output.pdf", is_title_page=False, create_title_page=create_default_title_page):
    if not pdf_files:
        raise Exception(f"No PDF files found")

    merger = PdfMerger()

    for pdf_file in pdf_files:
        # pdf_path = os.path.join(directory, pdf_file)
        pdf_name = os.path.basename(pdf_file)

        if is_title_page:
            # Determine the page size of the first page in the PDF
            reader = PdfReader(pdf_file)
            first_page = reader.pages[0]
            width, height = first_page.mediabox.upper_right
            page_size = (float(width), float(height))
            
            # Create a beautified title page with dynamic size
            title_page = create_title_page(pdf_name, page_size)
            with open(title_page, "rb") as temp_pdf:
                merger.append(PdfReader(temp_pdf))

        # Add the current PDF to the merger
        merger.append(pdf_file)

        # Remove the temporary title page
        os.remove(title_page)

    if os.path.exists(output_file_path):
        raise Exception(f"A file named '{output_file_name}' already exists at {output_file_path}. Please choose a different output file name or remove the existing file.")
    
    with open(output_file_path, "wb") as output_pdf:
        merger.write(output_pdf)
    
    return output_file_path