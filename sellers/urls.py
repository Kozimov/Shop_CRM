from django.urls import path
from .views import SellerListView


app_name = "sellers"

urlpatterns = [
    path('', SellerListView.as_view(), name="seller-list")
]