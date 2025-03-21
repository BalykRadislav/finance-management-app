from datetime import datetime, timedelta

def days_until_end_of_month():
    today = datetime.today()
    next_month = today.replace(day=28) + timedelta(days=4)
    end_of_month = next_month - timedelta(days=next_month.day)
    return (end_of_month - today).days

def calculate_budget_remaining(budget, spent):
    days_left = days_until_end_of_month()
    daily_budget = (budget - spent) / days_left
    return daily_budget, days_left

def days_until_end_of_week():
    today = datetime.today()
    end_of_week = today + timedelta(days=(6-today.weekday()))
    return (end_of_week - today).days


def filter_transactions_by_date(transactions, start_date, end_date):
    for transaction_id, details in transactions.items():
        transaction_date = datetime.strptime(details['date'], "%Y-%m-%d")
        if start_date <= transaction_date <= end_date:
            yield transaction_id, details

def generate_monthly_report(transactions, year, month):
    start_date = datetime(year, month, 1)
    end_date = start_date + timedelta(days=32)
    end_date = end_date.replace(day=1) - timedelta(days=1)

    report = []
    total_income = 0
    total_expenses = 0

    for transaction_id, details in filter_transactions_by_date(transactions, start_date, end_date):
        amount = details['amount']
        category = details['category']
        report.append(f"ID: {transaction_id}, Дата: {details['date']}, Сума: {amount}, Категорія: {category}")
        if amount > 0:
            total_income += amount
        else:
            total_expenses += abs(amount)
    report_summary = f"\nЗвіт за {year}-{month}:\n"
    report_summary += f"Загальний дохід: {total_income}\n"
    report_summary += f"Загальні витрати: {total_expenses}\n"
    report_summary += f"Чистий дохід: {total_income - total_expenses}\n"
    return "\n".join(report) + report_summary

def export_report_to_file(report, filename):
    with open(filename, 'w') as file:
        file.write(report)
    print(f"Звіт успішно збережено у файл {filename}")


monthly_budget = 1500
spent_so_far = 750

daily_budget, days_left_in_month = calculate_budget_remaining(monthly_budget, spent_so_far)
print(f"Залишок бюджету на день до кінця місяця: {daily_budget:.2f} грн, Днів до кінця місяця: {days_left_in_month}")

days_left_in_week = days_until_end_of_week()
print(f"Днів до кінця тижня: {days_left_in_week}")