from flask import Flask, render_template, request
from apiclient.discovery import build
from oauth2client.service_account import ServiceAccountCredentials

app = Flask(__name__)

@app.route('/', methods=["GET"])

def hello_world():
 prefix_google = """
 <!-- Google tag (gtag.js) -->
<script async
src="https://www.googletagmanager.com/gtag/js?id=G-R012264CT4"></script>
<script>
 window.dataLayer = window.dataLayer || [];
 function gtag(){dataLayer.push(arguments);}
 gtag('js', new Date());
 gtag('config', ' G-R012264CT4');
</script>
 """
 return prefix_google + "Hello World"



@app.route('/logger',methods=["GET"])
def logger_page():
    #log in the front-end and textbox
    logs = """
    <script>
    console.log('This message is a log on the front end');
    </script>
    
    <script>
    alert('Text box message');
    </script>
    """
    #log in the back-end
    print('This message is a log on the back-end')
    return logs + "Here is the logger page"


@app.route('/cookie', methods=["GET","POST"])
def mycookies():
    req = request.get("https://www.google.com/")
    return req.cookies.get_dict() 

@app.route('/cookiewithga', methods=["GET","POST"])
def mycookieganalytics():
    req = request.get("https://analytics.google.com/analytics/web/#/p344990265/reports/intelligenthome")
    return req.text
