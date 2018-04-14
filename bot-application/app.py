from flask import Flask
from flask import render_template,jsonify,request
import requests
from models import *
from response import *
import random

@app.route('/')
def hello_world():
    """
    Sample hello world
    """
    return render_template('home.html')

get_random_response = lambda intent:random.choice(response[intent])
isClosingCard = False;

def format_entities(entities):
    """
    formats entities to key value pairs
    """
    ## Should be formatted to handle multiple entity values
    e = {"day":None,"time":None,"place":None}
    for entity in entities:
        e[entity["entity"]] = entity["value"]
    return e

def get_event(day=None,time=None,place=None):
    """
    gets event date and time from user utterance
    and finds event within next half an hour of that range
    """
    if not day and not time:
        return get_random_response("events_link")
    date_time = get_date_time(day,time)
    print date_time
    events = Event.query.filter(Event.date_time>=date_time,
                                Event.date_time <= date_time + datetime.timedelta(minutes=30))
    events = events.all()
    if not events:
        return get_random_response("no_events")+ "<br/>" + get_random_response("events_link")
    event_description = "<br/>".join(event.event_description+" at "+event.place for event in events)
    return event_description

@app.route('/chat',methods=["POST"])
def chat():
    global isClosingCard
    """
    chat end point that performs NLU using rasa.ai
    and constructs response from response.py
    """
    try:
        response = requests.get("http://localhost:5000/parse",params={"q":request.form["text"]})
        #response = requests.get("http://localhost:5000/parse?q="+request.form["text"])
        response = response.json()
        intent = response["intent"]
        intent = intent["name"]
        entities = response["entities"]
        length = len(entities)
        if(length>0):
            entity = entities[0]["entity"]
            value = entities[0]["value"]  
        
        
        
        if intent == "event-request":
            response_text = get_event(entities["day"],entities["time"],entities["place"])
        elif isClosingCard == True:
           if response["text"] == "1234":
               response_text = "We are closing this card. Thanks for your patience."
               isClosingCard = False
            
           elif response["text"] == "ok":
               response_text = "How else I can help you? :)"
               isClosingCard = False
            
           else:
               response_text = "This card doesn't exist. Please check the number again. If you want to talk about anything else rather than this #then type ok"
        elif intent == "lost_card":
            response_text = "Please give us your credit card number"
            isClosingCard = True

        elif intent == "card_charge":
            if(length>0 and entity =="card_type"):
                if(value.lower() == "debit card"):
                    response_text = "For debit card first year is free and from second year onward we charge 300tk per year"
                elif(value.lower() =="credit card"):
                    response_text = "For credit cards we charge 500 taka per year"
                else:
                    response_text = "I am not sure about that, sorry!"
                
            else:
                response_text = "For credit cards we charge 500 tk per year. And for debit cards first year is free and from second year we charge 300tk per year"

        elif intent == "get_cheque_book":
            response_text = "We will send the new checkbook to your address."
        elif intent == "loan_car":
            response_text = "We provide car loan of minimum 5 lacs tk and maximum of 20 lacs tk"
        elif intent == "loan_home":
            response_text = "We provide home loan of minimum 20 lacs tk and maximum 1.2 crore tk"
        elif intent == "loan_max":
            if(length>0 and entity == "loan"):
                if (value.lower() =="medical" or value.lower() == "personal" or value.lower() == "marriage" or value.lower() == "traveling" or value.lower() == "education"):
                    response_text = "We provide personal loan of maximum 2 lacs tk"
                elif value.lower() == "car":
                    response_text = "We provide car loan of maximum of 20 lacs tk"
                elif value.lower() == "home":
                    response_text = "We provide home loan of maximum 1.2 crore tk"

        elif intent == "loan_min":
            if(length>0 and entity == "loan"):
                if (value.lower() =="medical" or value.lower() == "personal" or value.lower() == "marriage" or value.lower() == "traveling" or value.lower() == "education"):
                    response_text = "We provide minimum personal loan of 50,000 tk lacs tk"
                elif value.lower() == "car":
                    response_text = "We provide car loan of minimum of 5 lacs tk"
                elif value.lower() == "home":
                    response_text = "We provide home loan of minimum 20 lacs tk"
        elif intent == "loan_max_home":
             response_text = "We provide home loan of maximum 1.2 crore tk"

                        
        elif intent == "loan_details":
            response_text = "We provide 3 different kinds of loans currently.\n1.Personal loan(Marriage, traveling, education etc)\n2.Car loan\n3.Home loan"
        
        elif intent == "show_balance":
            response_text = "Your current account balance is 20,000 tk"

        elif intent == "summary":
            response_text = "Account type: Checking Account\nCurrent balance: 20,000 tk\nAvailable to withdraw: 19,500 tk"

        else:
            response_text = get_random_response(intent)
        return jsonify({"status":"success","response":response_text})
    except Exception as e:
        print e
        return jsonify({"status":"success","response":"Sorry I am not trained to do that yet..."})


app.config["DEBUG"] = True
if __name__ == "__main__":
    app.run(port=8000)
