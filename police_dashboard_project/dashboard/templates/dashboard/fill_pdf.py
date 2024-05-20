import PyPDF2

# Define the paths for the blank PDF form and the output filled form
blank_pdf_path = 'blank_form.pdf'
output_pdf_path = 'filled_form.pdf'

# Open the blank PDF form
with open(blank_pdf_path, 'rb') as pdf_file:
    pdf_reader = PyPDF2.PdfFileReader(pdf_file)
    pdf_writer = PyPDF2.PdfFileWriter()

    # Get the first page of the PDF form
    page = pdf_reader.getPage(0)

    # Access the form fields (if the PDF has fillable fields)
    form = page.getFields()

    # Fill out the form fields
    form['field_name'].update(
        PyPDF2.generic.createStringObject('Your Value')
    )

    # Add the updated page to the PDF writer
    pdf_writer.addPage(page)

    # Create a new PDF file with the filled form
    with open(output_pdf_path, 'wb') as output_pdf:
        pdf_writer.write(output_pdf)
