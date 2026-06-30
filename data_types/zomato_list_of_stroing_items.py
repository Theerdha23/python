user_name = "theerdha"
order_id = 123432532
location= "KPHB"
order_items= ["dossa","tea"]
order_items.append("snacks")
restaurants={'babai hotel','andhra hotel'}
restaurants.add('chandra hotel')
order_details={
    'user_name':"theerdha",
'order_id':1234324,
'location':"KPHB",
 'total_bill ' :750,
 'location':"KPHB",
 'restaurants':restaurants,

}
print("\n------order_details------")

for i in order_details:
    print(i , ':', order_details[i])

# #Zomato-like Food Ordering System (Dynamic)
#
# # Initialize user details
# user_name = input("Enter your name: ")
# order_id = int(input("Enter your order ID: "))
# location = input("Enter your delivery location: ")
#
# # Ordered food items (list)
# order_items = []
# while True:
#     item = input("Add a food item (or type 'done' to finish): ")
#     if item.lower() == "done":
#         break
#     order_items.append(item)
#
# # Restaurants (set ensures no duplicates)
# restaurants = set()
# while True:
#     rest = input("Add a restaurant (or type 'done' to finish): ")
#     if rest.lower() == "done":
#         break
#     restaurants.add(rest)
#
# # Order details dictionary
# order_details = {
#     "user_name": user_name,
#     "order_id": order_id,
#     "location": location,
#     "items": order_items,
#     "restaurants": restaurants,
#     "total_bill": float(input("Enter total bill amount: ")),
#     "order_status": "Confirmed"
# }
#
# # Display order details
# print("\n--- Order Details ---")
# for key, value in order_details.items():
#     print(key, ":", value)
#
