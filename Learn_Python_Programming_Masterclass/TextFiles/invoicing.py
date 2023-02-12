import datetime
from os import SEEK_SET
from typing import TextIO


def get_year() -> int:
    """Return the current year as an integer."""
    return datetime.datetime.now().year


def parse_invoice_number(number: str) -> tuple[int, int]:
    """Split a well-formed invoice "number" into its component parts.

    :param number: A string of the form YYYY-NNNN
        YYYY is the 4 digit year.
        NNNN is a 4 digit invoice number, left padded with zeros.
        The 2 parts are separated with a "-" character.
    :return: The returned tuple will contain:
        the 4 digit year as an integer,
        the invoice number as an integer.
    """
    year, number = number.split('-')
    return int(year), int(number)

def next_invoice_number(invoice_number: str) -> str:
    """ Produce the next invoice "number" in sequence.

    The format of `invoice_number` is described in `parse_invoice_number`.

    :param invoice_number: A string representing an invoice number.
    :return: A string representing the next invoice number.
        The numerical part will be incremented, unless the current year
        isn't the same as the year in `invoice_number`. In that case,
        the new invoice number will contain the current year, and the
        numerical part will be set to "0001".
    """
    invoice_year, invoice_number = parse_invoice_number(invoice_number)
    year = get_year()

    if invoice_year == year:
        return f"{invoice_year}-{invoice_number + 1:04d}"
    else:
        return f"{year}-{1:04d}"

def record_invoice(invoice_file: TextIO,
                   company: str,
                   amount: float,
                   last_line_pointer: int = 0) -> int:
    """Create a new invoice number, and write it to a file on disk.

    :param invoice_file: An open text file, opened using r+.
    :param company: The name of the company being invoiced.
    :param amount: The amount of the invoice.
    :param last_line_pointer: The position of the start of the last line in the file.
        This will be obtained by the previous call to `record_invoice`
    :return: The position of the start of the last line in the file
        This can be used in subsequent call to `record_invoice`
    """
    # Read the file line by line
        # initialise last_row to an empty string because the file might be empty.
        # If there are no lines of text in the file, we won't enter the for loop, and last_row would be undefined.
        # Initialising it avoids that problem
    last_row = ''

    # Restore file pointer to the start of the file
    invoice_file.seek(last_line_pointer, SEEK_SET)

    for line in invoice_file:
        last_row = line
    if last_row:    # Check last_row is not empty
        invoice_number, _, _ = last_row.split("\t")
        new_invoice_number = next_invoice_number(invoice_number)
    else:
        # if the file is empty, we'll start numbering from 1
        year = get_year()
        new_invoice_number = f"{year}-{1:04d}"

    # Store file pointer
    last_line_pointer = invoice_file.tell()

    # Write the new line to invoice_file
    print(f"{new_invoice_number}\t{company}\t{amount}", file=invoice_file)
    return last_line_pointer

data_file = 'invoices.csv'

with open(data_file, 'r+') as invoices:
    # That gives us the position of the start of the line that was added
    last_line = record_invoice(invoices, 'ACME Roadrunner', 18.4)
    last_line = record_invoice(invoices, 'Squirrel Storage', 355.45, last_line)

# Test code:
# current_year = get_year()
# test_data = [
#     ('2019-0005', (2019, 5), f'{current_year}-0001'),
#     (f'{current_year}-8514', (current_year, 8514), f'{current_year}-8515'),
#     (f'{current_year}-0001', (current_year, 1), f'{current_year}-0002'),
#     (f'{current_year}-0023', (current_year, 23), f'{current_year}-0024'),
# ]
#
# for test_string, result, next_number in test_data:
#     parts = parse_invoice_number(test_string)
#     if parts == result:
#         print(f'{test_string} parsed successfully')
#     else:
#         print(f'{test_string} failed to parse. Expected {result} got {parts}')
#
#     new_number = next_invoice_number(test_string)
#     if next_number == new_number:
#         print(f'New number {new_number} generated correctly for {test_string}')
#     else:
#         print(f'New number {new_number} is not correct for {test_string}')
#
#     print('-' * 80)
