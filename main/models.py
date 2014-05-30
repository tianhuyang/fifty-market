from django.db import models


# Contact model.
class Contact(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=63)
    email = models.EmailField(max_length=255)
    intention = models.CharField(max_length=255)
    phone = models.CharField(default='', max_length=15)

    class Meta:
        db_table = 'contact'
