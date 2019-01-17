from .views import pickles
from django.urls import path


urlpatterns = [
    path("pickles", pickles, name="pickle-api")
]
