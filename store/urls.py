from django.urls import path
from . import views

# from rest_framework.routers import SimpleRouter, DefaultRouter
from rest_framework_nested import routers

# router = SimpleRouter()
# router = DefaultRouter()

router = routers.DefaultRouter()
router.register("products", views.ProductViewSet, basename="products")
router.register("collections", views.CollectionViewSet, basename="collections")
router.register("carts", views.CartViewSet, basename="carts")
router.register("customers", views.CustomerViewSet, basename="customers")
router.register("orders", views.OrderViewSet, basename="orders")


products_router = routers.NestedDefaultRouter(router, "products", lookup="product")
carts_router = routers.NestedDefaultRouter(router, "carts", lookup="cart")


products_router.register("reviews", views.ReviewViewSet, basename="product-reviews")
carts_router.register("items", views.CartItemViewSet, basename="cart-items")


urlpatterns = router.urls + products_router.urls + carts_router.urls

# URLConf
# urlpatterns = [
# path("products/", views.product_list),
# path("products/", views.ProductList.as_view()),
# # path("products/<int:id>", views.product_detail),
# path("products/<int:pk>", views.ProductDetail.as_view()),
# # path("collections/", views.collection_list),
# path("collections/", views.CollectionList.as_view()),
# # path("collections/<int:pk>", views.collection_detail, name="collection_detail"),
# path(
#     "collections/<int:pk>",
#     views.CollectionDetail.as_view(),
#     name="collection_detail",
# ),
# ]
