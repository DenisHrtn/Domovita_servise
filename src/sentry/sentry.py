import logging
import sentry_sdk
from sentry_sdk.integrations.logging import LoggingIntegration

# sentry integration
sentry_logging = LoggingIntegration(
    level=logging.INFO,
    event_level=logging.ERROR,

)

sentry_sdk.init(
    dsn="",
    traces_sample_rate=1.0,
    integrations=[
        sentry_logging
    ]
)

