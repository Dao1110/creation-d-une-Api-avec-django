from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import LivreSerializer
from .models import Livre


# Create your views here.
@api_view(['GET'])
def allBooks(request):
    books = Livre.objects.all()
    serialization = LivreSerializer(books,many=True)
    return Response(serialization.data)

#------------------------------------------------------------
@api_view(['GET'])
def getBook(request,id):
    book = Livre.objects.get(id=id)
    serializer = LivreSerializer(book)
    return Response(serializer.data)

#-------------------------------------------------------------

@api_view(['POST'])
def addBooks(request):
    serialiser = LivreSerializer(data = request.data, many=True)
    if serialiser.is_valid():
        serialiser.save()
    return Response(serialiser.data)

#-------------------------------------------------------------
@api_view(['PUT'])
def updateBook(request,id):
    book = Livre.objects.get(id=id)
    serialiser = LivreSerializer(instance= book ,data = request.data)
    if serialiser.is_valid():
        serialiser.save()
    return Response(serialiser.data)

@api_view(['DELETE'])
def deleteBook(request,id):
    book = Livre.objects.get(id=id)
    book.delete()
    return Response("livre supprimé")