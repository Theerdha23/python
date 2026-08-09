# from functools import reduce
#
# # List of employee salaries
# salaries = [25000, 32000, 45000, 28000, 50000, 35000,2]
#
# # Step 1: Filter salaries greater than ₹30,000
# filtered_salaries = list(filter(lambda x: x > 30000, salaries))
#
# # Step 2: Increase each salary by 15%
# updated_salaries = list(map(lambda x: x * 1.15, filtered_salaries))
#
# # Step 3: Compute the total salary expenditure
# total_expenditure = reduce(lambda x, y: x + y, updated_salaries)+reduce(lambda x,y : x + y, list(filter(lambda x:x<3000,salaries)))
# print(total_expenditure)
#
# # Output
# print("Original Salaries:", salaries)
# print("Filtered Salaries (>₹30,000):", filtered_salaries)
# print("Updated Salaries (15% Increase):", updated_salaries)
# print("Total Salary Expenditure: ₹", total_expenditure)

# from functools import reduce
#
# # List of product prices
# prices = [250, 600, 1200, 450, 800, 1500]
#
# # Step 1: Filter products priced above ₹500
# filtered_prices = list(filter(lambda x: x > 500, prices))
#
# # Step 2: Apply a 10% discount
# discounted_prices = list(map(lambda x: x * 0.90, filtered_prices))
#
# # Step 3: Calculate the total bill amount
# total_bill = reduce(lambda x, y: x + y, discounted_prices)
#
# # Output
# print("Original Prices:", prices)
# print("Filtered Prices (>₹500):", filtered_prices)
# print("Discounted Prices (10% Off):", discounted_prices)
# print("Total Bill Amount: ₹", total_bill)