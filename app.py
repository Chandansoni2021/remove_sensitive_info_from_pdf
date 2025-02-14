from azure.core.credentials import AzureKeyCredential
from azure.ai.documentintelligence import DocumentIntelligenceClient


# Azure configuration
endpoint = ""
key = ""

# Path to your local file (replace with your actual file path)
file_path = "Invoice.pdf"

# Initialize the Document Intelligence client
document_intelligence_client = DocumentIntelligenceClient(
    endpoint=endpoint, credential=AzureKeyCredential(key)
)

# Open the file and pass it for processing
with open(file_path, "rb") as f:
    poller = document_intelligence_client.begin_analyze_document(
        "prebuilt-invoice", f
    )
    
    # Get the result of the analysis
    invoices = poller.result()

    # Process and print the  results as needed (same as your original code)
    for idx, invoice in enumerate(invoices.documents):
        print(f"--------Recognizing invoice #{idx + 1}--------")
        
        vendor_name = invoice.fields.get("VendorName")
        if vendor_name:
            print(f"Vendor Name: {vendor_name.value_string}")

        vendor_address = invoice.fields.get("VendorAddress")
        if vendor_address:
            print(f"Vendor Address: {vendor_address.value_address}")

        vendor_address_recipient = invoice.fields.get("VendorAddressRecipient")
        if vendor_address_recipient:
            print(f"Vendor Address Recipient: {vendor_address_recipient.value_string}")

        customer_name = invoice.fields.get("CustomerName")
        if customer_name:
            print(f"Customer Name: {customer_name.value_string}")

        customer_id = invoice.fields.get("CustomerId")
        if customer_id:
            print(f"Customer Id: {customer_id.value_string}")

        customer_address = invoice.fields.get("CustomerAddress")
        if customer_address:
            print(f"Customer Address: {customer_address.value_address}")

        customer_address_recipient = invoice.fields.get("CustomerAddressRecipient")
        if customer_address_recipient:
            print(f"Customer Address Recipient: {customer_address_recipient.value_string}")

        invoice_id = invoice.fields.get("InvoiceId")
        if invoice_id:
            print(f"Invoice Id: {invoice_id.value_string}")

        invoice_date = invoice.fields.get("InvoiceDate")
        if invoice_date:
            print(f"Invoice Date: {invoice_date.value_date}")

        invoice_total = invoice.fields.get("InvoiceTotal")
        if invoice_total:
            print(f"Invoice Total: {invoice_total.value_currency.amount}")

        due_date = invoice.fields.get("DueDate")
        if due_date:
            print(f"Due Date: {due_date.value_date}")

        purchase_order = invoice.fields.get("PurchaseOrder")
        if purchase_order:
            print(f"Purchase Order: {purchase_order.value_string}")

        billing_address = invoice.fields.get("BillingAddress")
        if billing_address:
            print(f"Billing Address: {billing_address.value_address}")

        billing_address_recipient = invoice.fields.get("BillingAddressRecipient")
        if billing_address_recipient:
            print(f"Billing Address Recipient: {billing_address_recipient.value_string}")

        shipping_address = invoice.fields.get("ShippingAddress")
        if shipping_address:
            print(f"Shipping Address: {shipping_address.value_address}")

        shipping_address_recipient = invoice.fields.get("ShippingAddressRecipient")
        if shipping_address_recipient:
            print(f"Shipping Address Recipient: {shipping_address_recipient.value_string}")

        print("Invoice items:")
        for idx, item in enumerate(invoice.fields.get("Items").value_array):
            print(f"...Item #{idx + 1}")
            item_description = item.value_object.get("Description")
            if item_description:
                print(f"......Description: {item_description.value_string}")

            item_quantity = item.value_object.get("Quantity")
            if item_quantity:
                print(f"......Quantity: {item_quantity.value_number}")

            unit = item.value_object.get("Unit")
            if unit:
                print(f"......Unit: {unit.value_number} has confidence: {unit.confidence}")

            unit_price = item.value_object.get("UnitPrice")
            if unit_price:
                print(f"......Unit Price: {unit_price.value_currency.amount}")

            item_date = item.value_object.get("Date")
            if item_date:
                print(f"......Date: {item_date.value_date} has confidence: {item_date.confidence}")

            tax = item.value_object.get("Tax")
            if tax:
                print(f"......Tax: {tax.value_string} has confidence: {tax.confidence}")

            amount = item.value_object.get("Amount")
            if amount:
                print(f"......Amount: {amount.value_currency.amount} has confidence: {amount.confidence}")

        subtotal = invoice.fields.get("SubTotal")
        if subtotal:
            print(f"Subtotal: {subtotal.value_currency.amount} has confidence: {subtotal.confidence}")

        total_tax = invoice.fields.get("TotalTax")
        if total_tax:
            print(f"Total Tax: {total_tax.value_currency.amount} has confidence: {total_tax.confidence}")

        previous_unpaid_balance = invoice.fields.get("PreviousUnpaidBalance")
        if previous_unpaid_balance:
            print(f"Previous Unpaid Balance: {previous_unpaid_balance.value_currency.amount} has confidence: {previous_unpaid_balance.confidence}")

        amount_due = invoice.fields.get("AmountDue")
        if amount_due:
            print(f"Amount Due: {amount_due.value_currency.amount} has confidence: {amount_due.confidence}")

        service_start_date = invoice.fields.get("ServiceStartDate")
        if service_start_date:
            print(f"Service Start Date: {service_start_date.value_date} has confidence: {service_start_date.confidence}")

        service_end_date = invoice.fields.get("ServiceEndDate")
        if service_end_date:
            print(f"Service End Date: {service_end_date.value_date} has confidence: {service_end_date.confidence}")

        service_address = invoice.fields.get("ServiceAddress")
        if service_address:
            print(f"Service Address: {service_address.value_address} has confidence: {service_address.confidence}")

        service_address_recipient = invoice.fields.get("ServiceAddressRecipient")
        if service_address_recipient:
            print(f"Service Address Recipient: {service_address_recipient.value_string} has confidence: {service_address_recipient.confidence}")

        remittance_address = invoice.fields.get("RemittanceAddress")
        if remittance_address:
            print(f"Remittance Address: {remittance_address.value_address} has confidence: {remittance_address.confidence}")

        remittance_address_recipient = invoice.fields.get("RemittanceAddressRecipient")
        if remittance_address_recipient:
            print(f"Remittance Address Recipient: {remittance_address_recipient.value_string} has confidence: {remittance_address_recipient.confidence}")

        print("----------------------------------------")
