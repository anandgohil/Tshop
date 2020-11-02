from instamojo_wrapper import Instamojo

API_KEY = "test_e6582de88962af12a93fa92b007"
AUTH_TOKEN = "test_8fe51d2f048f114df2e7535f024"
api = Instamojo(api_key=API_KEY, auth_token=AUTH_TOKEN, endpoint='https://test.instamojo.com/api/1.1/')

# Create a new Payment Request
response = api.payment_request_create(
    amount='101',
    purpose='i am Testing',
    send_email=True,
    email="anandgohil89@gmail.com",
    redirect_url="http://127.0.0.1:8000/handle_redirect"
    )

print ("longurl: ",response['payment_request']['longurl'])