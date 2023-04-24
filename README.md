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
    - package.json, package-lock.json - files with dependencies
    - index - entry html file for the app 
- ### docker-compose.yml (file to build and start both containers at once)

# How to run and use

 ## How to run (and use) only the server 

Provided you have python and dependencies installed, navigate to the FlaskApi folder and run
```
python -m NBPRequests.py 
```
or 
```
python3 -m NBPRequests.py 
```
Then, to access, for example, the first query you can navigate to your browser and enter a URL in the format (<ip:port> is the IP and port on which the server is listening. Usually on localhost:5000) :
```
http://<ip:port>/average_exchange_rate?code=<code>&date=<date>
```
Like, for example: 
```
http://localhost:5000/average_exchange_rate?code=gbp&date=2023-04-21
```
Alternatively in your bash terminal you can use:
```
curl 'http://<ip:port>/average_exchange_rate?code=gbp&date=2023-04-21'
```
Like, for example:
```
curl 'http://153.19.209.27:5000/average_exchange_rate?code=gbp&date=2023-04-21'
```
If it doesn't work double check on which IP the server is listening

 ## List of queries

- ### Query 1 is as mentioned before:
```
http://<ip:port>/average_exchange_rate?code=<code>&date=<date>
```
For example as:
```
http://localhost:5000/average_exchange_rate?code=gbp&date=2023-04-21
```

- ### Query 2 is:
```
http://<ip:port>/min_and_max_average_values?code=<code>&last_quotations_num=<last_quotations_num>
```
Like for example:
```
http://localhost:5000/min_and_max_average_values?code=GBP&last_quotations_num=3
```
- ### Query 3 is:
```
http://<ip:port>/major_difference?code=<code>&last_quotations_num=<last_quotations_num>
```
Like for example:
```
http://localhost:5000/major_difference?code=GBP&last_quotations_num=3
```

## Back-end container

Provided you have docker desktop installed and running you can run:
```
docker build -t backend .
```
From FlaskApi folder To create an image 
and 
```
docker run -p 5000:5000 backend
```
To run a container 

Then you can access the urls with ip's and docs provided in the log of flask server starting (Usually http://localhost:5000/) to run the queries 

Alternatively you can run 
```
docker pull romangellert/backend:latest
```
To pull an image from docker hub


## Front-end

Provided you have node.js and all dependencies installed you can navigate to ReactFrontend 
and run 
```
npm run dev
```
And go to http://localhost:5173/ or another port vite is running on to access the development server 

Make sure server is running for app to display data correctly 

## Front-end container 

Following the same logic as with back-end container you can run 
```
docker build -t frontend .
```
From ReactFrontend folder To create an image 
and 
```
docker run -p 5173:5173 frontend
```
To run a container 

Alternatively you can run 
```
docker pull romangellert/frontend
```
To pull the container from docker hub 

## Running both containers using docker compose

You can also navigate to the root folder (where docker-compose.yml file is situated) and run 
```
docker compose up
```
To build and run both containers simultaneously

## Accessing integration tests

In test_NBPRequests.py there are 3 classes for each query with integration tests 
Make sure pytest package is installed

You can run tests using 
```
python3 -m pytest -k test_NBPRequests -q
```
or
```
pytest -k test_NBPRequests -q
```
In vscode cmd terminal


