from django.urls import path
from .views import image_gallery
# from django.views.static import serve

urlpatterns = [
    path('gallery/', image_gallery, name='image_gallery')
] 

# if settings.DEBUG:
#     urlpatterns += [
#         path('static/<path>', serve, {
#             'document_root': settings.STATIC_ROOT,
#         }),
#     ]