from category.models import Category
from transaction.models import Transaction
from django.db.models import Sum
import json


def get_calculate_transactions(user):
    transactions = Transaction.objects.filter(user=user).order_by('-date')
    total_income = sum(t.amount for t in transactions if t.type_choice == 'income')
    total_expense = sum(t.amount for t in transactions if t.type_choice == 'expense')
    balance = total_income - total_expense
    recent_transactions = transactions[:5]

    type_transaction = list({
        item for transaction in transactions for item in dict(transaction.TRANSACTION_TYPES).values()})
    print(type_transaction)

    return dict(
        total_income = total_income,
        total_expense = total_expense,
        balance = balance,
        recent_transactions = recent_transactions,
    )
