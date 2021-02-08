#8888/ 이후 무엇이 들어오든 'opencv_webapp'에 맞긴다

from django.urls import path,include
from . import views # 같은 폴더 안 views
from django.conf import settings
from django.conf.urls.static import static #settings.py 에서 static

app_name = 'opencv_webapp'

urlpatterns = [
    path('',views.first_view, name='first_view'),
    path('simple_upload/',views.simple_upload, name='simple_upload'),
    path('detect_face/',views.detect_face, name='detect_face'),
    
]

urlpatterns += static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)
