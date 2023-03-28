from rest_framework import generics, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Book, Author, Publisher, User, Review
from .reports import report, ordered_report
from .serializers import BookSerializer, AuthorSerializer, PublisherSerializer, AuthorsKeySerializer, \
    BooksKeySerializer, UserSerializer, ReviewSerializer, ReportEntrySerializer, OrderedReportEntrySerializer
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


class ReviewReportAPIView(APIView):
    def get(self, request):
        data = report()
        serializer = ReportEntrySerializer(instance=data, many=True)
        return Response(data=serializer.data)


class ReviewOrderedReportAPIView(APIView):
    def get(self, request):
        data = ordered_report()
        serializer = OrderedReportEntrySerializer(instance=data, many=True)
        return Response(data=serializer.data)


class BookUserAPIView(APIView):
    def post(self, request, id):
        try:
            book = Book.objects.get(id=book_id)
        except Book.DoesNotExist:
            raise NotFound('Book not found')
        data = request.data
        newreviews = []
        for item in data:
            user_id = item.get('user')
            rating = item.get('rating')
            review = item.get('review')
            newreview = Review.objects.create(
                book=BookSerializer.objects.get(id=id),
                user_id=UserSerializer.objects.get(id=user_id),
                rating=rating,
                review=review
            )
            newreview.save()
            newreviews.append(newreview)
        serializers = ReviewSerializer(newreviews, many=True)
        return Response(serializers.data)
        # try:
        #     user = User.objects.get(id=user_id)
        # except User.DoesNotExist:
        #     raise NotFound('User not found')
        #
        # # retrieve rating and review data from request data
        # rating = request.data.get('rating')
        # review_text = request.data.get('review')
        #
        # # create a new review object and set its book and user attributes
        # review = Review.objects.create(book=book, user=user)
        #
        # # return an error if the review creation failed
        # if not review:
        #     return Response({'error': 'Failed to create review'}, status=status.HTTP_400_BAD_REQUEST)
        #
        # # return the serialized data of the new review object
        # serializer = ReviewSerializer(review)
        # return Response(serializer.data)
        #

