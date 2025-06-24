from django.db import models

class Course(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    mentor = models.CharField(max_length=100)
    image = models.ImageField(upload_to='course_images/')
    direction = models.CharField(max_length=100)

    def __str__(self):
        return self.title + ' ' + self.direction
