from django.contrib.sitemaps import Sitemap
from.models import *

class ArticleSitemap(Sitemap): 
	def items(self): 
		return Article.objects.all() 
		
	def lastmod(self, obj): 
		return obj.lastedit_date
