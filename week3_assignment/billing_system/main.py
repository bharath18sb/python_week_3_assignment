from models import Item, Invoice

def main():
    invoice = Invoice(tax_rate=18)

    while True:
        print("\n=== BILLING SYSTEM ===")
        print("1. Add Product")
        print("2. Generate Final Bill")
        print("3. Exit")
        choice = input("Enter choice: ")

        if choice == '1':
            name = input("Product Name: ")
            try:
                price = float(input("Price: "))
                qty = int(input("Quantity: "))
                item = Item(name, price, qty)
                invoice.add_item(item)
                print("Item added.")
            except ValueError as e:
                print(f"Error: {e}")
        elif choice == '2':
            print("\n" + "="*50)
            print("FINAL BILL")
            print("="*50)
            print(f"{'Product':<15} {'Price':<10} {'Qty':<5} {'Total':<10}")
            for item in invoice.items:
                print(f"{item.name:<15} {item.price:<10.2f} {item.quantity:<5} {item.get_total():<10.2f}")
            print("-" * 50)
            subtotal = invoice.calculate_subtotal()
            print(f"Subtotal: {subtotal:>35.2f}")
            print(f"Tax (18%): {invoice.calculate_tax():>35.2f}")
            print(f"Grand Total: {invoice.calculate_total():>35.2f}")
            print("="*50)
        elif choice == '3':
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
