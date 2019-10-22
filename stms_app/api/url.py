from rest_framework import routers
from .view import Authtoken,Authtoken1
from django.urls import path,include


router=routers.DefaultRouter()
router.register('sample',Authtoken)
router.register('sample1',Authtoken1)
router.register(r'', loginView, base_name='loginview')
urlpatterns=[
    path('',include(router.urls)),
    path('',router.urls),
]