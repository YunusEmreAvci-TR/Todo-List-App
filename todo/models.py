from django.db import models

class Todos(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=500, null=True, blank=True)
    is_complated = models.BooleanField(default=False, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-updated_at', '-created_at']