from django.db import models

class ShowManager(models.Manager):
    def new_validator(self, postData):
        errors = {}
        if len(postData["newTitle"]) < 2:
            errors["name"] = "Surely your show's title is longer. Please try again."
        if len(postData["newNetwork"]) < 2:
            errors["network"] = "That network doesn't exist. Please try again."
        if len(postData["newDesc"]) < 10:
            errors["description"] = "Descriptions require more characters than that."
        return errors


class Show(models.Model):
    title = models.CharField(max_length=255)
    network = models.CharField(max_length=45)
    desc = models.CharField(max_length=255)
    release_date = models.DateField(blank=True, null=True)    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ShowManager()