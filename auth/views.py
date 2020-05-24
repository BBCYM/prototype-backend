from rest_framework import views, response, status
import dialogflow_v2 as dialogflow
from google.oauth2 import service_account
from operator import itemgetter
import json
from google.api_core.exceptions import InvalidArgument
# Create your views here.
# 自訂義一個View叫AuthView，繼承了rest_framework.views的APIView
class AuthView(views.APIView):
    # http get method
    def get(self,request):
        res = {'data': 1, 'hello': 'world'}
        return response.Response(res)

    # def post(self,request):

    # http post method
    def post(self,request):
        
        credential = service_account.Credentials.from_service_account_file('dfcredentials.json').with_scopes(['https://www.googleapis.com/auth/dialogflow'])
        with open('dfcredentials.json', encoding='utf-8') as f:
            appSecret = json.load(f)
            PROJECT_ID = itemgetter("project_id")(appSecret)
        session_id = 'userforDemo182839'
        text = "給我柴柴的照片"

        session_client=dialogflow.SessionsClient(credentials=credential)
        session=session_client.session_path(PROJECT_ID,session_id)

        text_input = dialogflow.types.TextInput(text=text,language_code='zh-TW')
        query_input = dialogflow.types.QueryInput(text=text_input)
        try:
            res = session_client.detect_intent(session=session,query_input=query_input)
        except InvalidArgument:
            return response.Response("InvalidArgument",status=status.HTTP_400_BAD_REQUEST)
        print(res.query_result)
        # print("Query text:", res.query_result.query_text)
        # print("Detected intent:", res.query_result.intent.display_name)
        # print("Detected intent confidence:", res.query_result.intent_detection_confidence)
        # print("Fulfillment text:", res.query_result.fulfillment_text)
        print(res.query_result.parameters.fields['dog'].string_value)
        return response.Response("ok")
        
