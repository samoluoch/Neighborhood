from django.contrib import admin
from .models import Profile,Category,Neighborhood,Post,Business

# Register your models here.
admin.site.register(Profile)
admin.site.register(Category)
admin.site.register(Neighborhood)
admin.site.register(Post)
admin.site.register(Business)