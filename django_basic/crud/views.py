from django.views import generic
from .models import Goods
from .forms import GoodsCreateForm
 
class GoodsCreate(generic.CreateView):
    form_class = GoodsCreateForm
    template_name = 'crud/goods_create.html'
    success_url = '/crud/goods_create'
 
class GoodsList(generic.ListView):
    model = Goods
    template_name = 'crud/goods_list.html'
 
class GoodsDelete(generic.DeleteView):
    model = Goods
    template_name = 'crud/goods_delete.html'
