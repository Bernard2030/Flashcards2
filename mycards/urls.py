from django.urls import path
from .views import Flash,Flashbyid

urlpatterns = [
    path('Flashcards/', Flash.as_view()),
    path('Flashcards/<int:id>', Flashbyid.as_view()),
]