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




otp_user = random.randint(1000, 9999)

@app.post("/sendotp/")
async def send_otp(data: OtpRequest):
    email = data.email  # Generate a random 4-digit OTP
    
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
    # cpys jcyk yqiw scie app pass
    # "gwcy eovg hvmf smzj" main acc
    # "quyu ilzv kobs hcwp" harv app pass
     
    msg['From'] = sender_email
    msg['To'] = user
    
    msg['Subject'] = "this is otp message"
        
    welcome_message = f"""
    use this otp to login {otpuser}
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


@app.post("/register_user/")
async def register(phone: str = Form(...), email: str = Form(...),otp:int=Form(...)):
    # Insert the received data into MongoDB
    user_data = {
        "phone_number":phone,
        "email":email
    }
           
    if (otp != otp_user):
        return{"incorrect otp"}
    else:
        collection.insert_one(user_data)
        return {"message": "Data stored successfully!"}




