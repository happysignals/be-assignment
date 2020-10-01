# Assigment

Welcome to your first day at HappySignals, your first task is to get up and running. Please fork and clone this repository to your local machine.

`(1)` You're going to need a Python 3.7 or later environment to get productive, start by installing Python into a virtual environment and the requirements listed in `requirements.txt`.

You are going to be working with our brand new survey machine, unfortunately our designer had a day off for some well deserved rest so the UI is a bit bare to say the least. Start the application and familiarise yourself with the application and admin interface.

You can answer the example survey by visiting http://127.0.0.1:8000/form in the default configuration.

`(2) in form/forms.py` We're almost ready to launch the application but during testing we noticed that some people managed to submit scores outside the NPS range (0-10) and it throws off the calculations. Please add validation to the form that verifies that only valid NPS scores are accepted and render an error message in the form should that not be the case.

`(3) in form/forms.py` Additionally we found out that people sometimes use colorful language to express their feelings in the free comment field. The PR department would like to ensure the following expressions are not possible "I went bananas", "he was a complete pear", or "the machine was a lemon" by banning mentioning of the following fruit, "banana", "pear", and "lemon".

The initial reaction from the customers to the application has been great, despite the UX, but the customer needs to know what to do to improve their scores. To fix this another backend developer added factors which the user can choose between to help explain what influenced their score. Unfortunately just as he was about to add code to save the factors he got distracted setting up a service mesh on Kubernetes on his Raspberry PI cluster and has not been heard from since.

`(4) in forms/views.py` Ensure that the factors chosen by the user is persisted with the response. The form contains the slug(s) of the factors in the "factors" field.

The factors help the customer improve their scores immensely but there are lingering doubts by the users whether
their responses are actually stored as they entered them. They need to be able to confirm for themselves that their response was received in the right manner.

`(5) in forms/views.py and forms/templates/thank_you.html` Update the thank you page to show the comment, and the factors chosen after the user submitted their response.

`(6)` Everyone is happy, sales are booming, large corporations want to improve their services too and have shown interest. Security is a major concern for them though, and they have asked us to go through a penetration test and security review. Is there anything in the application that we need to fix before that?

