from django.shortcuts import render
from bazar.models import *
from django.views.generic import ListView, DetailView


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