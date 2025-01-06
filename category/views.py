from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Category
from .forms import CategoryForm
from django.contrib import messages


# Create your views here.
@login_required
def category_list(request):
    categories = Category.objects.filter(user=request.user)
    return render(request, 'category_list.html', {'categories': categories})


@login_required
def category_add(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            category = form.save(commit=False)
            category.user = request.user
            category.save()
            messages.success(request, 'Categoria adicionada com sucesso!')
            return redirect('category_list')
    else:
        form = CategoryForm()
    return render(request, 'category_add.html', {'form': form})


@login_required
def category_edit(request, pk):
    category = get_object_or_404(Category, pk=pk, user=request.user)
    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            messages.success(request, 'Categoria atualizada com sucesso!')
            return redirect('category_list')
    else:
        form = CategoryForm(instance=category)
    return render(request, 'category_edit.html', {'form': form})



@login_required
def category_delete(request, pk):
    category = get_object_or_404(Category, pk=pk, user=request.user)
    if request.method == 'POST':
        category.delete()
        messages.success(request, 'Categoria excluída com sucesso!')
        return redirect('category_list')
    return render(request, 'category_delete.html', {'category': category})