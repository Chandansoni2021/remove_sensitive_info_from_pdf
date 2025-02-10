import fitz # PyMuPDF

# Function to remove images from PDF
def remove_images_from_pdf(input_pdf, output_pdf):
    # Open the input PDF
    document = fitz.open(input_pdf)

    # Iterate through each page
    for page_num in range(len(document)):
        page = document.load_page(page_num)

        # Get the list of images on the page
        image_list = page.get_images(full=True)

        # Iterate through the images and remove them
        for img in image_list:
            xref = img[0]
            page.delete_image(xref)

    # Save the modified PDF (without images)
    document.save(output_pdf)
    document.close()

    print(f"✅ Images removed and saved to {output_pdf}")


# Sample invoice data
invoice_data = {
    "Vendor Name": "ANIKA INDUSTRIES",
    "Vendor Address Recipient": "Anika Industries Private Limited",
    "Customer Name": "Bonito Designs Private Limited",
    "Shipping Address Recipient": "Bonito Designs Private Limited"
}

# Function to modify PDF (remove text and replace with specified text)
def modify_pdf(input_pdf, output_pdf, keys_to_modify, replacement_text=""):
    doc = fitz.open(input_pdf)

    for page in doc:
        for key in keys_to_modify:
            if key in invoice_data:
                value_to_replace = invoice_data[key]

                # Convert to string if it's a dictionary
                if isinstance(value_to_replace, dict):
                    value_to_replace = "\n".join(value_to_replace.values())

                # Search for text in the PDF
                text_instances = page.search_for(str(value_to_replace))

                for inst in text_instances:
                    # First, remove the original text by redacting it
                    page.add_redact_annot(inst)
                    page.apply_redactions()

                    # Insert the replacement text after redacting
                    page.insert_text(
                        (inst.x0, inst.y0), # Position to insert text
                        replacement_text,
                        fontsize=10,
                        color=(0, 0, 0) # Black text
                    )

    # Save modified PDF
    doc.save(output_pdf)
    doc.close()
    print(f"✅ Modified PDF saved as {output_pdf}")


# Example usage
input_pdf = "BC ANIKA Tax Invoice.pdf"
output_pdf_without_images = "output_without_images.pdf"
output_pdf_final = "modified_invoice.pdf"

# First, remove images
remove_images_from_pdf(input_pdf, output_pdf_without_images)

# Then, modify the PDF to replace text
keys_selected = ["Vendor Address Recipient", "Customer Name", "Vendor Name", "Shipping Address Recipient"]
modify_pdf(output_pdf_without_images, output_pdf_final, keys_selected)
