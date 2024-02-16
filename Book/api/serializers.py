from rest_framework import serializers
from Book.models import BookModel, ReviewModel


class BookReviewSerializer(serializers.ModelSerializer):

    class Meta:
        model = ReviewModel
        fields = '__all__'


class BookSerializer(serializers.ModelSerializer):
    book_reviews = BookReviewSerializer(many=True, read_only=True)
    user=serializers.StringRelatedField()
    class Meta:
        model = BookModel
        fields = '__all__'
