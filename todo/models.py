from django.db import models

# Create your models here.



class Task(models.Model):
    content = models.CharField(max_length=255)
    is_done = models.BooleanField(default=False)
    created_date=models.DateField(auto_now_add=True)
    
    
    def __str__(self):
        return self.content
