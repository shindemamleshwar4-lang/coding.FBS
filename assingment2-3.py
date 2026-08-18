#convert distant give in feet and inches into meter and centimeter.
feet = int(input("Enter feets:-"))
inches = int(input("Enter inches:-"))

total_inches = (feet * 12)+ inches

centimeter = total_inches * 2.54
meter = centimeter / 100

print("meter:-",meter)
print("centimeter:-",centimeter)