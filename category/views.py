from django.shortcuts import render
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required
def categories(request):
    return render(request, 'category_list.html')