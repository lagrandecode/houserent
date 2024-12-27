from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import APIView
from .models import Grid
from .serializers import GridSerializer
from django.http import Http404
# Create your views here.


class GridList(APIView):
    def get(self,request,format=None):
        grid = Grid.objects.all()
        serializer = GridSerializer(grid,many=True)
        return Response(serializer.data)
    
    def post(self,request,format=None):
        serializer = GridSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
class GridDetail(APIView):
    def get_object(self,pk):
        try:
            return Grid.objects.get(pk=pk)
        except Grid.DoesNotExist:
            raise Http404
            
    def get(self,request,pk,format=None):
        data = self.get_object(pk)
        serializer = GridSerializer(data)
        return Response(serializer.data)
    def put(self,request,pk,format=None):
        grid = self.get_object(pk)
        serializer = GridSerializer(grid,data=request.data)
    def delete(self,request,pk,format=None):
        grid = self.get_object(pk)
        grid.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

