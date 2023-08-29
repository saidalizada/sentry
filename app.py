from flask import Flask
import sentry_sdk
from sentry_sdk.integrations.flask import FlaskIntegration
import os
from dotenv import load_dotenv
load_dotenv()  # take environment variables from .env.

app = Flask(__name__)

sentry_sdk.init(
    dsn=os.getenv('DSN'),
    integrations=[
        FlaskIntegration(),
    ],

    # Set traces_sample_rate to 1.0 to capture 100%
    # of transactions for performance monitoring.
    # We recommend adjusting this value in production.
    traces_sample_rate=1.0
)


@app.route('/')
def name_index():
    try:
        result = test
    except Exception as e:
        sentry_sdk.capture_exception(e)
        return "Exception captured by Sentry."