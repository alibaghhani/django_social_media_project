from django.contrib import admin
from socialmedia.models import *
from .models import *
# Register your models here.
admin.site.register(User)
admin.site.register(Follow)
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Like)




