# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib import admin
from apps.home.models import chart1,chart2 ,Patient
# Register your models here.
admin.site.register(chart1)
admin.site.register(chart2)
admin.site.register(Patient)