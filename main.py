# Friends split - Roommate Expense Manager
# Made this after moving into a PG with my roommate, we kept fighting over
# who paid for what last month lol. So built a simple tracker for it.
# Uses only core python stuff - dicts, lists, tuples, sets, loops, functions.

# people staying in the PG (using a set so no duplicate names accidentally get added)
roommates = {"Himanshu", "Aryan"}

# every expense is stored as a dictionary inside this list
# split_between is a tuple because once an expense is logged, who it was split
# between shouldn't change - tuples are immutable so that fits
expenses = []

# some starter data so the program has something to show when you run it
expenses.append({
    "payer": "Himanshu",
    "amount": 600,
    "category": "Groceries",
    "split_between": ("Himanshu", "Aryan")
})
expenses.append({
    "payer": "Aryan",
    "amount": 450,
    "category": "Electricity Bill",
    "split_between": ("Himanshu", "Aryan")
})
expenses.append({
    "payer": "Himanshu",
    "amount": 200,
    "category": "Wifi Recharge",
    "split_between": ("Himanshu", "Aryan")
})


def add_expense():
    payer = input("Who paid? ").strip().title()

    if payer not in roommates:
        add = input(f"{payer} is not in the roommate list yet. Add them? (y/n) ").lower()
        if add == "y":
            roommates.add(payer)
        else:
            print("Cancelled.\n")
            return

    try:
        amount = float(input("How much did they pay? Rs. "))
    except ValueError:
        print("That's not a valid number, try again.\n")
        return

    category = input("What was it for? (Groceries/Rent/Wifi/etc) ").strip().title()

    print(f"Split between everyone? Current roommates: {', '.join(roommates)}")
    split_input = input("Enter names separated by comma (or press enter for everyone): ")

    if split_input.strip() == "":
        split_between = tuple(roommates)
    else:
        names = [name.strip().title() for name in split_input.split(",")]
        split_between = tuple(names)

    new_expense = {
        "payer": payer,
        "amount": amount,
        "category": category,
        "split_between": split_between
    }
    expenses.append(new_expense)
    print(f"Added! {payer} paid Rs.{amount} for {category}\n")


def show_all_expenses():
    if len(expenses) == 0:
        print("No expenses logged yet.\n")
        return

    print("\n--- All Expenses ---")
    total = 0
    for i in range(len(expenses)):
        e = expenses[i]
        people_in_split = ", ".join(e["split_between"])
        print(f"{i+1}. {e['payer']} paid Rs.{e['amount']} for {e['category']} (split: {people_in_split})")
        total += e["amount"]
    print(f"Total spent so far: Rs.{total}\n")


def calculate_balances():
    # start everyone at 0
    balances = {}
    for person in roommates:
        balances[person] = 0

    for e in expenses:
        payer = e["payer"]
        amount = e["amount"]
        split_between = e["split_between"]
        share = amount / len(split_between)

        # payer gets credited the full amount (they spent it)
        balances[payer] = balances.get(payer, 0) + amount

        # everyone in the split (including payer) owes their share
        for person in split_between:
            balances[person] = balances.get(person, 0) - share

    return balances


def show_balances():
    balances = calculate_balances()
    print("\n--- Balance Summary ---")
    for person, amount in balances.items():
        amount = round(amount, 2)
        if amount > 0:
            print(f"{person} should receive Rs.{amount}")
        elif amount < 0:
            print(f"{person} owes Rs.{abs(amount)}")
        else:
            print(f"{person} is all settled up")
    print()


def category_summary():
    # dictionary to hold total per category
    totals = {}
    for e in expenses:
        cat = e["category"]
        if cat in totals:
            totals[cat] += e["amount"]
        else:
            totals[cat] = e["amount"]

    if len(totals) == 0:
        print("No expenses yet.\n")
        return

    print("\n--- Category Wise Spending ---")
    # sorted() so highest spend category shows first
    sorted_categories = sorted(totals.items(), key=lambda x: x[1], reverse=True)
    for category, amount in sorted_categories:
        print(f"{category}: Rs.{amount}")
    print()


def who_paid_most():
    balances = {}
    for e in expenses:
        payer = e["payer"]
        balances[payer] = balances.get(payer, 0) + e["amount"]

    if len(balances) == 0:
        print("No data yet.\n")
        return

    top_spender = max(balances, key=balances.get)
    print(f"\n{top_spender} has paid the most overall - Rs.{balances[top_spender]}\n")


def main_menu():
    while True:
        print("===== PG SPLIT MENU =====")
        print("1. Add an expense")
        print("2. Show all expenses")
        print("3. Show who owes what")
        print("4. Category wise spending")
        print("5. Who paid the most")
        print("6. Exit")

        choice = input("Enter choice (1-6): ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            show_all_expenses()
        elif choice == "3":
            show_balances()
        elif choice == "4":
            category_summary()
        elif choice == "5":
            who_paid_most()
        elif choice == "6":
            print("Bye! Settle up before someone gets annoyed.")
            break
        else:
            print("Enter a number between 1 and 6.\n")


if __name__ == "__main__":
    main_menu()
