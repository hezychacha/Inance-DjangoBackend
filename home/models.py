from django.db import models

# Create your models here.

class services(models.Model):
    service_title = models.CharField(max_length=100)
    service_image = models.ImageField(upload_to='uploads')
    service_description = models.TextField()
    service_date_modified = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.service_title