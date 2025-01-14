from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from . import metrics


@login_required
def dashboard(request):
    transactions = metrics.get_calculate_transactions(request.user)
    expense_months = metrics.get_expense_months(request.user)

    context = {
        'total_income': transactions['total_income'],
        'total_expense': transactions['total_expense'],
        'balance': transactions['balance'],
        'recent_transactions': transactions['recent_transactions'],
        'months': expense_months['months'],
        'totals': expense_months['totals'],
    }
    return render(request, 'dashboard.html', context)
