from multiprocessing import context
from django.shortcuts import redirect, render
from django.shortcuts import get_object_or_404
from .forms import *
from . import models

def leads_lists(request):
    leads = models.Lead.objects.all()
    context = {
        "leads": leads
    }
    return render(request, "leads_lists.html", context)


def lead_detail(request, pk):
    lead = get_object_or_404(models.Lead, id=pk)
    context = {
        "lead": lead
    }
    return render(request, 'details.html', context)

def lead_create(request):
    forms = LeadModelForm()
    if request.method == "POST":
        form = LeadModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/leads")
    context = {
        "forms": forms
    }
    return render(request, "create.html", context)

def lead_update(request, pk):
    lead = Lead.objects.get(id=pk)
    form = LeadModelForm(instance=lead)
    if request.method == "POST":
        form = LeadModelForm(request.POST, instance=lead)
        if form.is_valid():
            form.save()
            return redirect("/leads")
    context = {
        "form": form,
        "lead": lead,
    }
    return render(request, "update.html", context)

def lead_delete(request, pk):
    lead = models.Lead.objects.get(id=pk)
    lead.delete()
    return redirect("/leads")