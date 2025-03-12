from django.shortcuts import render
from rest_framework.views import APIView
from .models import SaveData
from .serializer import DataSerializer
from rest_framework.response import Response

# Create your views here.

class Save_Data(APIView):
    def post(self, request):
        serializer = DataSerializer(data=request.data)
        if serializer.is_valid():
            field = request.data.get('text')
            serializer.save(text=field)
            return Response({
                'success': str(field)
            })
        return Response({
            'failed': 'it is not valid!'
        })
    def get(self, request):
        texts = SaveData.objects.all().order_by()[:10]
        serializer = DataSerializer(texts, many=True)
        return Response(serializer.data)