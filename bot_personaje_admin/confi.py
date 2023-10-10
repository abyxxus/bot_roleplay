import pymongo

try:
  client = pymongo.MongoClient("mongodb+srv://arlex:cijmnXWKMJKwkYke@cluster0.xjmjtrz.mongodb.net/")
except pymongo.errors.ConfigurationError:
  print("An Invalid URI host error was received. Is your Atlas host name correct in your connection string?")
  
# creacion de la raza y de sus datos basicos en None
def raza_name (name):
  db = client.raza_db
    
  razadb = db["raza"]
  try :
    result = razadb.find_one({"name":name})
    print(result)
    if result != None:
      print("alredy exist!")
      return(result)
    else:
      new_raza = [{"name":name,
                  "history":None,
                  "stats":{"vida":0,
                            "fuerza":0,
                            "agilidad":0,
                            "inteligencia":0,
                            "fe":0,
                            "persepcion":0,
                            "precision":0},
                  "pais":None}]
      
      try:
        result = razadb.insert_many(new_raza)
        print(result)
        return(None)
      except pymongo.errors.OperationFailure:
        print("An authentication error was received. Are you sure your database user is authorized to perform write operations?")
      
  except pymongo.errors.OperationFailure:
    print("An authentication error was received. Are you sure your database user is authorized to perform write operations?")

#actualiza la historia de la raza
def raza_history(name,history):
  db = client.raza_db
    
  razadb = db["raza"]
  
  result = razadb.find_one({"name":name})
  print(result)
  if result != None:
    try:
      razadb.find_one_and_update({"name":name},{"$set":{"history":history}})
      return(True)
    except Exception:
      print("no se pudo actualizar")
      return(False)
  else:
    return(False)

#actualiza la estadisticas de la raza 
def raza_stats(name, data):
  db = client.raza_db
    
  razadb = db["raza"]
  
  try:
    result = razadb.find_one({"name":name})
  except pymongo.errors.ConfigurationError:
    return(False)
  
  if result != None:
    try:
      razadb.find_one_and_update({"name":name},{"$set":{"stats":{"vida":int(data[0]),
                                                                 "fuerza":int(data[1]),
                                                                 "agilidad":int(data[2]),
                                                                 "inteligencia":int(data[3]),
                                                                 "fe":int(data[4]),
                                                                 "persepcion":int(data[5]),
                                                                 "precision":int(data[6])}}})
      return(True)
    except Exception:
      print("no se pudo actualizar")
      return(False)
  
def class_name(name):
  db = client.clas_db
  classdb = db["clase"]
  
  try:
    rt = classdb.find_one({"name":name})
    print(rt)
    if rt != None:
      return(rt)
    else:
      new_class = [{"name":name,
                   "armor_u":None,
                   "weapon_u":None,
                   "level_up":None,
                   "place":None,
                   "abilitis":None}]
      
      rt = classdb.insert_many(new_class)
      
      print(rt)
      return(None)
  except Exception:
    print("An authentication error was received. Are you sure your database user is authorized to perform write operations?")
  
  