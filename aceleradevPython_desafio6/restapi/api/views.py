from django.shortcuts import render
from collections import Counter
from rest_framework.decorators import api_view
from rest_framework.response import Response
"""
Função 1) A função a ser implementada em um endpoint recebe um request com POST com um json,
 que contem uma lista de numeros, a função deve deve retornar uma lista com os numeros 
 ordenados pela quantidade de vezes que eles aparecem na lista.
"""
# Create your views here.
@api_view(['POST'])
def lambda_function(request):
    if request.method == 'POST':
        data = request.data
        question_list= data['question']
        # ordenando numeros
        answer = [num for num, c in Counter(question_list).most_common() for num in [num] * c]
        return Response({"solution": answer})


