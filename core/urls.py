from django.urls import path, include

from .views import home

V1_PATTERNS = [
    path("", home),
    path("auths/", include("core.auths.urls")),
]

urlpatterns = [
    path(
        "api/",
        include(
            [
                path("v1/", include(V1_PATTERNS)),
            ]
        ),
    ),
]
