from django import forms
from leads.models import Seller

class SellerModelForm(forms.ModelForm):
    class Meta:
        model = Seller
        fields = (
            'user',
        )