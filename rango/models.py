from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=128, unique=true)
    
    def __str__(self):
        return self.name

class Page(models.model):
    category =models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=128)
    url = models.URLField()
    views = models.IntegerField(default=0)
    
    def __str__(self):
        return self.title
