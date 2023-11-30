from django.shortcuts import render, HttpResponse
from django.views.generic import ListView

from .models import Profile, Link

# Create your views here.
class LinkListView(ListView):
    # What model we wanna grab info from
    model = Link
    # template called model_list.html -> link_list.html
    