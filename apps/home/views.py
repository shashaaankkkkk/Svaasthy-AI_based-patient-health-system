# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django import template
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from apps.home.models import chart1,chart2 ,Patient
from django.shortcuts import render
from django.views.generic import TemplateView
import random


def patient_list(request):
    patients = Patient.objects.all().values()
    return render(request, 'tables.html', {'patients': patients})

@login_required(login_url="/login/")
def index(request):
    context = {'segment': 'index'}

    html_template = loader.get_template('home/index.html')
    return HttpResponse(html_template.render(context, request))


@login_required(login_url="/login/")
def pages(request):
    pulsedata=[75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90]
    oxidata=[ 96, 97, 98, 99,100]
    l=random.choices(oxidata,oxidata,k= 14)
    l2=random.choices(pulsedata,pulsedata ,k= 10)
    l3=random.randint(97, 99)
    l4=[l3,l3,l3,l3,l3,l3,l3,l3,l3,l3,l3,l3,l3,l3,l3]
    #context = super().get_context_data(**kwargs)
    #context["qs"] = Editors.objects.all()
    patients =Patient.objects.all()
    context={"pulse":l2,"oxi":l,"tempa":l3,"patient":patients}
    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    try:

        load_template = request.path.split('/')[-1]

        if load_template == 'admin':
            return HttpResponseRedirect(reverse('admin:index'))
        context['segment'] = load_template

        html_template = loader.get_template('home/' + load_template)
        return HttpResponse(html_template.render(context, request))

    except template.TemplateDoesNotExist:

        html_template = loader.get_template('home/page-404.html')
        return HttpResponse(html_template.render(context, request))

    except:
        html_template = loader.get_template('home/page-500.html')
        return HttpResponse(html_template.render(context, request))
    