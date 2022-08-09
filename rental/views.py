import email
from pydoc import describe
from unicodedata import name
from urllib import response
from urllib.request import Request
from .serializers import cycleSerializer, sportSerializer, electronicSerializer
from rest_framework.generics import ListAPIView
from .models import cycle,sport,electronic
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
class cycleList(ListAPIView):
    queryset = cycle.objects.all()
    serializer_class = cycleSerializer

    def post(self,request):
        try:
            obj = cycle(name=request.data['name'], 
            email= request.data['email'],
            contact=request.data['contact'],
            describe=request.data['describe'])
            obj.save()
            return Response(request.data, status=status.HTTP_200_OK)
        except:
            return Response({"error" : "some error"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class sportList(ListAPIView):
    queryset = sport.objects.all()
    serializer_class = sportSerializer

class electronicList(ListAPIView):
    queryset = electronic.objects.all()
    serializer_class = electronicSerializer

 