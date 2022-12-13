from django.db import models
from Home.models import PetProduct

class comment(models.Model):
    pro=models.ForeignKey(PetProduct,related_name="comments",on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    cmnt=models.TextField()
    date=models.DateTimeField(auto_now_add=True)