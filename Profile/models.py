from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.


class ProfileTable(models.Model):
    id_user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
    )
    url_img = models.CharField(max_length=100, null=False)
    image = models.ImageField(blank=True, default='', upload_to='img/', null=True)
    created = models.DateTimeField(default=timezone.now)
    edited = models.DateTimeField(blank=True, null=True, default=None)

    class Meta:
        managed = True
        db_table = 'profile'
