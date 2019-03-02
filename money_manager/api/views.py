from money_manager.models import Event, Transaction
from .serializers import EventSerializer, TransactionSerializer
from rest_framework import generics


class EventListCreate(generics.ListCreateAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer


class TransactionListCreate(generics.ListCreateAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
