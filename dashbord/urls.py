from django.urls import path, include
from .views import VoitureListView, VoitureDetailView, VoitureCreateView, VoitureUpdateView, VoitureDeleteView

urlpatterns = [

    path('voitures/', VoitureListView.as_view(), name='voiture_list'),
    path('voitures/<int:pk>/', VoitureDetailView.as_view(), name='voiture_detail'),
    path('voitures/create/', VoitureCreateView.as_view(), name='voiture_create'),
    path('voitures/<int:pk>/update/', VoitureUpdateView.as_view(), name='voiture_update'),
    path('voitures/<int:pk>/delete/', VoitureDeleteView.as_view(), name='voiture_delete'),
] 
