from rest_framework import generics
from .models import Book, Author, Publisher
from .serializers import BookSerializer, AuthorSerializer, PublisherSerializer
from rest_framework.exceptions import NotFound


class BookList(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class AuthorList(generics.ListCreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class AuthorDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

    def get_queryset(self):
        # get the value of the "prize_value" query parameter
        prize_value = self.request.query_params.get('min_prize')
        # check if the parameter is present
        if prize_value is not None:
            # try to convert the parameter to an integer
            try:
                prize_value = int(prize_value)
                print(prize_value)
            except ValueError:
                raise NotFound('Invalid prize value')
            # filter the queryset to authors with no_of_prizes greater than the given value
            git initqueryset = Author.objects.filter(no_of_prizes__gt=prize_value)
        else:
            queryset = self.queryset
        return queryset


class PublisherList(generics.ListCreateAPIView):
    queryset = Publisher.objects.all()
    serializer_class = PublisherSerializer


class PublisherDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Publisher.objects.all()
    serializer_class = PublisherSerializer
