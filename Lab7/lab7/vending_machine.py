def parse_coins(coins_csv):
    if not isinstance(coins_csv, str) or not coins_csv.strip():
        raise ValueError("Invalid coin input")

    try:
        coins = [int(c.strip()) for c in coins_csv.split(',')]
    except ValueError:
        raise ValueError("Coin values must be integers")

    if any(c <= 0 for c in coins):
        raise ValueError("Coin values must be positive")

    return coins


def slot_position(code):
    if not isinstance(code, str):
        raise ValueError("Slot code must be a string")

    code = code.strip().upper()

    if len(code) < 2:
        raise ValueError("Invalid slot code")

    if not ('A' <= code[0] <= 'Z'):
        raise ValueError("Invalid row")

    if not code[1:].isdigit():
        raise ValueError("Invalid column")

    column_number = int(code[1:])

    if column_number <= 0:
        raise ValueError("Column must be positive")

    row = ord(code[0]) - ord('A')
    column = column_number - 1

    return row, column


def change_due(payment):
    if not isinstance(payment, str):
        raise ValueError("Payment must be a string")

    parts = payment.split('/')

    if len(parts) != 2:
        raise ValueError("Use paid/price format")

    try:
        paid = int(parts[0].strip())
        price = int(parts[1].strip())
    except ValueError:
        raise ValueError("Paid and price must be integers")

    if paid < 0 or price < 0:
        raise ValueError("Amounts cannot be negative")

    if paid < price:
        raise ValueError("Insufficient payment")

    change = paid - price
    return str(change // 5) + ' five-coins'


def main():
    print("==== Running parse_coins ====")
    user_input = input("Enter coin values as CSV (e.g. 5,10,25): ")
    try:
        print("Coins:", parse_coins(user_input))
    except ValueError as e:
        print("Error:", e)

    print("\n==== Running slot_position ====")
    user_input = input("Enter a slot code (e.g. B7): ")
    try:
        print("Row and Column:", slot_position(user_input))
    except ValueError as e:
        print("Error:", e)

    print("\n==== Running change_due ====")
    user_input = input("Enter paid/price (e.g. 200/150): ")
    try:
        print("Change Due:", change_due(user_input))
    except ValueError as e:
        print("Error:", e)


if __name__ == "__main__":
    main()
