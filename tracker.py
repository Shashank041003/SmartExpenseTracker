import pandas as pd

def add_expense(date, category, amount, payment_method, notes):
    new_entry = {
        'date': date,
        'category': category,
        'amount': amount,
        'payment_method': payment_method,
        'notes': notes
    }

    try:
        df = pd.read_csv('expenses.csv')
    except FileNotFoundError:
        df = pd.DataFrame(columns=['date', 'category', 'amount', 'payment_method', 'notes'])

    df = pd.concat([df, pd.DataFrame([new_entry])], ignore_index=True)
    df.to_csv('expenses.csv', index=False)
    print("✅ Expense added successfully!")

# Test entry
add_expense('2025-08-25', 'Food', 150, 'Cash', 'Lunch at canteen')

def weekly_summary():
    # Step 1: Read CSV file
    df = pd.read_csv('expenses.csv')

    # Step 2: Convert 'date' column to datetime format
    df['date'] = pd.to_datetime(df['date'])

    # Step 3: Extract week number and year
    df['week'] = df['date'].dt.isocalendar().week
    df['year'] = df['date'].dt.year

    # Step 4: Group by year, week, and category
    summary = df.groupby(['year', 'week', 'category'])['amount'].sum().reset_index()

    # Step 5: Print result
    print("\n📅 Weekly Expense Summary:\n")
    print(summary)

def monthly_summary():
    # Step 1: Read CSV file
    df = pd.read_csv('expenses.csv')

    # Step 2: Convert 'date' column to datetime format
    df['date'] = pd.to_datetime(df['date'])

    # Step 3: Extract month and year
    df['month'] = df['date'].dt.month
    df['year'] = df['date'].dt.year

    # Step 4: Group by year, month, and category
    summary = df.groupby(['year', 'month', 'category'])['amount'].sum().reset_index()

    # Step 5: Print result
    print("\n📅 Monthly Expense Summary:\n")
    print(summary)

weekly_summary()
monthly_summary()
