from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.shortcuts import render
from .models import Book
from .serializers import BookListSerializer, BookSerializer


@api_view(['GET', 'POST'])
def libraries_list(request):
    if request.method == 'GET':
        libraries = Book.objects.all()
        serializer = BookListSerializer(libraries, many=True)
        return Response(serializer.data)