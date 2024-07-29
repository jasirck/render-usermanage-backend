
from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt import views as jwt_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('defoult_admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/', include('usermanage.urls')),
    path('token/obtain/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
]+  static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

