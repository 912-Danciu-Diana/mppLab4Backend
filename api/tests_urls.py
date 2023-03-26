from unittest import TestCase

from django.test import SimpleTestCase
from django.urls import reverse, resolve
from rest_framework import status

from api.models import Author
from api.views import ReviewReportAPIView, ReviewOrderedReportAPIView, AuthorList
from rest_framework.test import APIClient


class TestUrls(SimpleTestCase):
    def test_report_url(self):
        url = reverse('report')
        self.assertEquals(resolve(url).func.view_class, ReviewReportAPIView)

    def test_orderedReport_url(self):
        url = reverse('orderedReport')
        self.assertEquals(resolve(url).func.view_class, ReviewOrderedReportAPIView)



class TestAuthorList(TestCase):
    def setUp(self):
        self.url = reverse('author-list')
        self.author1 = Author.objects.create(first_name='Author 1', no_of_prizes=2, no_of_books=10,
                                             date_of_birth='1980-03-26')
        self.author2 = Author.objects.create(first_name='Author 2', no_of_prizes=3, no_of_books=1,
                                             date_of_birth='1899-10-02')
        self.author3 = Author.objects.create(first_name='Author 3', no_of_prizes=1, no_of_books=5,
                                             date_of_birth='1945-05-20')

    def test_author_list(self):
        # Test with min_price parameter
        self.client = APIClient()
        response = self.client.get(self.url, {'min_prize': 2})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['first_name'], 'Author 2')
