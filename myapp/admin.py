from django.contrib.auth.models import User
from django.contrib import admin
from .models import Post

admin.site.register(Post)
# Unregister the User model if it was already registered
if admin.site.is_registered(User):
    admin.site.unregister(User)

# Then register the User model
admin.site.register(User)