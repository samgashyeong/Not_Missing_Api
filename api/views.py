from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Quiz
from .serializer import QuizSerializer


@api_view(['GET'])
def helloapi(request):
    return Response("helloworld")

# Create your views here.
