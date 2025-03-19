def main():
    # Initialize an empty dictionary to store fruit data
    fruits = {}

    # Get the number of fruits to input
    num_fruits = int(input("How many fruits would you like to enter? "))

    # Collect data for each fruit
    for _ in range(num_fruits):
        name = input("Enter the fruit's name: ").strip()
        color = input(f"Enter the color of {name}: ").strip()
        weight = float(input(f"Enter the average weight of {name} (in lbs): "))
        price = float(input(f"Enter the price per pound of {name} ($): "))

        # Store the data in the dictionary
        fruits[name] = {
            'Color': color,
            'Average Weight': weight,
            'Price per Pound': price
        }

    # Output the fruit data
    print("\nFruit Data Overview:\n")
    for fruit, details in fruits.items():
        print(f"Fruit: {fruit}")
        print(f"Color: {details['Color']}")
        print(f"Average Weight: {details['Average Weight']} lbs")
        print(f"Price per Pound: ${details['Price per Pound']}")
        print("-" * 20)

if __name__ == "__main__":
    main()

