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
    authentication_classes = []
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
                "type_distribution": df["Type"].value_counts().to_dict(),
                "averages": {
                    "flowrate": round(df["Flowrate"].mean(), 2),
                    "pressure": round(df["Pressure"].mean(), 2),
                    "temperature": round(df["Temperature"].mean(), 2),
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
        # Get latest dataset
        dataset = Dataset.objects.last()

        if not dataset:
            return Response({"error": "No dataset found"}, status=400)

        # Read CSV
        df = pd.read_csv(dataset.file.path)

        # Calculations
        total_count = len(df)
        type_distribution = df["Type"].value_counts().to_dict()
        avg_flowrate = round(df["Flowrate"].mean(), 2)
        avg_pressure = round(df["Pressure"].mean(), 2)
        avg_temperature = round(df["Temperature"].mean(), 2)

        # Create PDF
        buffer = io.BytesIO()
        p = canvas.Canvas(buffer)

        y = 800
        p.drawString(100, y, "Chemical Equipment Analysis Report")
        y -= 30

        p.drawString(100, y, f"Total Records: {total_count}")
        y -= 30

        p.drawString(100, y, "Average Values:")
        y -= 20
        p.drawString(120, y, f"Flowrate: {avg_flowrate}")
        y -= 20
        p.drawString(120, y, f"Pressure: {avg_pressure}")
        y -= 20
        p.drawString(120, y, f"Temperature: {avg_temperature}")
        y -= 30

        p.drawString(100, y, "Equipment Type Distribution:")
        y -= 20

        for equipment, count in type_distribution.items():
            p.drawString(120, y, f"{equipment}: {count}")
            y -= 20

        p.showPage()
        p.save()

        buffer.seek(0)
        return FileResponse(buffer, as_attachment=True, filename="chemical_equipment_report.pdf")

