

customer_details = ('theerdha', 555)
add_to_cart = ['laptop','phone']
brands = {'hp','apple'
}
order_details = {
    'customer_details':customer_details,
     'brands' : brands,
     'total_price':8899,
    'delivery_status': "within 7 days"
}
print("\n------order_details------")
for i in order_details:
    print(i , ':', order_details[i])

# Flipkart-like Shopping Cart System (Interactive)

# # Taking immutable user details as input (tuple)
# name = input("Enter customer name: ")
# customer_id = int(input("Enter customer ID: "))
# customer_details = (name, customer_id)
#
# # Mutable cart items (list)
# add_to_cart = []
# n = int(input("How many products do you want to add to cart? "))
# for i in range(n):
#     product = input(f"Enter product {i+1}: ")
#     add_to_cart.append(product)
#
# # Unique brands (set)
# brands = set()
# m = int(input("How many brands do you want to add? "))
# for i in range(m):
#     brand = input(f"Enter brand {i+1}: ")
#     brands.add(brand)
#
# # Order summary (dictionary)
# total_price = int(input("Enter total price: "))
# delivery_status = input("Enter delivery status: ")
#
# order_details = {
#     "customer_details": customer_details,
#     "cart_items": add_to_cart,
#     "brands": brands,
#     "total_price": total_price,
#     "delivery_status": delivery_status
# }
#
# # Display order details
# print("\n------ Order Details ------")
# for key in order_details:
#     print(key, ":", order_details[key])