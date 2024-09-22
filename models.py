from django.db import models

class Recipe(models.Model):
    name = models.CharField(max_length=100)
    content = models.TextField(default=1)
    ingredients = models.TextField()
    procedure = models.TextField()
    cuisine=models.CharField(max_length=100,default=1)
    cuisine_number=models.IntegerField(default=1)
    food_type=models.IntegerField(default=1)
    def __str__(self):
        return self.name
    def __str__(self):
        return self.cuisine

class commentbox(models.Model):
    com_name=models.CharField(max_length=100)
    com_content = models.TextField(default=1)
    rating=models.IntegerField(default=1)

