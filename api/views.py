from rest_framework.response import Response
from rest_framework.decorators import api_view
import requests
from .models import Quiz
from .serializer import QuizSerializer
from .loaddata import parsingData, safeLoadData


@api_view(['GET'])
def helloapi(request):
    return Response("helloworld")

@api_view(['GET'])
def missingPeople(request, page):
    result = parsingData(page)
    return Response(result.json())

@api_view(['GET'])
def safeSpotData(request, pageIndex):
    result = safeLoadData(pageIndex)
    return Response(result.json())
