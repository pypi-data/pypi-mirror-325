from sys import int_info

from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from django.http import JsonResponse
from django.db.models import Sum
from datetime import date, timedelta
from django.views.generic import *
from django.views import *

from .models import Template
from .forms import TemplateForm

import xlrd


def index(request):
    return render(request, 'index.html')
    

def form(request):
    return render(request, "form.template.html")


class Presentation_Template(View):

    model = Template
    template_name_main = "name.html"
    template_name_creating = "name_creating.html"
    template_name_edit = "name_edit.html"
    form = TemplateForm
    template_name_excel = "name_excel.html"

    def init_form(self, request, initial, instance):
        if request.method == "POST":
            return self.form(request.POST, instance=instance, initial = initial)
        else:
            return self.form(instance=instance, initial=initial)


    def get(self, request):
        return render(request, self.template_name_main, self.model.objects.all())


    def delete(self, request, id):
        object = get_object_or_404(self.model, id=id)
        object.delete()

        return redirect("template")


    def creating(self, request):
        if request.method == "POST":
            #forma = self.form(request.POST)
            forma = self.init_form(request, None, None)
            if forma.is_valid():
                object = forma.save(commit=False)
                object.save()
                return redirect("template")
        else:
            #forma = self.form() # initial={"registration_date": timezone.now().date()}
            forma = self.init_form(request, None, None)

        return render(request, self.template_name_creating, {"form": forma})


    def edit(self, request, id):
        object = get_object_or_404(self.model, id=id)
        if request.method == "POST":
            #forma = self.form(request.POST, instance=object)
            forma = self.init_form(request, None, object)
            if forma.is_valid():
                forma.save()
                return redirect("clients")
        else:
            #forma = self.form(instance=object)
            forma = self.init_form(request, None, object)

        return render(request, self.template_name_edit, {"form": forma})


    def creating_mult_chioce(self, request):
        if request.method == "POST":
            #forma = self.form(request.POST)
            forma = self.init_form(request, None, None)
            if forma.is_valid():
                object = forma.save(commit=False)
                # task_productionw.registration_date = timezone.now().date()
                object.save()
                forma.save_m2m()
                return redirect("task_production")
        else:
            #forma = self.form() # initial={"registration_date": timezone.now().date()}
            forma = self.init_form(request, None, None)

        return render(request, "task_production_new.html", {"form": forma})


    def edit_mult_chioce(self, request, id):
        object = get_object_or_404(self.model, id=id)
        if request.method == "POST":
            #forma = self.form(request.POST, instance=object)
            forma = self.init_form(request, None, object)
            if forma.is_valid():
                object = forma.save(commit=False)
                object.save()
                forma.save_m2m()
                return redirect("clients")
        else:
            #forma = self.form(instance=object)
            forma = self.init_form(request, None, object)

        return render(request, self.template_name_edit, {"form": forma})

    def reading_excel(self, request):
        if request.method == "POST":
            forma = self.form(request.POST, request.FILES)
            if forma.is_valid():
                file = request.FILES["file"]
                #работа с file
                return redirect("")
        else:
            forma = self.form()
        return render(request, self.template_name_excel, {"form" : forma})