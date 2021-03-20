from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from users.api.viewsets import CreateUserViewSet, AdminUsersViewSet
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

router = routers.DefaultRouter()
router.register(r'createUser', CreateUserViewSet, basename='CustomUser')
router.register(r'adminUser', AdminUsersViewSet, basename='CustomUser')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/auth-token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/refresh-token/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/verify-token/', TokenVerifyView.as_view(), name='token_verify'),
    path('api/', include(router.urls)),
]
