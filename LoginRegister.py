personalData = {"moon":"1234","jung":"5678"}

class Register:
  def __init__(self, id, password):
    self.id = id
    self.password = password

if __name__ == '__main__':
  success = True
  
  while (success):
    type = input("Type 1 for Register or 2 for Login : ")

    if (type == "1"):
      niceInput = True

      while (niceInput):
        id = input("Type your new ID : ")

        if id in personalData: 
          niceInput = False
        else:
          id = input("Someone is using same ID. Please type another ID : ")      
      
      password = input("Type your new PASSWORD : ")
      personalData[id] = password
      print("REGISTER SUCCESS !")
      success = False
    
    elif (type == "2"):
      isNotExist = True
      wrongPW = True

      while (isNotExist):
        id = input("Type your ID : ")

        if id in personalData: 
          isNotExist = False
        else:
          id = input("ID doesn't exist. Type again : ")      
      
      password = input("Type your PASSWORD : ")
      
      while (wrongPW):
        if (personalData[id] == password):
          print("LOGIN SUCCESS !")
          wrongPW = False
        else:
          password = input("Wrong ! Type your PASSWORD : ")
      
      success = False
    
    else:
      type = input("Type 1 for Register or 2 for Login : ")