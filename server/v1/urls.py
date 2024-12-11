from django.urls import path
from .views import main, details,contact

urlpatterns = [
    path('', main, name='index'),
    path("<int:pk>", details, name='more info'),
    path("contact", contact, name="contact")
]

