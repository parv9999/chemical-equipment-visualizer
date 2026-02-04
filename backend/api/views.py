from rest_framework.authentication import BasicAuthentication
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Dataset
import pandas as pd
from django.http import FileResponse
import io
from reportlab.pdfgen import canvas
from rest_framework.permissions import AllowAny
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator


@method_decorator(csrf_exempt, name='dispatch')
class UploadCSVView(APIView):
    authentication_classes = []   # 🔥 THIS LINE IS THE KEY
    permission_classes = [AllowAny]

    def post(self, request):
        file = request.FILES.get('file')

        if not file:
            return Response({"error": "No file uploaded"}, status=400)

        dataset = Dataset.objects.create(file=file)

        try:
            df = pd.read_csv(dataset.file.path)

            summary = {
                "total_count": len(df),
                "type_distribution": df["type"].value_counts().to_dict(),
                "averages": {
                    "flowrate": round(df["flowrate"].mean(), 2),
                    "pressure": round(df["pressure"].mean(), 2),
                    "temperature": round(df["temperature"].mean(), 2),
                }
            }

            return Response(summary)

        except Exception as e:
            dataset.delete()
            return Response({"error": str(e)}, status=400)



class SummaryView(APIView):
    authentication_classes = []
    permission_classes = [AllowAny]


    def get(self, request):
        datasets = Dataset.objects.order_by('-uploaded_at')[:5]
        data = []

        for d in datasets:
            try:
                df = pd.read_csv(d.file.path)
                data.append({
                    "total_count": len(df)
                })
            except:
                pass

        return Response(data)


class PDFReportView(APIView):
    authentication_classes = []
    permission_classes = [AllowAny]


    def get(self, request):
        buffer = io.BytesIO()
        p = canvas.Canvas(buffer)

        p.drawString(100, 800, "Chemical Equipment Report")
        p.drawString(100, 770, "Generated successfully")

        p.showPage()
        p.save()

        buffer.seek(0)
        return FileResponse(buffer, as_attachment=True, filename="report.pdf")
