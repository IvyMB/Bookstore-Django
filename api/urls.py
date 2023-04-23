
from django.contrib import admin
from django.urls import path, re_path, include

import order.urls
import product.urls

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path('api/(?P<version>(v1|v2))', include(order.urls)),
    re_path('api/(?P<version>(v1|v2))', include(product.urls))
]
