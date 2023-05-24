from django.contrib import admin

# Register your models here.
from .models import*
from .models import Produit
admin.site.register(Produit)
from .models import Categorie
admin.site.register(Categorie)
from .models import Fournisseur
admin.site.register(Fournisseur)
from .models import Commande
admin.site.register(Commande)
from .models import ProduitNC
admin.site.register(ProduitNC)

from .models import *

admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(ShippingAddress)