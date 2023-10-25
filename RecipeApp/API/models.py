from django.db import models
#deletion of s3 bucket images IMPORTS
from django.dispatch import receiver
from django.db.models.signals import post_delete
from django.core.files.storage import default_storage


class IngredientSubCategory(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Ingredient(models.Model):
    name = models.CharField(max_length=100)

    subCategory = models.ForeignKey(IngredientSubCategory, on_delete=models.CASCADE, related_name='ingredients')

    image = models.ImageField(upload_to='media/ingredient_pictures', blank= False)
    

    def __str__(self):
        return self.name
    


@receiver(post_delete, sender=Ingredient)
def delete_associated_files(sender, instance, **kwargs):
    instance.image.delete(save=False)

