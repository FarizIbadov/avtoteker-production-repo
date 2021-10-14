from django.shortcuts import render,redirect
from django.utils.translation import gettext as _
from django.views.generic import View
from .models import TireSize,Trim
import requests
import json

class TireSizeView(View):
    
    def get(self, request, *args, **kwargs):
        context =  self.get_context_data()

        self.make_slug = request.GET.get("make")
        self.model_slug = request.GET.get("model")
        self.year_slug = request.GET.get("year")
        self.trim_slug = request.GET.get("trim")
        queryset = self.get_queryset()

        if self.make_slug and self.model_slug and self.year_slug and self.trim_slug and queryset != None:
            new_queryset = self.fetch_tire_size(queryset)
            context['prepare_tire_list'] = self.get_prepare_tire_list(new_queryset)
            context['title'] = "%s %s - %s %s" % (self.trim.make.name,self.trim.model.name,self.trim.name,self.trim.year.name)
            return render(request,'main_site/wheel-size-page.html',context)
        else: 
            return redirect("home")


    def get_context_data(self):
        title = _("Seçim edin")
        context = {
            "tire_search_title":f"""<h2 class='tire-search__heading'>{title}</h2>""",
        }
        return context

    def get_queryset(self):
        self.trim = Trim.objects.filter(
            slug=self.trim_slug,
            make__slug=self.make_slug,
            model__slug=self.model_slug,
            year__slug=self.year_slug
        ).first()

        if not self.trim:
            return None

        return self.trim.tiresize_set.all()

    def get_prepare_tire_list(self,queryset):
        prepare_tire_list = []
        wheel_ids = list(
            queryset.values_list('wheel_id',flat=True).distinct()
        )
        for wheel_id in wheel_ids:
            filtered_set = queryset.filter(wheel_id=wheel_id)
            prepare_tire_list.append(filtered_set)
        
        return prepare_tire_list


    def fetch_tire_size(self,queryset):
        if queryset.count():
            return queryset
        else:
            try:
                query = "?make=%s&model=%s&year=%s&trim=%s" % (
                    self.make_slug,
                    self.model_slug,
                    self.year_slug,
                    self.trim_slug
                )
                req = requests.get("http://wheel-size/search/%s" % query)
                if req.status_code >= 400:
                    return queryset

                tire_list = json.loads(req.content)
                for tire in tire_list:
                    TireSize.objects.create(
                        **tire,
                        trim=self.trim,
                        year=self.trim.year,
                        model=self.trim.model,
                        make=self.trim.make 
                    )
                 
                return self.trim.tiresize_set.all()

            except requests.exceptions.ConnectionError:
                return queryset
