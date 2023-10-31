# 8
from django.shortcuts import render
from .models import BookModel


# Create your views here.
def index_view(request):
    bk = BookModel.objects.all()
    context = {'books': bk}
    return render(request, 'index.html', context=context)
