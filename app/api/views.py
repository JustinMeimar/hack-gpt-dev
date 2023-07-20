from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['POST'])
def prompt_endpoint(request):
    
    prompt = request.query_params.get('prompt', None)

    if prompt: 
        return Response({'prompt': prompt})
    else: 
        return Response({'error': 'prompt was not receieved or did not process'})