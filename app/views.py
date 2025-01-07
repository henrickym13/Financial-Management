from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from transaction.models import Transaction
from category.models import Category
from django.db.models import Count


@login_required
def dashboard(request):
    transactions = Transaction.objects.filter(user=request.user).order_by('-date')
    total_income = sum(t.amount for t in transactions if t.type_choice == 'income')
    total_expense = sum(t.amount for t in transactions if t.type_choice == 'expense')
    balance = total_income - total_expense

    popular_categories = Category.objects.filter(user=request.user).annotate(
        total_transactions=Count('transaction')
    ).order_by('-total_transactions')[:5]

    recent_transactions = transactions[:5]

    context = {
        'total_income': total_income,
        'total_expense': total_expense,
        'balance': balance,
        'popular_categories': popular_categories,
        'recent_transactions': recent_transactions,
    }
    return render(request, 'dashboard.html', context)
    