
# Solution for the internship task

Solution for the back-end (full-stack) task from https://github.com/joaquinfilipic-dynatrace/gdn-internship-2023 

# Components

- ### FlaskApi (folder with server)
    - NPBRequests.py - file with the flask server
    - test_NBPRequests.py - file with integration tests 
    - Dockerfile - docker file to build the container
    - requirements.txt - file with dependencies
- ### ReactFrontend (folder with front-end)
    - src - folder with source files
    - Dockerfile - docker file to build the container
    - requirements.txt - file with dependencies
    - package.json, package-lock.json - files with dependencies
    - index - entry html file for the app 
- ### docker-compose.yml (file to build and start both containers at once)

# How to run and use

- ## How to run (and use) only the server 

Provided you have python and dependencies installed, navigate to the FlaskApi folder and run
```
python -m NBPRequests.py 
```
or 
```
python3 -m NBPRequests.py 
```
Then, to access the first query you can navigate to your browser and enter a URL the format 
```
http://127.0.0.1:5000/average_exchange_rate?code=<code>&date=<date>
```
Like, for example: 
```
http://localhost:5000/average_exchange_rate?code=gbp&date=2023-04-21
```
Alternatively you can use:
```
curl http://localhost:5000/average_exchange_rate?code=gbp&date=2023-04-21
```
In your bash terminal
