from django.db import models
from django.contrib.auth.models import User
class Resume(models.Model):
    name = models.CharField(max_length=100)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    resume_file = models.FileField(upload_to='resumes/')


class Project(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    github_link = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp
    owner = models.ForeignKey(User, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.title
