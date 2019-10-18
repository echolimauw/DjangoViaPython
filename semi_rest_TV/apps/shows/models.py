from django.db import models

class ShowManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData['title']) < 2:
            errors["title"] = "Show title must be three or more characters."
        if len(postData['network']) < 2:
            errors["network"] = "Network must be two or more characters."
        if len(postData['desc']) < 1:
            errors["desc"] = "Show description must be ten or more characters."
        return errors

class Show(models.Model):
    title = models.CharField(max_length=255)
    network = models.CharField(max_length=45)
    desc = models.CharField(max_length=255)
    # release_date = models.DateTimeField(blank=True, null=True)    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ShowManager()