from django.conf.urls import url
import views

urlpatterns = [
    url(r'^$', views.index, name='homepage'),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^login/$', views.login, name='login'),
    url(r'^logout/$', views.logout, name='logout'),
    url(r'^set_password/$', views.set_password, name='set_password'),
    url(r'^add_book/$', views.add_book, name='add_book'),
    url(r'^add_img/$', views.add_img, name='add_img'),
    url(r'^view_book_list/$', views.view_book_list, name='view_book_list'),
    url(r'^video/$', views.video, name='video'),
    url(r'^view_book/detail/$', views.detail, name='detail'),
	url(r'^generate_qrcode/(?P<product_name>rice[0-9]+)/$', views.generate_qrcode, name='qrcode'),
]
