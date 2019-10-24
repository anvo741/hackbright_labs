melon_cost = 1.00

# Define function that takes an order text file.
def get_unexpected_payments(order_file):
  # Open the text file.
  the_file = open(order_file)
  
  for line in the_file:
    # Split each line in the file with | delimiter
    words = line.split('|')

    # Store relevant variables from order file.
    customer_name = words[1]
    melon_count = float(words[2])
    actual_payment = float(words[3])

    # Calculate expected payment.
    expected_payment = melon_count * melon_cost
  
    if expected_payment != actual_payment:
        print (f"{customer_name} paid ${actual_payment:.2f},",
               f"expected ${expected_payment:.2f}"
               )

get_unexpected_payments("customer-orders.txt")
