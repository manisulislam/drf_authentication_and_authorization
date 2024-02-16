from django.contrib import admin
from Book.models import BookModel, ReviewModel
# Register your models here.

admin.site.register(BookModel)
admin.site.register(ReviewModel)
