def decode(stringBytes):
  try:
    return stringBytes.decode()
  except Exception:
    return stringBytes

