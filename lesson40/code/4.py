def get_secret(setting):
    """Get the secret variable or return explicit exception."""
    try:
        return os.environ[setting]
    except KeyError:
        error_msg = f"Set the {setting} environment variable"
        raise ImproperlyConfigured(error_msg)