from rest_framework import viewsets
from . import models
from .serializers import BookSerializer, StudentSerializer, BookReservationSerializer

# Create your views here.

class BookViewSet(viewsets.ModelViewSet):
    queryset = models.Book.objects.all()
    serializer_class = BookSerializer

class StudentViewSet(viewsets.ModelViewSet):
    queryset = models.Student.objects.all()
    serializer_class = StudentSerializer
    
class BookReservationViewSet(viewsets.ModelViewSet):
    queryset = models.BookReservation.objects.all()
    serializer_class = BookReservationSerializer