from rest_framework.response import Response
from rest_framework.views import APIView

class BasicAPiView(APIView):

    def get(self, request):
        return Response(
            {
                "message" : "Basic View Rendering !"
            }
        )
    
class ProjectApiView(APIView):

    def get(self, request):
        return Response(
            {
                "message" : "Welcome to project !"
            }
        )