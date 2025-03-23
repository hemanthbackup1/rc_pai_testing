import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    """Configuration settings for the application."""
    # Astra DB credentials
    #ASTRA_DB_SECURE_BUNDLE_PATH = 'C:\\Users\\meeth\\OneDrive\\Documents\\rc_pai_batch\\mar 20\\secure-connect-rc-pai-test.zip'
    ASTRA_DB_SECURE_BUNDLE_PATH = '/app/secret_bundle/secure-connect-rc-pai-test.zip'
    ASTRA_DB_CLIENT_SECRET = "O8uglTzSG91,i-W52jMco+IpZWJTvzAyM1StnrgrtQwJdnCB-ein,GUZj_+yyHcYGqxNsr7OsM+iIdXrZRnDiU--f1ZPyYTm.FA+Dcwwa9vZtpsjuhG5ri6ok-CbTEWM"
    ASTRA_DB_CLIENT_ID = "uBNatRssAyFjivuYlOnHRmEH"
    ASTRA_DB_KEYSPACE='card_statement'
    ASTRA_DB_TABLE='fixed_statement_202406'
    # Google Cloud credentials

