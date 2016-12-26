from django.conf.urls import include, url
from .views import MacroBotView
urlpatterns = [
    url(r'^f8aa22868a60e6570970045b01cecf7f05c9f78f0a7b4824f3/?$', MacroBotView.as_view())
]