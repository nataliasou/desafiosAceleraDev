from django.db import models

# Create your models here.

class Numbers(models.Model):
    #numeros para a lista
"""
POST data = {"question": [2, 3, 2, 4, 5, 12, 2, 3, 3, 3, 12, 5]}
Response = {"solution":[3 ,3, 3, 3, 2, 2, 2, 5, 5, 12, 12, 4]}
Função =   solution([2, 3, 2, 4, 5, 12, 2, 3, 3, 3, 12, 5]) == [3, 3, 3, 3, 2, 2, 2, 5, 5, 12, 12, 4]]
"""
