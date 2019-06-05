from django.conf.urls import url
from rest_framework import routers
from .views import DepartmentViewSet, ProvinceViewSet, CustomView, RecognitionProduct, ProductViewSet, AuthenticateViewSet, UserViewSet, OrderViewSet, OrderDetailViewSet, ConditionViewSet
from rest_framework_swagger.views import get_swagger_view

router = routers.DefaultRouter()
router.register(r'departments', DepartmentViewSet)
router.register(r'provinces', ProvinceViewSet)
router.register(r'products', ProductViewSet)
router.register(r'users', UserViewSet)
router.register(r'orders', OrderViewSet)
router.register(r'orderdetails', OrderDetailViewSet)
router.register(r'conditions', ConditionViewSet)

schema_view = get_swagger_view(title="Comrade API")

urlpatterns = [
    url(r'customview', CustomView.as_view()),
    url(r'recproduct', RecognitionProduct.as_view()),
    url(r'authenticate',  AuthenticateViewSet.as_view()),
    url(r'^docs/', schema_view),

]

urlpatterns += router.urls