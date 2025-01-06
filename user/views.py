from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import CustomCreationForm
from django.contrib import messages

def register(request):
    if request.method == 'POST':
        form = CustomCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, f'Conta criada com sucesso! Bem-vindo(a), {user.username}')
            login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request, 'Erro ao criar conta. Verifique os dados fornecidos.')
    else:
        form = CustomCreationForm()
    return render(request, 'register.html', {'form': form})
