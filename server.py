from boltiot import Bolt, Sms #Import Sms and Bolt class  from boltiot library 

import bolt, json, time # accesing the json and time function 

 Maxlimit= 10 # the distance between device and garbage in dustbin in cm
  

mybolt = Bolt(bolt.API, bolt.ID) #Create object to fetch data 

sms = Sms(bolt.SID, bolt.AUTH, bolt.TO, bolt.FROM) #Create object to send SMS 

response = mybolt.serialRead('13')# we are now receiving the data read at the 13th pin of arduino board 

print(response) 

  

while True: 

    response = mybolt.serialRead('13')  #Fetching the value from Arduino 13th pin 

    data = json.loads(response)#storing the value received to the bolt from arduino 

    glevel = data['value'].rstrip()#storing the integer part  

    print("Garbage level is", glevel) 

     

     if (int(glevel) <= Maxlimit or int(glevel)==357): 

         response = sms.send_sms('Hello  I am full,please clean me out') #sending the sms to your mobile number 

    time.sleep(2.5)#time between two consecutive readings in seconds 
