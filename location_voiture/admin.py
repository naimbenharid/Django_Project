from django.contrib import admin
from .models import Voiture, Client, Location ,VoitureImage

# Register your models here.
@admin.register(Voiture)
class VoitureAdmin(admin.ModelAdmin):
    list_display = ('marque', 'modele', 'annee_fabrication', 'couleur', 'immatriculation')
    search_fields = ('marque', 'modele', 'immatriculation')

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('nom', 'prenom', 'email', 'numero_telephone')
    search_fields = ('nom', 'prenom', '')

@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ('client', 'voiture', 'date_debut', 'date_fin', 'prix_jour','nombres_jours','total')
    search_fields = ('client__nom', 'voiture__marque', 'utilisateur__username')

@admin.register(VoitureImage)
class VoitureImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'image', 'voiture')