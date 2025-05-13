from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Profile, Link

# Create your views here.
# Default template model_list.html -> link_list.html
class LinkListView(ListView):
  model = Link

# Default template model_form.html -> link_form.html
class LinkCreateView(CreateView):
  model = Link # Specifies the model
  fields = "__all__" # Specifies that we need to input all fields
  success_url = reverse_lazy('link-list') # Specifies what to do when it is created successfully

# Default template model_form.html -> link_form.html (sheres the same template as create)
class LinkUpdateView(UpdateView):
  model = Link
  fields = ['text', 'url']
  success_url = reverse_lazy('link-list')

# Default template for confirmation before delete
# It expects model_confirm_delete.html -> link_confirm_delete.html
class LinkDeleteView(DeleteView):
  model = Link
  success_url = reverse_lazy('link-list')

def profile_view(request, profile_slug):
  profile = get_object_or_404(Profile, slug=profile_slug)
  links = profile.links.all()
  context = {
    'profile': profile,
    'links': links
  }
  return render(request, 'link_plant/profile.html', context)
