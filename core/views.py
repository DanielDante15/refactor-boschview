from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from django.contrib.auth.hashers import make_password

from rest_framework import generics

from .models import User, Project
from .serializers import *

class UserCreate(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# View para obter detalhes de um usuário específico
class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# View para atualizar um usuário
class UserUpdate(generics.UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

   
    def update(self, request, *args, **kwargs):
        mutable_data = request.data.copy()

        if 'password' in mutable_data:
            # Se sim, atualize a senha usando set_password
            mutable_data['password'] = make_password(mutable_data['password'])

        # Substitua os dados originais pelos dados modificados
        request.data._mutable = True
        request.data.clear()
        request.data.update(mutable_data)
        request.data._mutable = False

        return super().update(request, *args, **kwargs)

# View para excluir um usuário
class UserDelete(generics.DestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer



class ProjectCreate(generics.CreateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

# View para listar todos os projetos
class ProjectList(generics.ListAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

# View para obter detalhes de um projeto específico
class ProjectDetail(generics.RetrieveAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

# View para atualizar um projeto
class ProjectUpdate(generics.UpdateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

# View para excluir um projeto
class ProjectDelete(generics.DestroyAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class UserWithProjectsList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserWithProjectsSerializer

class SingleProjectWithUser(generics.RetrieveAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectWithUserSerializer
class ProjectsWithUserList(generics.ListAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectWithUserSerializer