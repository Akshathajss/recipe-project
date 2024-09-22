from django.contrib import admin

# Register your models here.
from .models import Recipe,commentbox

admin.site.register(Recipe)
admin.site.register(commentbox)