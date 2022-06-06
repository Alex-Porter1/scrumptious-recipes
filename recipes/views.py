from django.shortcuts import redirect, render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from recipes.forms import RatingForm
from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse_lazy

try:
    from recipes.forms import RecipeForm
    from recipes.models import Recipe
except Exception:
    RecipeForm = None
    Recipe = None


def change_recipe(request, pk):
    if Recipe and RecipeForm:
        instance = Recipe.objects.get(pk=pk)
        if request.method == "POST":
            form = RecipeForm(request.POST, instance=instance)
            if form.is_valid():
                form.save()
                return redirect("recipe_detail", pk=pk)
        else:
            form = RecipeForm(instance=instance)
    else:
        form = None
    context = {
        "form": form,
    }
    return render(request, "recipes/edit.html", context)


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
