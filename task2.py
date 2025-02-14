def typeBasedTransformer(**kwargs):
  newkwargs={}
  for key, value in kwargs.items():
    if isinstance(value, bool):
      newkwargs[key]=not(value)
    elif isinstance(value, int) or isinstance(value, float):
      newkwargs[key]=value**2
    elif isinstance(value, str):
      newkwargs[key]=value[::-1]
    elif isinstance(value, list) or isinstance(value, tuple):
      newkwargs[key]=value[::-1]
    elif isinstance(value, dict):
      newkwargs[key]={val: new_key for new_key, val in value.items()}
  return newkwargs
