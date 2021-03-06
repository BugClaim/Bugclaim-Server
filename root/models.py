from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL


class RootAdmin(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name='rootadmin')
    bio = models.TextField(blank=True, max_length=100, default="")
    country = models.CharField(max_length=20, blank=True, default="")
    facebook_url = models.URLField(blank=True, default="")
    twitter_handler = models.CharField(max_length=40, blank=True, default="")

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}'

    @property
    def full_name(self):
        return f'{self.user.first_name} {self.user.last_name}'

    @property
    def username(self):
        return self.user.username

    class Meta:
        db_table = 'rootadmin'


class Rootmod(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='rootmod')
    admin = models.ForeignKey(RootAdmin, related_name="admin_moderators", on_delete=models.CASCADE,null=True)
    bio = models.TextField(blank=True, max_length=100, default="")
    country = models.CharField(max_length=20, blank=True, default="")
    facebook_url = models.URLField(blank=True, default="")
    twitter_handler = models.CharField(max_length=40, blank=True, default="")

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}'

    @property
    def full_name(self):
        return f'{self.user.first_name} {self.user.last_name}'

    @property
    def username(self):
        return self.user.username

    class Meta:
        db_table = 'rootmoderator'
