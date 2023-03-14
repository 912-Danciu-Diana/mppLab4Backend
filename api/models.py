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
        return self.title


class User(models.Model):
    username = models.CharField(max_length=30, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)
    date_joined = models.DateTimeField(auto_now_add=True)
    birthday = models.DateTimeField()

    def __str__(self):
        return self.username


class Review(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    #date = models.DateTimeField(auto_now_add=True)
    rating = models.IntegerField()
    review = models.TextField()

    class Meta:
        unique_together = ('book', 'user')
