from django.test import TestCase
from .models import Author, Review, User, Book, Publisher
from datetime import date
from django.db import models


class AuthorModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Author.objects.create(first_name='John', last_name='Doe', no_of_prizes=3, no_of_books=10, date_of_birth=date(1980, 1, 1))

    def test_author_first_name(self):
        author = Author.objects.get(id=1)
        self.assertEqual(author.first_name, 'John')

    def test_author_last_name(self):
        author = Author.objects.get(id=1)
        self.assertEqual(author.last_name, 'Doe')

    def test_author_no_of_prizes(self):
        author = Author.objects.get(id=1)
        self.assertEqual(author.no_of_prizes, 3)

    def test_author_no_of_books(self):
        author = Author.objects.get(id=1)
        self.assertEqual(author.no_of_books, 10)

    def test_author_date_of_birth(self):
        author = Author.objects.get(id=1)
        self.assertEqual(author.date_of_birth, date(1980, 1, 1))


class ReviewModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        # Create test data for the Review model
        author = Author.objects.create(first_name='John', last_name='Doe', no_of_prizes=3, no_of_books=10,
                                       date_of_birth='2000-01-01')
        publisher = Publisher.objects.create(name='Test Publisher', founder='Jane Smith',
                                             executive_director='John Smith', no_of_employees=50,
                                             founding_date='1990-01-01')
        book = Book.objects.create(title='Test Book', author=author, publisher=publisher, published_date='2022-01-01',
                                   description='Test description')
        user = User.objects.create(username='testuser', email='testuser@example.com', password='test123',
                                   birthday='2000-01-01')
        Review.objects.create(book=book, user=user, rating=4, review='Test review')

    def test_review_book(self):
        review = Review.objects.get(id=1)
        self.assertEqual(review.book.title, 'Test Book')

    def test_review_user(self):
        review = Review.objects.get(id=1)
        self.assertEqual(review.user.username, 'testuser')

    def test_review_rating(self):
        review = Review.objects.get(id=1)
        self.assertEqual(review.rating, 4)

    def test_review_review(self):
        review = Review.objects.get(id=1)
        self.assertEqual(review.review, 'Test review')

    def test_review_unique_together(self):
        author = Author.objects.create(first_name='Jane', last_name='Doe', no_of_prizes=3, no_of_books=10,
                                       date_of_birth='2000-01-01')
        publisher = Publisher.objects.create(name='Test Publisher 2', founder='Jane Smith',
                                             executive_director='John Smith', no_of_employees=50,
                                             founding_date='1990-01-01')
        book = Book.objects.create(title='Test Book 2', author=author, publisher=publisher, published_date='2022-01-01',
                                   description='Test description')
        user = User.objects.create(username='testuser2', email='testuser2@example.com', password='test123',
                                   birthday='2000-01-01')
        Review.objects.create(book=book, user=user, rating=3, review='Test review 2')
        with self.assertRaises(Exception):
            Review.objects.create(book=book, user=user, rating=2, review='Duplicate review')