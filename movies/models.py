from django.db import models
from accounts.models import CustomUser
from django.urls import reverse

# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=64)
    purchaser = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    description  = models.TextField(default="there is no description")

    def __str__(self):
        return self.title
    
    class Meta :
        ordering =["-pk"]
    
    def get_absolute_url(self):
        # return reverse("movies_detail", kwargs={"pk": self.pk})
        return reverse("movies_detail", args=[self.pk])