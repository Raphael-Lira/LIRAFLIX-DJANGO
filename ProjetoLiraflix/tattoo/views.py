from django.shortcuts import render
from .models import Tattoo
from trabalhos.models import Trabalho
from django.views.generic import TemplateView, ListView, DetailView

#
# Create your views here.
#def homepage(request):
#    return render(request, 'homepage.html')

class Homepage(TemplateView):
    template_name = 'homepage.html'


def home_tattoo(request):
    context = {}
    context['lista_tattoos'] = Tattoo.objects.all()
    context['lista_trabalhos'] = Trabalho.objects.all()
    return render(request, 'hometattoos.html', context)
# url - view - html

class Detalheview(DetailView):
    template_name = 'detalhestattoo.html'
    model = Tattoo