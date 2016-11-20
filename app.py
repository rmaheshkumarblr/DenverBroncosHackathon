from flask import Flask, request
import RPi.GPIO as GPIO
from kulka import Kulka
from selenium import webdriver  
from selenium.common.exceptions import NoSuchElementException  
from selenium.webdriver.common.keys import Keys  
import time
import requests
import json
import sendgrid
import os
from sendgrid.helpers.mail import *

sg = sendgrid.SendGridAPIClient(apikey='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')
from_email = Email("rmaheshkumarblr@gmail.com")
to_email = Email("mara0940@colorado.edu")
subject = "Twenty Questions"
url = "http://www.mapquestapi.com/directions/v2/optimizedroute"

ADDR = '00:06:66:4F:74:90'

app = Flask(__name__)

GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)

def do_a_square(kulka):
	print "Inside Square"
	speed = 0x88
	sleep_time = 5

	for angle in [1, 90, 180, 270]:
        	kulka.roll(speed, angle)
        	time.sleep(sleep_time)
    
	kulka.roll(0, 0)

@app.route("/on")
def on():
    GPIO.output(17, 1)
    return "The Light is now On!"

@app.route("/off")
def off():
    GPIO.output(17, 0)
    #return "The Light is now Off!"
    with Kulka(ADDR) as kulka:
	print "Inside With"
    	do_a_square(kulka)
    return "The Light is now Off!"

browser = webdriver.PhantomJS()
questions = []
answers = []
solution = ""

@app.route("/setUpAkinator")
def set_up():
   #browser = webdriver.PhantomJS()
   questions = []
   answers = []
   solution = ""
   browser.set_window_size(1124, 850)
   browser.get('http://en.akinator.com/')  
   browser.find_element_by_link_text('Play').click()
   time.sleep(1)
   ele =browser.find_element_by_id('elokence_sitebundle_identification_age')
   time.sleep(1)
   ele.send_keys("21")
   time.sleep(1)
   browser.find_element_by_tag_name("form").submit()
   time.sleep(1)
   return "Success"


@app.route("/getFirstQuestion")
def first_question():
   question = browser.find_element_by_id('bulle-inner').text
   questions.append(question)
   time.sleep(1)
   return question


@app.route("/getOtherQuestion")
def next_question():
 print "Answer: " + request.args['answer']
 providedAnswer = request.args['answer']
 if providedAnswer != 'dn' and providedAnswer != "yes" and providedAnswer != "no":
       providedAnswer = "Don't know"
 if providedAnswer == 'dn':
       providedAnswer = "Don't know"
 answers.append(providedAnswer) 
 providedAnswer = providedAnswer[0].upper() + providedAnswer[1:]
 browser.find_element_by_link_text(providedAnswer).click()
 time.sleep(2)
 if 'I think of' in browser.page_source:
       question = "I got it. It's" + browser.find_element_by_id('perso').text
       solution = browser.find_element_by_id('perso').text
       #content = Content("",<table><thead><tr>Question</tr><tr>Answer</tr></thead></table> "Questions: " + ' '.join(questions) + " Answers: "  + ' '.join(answers) + ' Solution: ' + solution )
       tableFormation = "<table><thead><td>Question</td><td>Answer</td></thead><tbody>"
       for q, a in zip(questions, answers):
       	tableFormation += "<tr><td>" + q + "</td><td>" + a + "</td></tr>"
       tableFormation += "</tbody></table>"
       tableFormation += "<br> <h4> The imagined person was: " + solution + "</h4>"
       print tableFormation
       content = Content("text/HTML",tableFormation)
       mail = Mail(from_email, subject, to_email, content)
       response = sg.client.mail.send.post(request_body=mail.get())
#print(response.status_code)
#print(response.body)
#print(response.headers)
 else:
     question = browser.find_element_by_id('bulle-inner').text
     questions.append(question)
 time.sleep(1)
 return question
 #return browser


@app.route("/getLocationInformation")
def get_location():
 source = request.args['source']
 destination = request.args['destination']
 locations = {}
 location = []
 location.append(source)
 location.append(destination)
 locations['locations'] = location
 querystring = {"key":"UShjaMayAC4UkuBJ5nu5rqFuraxzEOQU", "json": json.dumps(locations) }
 headers = { 'cache-control': "no-cache" }
 response = requests.request("GET", url, headers=headers, params=querystring)
 print response
 output_of_request = json.loads(response.text)['route']['distance']
 print output_of_request
 return str(output_of_request)
 #return "From Flask, the source is " + source + " and " + " destination is " + destination


	
if __name__ == "__main__":
    app.run()
