from django.urls import re_path, path
from . import views


urlpatterns = [
    path('order/', views.item_view, name = 'items-view'),
    path('order/send/', views.ContactSendView.as_view(), name = 'send'),
    path('newWP/', views.new_WP, name = 'newWP'),
    path('dequeueWP/', views.dequeue_WP, name = 'dequeuedWP'),
    path('dispatcher/', views.new_D, name = 'dispatcher'),
    path('dispatcher/change/', views.Dispatch.as_view(), name = 'dispatch'),
    path('warehouse/pdf/', views.PDF.as_view(), name = 'pdf-creation'),
    path('newWP/change/', views.DequeueOrder.as_view(), name = 'dequeue'),
    path('dequeueWP/complete/', views.CompleteOrder.as_view(), name = 'dequeue'),
    path('login/', views.login, name = 'login'),
    path('register/', views.reg, name = 'register'),
    path('register/submit/', views.Submit.as_view(), name = 'submit'),
    path('cmorders/', views.cmorders, name = 'cmorders'),
    path('cmorders/change/', views.DeliveredOrder.as_view(), name = 'cmorders'),
    path('dispatcher/csv/', views.CSV.as_view(), name = 'csv-creation'),
    re_path('^forgot/?', views.forgot, name = 'forgot-password'),
    re_path('^new-password/?', views.new_password, name = 'new-password-setting')
]
