from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from . import metrics


@login_required
def dashboard(request):
    transactions = metrics.get_calculate_transactions(request.user)
    category_data = metrics.get_category_data(request.user)

    context = {
        'total_income': transactions['total_income'],
        'total_expense': transactions['total_expense'],
        'balance': transactions['balance'],
        'recent_transactions': transactions['recent_transactions'],
        'category_labels': category_data['category_labels'],
        'category_values': category_data['category_values'],    
    }
    return render(request, 'dashboard.html', context)
    