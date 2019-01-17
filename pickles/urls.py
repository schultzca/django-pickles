from django.urls import path

from .views import PickleList, PickleDetail


urlpatterns = [
    path("pickles/", PickleList.as_view(), name="pickle-list"),
    path("pickles/<int:pk>/", PickleDetail.as_view(), name="pickle-detail")
]
