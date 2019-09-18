from django.contrib import admin

from django.urls import path

from products.views import  (
 product_create_view,
	render_initial_data,
	dynamic_lookup_view, 
	product_delete_view, 
	product_list_view,
	product_update_view,

	render_initial_data,
	
 )

app_name ='products'
urlpatterns =[
	path('<int:id>/',dynamic_lookup_view,name='product-detail'),
	path('<int:id>/delete/',product_delete_view,name='product-delete'),
	path('', product_list_view,name='product-list'),
	path('<int:id>/update/', product_update_view, name = 'product-update'),
	path('initial/',render_initial_data, name='product-create'),
	path('create/',product_create_view),
]
