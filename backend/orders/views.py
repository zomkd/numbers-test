from rest_framework.response import Response
from rest_framework.decorators import api_view

from .tasks import get_gs_data


@api_view(['GET'])
def orders_list(request):
    if request.method == 'GET':
        gs_data = get_gs_data.delay()
        return Response({'data': 'work!!1'})
        