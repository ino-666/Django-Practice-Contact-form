from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required
 
app_name = 'crud'
urlpatterns = [
    path('goods_create/', login_required(views.GoodsCreate.as_view()), name='goods_create'),
]
