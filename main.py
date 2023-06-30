class Snack:
    def __init__(self, snack_id, name, price, available):
        self.snack_id = snack_id
        self.name = name
        self.price = price
        self.available = available


class Canteen:
    def __init__(self):
        self.inventory = []
        self.sales_records = []

    def add_snack(self, snack):
        self.inventory.append(snack)
        print("Snack added to the inventory.")

    def remove_snack(self, snack_id):
        for snack in self.inventory:
            if snack.snack_id == snack_id:
                self.inventory.remove(snack)
                print("Snack removed from the inventory.")
                return
        print("Snack not found in the inventory.")

    def update_availability(self, snack_id, availability):
        for snack in self.inventory:
            if snack.snack_id == snack_id:
                snack.available = availability
                print("Availability updated.")
                return
        print("Snack not found in the inventory.")

    def sell_snack(self, snack_id):
        for snack in self.inventory:
            if snack.snack_id == snack_id:
                if snack.available:
                    snack.available = False
                    self.sales_records.append(snack)
                    print("Snack sold.")
                    return
                else:
                    print("Snack is not available.")
                    return
        print("Snack not found in the inventory.")

    def display_inventory(self):
        print("Snack Inventory:")
        for snack in self.inventory:
            print(f"ID: {snack.snack_id}\tName: {snack.name}\tPrice: {snack.price}\tAvailable: {snack.available}")

    def display_sales_records(self):
        print("Sales Records:")
        for snack in self.sales_records:
            print(f"ID: {snack.snack_id}\tName: {snack.name}\tPrice: {snack.price}")


def main():
    canteen = Canteen()

    while True:
        print("\n===== Mumbai Munchies Canteen =====")
        print("1. Add Snack")
        print("2. Remove Snack")
        print("3. Update Snack Availability")
        print("4. Sell Snack")
        print("5. Display Inventory")
        print("6. Display Sales Records")
        print("0. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            try:
                snack_id = input("Enter Snack ID: ")
                name = input("Enter Snack Name: ")
                price = float(input("Enter Snack Price: "))
                available = input("Is Snack Available? (yes/no): ").lower()
                if available not in ['yes', 'no']:
                    raise ValueError("Invalid availability input. Please enter 'yes' or 'no'.")
                snack = Snack(snack_id, name, price, available == 'yes')
                canteen.add_snack(snack)
            except ValueError as e:
                print(str(e))
            except Exception as e:
                print("An error occurred:", str(e))

        elif choice == '2':
            try:
                snack_id = input("Enter Snack ID to remove: ")
                canteen.remove_snack(snack_id)
            except Exception as e:
                print("An error occurred:", str(e))

        elif choice == '3':
            try:
                snack_id = input("Enter Snack ID to update availability: ")
                availability = input("Is Snack Available? (yes/no): ").lower()
                if availability not in ['yes', 'no']:
                    raise ValueError("Invalid availability input. Please enter 'yes' or 'no'.")
                canteen.update_availability(snack_id, availability == 'yes')
            except ValueError as e:
                print(str(e))
            except Exception as e:
                print("An error occurred:", str(e))

        elif choice == '4':
            try:
                snack_id = input("Enter Snack ID to sell: ")
                canteen.sell_snack(snack_id)
            except Exception as e:
                print("An error occurred:", str(e))

        elif choice == '5':
            canteen.display_inventory()

        elif choice == '6':
            canteen.display_sales_records()

        elif choice == '0':
            print("Exiting the application...")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
