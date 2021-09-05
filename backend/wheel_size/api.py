from rest_framework import generics,response,status
from .models import Make,Model,Year
from .serializers import MakeSerializer,ModelSerializer,YearSerializer,TrimSerializer
import requests
import json

class MakeListAPIView(generics.ListAPIView):
    serializer_class = MakeSerializer

    def get_queryset(self):
        return Make.objects.all()

    def list(self,request):
        queryset = self.get_queryset()
        if queryset.count():
            filtered_queryset = queryset.filter(active=True)
            serializer = self.get_serializer(filtered_queryset,many=True)
            return response.Response(serializer.data)
        else:
            serializer = None
            try:
                req = requests.get("http://wheel-size/makes")
                if req.status_code >= 400:
                    serializer = self.get_serializer(data=[],many=True)
                else:
                    data = json.loads(req.content) 
                    serializer = self.get_serializer(data=data,many=True)
            except requests.exceptions.ConnectionError:
                return response.Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)

            serializer.is_valid(raise_exception=True)
            serializer.save()
            return response.Response(serializer.data)

class ModelListAPIView(generics.ListAPIView):
    serializer_class = ModelSerializer

    def get_queryset(self):
        self.make_slug = self.request.GET.get('make')
        self.make = Make.objects.filter(slug=self.make_slug).first()
        
        if not self.make:
            return None

        return self.make.model_set.all()

    def list(self,request):
        queryset = self.get_queryset()

        if queryset == None:
            return response.Response(status=status.HTTP_404_NOT_FOUND)

        if queryset.count():
            filtered_queryset = queryset.filter(active=True)
            serializer = self.get_serializer(filtered_queryset,many=True)
            return response.Response(serializer.data)
        else:
            serializer = None
            try:
                req = requests.get("http://wheel-size/models/%s/" % self.make_slug)
                if req.status_code >= 400:
                    serializer = self.get_serializer(data=[],many=True)
                else:
                    data = json.loads(req.content) 
                    serializer = self.get_serializer(data=data,many=True)
            except requests.exceptions.ConnectionError:
                return response.Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)

            serializer.is_valid(raise_exception=True)
            serializer.save(make=self.make)
            return response.Response(serializer.data)

class YearListAPIView(generics.ListAPIView):
    serializer_class = YearSerializer

    def get_queryset(self):
        self.make_slug = self.request.GET.get('make')
        self.model_slug = self.request.GET.get('model')
        self.model = Model.objects.filter(
            slug=self.model_slug,
            make__slug=self.make_slug
        ).first()

        if not self.model:
            return None
        
        return self.model.year_set.all()

    def list(self,request):
        queryset = self.get_queryset()
        if queryset == None:
            return response.Response(status=status.HTTP_404_NOT_FOUND)

        if queryset.count():
            filtered_queryset = queryset.filter(active=True)
            serializer = self.get_serializer(filtered_queryset,many=True)
            return response.Response(serializer.data)
        else:
            serializer = None
            try:
                req = requests.get("http://wheel-size/years/%s/%s/" % (
                    self.make_slug,
                    self.model_slug
                ))
                if req.status_code >= 400:
                    serializer = self.get_serializer(data=[],many=True)
                else:
                    data = json.loads(req.content) 
                    serializer = self.get_serializer(data=data,many=True)
            except requests.exceptions.ConnectionError:
                return response.Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)

            serializer.is_valid(raise_exception=True)
            serializer.save(model=self.model,make=self.model.make)
            return response.Response(serializer.data)

class TrimListAPIView(generics.ListAPIView):
    serializer_class = TrimSerializer

    def get_queryset(self):
        self.make_slug = self.request.GET.get('make')
        self.model_slug = self.request.GET.get('model')
        self.year_slug = self.request.GET.get('year')
        self.year = Year.objects.filter(
            slug=self.year_slug,
            make__slug=self.make_slug,
            model__slug=self.model_slug
        ).first()

        if not self.year:
            return None
        
        return self.year.trim_set.all()

    def list(self,request):
        queryset = self.get_queryset()
        if queryset == None:
            return response.Response(status=status.HTTP_404_NOT_FOUND)

        if queryset.count():
            filtered_queryset = queryset.filter(active=True)
            serializer = self.get_serializer(filtered_queryset,many=True)
            return response.Response(serializer.data)
        else:
            serializer = None
            try:
                req = requests.get("http://wheel-size/trims/%s/%s/%s/" % (
                    self.make_slug,
                    self.model_slug,
                    self.year_slug
                ))
                if req.status_code >= 400:
                    serializer = self.get_serializer(data=[],many=True)
                else:
                    data = json.loads(req.content) 
                    serializer = self.get_serializer(data=data,many=True)
            except requests.exceptions.ConnectionError:
                return response.Response(
                    status=status.HTTP_500_INTERNAL_SERVER_ERROR
                )

            serializer.is_valid(raise_exception=True)
            serializer.save(
                year=self.year,
                model=self.year.model,
                make=self.year.make
            )
            return response.Response(serializer.data)
