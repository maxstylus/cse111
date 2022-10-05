from datetime import datetime

"""
CSE 111 - Team Activity #1
Calculate the subtotal when 10% discounts are given on Tuesdays and Wednesdays
"""

# Get the day of the week in an integer. Use the dictionary to print the day of the week as string. 
day_of_week_string = {
    0 : "Monday",
    1 : "Tuesday",
    2 : "Wednesday",
    3 : "Thursday",
    4 : "Friday",
    5 : "Saturday",
    6 : "Sunday"
}

DISCOUNT_RATE = 0.10
SALES_TAX_RATE = 0.06

# Get the day of the week in an integer 0 - 6.
current_date_and_time = datetime.now()
weekday = current_date_and_time.weekday()

print(f"weekday: {weekday}")

# Print the day of the week for the user to see.
today = day_of_week_string[weekday]
print(f"Today is: {today}")

# Get the order subtotal
subtotal = float(input("Please enter the subtotal: "))
   
# 10% discount for being Tuesday or Wednesday
discount = round((subtotal * DISCOUNT_RATE), 2)


if subtotal >= 50 and (weekday == 1 or weekday == 2): 
    
    print(f"Discount amount: {discount}")
    discounted_subtotal = subtotal - discount 

    # Sales tax calculated off of new subtotal (after discount)
    sales_tax = round((discounted_subtotal * SALES_TAX_RATE), 2)
    print(f"Sales tax amount: {sales_tax}")

    total = round(discounted_subtotal + sales_tax, 2)
    print(f"Total: {total}")
else:
    # Sales tax calcuated against discount only (no disount)
    sales_tax = round(subtotal * SALES_TAX_RATE, 2)
    print(f"Sales tax amount: {sales_tax}")

    total = round((subtotal + sales_tax), 2)
    print(f"Total: {total}")












