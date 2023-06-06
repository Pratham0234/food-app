from django.urls import path
from . import views
app_name='food'
urlpatterns = [
    path("",views.index,name='index'),
    # path("items/",views.index,name='items'),
    path("<int:item_id>/",views.item_detail,name='item_detail'),

    # add item route
    path('add/',views.add_item,name="add_item"),
    #update item
    path('update/<int:item_id>/',views.update_item,name="update_item"),
    #delete item
    path('delete/<int:item_id>/',views.delete_item,name="delete_item")

]