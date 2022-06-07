from django.shortcuts import redirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from recipes.forms import RatingForm
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

try:
    from recipes.forms import RecipeForm
    from recipes.models import Recipe
except Exception:
    RecipeForm = None
    Recipe = None


class RecipeCreateView(CreateView):
    model = Recipe
    fields = ["name", "author", "description", "image"]
    template_name = "recipes/new.html"
    success_url = reverse_lazy("recipes_list")


class RecipeUpdateView(UpdateView):
    model = Recipe
    fields = ["name", "author", "description", "image"]
    template_name = "recipes/edit.html"
    success_url = reverse_lazy("recipes_list")


class RecipeListView(ListView):
    model = Recipe
    context_object_name = "recipes"
    template_name = "recipes/list.html"
    paginate_by = 6

    def get_queryset(self):
        # Get the querystring from search
        querystring = self.request.GET.get("q")
        if querystring is None:
            querystring = ""
        # generate list of all recipes we want to filter.
        return Recipe.objects.filter(description__icontains=querystring)
        # filter the list based on the querystring.

        # return the filtered list


class RecipeDeleteView(DeleteView):
    model = Recipe
    template_name = "recipes/delete.html"
    success_url = reverse_lazy("recipes_list")


class RecipeDetailView(DetailView):
    model = Recipe
    context_object_name = "recipe"
    template_name = "recipes/detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["rating_form"] = RatingForm()
        return context


def log_rating(request, recipe_id):
    if request.method == "POST":
        form = RatingForm(request.POST)
        if form.is_valid():
            rating = form.save(commit=False)
            rating.recipe = Recipe.objects.get(pk=recipe_id)
            rating.save()
    return redirect("recipe_detail", pk=recipe_id)
