from django.shortcuts import redirect
from django.contrib.postgres.search import TrigramSimilarity
from django.urls import reverse
from django.views.generic import TemplateView, ListView, DetailView,View
from .mixins import FilterBySizeMixin
from tireapp.models import Tire
from specific.models import Brand,Serie
from ordering.forms import OrderForm
import re


class MainPage(TemplateView):
    template_name = "main_site/index.html"

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['tire_search_title'] = "<h2 class='tire-search__heading'>Təkər seçimi</h2>"
        return context


class MainListView(FilterBySizeMixin, ListView):
    paginate_by = 8
    template_name = "main_site/list.html"

    def get_queryset(self):        
        kwargs = self.get_filter()
        return Tire.objects.available().filter(**kwargs).order_by("-brand__order_number")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = OrderForm
        context['tire_search_title'] = "<h2 class='tire-search__heading'>Seçim edin</h2>"
        return context


class MainDetailView(DetailView):
    template_name = "main_site/detail.html"
    query_pk_and_slug = True

    def get_object(self):
        pk = self.kwargs['pk']
        slug = self.kwargs['slug']
        return Tire.objects.get(slug=slug,pk=pk)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = OrderForm
        context['tire_search_title'] = "<h2 class='tire-search__heading'>Seçim edin</h2>"
        return context


# class MainSearchView(View):
#     def get(self,request,*args,**kwargs):
#         list_query_list = [] 
#         search = request.GET['search'].strip()
#         regex = re.compile(r"\s+")
#         search_list = regex.split(search) 

#         for search_query in search_list:
#             size_query = self.check_for_size(search_query)
#             if size_query:
#                 list_query_list.append(size_query)
#                 continue

#             brand_query = self.check_for_brand(search_query)
#             if brand_query:
#                 list_query_list.append(brand_query)
#                 continue
            
#             serie_query = self.check_for_serie(search_query)
#             if serie_query:
#                 list_query_list.append(serie_query)
#                 continue

#         list_query = "&".join(list_query_list)
#         list_path = reverse('list')
#         list_url = "?".join([list_path,list_query])
#         return redirect(list_url)

#     def check_for_size(self,query):
#         regex = re.compile(r"(\d{3})?(\d{0,2})?(\d{0,3})?")
#         groups = regex.search(query)

#         if not groups:
#             return None

#         width,height,radius = groups.groups()

#         if not width and not height and not radius:
#             return None

#         width_query = "width=%s" % width
#         height_query = "height=%s" % height
#         radius_query = "radius=%s" % radius
#         return "&".join([width_query,height_query,radius_query])

#     def check_for_brand(self,query):
#         brand_title = Brand.objects.annotate(similarity=TrigramSimilarity('title',query)).all().order_by('-similarity','-order_number').first().title
#         return "brand=%s" % brand_title.lower()

#     def check_for_serie(self,query):
#         serie_title = Serie.objects.annotate(similarity=TrigramSimilarity('title',query)).all().order_by('-similarity').first().title
#         return "serie=%s" % serie_title.lower()
