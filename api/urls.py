from django.urls import path
from .views import BookList, BookDetail, AuthorList, AuthorDetail, PublisherList, PublisherDetail, UserList, \
    UserDetail, ReviewList, ReviewDetail, ReviewReportAPIView, ReviewOrderedReportAPIView

urlpatterns = [
    path('book/', BookList.as_view()),
    path('book/<int:pk>', BookDetail.as_view()),
    path('author/', AuthorList.as_view()),
    path('author/<int:pk>', AuthorDetail.as_view()),
    path('publisher/', PublisherList.as_view()),
    path('publisher/<int:pk>', PublisherDetail.as_view()),
    path('user/', UserList.as_view()),
    path('user/<int:pk>', UserDetail.as_view()),
    path('review/', ReviewList.as_view()),
    path('review/<int:pk>', ReviewDetail.as_view()),
    path('report/', ReviewReportAPIView.as_view()),
    path('orderedreport/', ReviewOrderedReportAPIView.as_view()),
]
