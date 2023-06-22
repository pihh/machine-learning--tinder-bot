from dotenv import dotenv_values

ENVIRONMENT = dotenv_values('.env')
ENVIRONMENT['FACEBOOK_ID'] = int(ENVIRONMENT['FACEBOOK_ID'])