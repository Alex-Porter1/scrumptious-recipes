
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

try:
    from tags.models import Tag
except Exception:
    Tag = None


# Create your views here.


class TagCreateView(CreateView):
    model = Tag
    fields = ["name", "recipes"]
    template_name = "tags/new.html"
    success_url = reverse_lazy("recipes_list")


class TagUpdateView(UpdateView):
    model = Tag
    fields = ["name", "recipes"]
    template_name = "tags/edit.html"
    success_url = reverse_lazy("recipes_list")


class TagListView(ListView):
    model = Tag
    context_object_name = "tags"
    template_name = "tags/list.html"


class TagDeleteView(DeleteView):
    model = Tag
    template_name = "tags/delete.html"
    success_url = reverse_lazy("recipes_list")


class TagDetailView(DetailView):
    model = Tag
    context_object_name = "tags"
    template_name = "tags/detail.html"
    success_url = reverse_lazy("recipes_list")
