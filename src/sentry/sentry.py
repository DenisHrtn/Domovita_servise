import logging
import sentry_sdk
from sentry_sdk.integrations.logging import LoggingIntegration

# sentry integration
sentry_logging = LoggingIntegration(
    level=logging.INFO,
    event_level=logging.INFO
)

sentry_sdk.init(
    dsn="https://5eb563c6b12e4ff2821ab1a536ebe2c0@o4504871217987584.ingest.sentry.io/4504871233323008",
    traces_sample_rate=1.0,
    integrations=[
        sentry_logging
    ]
)

