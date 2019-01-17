from django.shortcuts import render
from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Pickle, PickleType


class PickleTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PickleType
        fields = ("name",)


class PickleSerializer(serializers.HyperlinkedModelSerializer):
    pickle_type = PickleTypeSerializer()

    class Meta:
        model = Pickle
        fields = ("pickle_type", "size", "price")


# Create your views here.
@api_view()
def pickles(request):
    queryset = Pickle.objects.all()
    return Response(PickleSerializer(queryset))
