from rest_framework import viewsets
from .models import User, Coords, Level, Pereval, Images
from .serializers import UserSerializer, CoordsSerializer, LevelSerializer, PerevalSerializer, ImagesSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class CoordsViewSet(viewsets.ModelViewSet) :
    queryset = Coords.objects.all()
    serializer_class = CoordsSerializer

class LevelViewSet(viewsets.ModelViewSet):
    queryset = Level. objects.all()
    serializer_class = LevelSerializer

class PerevalViewSet(viewsets.ModelViewSet) :
    queryset = Pereval. objects.all()
    serializer_class = PerevalSerializer

class ImagesV1ewSet(viewsets.ModelViewSet) :
    queryset = Images.objects.all()
    serializer_class = ImagesSerializer
