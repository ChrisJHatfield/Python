from django.db import models

class ShowManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData['title']) < 2:
            errors["title"] = "Title should be at least 2 characters"
        if len(postData['network']) < 3:
            errors["network"] = "Network should be at least 3 characters"
        if len(postData['description']) == "":
            errors['description'] = None
        elif len(postData['description']) > 0 and len(postData['description']) < 10:
                errors["description"] = "Description should be at least 10 characters"
        potential_match_list = Shows.objects.filter(title=postData['title'])
        if len(potential_match_list) > 0:
            errors['show_exists'] = "Show already exists"
        return errors

class Shows(models.Model):
    title = models.CharField(max_length=60)
    network = models.CharField(max_length=60)
    release_date = models.CharField(max_length=60)
    description = models.TextField(default="", max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ShowManager()