from django.views import generic
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import SellerModelForm
from leads.models import Seller

class SellerListView(LoginRequiredMixin, generic.ListView):
    template_name = "sellers/list.html"

    def get_queryset(self):
        return Seller.objects.all()

class SellerCreateView(LoginRequiredMixin, generic.CreateView):
    template_name = "sellers/create.html"
    form_class = SellerModelForm

    def get_success_url(self):
        return reverse("sellers:seller-list")

    def form_valid(self, form):
        seller = form.save(commit=False)
        seller.profil = self.request.user.userprofil
        seller.save()
        return super(SellerCreateView, self).form_valid(form)