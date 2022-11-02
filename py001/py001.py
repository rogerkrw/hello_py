# https://www.computersciencemaster.com.br/como-ler-pdf-com-python/

import PyPDF2
import re

pdf_file = open('/code/hello_py/py001/pdf.pdf', 'rb')

read_pdf = PyPDF2.PdfFileReader(pdf_file)

number_of_pages = read_pdf.getNumPages()

page = read_pdf.getPage(0)

page_content = page.extractText()

parsed = ''.join(page_content)

print(parsed)

