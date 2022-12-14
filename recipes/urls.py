from django.urls import path

from recipes.views import (

    log_rating,
    RecipeListView,
    RecipeDetailView,
    RecipeCreateView,
    RecipeDeleteView,
    RecipeUpdateView
)

urlpatterns = [
    path("", RecipeListView.as_view(), name="recipes_list"),
    path("<int:pk>/", RecipeDetailView.as_view(), name="recipe_detail"),
    path("new/", RecipeCreateView.as_view(), name="recipe_new"),
    path("<int:pk>/update", RecipeUpdateView.as_view(), name="recipe_edit"),
    path("<int:recipe_id>ratings/", log_rating, name="recipe_rating"),
    path("<int:pk>/delete/", RecipeDeleteView.as_view(), name="recipe_delete")
]
