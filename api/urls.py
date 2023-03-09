from django.urls import path
from .views import BookList, BookDetail, AuthorList, AuthorDetail, PublisherList, PublisherDetail


urlpatterns = [
    path('book/', BookList.as_view()),
    path('book/<int:pk>', BookDetail.as_view()),
    path('author/', AuthorList.as_view()),
    path('author/<int:pk>', AuthorDetail.as_view()),
    path('publisher/', PublisherList.as_view()),
    path('publisher/<int:pk>', PublisherDetail.as_view()),
]