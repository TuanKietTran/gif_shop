"""
URL configuration for gif_shop project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from landing import views as landing_views
from auth import views as auth_views
# from checkouts import views as checkout_views
from subscriptions import views as subscriptions_views

urlpatterns = [
    path('accounts/billing/', subscriptions_views.user_subscription_view, name='user_subscription'),
    path('accounts/billing/cancel', subscriptions_views.user_subscription_cancel_view, name='user_subscription_cancel'),
    path('accounts/', include('allauth.urls')),
    path("", landing_views.landing_dashboard_page_view, name='home'),
    path("pricing/", subscriptions_views.subscription_price_view, name='pricing'),
    path("pricing/<str:interval>/", subscriptions_views.subscription_price_view, name='pricing_interval'),
    path('admin/', admin.site.urls),
]
