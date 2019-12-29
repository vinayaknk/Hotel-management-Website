from django.urls import path
from . import views
from django.conf.urls import url


app_name = 'reservation'

urlpatterns = [
    path('reserve/',views.ReservePage.as_view(), name='reserve'),
    url(r"by/(?P<username>[-\w]+)/(?P<pk>\d+)/$", views.ReserveDetail.as_view(), name="detail"),
    url(r"by/(?P<username>[-\w]+)/$", views.UserPosts.as_view(), name="list"),
    url(r"delete/(?P<pk>\d+)/$",views.DeletePost.as_view(),name="delete"),
    url(r"update/(?P<pk>\d+)/$",views.UpdateReservePage.as_view(),name="update"),
    url(r"reserve/(?P<pk>\d+)/service/$",views.RoomserviceView.as_view(),name="service"),
    url(r"by/(?P<username>[-\w]+)/meal/$", views.MealListView.as_view(), name="meal_list"),
    url(r"deleteMeal/(?P<pk>\d+)/$", views.DeleteRoomService.as_view(), name="delete_meal"),
]