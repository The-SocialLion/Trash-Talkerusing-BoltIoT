# Trash-Talkerusing-BoltIoT
This system monitors the garbage level and sends an sms to the user when value crosses threshold value.

## Story
# INTRODUCTION
Hello guys, my name is Vishal Balaji Sivaraman.I am currently pursuing my Bachler’s of engineering at Rajalakshmi engineering college. I am in the department of ECE, I am currently pursuing my second year in this course so anyways back to the topic, I choose the topic trash talker a.k.a(garbage monitoring system)

The reason I choose this topic is given in the next section

# Problem:
Today as we know population is flourishing in our country like ever before so more and more apartment complexes and houses are constructed every day, so due to this the rate of waste generated is significantly high and due to this the bins get full at a faster rate and hence after a point the bins start to overflow, although the corporation people are trying their level best to send garbage trucks to every single area to empty the bins but after an hour or so the bins get full again also sometimes these garbage trucks go the areas where the bins are hardly even full rather than assigning these trucks to the right places where they need to be.so instead of exploiting manpower, fuel, etc we can let technology to do its work with the new garbage monitoring system Garbage monitoring system

# Introduction to the project:

This system which I designed is a simple solution to the above problem.It basically monitors the amount of garbage in the bin and once if the bin is full it sends a message to the head of the corporation mobile number stating “i am full, so please clean me out” and then he /she could send the truck to clean the waste out

Components required are:
Bolt wifi module:
Bolt wifi module:
BOLT is an internet of things platform Hardware + Software that enables user to build IOT products and projects. Using BOLT, users can control and monitor devices from any part of the world.

BOLT functionalities

> Station mode in which it can connect to WiFi networks.

> Station mode in which it can connect to WiFi networks.
>When not connected to any WiFi network it hosts its own WiFi hotspot to which users can connect.

>When not connected to any WiFi network it hosts its own WiFi hotspot to which users can connect.
>Commands an AT mega to do all GPIO and UART based tasks

>Commands an AT mega to do all GPIO and UART based tasks
>Runs at a frequency of 80Mhz

>Runs at a frequency of 80Mhz
Arduino (UNO)board :
Arduino (UNO)board :
Arduino is an open-source platform used for building electronics projects. Arduino consists of both a physical programmable circuit board (often referred to as a micro controller) and a piece of software, or IDE (Integrated Development Environment) that runs on your computer, used to write and upload computer code to the physical board.

HCSR04 SENSOR:
HCSR04 SENSOR:
The HC-SR04 Ultrasonic (US) sensor is a 4 pin module, whose pin names are Vcc, Trigger, Echo and Ground respectively. This sensor is a very popular sensor used in many applications where measuring distance or sensing objects are required. The module has two eyes like projects in the front which forms the Ultrasonic transmitter and Receiver. The sensor works with the simple high school formula that.

Distance = Speed × Time

Jumper wires:
Jumper wires:
A jumper wire (also known as jumper) is an electrical wire, or group of them in a cable, with a connector or pin at each or some times without them tinned, which is normally used to interconnect the components of a bread board or the other prototype or test circuit, internally or with other prototype or test circuit, internally or with other equipment or components, without soldering.

Individual jump wires are fitted by inserting their “end connectors”into the slots provided in a breadboard, the header connector of a circuit board or a piece of test equipment.

jumper wires (male and female pins)

# SOFTWARE NEEDED ARE:

1. BOLT IOT BOLT CLOUD
2. ARDUINO IDE
3. TWILLIO
4. VM-WARE

Steps to register in these above mentioned applications are mentioned below
BOLT IOT BLOT CLOUD
As per the mentioned above setup we can get thecloud accessed.
ARDUINO IDE
ARDUINO IDE
The Arduino Integrateddevelopment environment (IDE) is a cross-platform application (for Windows, mac OS, Linux)that is written in the programming language Java. It is used to write and upload programs to Arduino board. It is a open source software so either visit the Arduino home page and download the software in your system else you can use the link below to guide you in setting up Arduino IDE in your system

https://www.youtube.com/watch?v=TbHsOgtCMDc

TWILLIO ACCOUNT
TWILLIO ACCOUNT
Step 1 : Login in the twillio account as above

Step 2 : Next you need to verify our phone number.

Step 3 : Next we will create the product as shown in the figure.

Step 4: then we select the programmable sms andphone number options due to we need to get sms so we use that.

Step 5: Next we click continue.

Step 6 : enter your project name and then continue.

Step 7 : you can skip this step

Step 8 : enter the project info

Step 9 : According to the step we need to select that.

Step 10 : you can the get started

Step 11 : next you need to generate the new phone number according to the option

Step 12 : Next we get the new phone number and you can now access the account.

VM-WARE:(virtual private server)

Minimum Specifications

For installing a virtual machine on your Desktop/Laptop, it should meet the minimum specifications mentioned below,

OS - Windows 7 or Windows 10
CPU - Dual Core 2Ghz
RAM - 4GB
HDD - Should have at least 10GB free space
High-Speed Internet Access
Brief Overview
The installation steps are mentioned in brief as below,

Download VmWare.
Install VmWare.
Download Ubuntu Server image.
Install Ubuntu Server image on VmWare.
Do note that the setup requires high-speed internet access and will download approximately 1.2GB of data.

The links to the softwares is given below:

VMWare Download link - https://my.vmware.com/web/vmware/free#desktop_end_user_computing/vmware_workstation_player/12_0

Ubuntu Server ISO link - http://releases.ubuntu.com/16.04/ubuntu-16.04.6-server-i386.iso

# Hardware setup:

Ultrasonic to arduino connections
Vcc -> 5V#SUPPLY VOLTAGE TO SENSOR
Trig -> 12
Echo -> 13
GND -> GND
Arduino to bolt wifi modiule connections
Rx -> TX#RX->RECIEVER, TX->TRANSMITTER
Tx -> RX
GND -> GND
VIN->5V #SUPPLY VOLTAGE TO BOLT
NOTE:
guys do power your arduino using usb cable to see the different set of values sensed by serial monitor and then u can compare them with your output obtained by running the server code

After completing the above connections just power on your arduinoby connecting the arduino to your laptop/pc via usb cable and then u will see all the light glowing like this In the below picture

Unfortunately I didn’t have arduino uno at that time hence I used arduino mega 2560 but don’t worry the connections and the coding is the same

# Serial monitor:
There is a magnifying glass on the top right corner of your laptop /pc screen click that so you can see the list of values (distances)measured by sensor

The below screenshot is the serial monitor
NOTE:

We read 13th pin rather than the 12th pin cause if we read 12th pin we get a set of present values sensed by sensor but are not compatible with int()base with 10 but if we use 13th pin we get only one value at a time.But u guys will be wondering wont there be any delay between the reading of sensor and the reading received at the bolt.actually this delay does exist so I also found the solution to it by increasing time between two consecutive readings sensed by sensor and lowered the time.sleep() of bolt. After this I noticed a drastic change between the delay it was minimized to a large extent. One more thing when any object is bought too close to the sensor it displays an error value of 357 and hence we do consider it here also if u change the ports of the sensor in your code please do change the port in the command response = mybolt.serialRead('13') , else it will read the voltage at the unused port and that value is transmitted to the bolt rather than the distance sensed by sensor
