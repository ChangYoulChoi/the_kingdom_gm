from django.db import models

# Create your models here.
class Manager(models.Model):
    user_id = models.CharField(max_length=50, unique=True, null=False)
    user_pw = models.CharField(max_length=50, null=False)
    user_name = models.CharField(max_length=50, null=False)
    user_level = models.PositiveSmallIntegerField(null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering = ('-id', )