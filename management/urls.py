from django.conf.urls import url
import views

urlpatterns = [
    url(r'^$', views.index, name='homepage'),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^login/$', views.login, name='login'),
    url(r'^logout/$', views.logout, name='logout'),
    url(r'^set_password/$', views.set_password, name='set_password'),
    url(r'^add_book/$', views.add_book, name='add_book'),
    url(r'^generate_qrcode/$', views.generate_qrcode, name='add_img'),
    url(r'^realtime_info/$', views.realtime_info, name='realtime_info'),
    url(r'^view_book_list/$', views.view_book_list, name='view_book_list'),
    url(r'^video/$', views.video, name='video'),
    url(r'^json_test/$', views.json_test, name='json_test'),
    url(r'^view_book/detail/$', views.detail, name='detail'),
    url(r'^qrcode/(?P<product_name>rice[0-9]+)/$', views.qrcode_generate_page, name='qrcode'),
]
