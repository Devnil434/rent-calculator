# # Rent Calculator

rent = int(input("Enter your hostel/flat rent = "))
food = int(input("Enter the amount of food ordered = "))
electricity_spend = int(input("Electricity you've spent = "))
charge_per_unit = int(input("Enter the charge per unit = "))
persons = int(input("Enter the no of persons living in room/flat = "))

total_bill = electricity_spend * charge_per_unit


# # output will be:

# output = (food + rent + total_bill) / persons

# print("Each person will pay = ", output)