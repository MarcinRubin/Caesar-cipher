import sentry_sdk

from src.user_interface import UserInterface

sentry_sdk.init(
    dsn="https://f23ca7da397e443d86a9c89734a36875@o4505478848184320.ingest.sentry.io/4505478855720960",
    # Set traces_sample_rate to 1.0 to capture 100%
    # of transactions for performance monitoring.
    # We recommend adjusting this value in production.
    traces_sample_rate=1.0,
)


def main():
    """
    Main function of the program,
    used mainly to start the user interface module
    """
    UserInterface()


if __name__ == "__main__":
    main()
