from django.db import models
import uuid

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=200) # Character field (text value) By default null is set to False meaning that the field is required.
    description = models.TextField(null=True, blank=True) # This is a bigger field, null means that we can ignore that field. 
                                                          # Blank=True means that we can submit the form with the field empty
    demo_link = models.CharField(max_length=2000, null=True, blank=True)
    source_link = models.CharField(max_length=2000, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True) # Gives use the date and time stamp, 
                                                      # auto_now_add - generate the time whenever the model instance is created
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False) # 16 character string of numbers and letters
                            # By default django creates ids of 1, 2 etc, but here we override the id attribute
                                              
    def __str__(self):
        return self.title