from django.urls import path
from .views import getIngredients, postIngredients, getCategories



urlpatterns = [
    path("getIngredients/", getIngredients, name="getIngredients"),
    path("getIngredients/<category>", getIngredients,name="getIngredientsWithCategory"),
    path("getCategories/",getCategories,name="getCategories"),
    path('postIngredients/',postIngredients, name="postIngredients"),
]

