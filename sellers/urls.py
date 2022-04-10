from unicodedata import name
from django.urls import path
from .views import *


app_name = "sellers"

urlpatterns = [
    path('', SellerListView.as_view(), name="seller-list"),
    path('create-sellers/', SellerCreateView.as_view(), name="seller-create"),
]