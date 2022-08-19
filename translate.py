def translate_text(target, text):
    """
    Takes a ISO 639-1 language code and some
    target text, leverages Google Translate API
    enpoint to perform conversion to target language

    Source text language is processed by Google API and
    auto detected
    """

    # Six provides smoother intercompatibilty between Python versions
    import six

    # Import API from Google
    from google.cloud import translate_v2 as translate

    # translate client provides methods for handling data returnd from Google
    translate_client = translate.Client()

    if isinstance(text, six.binary_type):
        text = text.decode("utf-8")

    # take our target ISO 639-1 as well as our text, perform translation
    # result is returned to the caller as a dict
    result = translate_client.translate(text, target_language=target)

    return result
