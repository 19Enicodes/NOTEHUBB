from django.db import models
# from django.contrib.auth.models import AbstractUser


class CreateMaterials(models.Model):
    title = models.CharField(max_length=20)
    file = models.FileField(upload_to='uploads/', default=0)
    coursecode = models.CharField(max_length=20, default=0)
    author = models.CharField(max_length=50, default=0)

    def __str__(self):
        return f"{self.title}"


# # class CustomUser(AbstractUser):
#     # matric_number = models.CharField(max_length=20, unique=True)

#     def __str__(self):
#         return f"{self.username} ({self.matric_number})"
