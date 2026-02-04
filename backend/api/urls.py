from django.urls import path
from .views import UploadCSVView, SummaryView, PDFReportView

urlpatterns = [
    path('upload/', UploadCSVView.as_view()),
    path('summary/', SummaryView.as_view()),
    path('pdf/', PDFReportView.as_view()),
]
