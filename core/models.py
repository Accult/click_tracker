from django.db import models


class UserData(models.Model):
    ip = models.GenericIPAddressField()
    browser = models.CharField(max_length=200)
    click_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"IP: {self.ip}, Browser: {self.browser}, Click Time: {self.click_time}"
