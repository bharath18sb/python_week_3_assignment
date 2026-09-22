import math
import random
import datetime

def demonstrate_libraries():
    print("--- Python Standard Library Demo ---")

    # Math module
    print("\n[Math]")
    print(f"Square root of 16: {math.sqrt(16)}")
    print(f"Pi: {math.pi:.4f}")

    # Random module
    print("\n[Random]")
    print(f"Random integer (1-10): {random.randint(1, 10)}")
    items = ["Apple", "Banana", "Cherry"]
    print(f"Random selection: {random.choice(items)}")

    # Datetime module
    print("\n[Datetime]")
    now = datetime.datetime.now()
    print(f"Current Date/Time: {now.strftime('%Y-%m-%d %H:%M:%S')}")

if __name__ == "__main__":
    demonstrate_libraries()
