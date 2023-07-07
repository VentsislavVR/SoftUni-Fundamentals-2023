import re
def check_valid_bar(barcode):
    product_group = re.findall(r"@\#{1,}[A-Z][A-Za-z0-9]+[A-Z]@\#{1,}", barcode)
    if not product_group:
        return print("Invalid barcode")
    return product_group


def check_groups(barcode):
    group = re.findall(r"\d+", barcode)
    digits = group
    if digits:
        return f"Product group: {''.join(digits)}"
    return f"Product group: 00"


number_of_barcodes = int(input())

for bar in range(number_of_barcodes):
    barcodes = input()

    valid_barcode = check_valid_bar(barcodes)
    if valid_barcode:
        print(check_groups(barcodes))



