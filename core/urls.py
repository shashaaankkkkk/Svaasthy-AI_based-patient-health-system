# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib import admin
from django.urls import path, include  # add this
from patient_api.views import create_patient

urlpatterns = [
    path('admin/', admin.site.urls),          # Django admin route
    path("", include("apps.authentication.urls")), # Auth routes - login / register

    # ADD NEW Routes HERE
    path('patients/', create_patient, name='create_patient'),
    # Leave `Home.Urls` as last the last line
    path("", include("apps.home.urls"))
]
