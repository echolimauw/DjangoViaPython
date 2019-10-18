from django.db import models
import re

class UserManager(models.Manager):
    def reg_validator(self, postData):
        email_regex = r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"
        fn = postData['first_name']
        ln = postData['last_name']
        em = postData['email']
        pw = postData['password']
        cp = postData['confirm_pass']
        

        errors = {}

        if len(fn) < 3:
            errors["first_name"] = "First name should be at least 3 characters long"
        if len(ln) < 3:
            errors["last_name"] = "Last name should be at least 3 characters long"                    
        if len(User.objects.filter(email=em)) > 0:
            errors["unique_email"] = "Please use another email address."
        # ^^ This validation can be commented out for testing ^^
        match = re.match(email_regex, em)
        if not match:
            errors["email"] = "Please enter a valid email"
        if len(pw) < 3:
            errors["password"] = "Password must be at least 3 characters long"  # This should be changed to something more advanced at the very end.
        if pw != cp:
            errors["confirm_pass"] = "Unable to confirm password"
        return errors

class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()