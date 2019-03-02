from django.urls import path
from . import views

urlpatterns = [
    path('api/event/', views.EventListCreate.as_view()),
    path('api/transaction/', views.TransactionListCreate.as_view()),
]
