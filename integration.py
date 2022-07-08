import sib_api_v3_sdk
from sib_api_v3_sdk.rest import ApiException

API_KEY = 'SEND_IN_BLUE_API_KEY'          //  "replace api key"
TEMPLATE_ID = 'send-in-blue template id'  // "replace template id"

configuration = sib_api_v3_sdk.Configuration()
configuration.api_key['api-key'] = API_KEY

def send_mail_to_agent(cls, data):
    """
    This function used to send email to agent
    """
    
    api_instance = sib_api_v3_sdk.TransactionalEmailsApi(sib_api_v3_sdk.ApiClient(cls.configuration))
    to = [{"email": "email", "name": "Title of recipient"}]
    params = {"body": body, "templateId": TEMPLATE_ID}
    
    send_smtp_email = sib_api_v3_sdk.SendSmtpEmail(to=to, params=params, template_id=TEMPLATE_ID)

    try:
        api_response = api_instance.send_transac_email(send_smtp_email)
        return api_response
    except ApiException as e:
        print(e)
        return None