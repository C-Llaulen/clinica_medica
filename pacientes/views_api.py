from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from django.shortcuts import get_object_or_404
from .models import Paciente
from .serializers import PacienteSerializer


class LoginAPIView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        user = authenticate(username=username, password=password)
        if user:
            token, _ = Token.objects.get_or_create(user=user)
            return Response({
                'token': token.key,
                'username': user.username,
                'mensaje': 'Autenticación exitosa.'
            }, status=status.HTTP_200_OK)

        return Response({
            'error': 'Credenciales inválidas. Verifique usuario y contraseña.'
        }, status=status.HTTP_400_BAD_REQUEST)


class PacienteListCreateAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        pacientes = Paciente.objects.all().order_by('-id')
        serializer = PacienteSerializer(pacientes, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = PacienteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PacienteDetailAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        paciente = get_object_or_404(Paciente, pk=pk)
        serializer = PacienteSerializer(paciente)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        paciente = get_object_or_404(Paciente, pk=pk)
        serializer = PacienteSerializer(paciente, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        paciente = get_object_or_404(Paciente, pk=pk)
        paciente.delete()
        return Response(
            {'mensaje': 'Paciente eliminado correctamente de la base de datos.'},
            status=status.HTTP_204_NO_CONTENT
        )