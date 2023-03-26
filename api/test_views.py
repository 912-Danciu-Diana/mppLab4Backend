from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

from api.models import Review, Author
from api.reports import report, ordered_report
from api.serializers import ReportEntrySerializer, OrderedReportEntrySerializer, AuthorSerializer


class AuthorListTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.url = reverse('author-list')
        self.author1 = Author.objects.create(first_name='Author 1', no_of_prizes=2, no_of_books=10, date_of_birth='1980-03-26')
        self.author2 = Author.objects.create(first_name='Author 2', no_of_prizes=3, no_of_books=1, date_of_birth='1899-10-02')
        self.author3 = Author.objects.create(first_name='Author 3', no_of_prizes=1, no_of_books=5, date_of_birth='1945-05-20')

    def test_get_queryset_with_valid_prize_value(self):
        response = self.client.get(self.url, {'min_prize': '2'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        queryset = Author.objects.filter(no_of_prizes__gt=2)
        serializer = AuthorSerializer(instance=queryset, many=True)
        self.assertEqual(response.data, serializer.data)

    def test_get_queryset_with_invalid_prize_value(self):
        response = self.client.get(self.url, {'min_prize': 'abc'})
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


class ReviewReportAPIViewTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.url = reverse('report')

    def test_report_view(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        expected_data = report()
        serializer = ReportEntrySerializer(instance=expected_data, many=True)
        self.assertEqual(response.data, serializer.data)


class ReviewOrderedReportAPIViewTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.url = reverse('orderedReport')

    def test_ordered_report_view(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        expected_data = ordered_report()
        serializer = OrderedReportEntrySerializer(instance=expected_data, many=True)
        self.assertEqual(response.data, serializer.data)
