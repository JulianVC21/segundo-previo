from . import models
from rest_framework import serializers

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Book
        fields = '__all__'
        
class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Student
        fields = '__all__'
        
class BookReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.BookReservation
        fields = '__all__'
    