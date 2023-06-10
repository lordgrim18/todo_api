from django.urls import path, include
from . import views
# from rest_framework.authtoken.views import obtain_auth_token
from .views import TaskDetail, TaskList, TaskCreate
from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
	path('', views.apiRoutes, name="api-routes"),

	path('task-list/', TaskList.as_view(), name="task-list"),
	path('task-detail/<str:pk>/', TaskDetail.as_view(), name="task-detail"),

	path('task-create/', TaskCreate.as_view(), name="task-create"),


    path('api-auth/', include('rest_framework.urls')),

    # path('rest-auth/', include('rest_auth.urls')),
    #path('api/token/', obtain_auth_token, name='obtain-token')
	path('api/token/',jwt_views.TokenObtainPairView.as_view(),name ='token_obtain_pair'),
    path('api/token/refresh/',jwt_views.TokenRefreshView.as_view(),name ='token_refresh'),

]