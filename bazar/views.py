from django.shortcuts import render

def index(request):
    context = {
        'nadpis': 'Úvodní stránka',
        'obsah': 'Obsah stránky'
    }

    return render(request, template_name='index.html', context=context)