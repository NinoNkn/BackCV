from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=120)
    email = models.EmailField()
    message = models.TextField(max_length=2000)
    created_at = models.DateTimeField(auto_now_add=True)
    ip_address = models.GenericIPAddressField(null=True, blank=True)

    def __str__(self):
        return f"{self.name} <{self.email}>"
