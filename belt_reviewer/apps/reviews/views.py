# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, HttpResponse
from .models import *

# Create your views here.
def index(request):
	return render(request, 'reviews/index.html')