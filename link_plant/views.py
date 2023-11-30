from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from .models import Profile, Link

# Create your views here.

# List the links
class LinkListView(ListView):
    model = Link # What model we wanna grab info from
    
# Create the links and save them to DB
class LinkCreateView(CreateView):
    model = Link # What model we wanna grab info from
    fields = '__all__' # This creates the forms for us. in this case it will include all the fields
    success_url = reverse_lazy('link-list') # This here is where we send the user when they have successfully created a link. reverse_lazy takes in the url name as a parameter. 
    # This class creates a few things by default. the first thing is that it creates a template that takes the model name then _forms -> link_form.html
    # It will also create a form context variable that we will have access to inside the above html-file.
    
# Update the links
class LinkUpdateView(UpdateView):
    model = Link
    fields = ['text', 'url'] # specifies which DB fields become form fields to edit.
    success_url = reverse_lazy('link-list') # This here is where we send the user when they have successfully created a link. reverse_lazy takes in the url name as a parameter.
    

# Deletes object(link)
class LinkDeleteView(DeleteView):
    model = Link
    success_url = reverse_lazy('link-list') # This here is where we send the user when they have successfully created a link. reverse_lazy takes in the url name as a parameter.
    

def profile_view(request, profile_slug):
    profile = get_object_or_404(Profile, slug=profile_slug) # fetches Profile objects from DB by their slug
    links = profile.links.all() # gets all the links for the specific profiles
    context = {
        'profile': profile,
        'links': links,
    }
    return render(request, 'link_plant/profile.html', context)