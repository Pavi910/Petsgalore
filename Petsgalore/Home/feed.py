from django.contrib.syndication.views import Feed
from django.template.defaultfilters import truncatewords
from .models import PetProducts
from django.urls import reverse

class latestproduct(Feed):

    title="petinaries"
    link="/drcomments/"
    discription="newly launching food product esspecailly for cats,hygene and healthy quality product"

    def items(self):
        return PetProducts.objects.all()[:4]

    def item_title(self,x):
        return x.name

    def item_description(self,x):
        return truncatewords(x.desc,10)

    def item_link(self,i):
        return reverse("homepage")
    