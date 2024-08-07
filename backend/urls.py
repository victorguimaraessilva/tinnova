from rest_framework import routers
from django.contrib import admin
from django.urls import path, include
from .views import UserViewSet
from culture.views import CultureViewSet
from producer.views import ProducerViewSet
from dashboard.views import dashboard
from dashboard.views import DashboardView

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'cultures', CultureViewSet)
router.register(r'producers', ProducerViewSet)

urlpatterns = [
    path('', dashboard, name="dashboard"),
    path('api/dashboard', DashboardView.as_view()),
    path('api/', include(router.urls)),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls'))
]

