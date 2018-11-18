##dict of response for each type of basic intent
response = {
    "greet":["hey","hello","hi"],
    "goodbye":["bye","It was nice talking to you","see you","ttyl"],
    "affirm":["cool","I know you would like it"],
    "intro":["I am a chat-bot for abc bank, I can help you with your bank related queries","I'm a chat-bot traied to help people with their queries related to bank"],
    "atm_video":["Sorry, I can not help you with this directly, it will be better if you go and talk to the nearest branch of our bank and talk to the manager personally, thanks"],
    "card_limit":["By using your card you can withdraw maximum 50,000 tk and minimum 500tk in one day with maximum 5 transactions"],
    "credit_card_limit":["You can spend total 70,000tk with your credit card"],
    "new_card":["To get a new credit/debit card go to the nearest bank with your 2 passport sized photo and photocopy of one of the following documents: 1.NID\n2.Driving license\n3. Passport "]
}
import datetime
mapping = {
    "now":datetime.datetime.now(),
    "tomorrow": datetime.date.today() + datetime.timedelta(days=1),
    "today":datetime.date.today(),
    "same time":datetime.datetime.now(),
    "second day":datetime.datetime.now()
}

def try_parsing_date(text):
    """
    Parses time of string format to a time object
    """
    for fmt in ('%I %p', '%I %M %p', '%I:%M %p'):
        try:
            return datetime.datetime.strptime(text, fmt)
        except ValueError:pass
    if ":" in text:
        return datetime.datetime.strptime(text+" "+
                ("AM" if int(text.split(":")[0])>=8 else "PM"), '%I:%M %p')
    return datetime.datetime.strptime(text+" "+
            ("AM" if int(text)>=8 else "PM"), '%I %p')

def get_date_time(day,time):
    """
    Maps words like now today tom etc., to corresponding datetime objects
    """
    try:time = mapping[time]
    except KeyError:
        if not time:
            time = datetime.datetime.now()
        else:
            time = try_parsing_date(time)
    try:date = mapping[day]
    except KeyError:date = datetime.date.today()

    return datetime.datetime.combine(date, time.time())
