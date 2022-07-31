from rest_framework.response import Response
from rest_framework.decorators import api_view



@api_view(['GET'])
def orders_list(request):
        # gs_data = get_gs_data.delay()
        return Response({'data': 'work!!1'})
