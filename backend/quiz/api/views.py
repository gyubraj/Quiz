from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import MyQuizSerializer
from quiz.models import Question

class Quiz(APIView):
    def get(self,request):
        # language=self.request.query_params.get('language')
        language=request.GET.get('language','ENG')
        data=Question.get_13_question(self=Question,lan=language)
        serializer=MyQuizSerializer(data,many=True)
        return Response(serializer.data)
