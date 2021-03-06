from django.conf.urls import url
import views

urlpatterns = [
    url(r'^$', views.index_test, name='index_test'),
    # url(r'^index_new/$', views.index_new, name='index_new'),
    # url(r'^index_test/$', views.index_test, name='index_test'),    
    

    url(r'^suyuan/$', views.suyuan, name='suyuan'),
    url(r'^signup/$', views.signup, name='signup'),

    url(r'^login/$', views.login, name='login'),
    url(r'^logout/$', views.logout, name='logout'),
    url(r'^set_password/$', views.set_password, name='set_password'),
    url(r'^add_book/$', views.add_book, name='add_book'),
    url(r'^control/$', views.control, name='control'),
    url(r'^demo/$', views.control_demo, name='control_demo'),    
    url(r'^csa_demo/$', views.csa_demo, name='csa_demo'),    

    url(r'^mqtt/$', views.mqtt, name='mqtt'),
    url(r'^generate_qrcode/$', views.generate_qrcode, name='generate_qrcode'),
    url(r'^realtime_info/$', views.realtime_info, name='realtime_info'),
    url(r'^view_book_list/$', views.view_book_list, name='view_book_list'),
    url(r'^video/$', views.video, name='video'),
    url(r'^json_test/$', views.json_test, name='json_test'),
    url(r'^crontab_daily/$', views.crontab_daily, name='crontab_daily'),
    url(r'^crontab_daily_incremental/$', views.crontab_daily_incremental, name='crontab_daily_incremental'),
    url(r'^view_book/detail/$', views.detail, name='detail'),
    url(r'^qrcode/(?P<field_name>field[0-9]+)/$', views.qrcode_generate_page, name='qrcode'),
    url(r'^fields/(?P<field_name>field[0-9]+)/$', views.fields, name='fields'),
]
