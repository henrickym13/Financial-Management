from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Transaction
from .forms import TransactionForm, TransactionFilterForm


# Create your views here.
@login_required
def transaction_list(request):
    transactions = Transaction.objects.filter(user=request.user).order_by('-date')

    # filters
    form = TransactionFilterForm(request.GET)
    if form.is_valid():
        start_date = form.cleaned_data.get('start_date')
        end_date = form.cleaned_data.get('end_date')
        transaction_type = form.cleaned_data.get('type_choice')
        category = form.cleaned_data.get('category')

        if start_date:
            transactions = transactions.objects.filter(date__gte=start_date)
        if end_date:
            transactions = transactions.objects.filter(date__lte=end_date)
        if transaction_type:
            transactions = transactions.objects.filter(type_choice=transaction_type)
        if category:
            transactions = transactions.objects.filter(category__icontains=category)
        
        context = {
            'transactions': transactions,
            'form': form,
        }
    return render(request, 'transaction_list.html', context)


@login_required
def transaction_add(request):
    if request.method == 'POST':
        form = TransactionForm(request.POST)
        if form.is_valid():
            transaction = form.save(commit=False)
            transaction.user = request.user
            transaction.save()
            messages.success(request, 'Transação adicionada com sucesso!')
            return redirect('transaction_list')
    else:
        form = TransactionForm()
    return render(request, 'transaction_add.html', {'form': form})


@login_required
def transaction_edit(request, pk):
    transaction = get_object_or_404(Transaction, pk=pk, user=request.user)
    if request.method == 'POST':
        form = TransactionForm(request.POST, instance=transaction)
        if form.is_valid():
            form.save()
            messages.success(request, 'Transação atualizada com sucesso!')
            return redirect('transaction_list')
    else:
        form = TransactionForm(instance=transaction)
    return render(request, 'transaction_edit.html', {'form': form})


@login_required
def transaction_delete(request, pk):
    transaction = get_object_or_404(Transaction, pk=pk, user=request.user)
    if request.method == 'POST':
        transaction.delete()
        messages.success(request, 'Transação excluída com sucesso!')
        return redirect('transaction_list')
    return render(request, 'transaction_delete.html', {'transaction': transaction})