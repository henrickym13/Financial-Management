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


def get_category_data(user):
    category_data = Category.objects.filter(user=user).annotate(
        total_amount=Sum('transaction__amount')
    ).order_by('-total_amount')

    category_labels = [category.name for category in category_data if (category.total_amount or 0) > 0]
    category_values = [float(category.total_amount) or 0 for category in category_data if (category.total_amount or 0) > 0]
    
    return dict(
        category_labels = json.dumps(category_labels),
        category_values = json.dumps(category_values),
    )