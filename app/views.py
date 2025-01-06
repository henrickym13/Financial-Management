from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from transaction.models import Transaction


@login_required
def dashboard(request):
    transactions = Transaction.objects.filter(user=request.user).order_by('-date')
    total_income = sum(t.amount for t in transactions if t.type == 'income')
    total_expense = sum(t.amount for t in transactions if t.type == 'expense')
    balance = total_income - total_expense

    context = {
        'transactions': transactions[:5],
        'total_income': total_income,
        'total_expense': total_expense,
        'balance': balance,
    }
    return render(request, 'dashboard.html', context)
    