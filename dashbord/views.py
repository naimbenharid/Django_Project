from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from location_voiture.models import Voiture

# Create your views here.
class VoitureListView(ListView):
    model = Voiture
    template_name = 'location/voiture/voiture_list.html' 
    context_object_name = 'voitures'

class VoitureDetailView(DetailView):
    model = Voiture
    template_name = 'location/voiture/voiture_detail.html'  
    context_object_name = 'voiture'

class VoitureCreateView(CreateView):
    model = Voiture
    template_name = 'location/voiture/voiture_form.html'  
    fields = ['immatriculation', 'marque', 'modele', 'annee_fabrication', 'couleur', 'status']

class VoitureUpdateView(UpdateView):
    model = Voiture
    template_name = 'location/voiture/voiture_form.html'  
    fields = ['immatriculation', 'marque', 'modele', 'annee_fabrication', 'couleur', 'status']

class VoitureDeleteView(DeleteView):
    model = Voiture
    template_name = 'location/voiture/voiture_confirm_delete.html' 
    success_url = reverse_lazy('voiture_list') 