# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path, re_path
from apps.home import views,apicall
from patient_api.views import create_patient



urlpatterns = [

    # The home page
    path('', views.index, name='home'),
    # Matches any html file
    re_path(r'^.*\.*', views.pages, name='pages'),
    path('patients/', create_patient, name='create_patient'),
]
