from transaction.models import Transaction
from django.db.models import Sum
from django.db.models.functions import TruncMonth


def get_calculate_transactions(user):
    transactions = Transaction.objects.filter(user=user).order_by('-date')
    total_income = sum(t.amount for t in transactions if t.type_choice == 'income')
    total_expense = sum(t.amount for t in transactions if t.type_choice == 'expense')
    balance = total_income - total_expense
    recent_transactions = transactions[:5]

    type_transaction = list({
        item for transaction in transactions for item in dict(transaction.TRANSACTION_TYPES).values()})

    return dict(
        total_income = total_income,
        total_expense = total_expense,
        balance = balance,
        recent_transactions = recent_transactions,
    )


def get_expense_months(user):
    transactions = Transaction.objects.filter(user=user, type_choice='expense')

    monthly_expenses = transactions.annotate(month=TruncMonth('date')).values('month').annotate(
        total=Sum('amount'))
    
    months = [expense['month'].strftime('%B/%Y') for expense in monthly_expenses]
    totals = [expense['total'] for expense in monthly_expenses]
    
    return dict(
        months=months,
        totals=totals
    )