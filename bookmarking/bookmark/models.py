from django.db import models


class Website(models.Model):
    website_address=models.CharField(max_length=1000)
    description=models.CharField(max_length=1000)

    def __str__(self):
        return self.description
