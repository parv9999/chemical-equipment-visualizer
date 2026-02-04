from django.urls import path
from .views import UploadCSVView, SummaryView, PDFReportView

urlpatterns = [
    path("upload/", UploadCSVView.as_view(), name="upload"),
    path("summary/", SummaryView.as_view(), name="summary"),
    path("report/", PDFReportView.as_view(), name="report"),
]
