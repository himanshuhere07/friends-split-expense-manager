# Friends split - Roommate Expense Manager

A simple command-line tool to track shared expenses between PG/hostel roommates and figure out who owes who.

I built this because I'm moving into a PG with my friend for college and we already know we're going to lose track of who paid for what (groceries, wifi bill, electricity etc). Instead of doing it on paper or fighting about it later, I made this.

## What it does

- Add an expense (who paid, how much, what for, split between whom)
- Show all logged expenses with running total
- Calculate balances - tells you who should receive money and who owes money
- Category wise spending breakdown (groceries vs bills vs other stuff)
- Shows who has paid the most overall
- Search expenses by category

## How it works

Every expense is stored as a dictionary with the payer, amount, category and who it's split between. The split is stored as a tuple since once you log an expense, the people it was split between shouldn't be changed. All the expenses live inside a list, and roommates are stored in a set so the same person can't accidentally get added twice.

Balances are calculated by looping through every expense - the payer gets credited the full amount, and everyone included in the split gets their share deducted. Whatever's left over per person is their balance (positive means they're owed money, negative means they owe).

## Concepts used

- Dictionaries (expense records, balance tracking)
- Lists (storing all expenses)
- Tuples (immutable split-between records)
- Sets (roommate list, no duplicates)
- Functions (one function per feature)
- Loops and conditionals
- f-strings for all the output formatting
- Basic error handling (try/except for invalid number input)

No external libraries, no file handling, no OOP - kept it to what I've actually learned so far.

## How to run

```
python main.py
```

You'll get a menu with 6 options. Comes preloaded with 3 sample expenses between two roommates (Himanshu and Aryan) so you can see how it works immediately, then you can add your own.

## Sample output

```
--- Balance Summary ---
Aryan owes Rs.175.0
Himanshu should receive Rs.175.0
```

