from .views import addImage
from django.urls import path
app_name = 'imageuploader'

urlpatterns = [
    path('imageupload/', addImage, name='image'),

    ]