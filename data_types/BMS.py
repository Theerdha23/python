import copy

print("===== BOOK MY SHOW APPLICATION =====")

# Original seat details
seats = [
    {"seat": "A1", "category": {"type": "Gold", "price": 300}},
    {"seat": "A2", "category": {"type": "Gold", "price": 300}},
    {"seat": "B1", "category": {"type": "Silver", "price": 200}},
]




shallow_booking = copy.copy(seats)

# Modify nested data
shallow_booking[0]["category"]["price"] = 350



if seats[0]["category"]["price"] == 350:
    print("\nBooking affected! Original data also changed because of Shallow Copy.")

# ---------------- DEEP COPY ----------------
print("\n===== DEEP COPY =====")

deep_booking = copy.deepcopy(seats)

# Modify nested data
deep_booking[1]["category"]["price"] = 400

print("\nAfter modifying price in Deep Copy:")

print("\nDeep Copy:")
for seat in deep_booking:
    print(seat)

print("\nOriginal List:")
for seat in seats:
    print(seat)

if seats[1]["category"]["price"] != 400:
    print("\nOriginal booking is NOT affected because Deep Copy creates an independent copy.")