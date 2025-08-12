from rest_framework import viewsets
from .models import User, Coords, Level, Pereval, Images
from .serializers import UserSerializer, CoordsSerializer, LevelSerializer, PerevalSerializer, ImagesSerializer
from django.db import DatabaseError
from rest_framework import status
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class CoordsViewSet(viewsets.ModelViewSet) :
    queryset = Coords.objects.all()
    serializer_class = CoordsSerializer

class LevelViewSet(viewsets.ModelViewSet):
    queryset = Level. objects.all()
    serializer_class = LevelSerializer

class ImagesViewSet(viewsets.ModelViewSet) :
    queryset = Images.objects.all()
    serializer_class = ImagesSerializer

class PerevalViewSet(viewsets.ModelViewSet) :
    queryset = Pereval. objects.all()
    serializer_class = PerevalSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['user__email']

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)

        try:
            if not serializer.is_valid():
                return Response(
                    {
                        "status": 400,
                        "message": serializer.errors,
                        "id": None
                    },
                    status=status.HTTP_400_BAD_REQUEST
                )
            serializer.save()
            return Response(
                {
                    "status": 200,
                    "message": None,
                    "id": serializer.instance.id
                },
                status=status.HTTP_200_OK
            )
        except DatabaseError as e:
            return Response(
                {
                    "status": 500,
                    "message": f"Ошибка подключения к базе данных: {str(e)}",
                    "id": None
                },
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

    def partial_update(self, request, *args, **kwargs):
        pereval = self.get_object()
        serializer = self.get_serializer(pereval, data=request.data, partial=True)

        if pereval.status != "new":
            return Response(
                {'state': 0, 'message': 'Некорректный статус'},
                status=status.HTTP_400_BAD_REQUEST
            )

        if 'user' in request.data:
            current_user_data = UserSerializer(pereval.user).data
            for field in current_user_data:
                if field in request.data['user'] and request.data['user'][field] != current_user_data[field]:
                    return Response(
                        {'state': 0, 'message': 'Нельзя изменять данные пользователя'},
                        status=status.HTTP_400_BAD_REQUEST
                    )

        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(
            {'state': 1, 'message': 'Запись успешно обновлена'},
            status=status.HTTP_200_OK
        )


