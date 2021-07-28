"""from django.test import TestCase

# Create your tests here.
"""
"""curl -X POST http://127.0.0.1:8000/lambda/ -H "Content-Type: application/json" -d '{"question": [2, 3, 2, 4, 5, 12, 2, 3, 3, 3, 12, 5]}'
response {"solution":[3,3,3,3,2,2,2,5,5,12,12,4]}
""""""
from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework.views import status
from models import Numbers
from .serializers import NumbersSerializer

#tests for views

class BaseViewTest(APITestCase):
    client = APIClient()

    @staticmethod
    def receiving_numbers(numbers_list):
        if numbers_list != "":
            Numbers.object.create(question=numbers_list)

    def setUp(self):
        #add

class testing_if_answer_is_correct(BaseViewTest):
    response = self.client.get(reverse("answer")) #kwargs talvez aqui
    serialized = NumbersSerializer(expected, many=True)
    self.assertEqual(response.data, serialized.data)
    self.assertEqual(response.status_code, status.HTTP_200_OK)

"""