import subprocess


def get_pdf_pages(file):
    """Get PDF pages"""
    pdf_command = "pdfinfo " + file + "|grep Pages|awk '{print $2}'"
    pages = subprocess.run(pdf_command, shell=True, stdout=subprocess.PIPE)
    return int(pages.stdout)
