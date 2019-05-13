import json
from audioop import reverse

from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from core.forms import KiteForm
from core.models import Kite


def index(request):
    kites = Kite.objects.all()
    if request.method == 'POST':
        form = KiteForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            name = form.cleaned_data['name']
            body = form.cleaned_data['body']
            p = Kite(title=title, name=name, body=body)
            p.save()
            return HttpResponseRedirect('/')
    else:
        form = KiteForm()
        return render(request, 'index.html', context={'kites': kites, 'form': form})
