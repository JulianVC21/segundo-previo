from django.db import models
from .book import Book
from .student import Student

class BookReservation(models.Model):
    
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    reservation_date = models.DateField()
    return_date = models.DateField(null=True)