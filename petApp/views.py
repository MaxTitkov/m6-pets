from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from petApp.models import Pet

class AboutShelter(TemplateView):
    template_name = 'about.html'

class PetsListView(ListView):
    template_name = "pets_list.html"
    model = Pet
    context_object_name = 'pets'

class PetDetailView(DetailView):
    template_name = "pet_detail.html"
    model = Pet
    context_object_name = "pet"
    