from .models import Transaction
from django.db.models import Q
from django.db.models.functions import TruncMonth
from django.db.models import Sum


def get_months_name(pos):
    months = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho',
              'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']
    
    return months[pos - 1]


def get_monthly_summary(user):
    return Transaction.objects.filter(user=user).annotate(
        month=TruncMonth('date')
    ).values('month').annotate(
        total_expenses=Sum('amount', filter=Q(type_choice='expense')),
        total_income=Sum('amount', filter=Q(type_choice='income'))
    ).order_by('-month')


def get_monthly_history(user, year, month):
    transaction_history = Transaction.objects.filter(
        user=user,
        date__year=year,
        date__month=month
    ).order_by('-date')

    total_income = transaction_history.filter(type_choice='income').aggregate(Sum('amount'))['amount__sum'] or 0
    total_expense = transaction_history.filter(type_choice='expense').aggregate(Sum('amount'))['amount__sum'] or 0
    net_value = total_income - total_expense

    months = get_months_name(month)

    return dict(
        transaction_history = transaction_history,
        total_income = total_income,
        total_expense = total_expense,
        net_value = net_value,
        month = months,
        year = year,
    )