from django.forms import model_to_dict
from django.shortcuts import render
from rest_framework import generics, viewsets, mixins
from rest_framework.decorators import action
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from .models import Women, Category
from .serializers import WomenSerializer


class WomenViewSet(mixins.CreateModelMixin,
                   mixins.RetrieveModelMixin,
                   mixins.UpdateModelMixin,
                   mixins.DestroyModelMixin,
                   mixins.ListModelMixin,
                   GenericViewSet):
    #queryset = Women.objects.all()
    serializer_class = WomenSerializer

    #переопределеяем get_queryset для получения определенного кол-ва записей по запросу
    def get_queryset(self):
        pk = self.kwargs.get('pk')
        if not pk:
            return Women.objects.all()[:3]
        else:
            return Women.objects.filter(pk=pk)

    #получить список категорий
    @action(methods=['get'], detail=True)
    def category(self, request, pk=None):
        cats = Category.objects.get(pk=pk)
        return Response({'cats': cats.name})


# #для возвращения списка записей по GET и добавления новой записи по POST
# class WomenAPIList(generics.ListCreateAPIView):
#     queryset = Women.objects.all()
#     serializer_class = WomenSerializer
#
#
# #для обновления одной записи(только PUT или PATCH
# class WomenAPIUpdate(generics.UpdateAPIView):
#     #отправляем одну измененную запись клиенту(ленивый запрос)
#     queryset = Women.objects.all()
#     serializer_class = WomenSerializer
#
#
# #для изменения/удаления/чтения записи
# class WomenAPIDetailView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Women.objects.all()
#     serializer_class = WomenSerializer
