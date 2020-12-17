from django.urls import path
from .views import me_page, contact_page

urlpatterns = [
    path('me', me_page),
    path('contact', contact_page),
]