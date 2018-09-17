# Banking Chat Bot
Currently the world is moving towards automation. Chatbots are really useful interms of customer services. Even if the chatbot can help you by solving 60-70% problems, it would still be very efficient in terms of money and time. So, our vision was to make a chatbot that can help you with the bank related questions. We made a smart bot which can understand the context by analyzing the texts using NLP techniques.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

You need to have python and flask installed on your system to run it.

### Installing

Follow the link to get the step by step guide to install the the Rasa Nlu and how to run a the server. 
Also select the training data from  "bankingchatbotabc/AI-engine/data/" directory. "testData(2).json" is the most updated dataset.

https://rasa.com/docs/nlu/installation/

## Deployment

To train the model with dataset

```
python -m rasa_nlu.train -c config_spacy.json
```
To run the server

```
python -m rasa_nlu.server -c config_spacy.json
```

Then run the App.py to deploy the chatbot

## Demo

[![Alt text](https://img.youtube.com/vi/QRa4cQv-xoQ/0.jpg)](https://www.youtube.com/watch?v=QRa4cQv-xoQ)

## Built With

* [Python](https://www.python.org/) - The HTTP API was built in python
* [RASA NLU](https://rasa.com/docs/nlu/) - The Natural Language processing was done with it
* [Flask](http://flask.pocoo.org/) - The web framework was used for the chatbot application


## Authors

* **A. K. M. Saiful Islam** - *Initial work* - [adar2378](https://github.com/adar2378)


## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Rasa NLU, the framework helped us a lot.
* I followed their path to build it https://github.com/bhavaniravi/rasa-site-bot
