import csv
from datetime import datetime
import print_exception

def main():

    STORE_NAME = "Great Value Foods"
    SALES_TAX_RATE= .06
    DISCOUNT = .10

    PRODUCT_NUMBER_INDEX = 0
    PRODUCT_NAME_INDEX = 1
    PRODUCT_PRICE_INDEX = 2

    # Read the contents of the csv file into a dictionary
    try: 
        products_dict = read_dict("products.csv", PRODUCT_NUMBER_INDEX)

    except FileNotFoundError: 
        print("FILE NOT FOUND. Please check your filename. ")
        print()
        print_exception.PrintException() 
        print()        

    # Index numbers for values in requests.csv
    PRODUCT_NUMBER = 0
    QUANTITY = 1

    # Read each line of the csv file
    try:
        with open("request.csv", "rt") as requests_file:

            reader = csv.reader(requests_file)

            # skip the first row because it's header data
            next(reader)

            num_items = 0
            subtotal = 0
            for row_list in reader:

                product_key =  row_list[PRODUCT_NUMBER]

                try: 
                    product_name = products_dict[product_key][PRODUCT_NAME_INDEX]
                    quantity = row_list[QUANTITY]
                    product_price = products_dict[product_key][PRODUCT_PRICE_INDEX]
                except KeyError: 
                    print("********************")
                    print("Unable to locate the product you are looking for")
                    print()
                    print_exception.PrintException() 
                    print()
                    print("********************")

                # count the number of items in the list
                num_items += int(quantity)

                # The item amount times the quantity
                item_subtotal = float(product_price) * float(quantity)

                # Add each product and quantity to a subtotal
                subtotal += item_subtotal
                
                print(f"{product_name} {quantity} @ {product_price}")

    except (FileNotFoundError, PermissionError) as err: 
        print("FILE NOT FOUND. Please check your filename. ")
        print()
        print_exception.PrintException() 
        print()

    # Print receipt 
    print()
    print(f"Number of Items: {num_items}")    
    print(f"Subtotal: {round(subtotal, 2)}")

    # Only if today is Tuesday, add the discount
    subtotal = check_for_discount(subtotal, DISCOUNT)
    
    subtotal = round(subtotal, 2)    
    sales_tax = round(subtotal * SALES_TAX_RATE, 2)
    total = round(subtotal + sales_tax, 2)

    print(f"Sales Tax: {sales_tax}")
    print(f"Total: {total}")
    print()
    print(f"Thank you for shopping at {STORE_NAME}.")
    current_date_and_time = datetime.now()
    print(f"{current_date_and_time:%a %b %d %I:%M:%S %Y}")
    print()


def check_for_discount(subtotal, discount_rate):
    discount = 0
    TUESDAY = 1 
    if datetime.today().weekday() == TUESDAY:
        discount = round(subtotal * discount_rate, 2)
        print(f"Tuesday Discount: {discount}")
        subtotal = round(subtotal - discount, 2) 
        print(f"Subtotal with discount applied: {subtotal}")  

    return subtotal 


def read_dict(filename, key_column_index):
    """Read the contents of a CSV file into a compound
    dictionary and return the dictionary.

    Parameters
        filename: the name of the CSV file to read.
        key_column_index: the index of the column
            to use as the keys in the dictionary.
    Return: a compound dictionary that contains
        the contents of the CSV file.
    """
    # Create an empty dictionary that will
    # store the data from the CSV file.
    dictionary = {}

    # Open the CSV file for reading and store a reference
    # to the opened file in a variable named csv_file.
    with open(filename, "rt") as csv_file:

        # Use the csv module to create a reader object
        # that will read from the opened CSV file.
        reader = csv.reader(csv_file)

        # The first row of the CSV file contains column
        # headings and not data, so this statement skips
        # the first row of the CSV file.
        next(reader)

        # Read the rows in the CSV file one row at a time.
        # The reader object returns each row as a list.
        for row_list in reader:

            # If the current row is not blank, add the
            # data from the current to the dictionary.
            if len(row_list) != 0:

                # From the current row, retrieve the data
                # from the column that contains the key.
                key = row_list[key_column_index]

                # Store the data from the current
                # row into the dictionary.
                dictionary[key] = row_list

    # Return the dictionary.
    return dictionary


# Call main to start this program.
if __name__ == "__main__":
    main()