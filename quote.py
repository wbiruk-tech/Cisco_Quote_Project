# This is a comment. Python ignores lines starting with #
firewall_price = 5000
quantity = 2
tax_rate = 0.15

subtotal = firewall_price * quantity
total = subtotal + (subtotal * tax_rate)

print("The total price for the client is:", total, "USD")