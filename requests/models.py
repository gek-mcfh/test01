from django.db import models


class Request(models.Model):
    headers = models.fields.TextField(
        max_length=5000
    )
    body = models.fields.TextField(
        max_length=5000
    )
