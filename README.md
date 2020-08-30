# Welcome to Intelligent Product Master - IPM! 

## About the project

> **Jarvis (software robot assistant) for corporations**

**Description:** ***Background:*** Today organizations have multiple tools and systems to help assist them in their day to day software development activities. There is need of a system which can connect to applications, mine & analyze data and provide results to stakeholders whenever they need it. Problem Statement: For example, questions to
assist development activities could be: What is the status of the release of Project X that was due this Friday? Why was Feature Y not fulfilled in the last release for Project X? How many test cases failed in the last release of Project X? Send me an email with the last release notes for Project X How to install Project X? How was Feature Z implemented? (Note: the robot would need to connect to all the applications, and dig out all the relevant information (description of features and linked commits / comments /guides) related the Feature Z Help me solve the class not found exception against “ClassName” (Note: this would mean running a query on stack overflow) Create an AI/ML based application to be hosted within a corporate/organization intranet with complete access to corporate/organization resources of JIRA, Confluence, Bitbucket and Stack Overflow. The primary responsibility of this software robot (Intelligent Product Master - IPM) is to learn-mine-analyze-serve information about a product to optimize development and support processes in a product team. IPM’s input interfaces would be a mic and email to receive input from users. IPM’s output interfaces would be speaker and email to revert to users. Following are the two main use cases (but not limited to) 1. Anyone can ask/look up for any information to IPM. It responds with accurate answer by voice-to-text-conversion/email. Mining existing data (could use APIs of the information hosting applications). Co-relating multiple information, analyzes and respond text-to-voice/email. 2. Take the Speaker in a meeting (example: scrum ceremonies/meetings). It records the meeting MOM in detail in its own data-reservoir (database). The scrum master can also instruct IPM to do multiple activity during the meeting. Say: Create a jira task, pull out the last updated jira task. Send me the last email from XYZ to me etc. To implement this, you can use a computer/speak/mail server and client, Voice-text-voice converter, text to jira / confluence / bitbucket / Stack Overflow APIs, AI to Analyze data to get accurate information, ML to learn when taken in a meeting. The key challenges in the problem would be to architect an information store that is optimally designed to answer queries, and accurately answer questions posed to it. For voice to text, and text to voice, you may use standard (free) libraries/services available in the market.


## Installation
### Steps are-
#### 1- Clone the repository
#### 2- Create a new virtual environment
#### 3- Now install the requirements.txt file
#### 4- Now run the server as python manage.py runserver
