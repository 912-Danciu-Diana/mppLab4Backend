from django.db import models


class Author(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    no_of_prizes = models.IntegerField()
    no_of_books = models.IntegerField()
    date_of_birth = models.DateField()

    def __str__(self):
        return self.first_name + " " + self.last_name


class Publisher(models.Model):
    name = models.CharField(max_length=255)
    founder = models.CharField(max_length=255)
    executive_director = models.CharField(max_length=255)
    no_of_employees = models.IntegerField()
    founding_date = models.DateField()

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    published_date = models.DateField()
    description = models.TextField()

    def __str__(self):
        return "Title: " + self.title + "\nAuthor: " + self.author.__str__() + "\nPublisher: " + self.publisher.__str__() + \
            "\nPublished date: " + self.published_date.__str__() + "\nDescription: " + self.description.__str__()
