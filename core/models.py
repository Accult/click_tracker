from django.db import models


class UserData(models.Model):
    ip = models.GenericIPAddressField()
    browser = models.CharField(max_length=200)
    click_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.ip


class RedirectData(models.Model):
    url = models.URLField()

    def __str__(self):
        return self.url
