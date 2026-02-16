user = input("Enter you want to check celsius/fahrenheit in (c/f): ").lower()

if user == 'c':
    # This block converts Fahrenheit TO Celsius
    a = float(input("Enter the fahrenheit value: "))
    d = (a - 32) * (5/9)
    # Use f-string formatting :.2f for a clean output
    print(f"The celsius of your place is {d:.2f}°C")
elif user == 'f':
    # This block converts Celsius TO Fahrenheit
    b = float(input("enter the celsius value: "))
    e = (b * (9/5)) + 32
    print(f"The fahrenheit of your place is {e:.2f}°F")
else:
    print("Invalid option selected.")
