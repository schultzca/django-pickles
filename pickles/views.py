from django.shortcuts import render
from rest_framework import serializers, permissions
import rest_framework.generics as generics
from .models import Pickle, PickleType


class PickleTypeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PickleType
        fields = ("name",)


class PickleSerializer(serializers.HyperlinkedModelSerializer):
    pickle_type = PickleTypeSerializer()
    class Meta:
        model = Pickle
        fields = ("pickle_type", "size", "price")


# Create your views here.
class PickleList(generics.ListAPIView):
    queryset = Pickle.objects.all()
    serializer_class = PickleSerializer


class PickleDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Pickle.objects.all()
    serializer_class = PickleSerializer