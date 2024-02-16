from django.urls import path
from .views import BookListView, BookReviewView
urlpatterns = [
    path('book_list/', BookListView.as_view(), name='book-list'),
    path('review/<int:pk>/', BookReviewView.as_view(), name='book-review')
]