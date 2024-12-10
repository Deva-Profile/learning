from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.sitemaps.views import sitemap
from store.sitemap import ArticleSitemap


urlpatterns=[

    path('registerUserAPI',views.RegisterUserAPI.as_view(),name='registerUserAPI'),
    path('ProductView',views.ProductView.as_view(),name='ProductView'),
    # path('createProductView',views.CreateProductView.as_view(),name='createProductView'),
    path('productdetail',views.ProductDetail.as_view(),name='productdetail'),
    path('sitemap.xml', sitemap, {'sitemaps': {'article' : ArticleSitemap}}, 
            name='django.contrib.sitemaps.views.sitemap'),
       
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

   

