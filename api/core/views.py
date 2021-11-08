from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import render
from rest_framework import viewsets
from .serializers import FichaUsuarioSerializer
from .models import FichaUsuario

class FichaUsuarioViewSet(viewsets.ModelViewSet):
    queryset = FichaUsuario.objects.all()
    serializer_class = FichaUsuarioSerializer

#@api_view(['GET', 'POST'])
#def usuario_list(request):
#    """
#    List all code snippets, or create a new snippet.
#    """
#    if request.method == 'GET':
#        FichaUsuario = FichaUsuario.objects.all()
#        serializer = FichaUsuarioSerializer(FichaUsuario, many=True)
#        return Response(serializer.data)
#
#    elif request.method == 'POST':
#        serializer = FichaUsuarioSerializer(data=request.data)
#        if serializer.is_valid():
#            serializer.save()
#            return Response(serializer.data, status=status.HTTP_201_CREATED)
#        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)