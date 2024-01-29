from fastapi import FastAPI,Form, Request
from fastapi.staticfiles import StaticFiles
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import random
from pydantic import BaseModel
from fastapi import Form, Depends
from fastapi.responses import JSONResponse
import secrets


class OtpRequest(BaseModel):
    email: str
    


# http://127.0.0.1:8000/docs.
uri = "mongodb+srv://harveal:harveal2024@cluster0.25sb0oo.mongodb.net/?retryWrites=true&w=majority"

client = MongoClient(uri, server_api=ServerApi('1'))
db = client["harveal"]
collection = db["users"]

sender_email = "harvealsup628@gmail.com"
sender_password = "pcla mrfa myju mdtp"
    
app = FastAPI()
templates = Jinja2Templates(directory="templates")  #html files
app.mount("/static", StaticFiles(directory="static"), name="static")#css and js files 


@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("LogReg.html", {"request": request})



# Generate a random 5-digit OTP
otp_user = random.randint(10000, 99999)

@app.post("/sendotp/")
async def send_otp(data: OtpRequest):
    email = data.email  
    
    try:
        send_mail(email, otp_user)
        return {"message": "OTP sent successfully!"}
    except Exception as e:
        return JSONResponse(content={"error": f"Failed to send OTP: {str(e)}"}, status_code=500)



def send_mail(user,otpuser):
    sender_email = "harvealsup628@gmail.com"
    sender_password = "pcla mrfa myju mdtp"
    print(user)
    msg=MIMEMultipart()
    # cpys jcyk yqiw scie -  app pass
    # "gwcy eovg hvmf smzj" - main acc
    # "quyu ilzv kobs hcwp" - harv app pass
     
    msg['From'] = sender_email
    msg['To'] = user
    msg['Subject'] = "Welcome to Harveal: your plant specialist"
        
    welcome_message = f"""
    Dear {user},

Welcome to Harveal! We are glad to have you on board and want to extend our warmest greetings.

At Harveal, we're dedicated to providing you with all services related to your plant health. Whether you're a seasoned user 
or just getting started, our goal is to make your experience best of best and rewarding.Feel free to reach out at harvealsup628@gmail.com if you have any 
questions, feedback, or if there's anything else we can assist you with. We're here to help!

Use this otp to signup {otpuser}
This is your User ID-{Id_user}, you can use for login, whenever you need.



Thank you for choosing Harveal. We look forward to being a part of your journey.

Best regards,

The Harveal Team.
    
    """
    msg.attach(MIMEText(welcome_message, 'plain'))
        
        #SMTP server
    try:
        server=smtplib.SMTP('smtp.gmail.com',587)
        server.starttls()
        server.login(sender_email,sender_password)

        server.sendmail(sender_email,user,msg.as_string())
        server.quit()
        print("email sent successfully!")
           
            
    except Exception as e:
        return f"An error occurred: {str(e)}"
    
    
    
def log_send_mail(log_user,log_otp_user):
    sender_email = "harvealsup628@gmail.com"
    sender_password = "pcla mrfa myju mdtp"
    
    msg=MIMEMultipart()
    # cpys jcyk yqiw scie -  app pass
    # "gwcy eovg hvmf smzj" - main acc
    # "quyu ilzv kobs hcwp" - harv app pass
     
    msg['From'] = sender_email
    msg['To'] = log_user
    
    msg['Subject'] = f"login to Harveal: otp:{log_otp_user}"
        
    welcome_message = f"""
    Dear {log_user},

    Use this otp to login:{log_otp_user}

    Thank you for choosing Harveal. We look forward to being a part of your journey.

    Best regards,

    The Harveal Team.
    
    """
    msg.attach(MIMEText(welcome_message, 'plain'))
        
        #SMTP server
    try:
        server=smtplib.SMTP('smtp.gmail.com',587)
        server.starttls()
        server.login(sender_email,sender_password)

        server.sendmail(sender_email,log_otp_user,msg.as_string())
        server.quit()
        print("email sent successfully!")
               
    except Exception as e:
        return f"An error occurred: {str(e)}"
    
    


@app.post("/register_user/")
async def register(phone: str = Form(...), email: str = Form(...),otp:int=Form(...)):
    # Insert the received data into MongoDB
    user_data = {
        "phone_number":phone,
        "email":email,
        "HARV_ID":Id_user
    }       
    if (otp != otp_user):
        return{"incorrect otp"}
    else:
        collection.insert_one(user_data)
        return {"message": "Data stored successfully!"}

    
#logic for id generation

log_id=random.randint(100000,999999) 
Id_user="HARV2024"+str(log_id)
 
 
 

log_otp_user = secrets.randbelow(90000) + 10000
  
  
@app.post("/login_user/")
async def login(logOTP:int=Form(...)):
    print(logOTP)
    if (logOTP == log_otp_user):
        return{"login successfully!"}
    else:
        return {"what a waste!"}
    
   
class LogOtpRequest(BaseModel):
    uid: str
 
@app.post("/send_log_otp/") 
async def send_log_otp(lgdata:LogOtpRequest):
    log_ID = get_user_by_id(lgdata.uid)
    print(log_ID)
    print(log_ID["email"])
    log_send_mail(log_ID["email"], log_otp_user)

      
def get_user_by_id(uid):
    return db.users.find_one({"HARV_ID": uid})



