from django.urls import path, include
from . import views
from rest_framework.authtoken.views import obtain_auth_token


urlpatterns = [
	path('', views.apiRoutes, name="api-routes"),

	path('task-list/', views.taskList, name="task-list"),
	path('task-detail/<str:pk>/', views.taskDetail, name="task-detail"),

	path('task-create/', views.taskCreate, name="task-create"),

	path('task-update/<str:pk>/', views.taskUpdate, name="task-update"),
	path('task-delete/<str:pk>/', views.taskDelete, name="task-delete"),

    path('api-auth/', include('rest_framework.urls')),
    path('rest-auth/', include('rest_auth.urls')),


    path('api/token/', obtain_auth_token, name='obtain-token')

]