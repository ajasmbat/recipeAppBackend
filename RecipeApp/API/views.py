import json

from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import IngredientSerializer, IngredientSubCategorySerializer
from .models import Ingredient, IngredientSubCategory
from .GPTAPI import generate_recipe, getRecipeImageLink



@api_view(['GET'])
def getIngredients(request, category = False):

    


    if category:
        try:
            category = IngredientSubCategory.objects.get(name=category)
            ingredients = Ingredient.objects.filter(subCategory = category)
        except IngredientSubCategory.DoesNotExist:
            return Response({"message": f"No category named '{category}' found."}, status=404)
        
    else:
        ingredients = Ingredient.objects.all()




    serializer = IngredientSerializer(ingredients,many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getCategories(request):
    categories = IngredientSubCategory.objects.all()
    serializer = IngredientSubCategorySerializer(categories, many=True)
    return Response(serializer.data)





@api_view(['POST'])
def postIngredients(request):
    try:
        data = request.data 

        IngredientNames = [item['name'] for item in data]

        
        response = generate_recipe(IngredientNames)
        title, image_url , context_url = getRecipeImageLink(response)



        
        
        data = {

        }
        
    
        
        return Response({"title":title,"message": response,"image": image_url,"contextUrl": context_url })
    except json.JSONDecodeError:
         return Response({"error": "Invalid JSON data"}, status=400)
