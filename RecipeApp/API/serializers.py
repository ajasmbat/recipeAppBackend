from rest_framework import serializers
from .models import Ingredient, IngredientSubCategory

class IngredientSerializer(serializers.ModelSerializer):
    subCategoryName = serializers.CharField(source='subCategory.name', read_only=True)
    
    class Meta:
        model = Ingredient
        fields = '__all__'


class IngredientSubCategorySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = IngredientSubCategory
        fields = '__all__'