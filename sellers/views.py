from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from leads.models import Seller

class SellerListView(LoginRequiredMixin, generic.ListView):
    template_name = "sellers/list.html"

    def get_queryset(self):
        return Seller.objects.all()
