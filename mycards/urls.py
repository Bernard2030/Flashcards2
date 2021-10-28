from django.urls import path
from .views import Flash,Flashbyid

urlpatterns = [
   path('',Flash.as_view()),
   path('<int:id>', Flashbyid.as_view()), 
]