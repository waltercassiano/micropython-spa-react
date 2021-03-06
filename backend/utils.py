import upip

def decode(stringBytes):
    try:
        return stringBytes.decode()
    except Exception:
        return stringBytes

def import_or_install(name_to_install=None, import_name=None):
    try:
        if not import_name:
            return __import__(name_to_install)

        return __import__(import_name)
    except ImportError:
        upip.install(name_to_install)
        if import_name:
            return __import__(import_name)