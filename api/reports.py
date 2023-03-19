from dataclasses import dataclass
from django.db.models import Count
from api.models import Review, User


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
