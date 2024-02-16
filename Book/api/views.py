from rest_framework import generics
from .serializers import BookSerializer, BookReviewSerializer
from Book.models import BookModel, ReviewModel

class BookListView(generics.ListAPIView):
    queryset = BookModel.objects.all()
    serializer_class = BookSerializer

class BookReviewView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ReviewModel.objects.all()
    serializer_class = BookReviewSerializer

