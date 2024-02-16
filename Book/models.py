from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class BookModel(models.Model):
    name=models.CharField(max_length=100)
    author=models.CharField(max_length=100)
    price=models.IntegerField()
    pages=models.IntegerField()

    def __str__(self):
        return self.name

class ReviewModel(models.Model):
    book=models.ForeignKey(BookModel,on_delete=models.CASCADE, related_name="book_reviews")
    review=models.CharField(max_length=100)
    user=models.ForeignKey(User, on_delete=models.CASCADE, related_name="user")

    def __str__(self):
        return f"{self.review} - {self.book.name}"