# digital-traces
Small python app with flask, using google analytics and deployed with deta

## Requirements
pip install -r requirements.txt

## Deploy
You can deploy the micro using the following deta commands
first install deta using 
iwr https://get.deta.dev/cli.ps1 -useb | iex
login with 
deta login
deta new --python first_micro
deta new --project <your-project> 
finally you can deploy the changes using 
deta deploy

## URL 
The app is accessible with the following URL
https://9iri6z.deta.dev

## Routes
The app has several pages
  - The home page says hello world and count the visitors
  - /logger shows some logs to the front end
  - /cookie shows the cookies from the get request to the google URL
  - /cookiewithga shows the cookies from the request to my google analytics URL
