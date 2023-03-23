from dataclasses import dataclass
from django.db.models import Count
from api.models import Review, User, Book


@dataclass
class ReportEntry:
    user: User
    count: int


def report():
    data = []
    queryset = Review.objects.values("user").annotate(count=Count("id"))
    for entry in queryset:
        user = User.objects.get(pk=entry["user"])
        report_entry = ReportEntry(user, entry["count"])
        data.append(report_entry)
    return data


""""
def ordered_report():
    queryset1 = Book.objects.values("author")
    queryset2 = Author.objects.all().order_by("no_of_prizes")
    #queryset3 = Book.objects.all().order_by(queryset2)
    combined_queryset = queryset1.union(queryset2)
    #queryset = queryset1 | queryset2
    return combined_queryset
"""

"""
@dataclass
class OrderedReportEntry:
    book: Book
    no_reviews: int
"""


def ordered_report():
    """"
    data = []
    queryset1 = Book.objects.all().order_by("author")
    queryset = Book.objects.values("author").annotate(count=Count("id"))
    for entry in queryset:
        author = Author.objects.get(pk=entry["author"])
        report_entry = OrderedReportEntry(author, entry["count"])
        data.append(report_entry)
    #dataa = data.sort(key=get_author)
    return queryset1
    """
    """
    statistics = Review.objects.values("book").annotate(
        no_reviews=Count('book')
    ).order_by('-no_reviews')
    return statistics
    """
    data = []
    queryset = Review.objects.values("user").annotate(count=Count("id")).order_by("-count")
    for entry in queryset:
        user = User.objects.get(pk=entry["user"])
        report_entry = ReportEntry(user, entry["count"])
        data.append(report_entry)
    return data
