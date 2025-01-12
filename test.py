# from pasta.core import merge_pdfs_from_paths


# path = merge_pdfs_from_paths([r"C:\Users\abhin\D_drive\AA_WORKSPACE\PASTA\Pasta\C Programming\unit5\1.pdf", r"C:\Users\abhin\D_drive\AA_WORKSPACE\PASTA\Pasta\C Programming\unit5\2.pdf", r"C:\Users\abhin\D_drive\AA_WORKSPACE\PASTA\Pasta\C Programming\unit5\8.pdf"],
#                       output_file_path = r"C:\Users\abhin\D_drive\AA_WORKSPACE\PASTA\Pasta\test2.pdf",
#                       is_title_page=True
#                       )

# print(path)

##########################################################

from pasta.core import merge_pdfs_from_paths
from reportlab.pdfgen import canvas


def create_title_page(pdf_name, page_size, temp_file="temp_title_page.pdf"):
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
    c.drawCentredString(width / 2, height - 150, f"Documeeeeeeeeent: {pdf_name}")
    
    # Draw a footer line
    c.line(50, 100, width - 50, 100)
    
    # Save the title page
    c.save()
    return temp_file



path = merge_pdfs_from_paths([r"C:\Users\abhin\D_drive\AA_WORKSPACE\PASTA\Pasta\C Programming\unit5\1.pdf", r"C:\Users\abhin\D_drive\AA_WORKSPACE\PASTA\Pasta\C Programming\unit5\2.pdf", r"C:\Users\abhin\D_drive\AA_WORKSPACE\PASTA\Pasta\C Programming\unit5\8.pdf"],
                      output_file_path = r"C:\Users\abhin\D_drive\AA_WORKSPACE\PASTA\Pasta\test1.pdf",
                      is_title_page=True,
                      create_title_page=create_title_page
                      )

print(path)