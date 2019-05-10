import json

from django.shortcuts import render

# Create your views here.
from core.models import Kite


def index(request):
    kites = Kite.objects.all()
    return render(request, 'index.html', context={'kites': kites})
