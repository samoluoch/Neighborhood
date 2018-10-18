from django.contrib import admin
from .models import Profile,Category,Neighborhood,Post,Business,Location

# Register your models here.
admin.site.register(Profile)
admin.site.register(Category)
admin.site.register(Neighborhood)
admin.site.register(Post)
admin.site.register(Business)
admin.site.register(Location)
