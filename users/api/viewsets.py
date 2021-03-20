from rest_framework import viewsets, mixins, permissions
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from users.models import CustomUser
from .serializers import CustomUserSerializer


# class UsersViewSet(ModelViewSet):
#     """
#     A simple ViewSet for viewing and editing accounts.
#     """
#     # queryset = CustomUser.objects.all()
#     serializer_class = CustomUserSerializer
#
#     def get_queryset(self):
#         return CustomUser.objects.all()
#         # return CustomUser.objects.filter(is_staff=True) # Pega somente se for staff admin

# class UsersViewSet(viewsets.ModelViewSet):
#     # permission_classes = (
#     #     EhSuperUser,
#     #     permissions.DjangoModelPermissions,
#     # )
#     queryset = CustomUser.objects.all()
#     serializer_class = CustomUserSerializer
#
#     def create(self, request, *args, **kwargs):
#         queryset = User.objects.all()
#         serializer = UserSerializer(queryset, many=True)
#         return Response(serializer.data)
#
#     # @action(detail=True, methods=['get'])
#     # def avaliacoes(self, request, pk=None):
#     #     self.pagination_class.page_size = 1
#     #     avaliacoes = Avaliacao.objects.filter(curso_id=pk)
#     #     page = self.paginate_queryset(avaliacoes)
#     #
#     #     if page is not None:
#     #         serializer = AvaliacaoSerializer(page, many=True)
#     #         return self.get_paginated_response(serializer.data)
#     #
#     #     # curso = self.get_object()
#     #     serializer = AvaliacaoSerializer(avaliacoes, many=True)
#     #     return Response(serializer.data)


# Create User - New User
class CreateUserViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    permission_classes = [permissions.AllowAny]
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer


# All - Admins
class AdminUsersViewSet(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet
):
    permission_classes = [permissions.IsAdminUser]
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
