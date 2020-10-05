# We read 13th pin rather than the 12th pin cause if we read 12th pin we get a set of present values sensed by sensor but are not compatable with int()base with 10 but if we use 13th pin we get only one value at a time .But u guys will be wondering wont there be any delay between the reading of sensor and the reading received at the bolt.actually this delay does exist so I also found the solution to it by increasing time between two consecutive readings sensed by sensor and lowered the time.sleep() of bolt. After this I noticed a drastic change between the delay it was minimised to a large extent . One more thing when any object is bought too close to the sensor it displays an error value of 357 and hence we do consider it here also if u change the ports of the sensor in your code please do change the port in the command response = mybolt.serialRead('13') ,else it will read the voltage at the unused port and that value is transmitted to the bolt rather than the distance sensed by sensor

from boltiot import Bolt, Sms #Import Sms and Bolt class  from boltiot library 

import bolt, json, time # accesing the json and time function 

 Maxlimit= 10 # the distance between device and garbage in dustbin in cm
  

mybolt = Bolt(bolt.API, bolt.ID) #Create object to fetch data 

sms = Sms(bolt.SID, bolt.AUTH, bolt.TO, bolt.FROM) #Create object to send SMS 

response = mybolt.serialRead('13')# we are now receiving the data read at the 13th pin of arduino board 

print(response) 

  



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
