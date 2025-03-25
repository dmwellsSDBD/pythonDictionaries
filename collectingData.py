def collect_data():
    outer_dict = {}
    print("Let's build a nested dictionary. Enter 'done' when you are finished adding categories.")
    
    while True:
        category = input("\nEnter a category (e.g., 'Books', 'Movies'): ").strip()
        if category.lower() == 'done':
            break

        if category not in outer_dict:
            outer_dict[category] = {}

        print(f"Adding items to the category '{category}'. Enter 'done' when you are finished adding items to this category.")
        while True:
            item = input("\nEnter an item name for this category (e.g., 'Harry Potter', 'Inception'): ").strip()
            if item.lower() == 'done':
                break

            detail = input(f"Enter details for the item '{item}' (e.g., price, year): ")
            outer_dict[category][item] = detail

    return outer_dict

def display_nested_dict(nested_dict):
    print("\nNested Dictionary Contents:")
    for category, items in nested_dict.items():
        print(f"\nCategory: {category}")
        for item, detail in items.items():
            print(f"  {item}: {detail}")

# Main function to run the program
if __name__ == "__main__":
    nested_dict = collect_data()
    display_nested_dict(nested_dict)

    # Outer while loop to create main dictionary with a Key
    # The Key for the main dictionary can be anything: Movies, Books, Records, etc



        # Inner While loop to create nested dictionary for the Value of the main Key
        # This dictionary will be made up of it's own Key:Value pairs