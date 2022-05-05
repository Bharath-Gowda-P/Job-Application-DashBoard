
from django.db import models
from django.core.validators import RegexValidator

# Create your models here.
class candidate_info(models.Model):
    name = models.CharField(max_length=25)
    phone = models.CharField(max_length=13)
    address = models.TextField()
    course = models.CharField(max_length=25)
    degree = models.CharField(max_length=25)
    yoe = models.IntegerField(null=True)
    pcompany = models.CharField(max_length=30)
    skills = models.TextField()
    resume = models.FileField(upload_to="media")
    status = models.CharField(max_length=25, default="Applied")

    def __str__(self):
        return self.name