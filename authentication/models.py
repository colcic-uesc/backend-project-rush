from django.db import models
from django.contrib.auth.models import User as BaseUser


# User do Django possui os seguintes campos:
# username, first_name, last_name, email, password, groups, user_permissions,
# is_staff, is_active, is_superuser, last_login, date_joined
class User(BaseUser):
    rules = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.username
