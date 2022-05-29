# backend/notes/urls.py
from rest_framework import routers

from .views import usdruViewSet

# Создаем router и регистрируем наш ViewSet
router = routers.DefaultRouter()
router.register(r'usdrub', usdruViewSet)

# URLs настраиваются автоматически роутером
urlpatterns = router.urls