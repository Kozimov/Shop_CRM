from multiprocessing import context
from django.shortcuts import render
from . import models

def leads(request):
    leads = models.Lead.objects.all()
    context = {
        "leads": leads
    }
    return render(request, "leads_lists.html", context)