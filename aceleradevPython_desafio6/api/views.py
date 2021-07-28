from django.shortcuts import render
from collections import Counter
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.
@api_view(['POST'])
def lambda_function(request):
    if request.method == 'POST':
        question_list= request.data['question']
        # ordenando numeros
        answer = [num for num, c in Counter(question_list).most_common() for num in [num] * c]
        return Response({"solution": answer})

