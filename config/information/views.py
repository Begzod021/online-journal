from multiprocessing import context
from django.shortcuts import render
from users.models import *
from .models import *
# Create your views here.

def get_journal(request):

    return render(request, 'index.html')
