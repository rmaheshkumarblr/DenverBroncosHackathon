# DenverBroncosHackathon
# EchoMania

## Inspiration

We wanted to build a product that is useful and productive. A product that has multiple functionality and can help a person in his day to day activity. 

## What it does

* We as students tend to play a lot and [Akinator](http://en.akinator.com/) was one of them. It has no API but it is a very interesting game which asks questions to figure out the person whom you were thinking about. Generally, if the person is famous and questions are asked appropriately, it can figure out the person in 20 questions, hence we decided to name the Alexa Skillset as Twenty Questions. We use SendGrid API to send  the set of Questions, Answers and person Imagined over mail.
* We wanted to use Hardware since we have generally not used them before. We wanted to do something with Sphero and RaspberryPi. Our complete setup including the server is based on RaspberryPi. We are able to control Sphero to some extent and a LED from Alexa (IOT).
* We build an Alexa Skillset to get Optimized Route Information from MapQuest API. You can get information such as Fuel Consumptions, Toll Information, Distance and the Narrative Instructions through Alexa

## How we built it

**Twenty Questions**
* We used Amazon Alexa Skill Set and Amazon Lambdas to help us use Amazon Echo
* We built a Flask server on the RaspberryPi which provides the Backend Support to Alexa by getting information from Akinator
* Since the Flask Server runs locally on the RaspberryPI, we used Ngrok to Tunnel it and provide a Public Web URL that everyone can access.
* Akinator is the backend to our product. They don't provide an API to communicate with their database and hence we use Selenium Webdriver (Hacky!)  to use their services

**IOT**
* We used Amazon Alexa Skill Set and Amazon Lambdas to help us use Amazon Echo
* We power the LED through Raspberry Pi and control the GPIO pin from Amazon Echo
* We use the Bluetooth of RaspberryPi to control Sphero

**MapQuest**
* We used Amazon Alexa Skill Set and Amazon Lambdas to help us use Amazon Echo
* We use the MapQuest API to get the optimized route and feed it to the Amazon Lambda where the states are stored for further queries

## Challenges we ran into

* It was not straight forward to get the information our of Akinator. We started with beautifulsoup to get the information extracted from the website but then it was less of HTML and more of Javascript and hence decided to use Selenium Webdriver to extract the Information.
* Since we were using our own Flask Server having the option of repeat on Amazon Lambda was a bit complicated since the session information is maintained on the server.
* The pages don't load at the same rate in Akinator and hence we had to choose a optimum sleep/delay time to provide good response times as well as to avoid unexpected exception scenario.
* We tried using multi-processing in Python to control the Sphero and have the Twenty Questions application working at the same time but it did put huge load on the RaspberryPi and lead it to hung state.
* Since each RaspberryPI has just one Bluetooth, we were not able to control multiple Spheros at the same time and hence we could not do Swarm Robotics.

## Accomplishments that we're proud of

We are extremely happy to have our Twenty Questions working very well. We probably have played the game over 50 times to make sure we don't hit any unexpected bug. We had multiple people in random play the game to get user feedback based on which we improved the application overtime.

## What we learned

* We learnt how to debug Alexa and Echo better. 
* We learnt how to use Selenium Webdriver (We have never used before)
* We learnt to use Hardware (RaspberryPi and Sphero) along with Software
* We also experimented and used SendGrid Mail APIv3 and MapQuest API
* Using a single programming language for all the functionalities simplifies the integration

## What's next for EchoMania

* We plan to release Twenty Questions as a Alexa Skill Set
* We would try to avoid our own server and integrate it completely within the Amazon Lambda
* We plan to make patterns using multiple Spheros in future
* We plan to improve and provide all the features available with MapQuest API from Alexa
