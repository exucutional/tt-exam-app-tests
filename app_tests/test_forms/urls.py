from .views import index_page, test_create, send_test_to_student, get_test_results
from django.urls import path

urlpatterns = [
  path('', index_page, name='index_page'),
  path('test_form', test_create, name='test_create'),
  path('send_test_to_student/<str:test_name>/<int:user_id>', send_test_to_student, name='send_test_to_student'),
  path('get_test_results', get_test_results, name='get_test_results'),
]