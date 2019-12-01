from django.urls import path
from petApp import views

urlpatterns = [
    path("", views.AboutShelter.as_view(), name="AboutView"),
    path("pets_list/", views.PetsListView.as_view(), name="PetsList"),
    path("pet_<int:pk>", views.PetDetailView.as_view(), name="PetDetail"),
]