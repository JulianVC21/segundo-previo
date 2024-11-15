from django.urls import include, path
from rest_framework import routers
from .views import BookViewSet, StudentViewSet, BookReservationViewSet

router = routers.DefaultRouter()
router.register(r'books', BookViewSet)
router.register(r'students', StudentViewSet)
router.register(r'book-reservations', BookReservationViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api/', include('rest_framework.urls', namespace='rest_framework'))
]