from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from .serializers import *
from .models import *
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework import status
from .serializers import FileSerializer
class FileView(APIView):
    parser_classes = (MultiPartParser, FormParser)
    def post(self, request, *args, **kwargs):
        file_serializer = FileSerializer(data=request.data)
        if file_serializer.is_valid():
            file_serializer.save()
            return Response(file_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ImageDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = File.objects.all()
    serializer_class = FileSerializer


class ImageList(generics.ListCreateAPIView):
    serializer_class = FileSerializer
    queryset = File.objects.all()
    filter_backends = (DjangoFilterBackend,)
    filter_fields = '__all__'

