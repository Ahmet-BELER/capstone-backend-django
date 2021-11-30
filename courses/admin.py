from django.contrib import admin
from .models import (
    Category,
    Course,
    Lesson,
    Like,
    Post,
    Comment,
    PostView
)
# Register your models here.
admin.site.register(Category)
admin.site.register(Course)
admin.site.register(Lesson)
admin.site.register(Like)
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(PostView)