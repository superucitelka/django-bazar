from django.shortcuts import render
from .models import *
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

def index(request):
    context = {
        'nadpis': 'Úvodní stránka',
        'obsah': 'Obsah stránky'
    }

    return render(request, template_name='index.html', context=context)


class BazarListView(ListView):
    model = Zbozi

    context_object_name = 'zbozi_list'
    template_name = 'list.html'
    #paginate_by = 3


class BazarDetailView(DetailView):
    model = Zbozi

    context_object_name = 'zbozi'
    template_name = 'detail.html'


class ZboziCreate(CreateView):
    model = Zbozi
    fields = ['nazev', 'popis', 'foto', 'cena', 'stav', 'druh']
    initial = {'cena': 200}


class ZboziUpdate(UpdateView):
    model = Zbozi
    fields = '__all__' # Not recommended (potential security issue if more fields added)


class ZboziDelete(DeleteView):
    model = Zbozi
    success_url = reverse_lazy('list')