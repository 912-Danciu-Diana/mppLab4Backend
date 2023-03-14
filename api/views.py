from rest_framework import generics
from .models import Book, Author, Publisher, User, Review
from .serializers import BookSerializer, AuthorSerializer, PublisherSerializer, AuthorsKeySerializer, \
    BooksKeySerializer, UserSerializer, ReviewSerializer
from rest_framework.exceptions import NotFound


class BookList(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BooksKeySerializer


class AuthorList(generics.ListCreateAPIView):
    serializer_class = AuthorSerializer

    def get_queryset(self):
        queryset = Author.objects.all()
        # get the value of the "prize_value" query parameter
        prize_value = self.request.query_params.get('min_prize')
        # check if the parameter is present
        if prize_value is not None:
            # try to convert the parameter to an integer
            try:
                prize_value = int(prize_value)
            except ValueError:
                raise NotFound('Invalid prize value')
            # filter the queryset to authors with no_of_prizes greater than the given value
            queryset = queryset.filter(no_of_prizes__gt=prize_value)
        return queryset


class AuthorDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorsKeySerializer


class PublisherList(generics.ListCreateAPIView):
    queryset = Publisher.objects.all()
    serializer_class = PublisherSerializer


class PublisherDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Publisher.objects.all()
    serializer_class = PublisherSerializer


class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class ReviewList(generics.ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer


class ReviewDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
