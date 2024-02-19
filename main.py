'''-------------------------------------------------HARVEAL----------------------------------------------------------'''
''' IMPORTS ||
            \/ '''
from fastapi import FastAPI,Form, Request,UploadFile,File
from fastapi.staticfiles import StaticFiles
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from fastapi.responses import HTMLResponse,JSONResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import random
from pydantic import BaseModel
from fastapi import Depends,  HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from datetime import datetime, timedelta
from langdetect import detect
from gtts import gTTS
import os
from translate import Translator
import secrets
from starlette.middleware.sessions import SessionMiddleware
from fastapi.security import OAuth2PasswordBearer
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np
#-----------------------------------------------------------------------------------------------------------------------
#loading tomato madel---------------------------------------------------------------------------------------------------

mod='mymod.h5'
loaded_model = load_model(mod)

#-----------------------------------------------------------------------------------------------------------------------
class OtpRequest(BaseModel):
    email: str

#----------------------------------------------------database-----------------------------------------------------------
# http://127.0.0.1:8000/docs.
uri = "mongodb+srv://harveal:harveal2024@cluster0.25sb0oo.mongodb.net/?retryWrites=true&w=majority"

client = MongoClient(uri, server_api=ServerApi('1'))
db = client["harveal"]
collection = db["users"]
dis_col=db['disease']
#----------------------------------------------------database-----------------------------------------------------------

#-------------email-----------------------------------
sender_email = "harvealsup628@gmail.com"
sender_password = "pcla mrfa myju mdtp"
#-------------email-----------------------------------
app = FastAPI()
templates = Jinja2Templates(directory="templates")  #html files
app.mount("/static", StaticFiles(directory="static"), name="static")#css and js files 

origins = ["*"]  # Update this with your frontend's actual origin(s)

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
    
)
SECRET_KEY = "harveal_45512"

# Session timeout in minutes
SESSION_TIMEOUT_MINUTES = 30

app.add_middleware(SessionMiddleware, secret_key=SECRET_KEY)

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

def get_current_user(session: dict = Depends(lambda s: s.session)):
    user_id = session.get("user_id")
    if user_id not in collection:
        return None
    return collection[user_id]



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

        server.sendmail(sender_email,log_user,msg.as_string())
        server.quit()
        print("email sent successfully!")
               
    except Exception as e:
        return f"An error occurred: {str(e)}"
    
    
log_id=random.randint(100000,999999) 
Id_user="HARV2024"+str(log_id)


#new user---------------------------------------------------------------------------------------------------------------
@app.post("/register_user/")
async def register(phone: str = Form(...), email: str = Form(...),otp:int=Form(...)):
    # Insert the received data into MongoDB
    user_data = {
        "phone_number":phone,
        "email":email,
        "HARV_ID":Id_user
    }       
    find=db.users.find_one({"email": email})
    print(find)
    if (email==find):
        return {"user already exist"} 
    elif (otp != otp_user):
        return{"incorrect otp"}
    else:
        collection.insert_one(user_data)
  
    # Store the session ID in a cookie
        return RedirectResponse(url="/mainpg/")

   
#----------------------------------------------------------------------------------------------------------------------   
log_otp_user = secrets.randbelow(90000) + 10000  #logic for id generation

#for regesistered user(login)
@app.post("/login_user/",response_class=HTMLResponse)
async def login(request: Request,logID:str=Form(...),logOTP:int=Form(...)):
    print(logOTP)
    print(logID)
    if (logOTP == log_otp_user):
        session_id = str(datetime.utcnow().timestamp())
        request.session["user_id"] = logID
        response = templates.TemplateResponse("logtest.html", {"request": request})
        response.set_cookie(key="session_id", value=session_id, expires=timedelta(minutes=SESSION_TIMEOUT_MINUTES))
        return templates.TemplateResponse("logtest.html", {"request": request})
    else:
        return {"what a waste!"}  
    

class LogOtpRequest(BaseModel):
    uid: str
@app.post("/send_log_otp/") 
async def send_log_otp(lgdata:LogOtpRequest):
    log_ID = get_user_by_id(lgdata.uid)
    print(log_ID)
    print(log_ID["email"])
    v=log_ID["email"]
    log_send_mail(v, log_otp_user)
     
def get_user_by_id(uid):
    return db.users.find_one({"HARV_ID": uid})
#------------------------------------------------------------------------------------------------------------------------
#for translation in marathi
@app.post("/translate/")
async def translate_to_marathi(text: str = Form(...)):
    #text to Marathi
    translator = Translator(to_lang="mr")
    translated_text = translator.translate(text)
    chunk_size = 200
    text_chunks = [text[i:i+chunk_size] for i in range(0, len(text), chunk_size)]

    # Translate each chunk separately
    translated_text = ""
    for chunk in text_chunks:
        translator = Translator(to_lang="mr")
        translated_chunk = translator.translate(chunk)
        translated_text += translated_chunk + " "

    return JSONResponse(content={"translatedText": translated_text.strip()})

    # return JSONResponse(content={"translatedText": translated_text})
    
   #for translation in marathi 
#for translation in hindi
@app.post("/translate_hindi/")
async def translate_to_hindi(text_h: str = Form(...)):
    chunk_size = 200
    text_chunks = [text_h[i:i+chunk_size] for i in range(0, len(text_h), chunk_size)]

    translated_text = ""
    for chunk in text_chunks:
        translator = Translator(to_lang="hi")
        translated_chunk = translator.translate(chunk)
        translated_text += translated_chunk + " "

    return JSONResponse(content={"translatedText": translated_text.strip()})

#-----------------------------------------------------------------------------------------------------------------------
#read out loud feature
@app.post("/read_out_loud/")
async def read_out_loud(text: str = Form(...)):

    detected_lang = detect(text)

    # gTTS object
    tts = gTTS(text=text, lang=detected_lang)

    # Save the audio file
    audio_path = "static/audio/output.mp3"
    tts.save(audio_path)

    # Play the audio file
    os.system("start " + audio_path)

    return JSONResponse(content={"audio_url": "/static/audio/output.mp3"})

@app.get("/protected")
async def protected_route(current_user: dict = Depends(get_current_user)):
    if current_user:
        return {"message": "This is a protected route", "user": current_user}
    else:
        raise HTTPException(status_code=401, detail="Not authenticated")


#-----------------------------------------------------------------------------------------------------------------------
#logout endpoint
@app.post("/logout", response_class=HTMLResponse)
async def logout(request: Request, response: JSONResponse):
    response.delete_cookie(key="session_id")
    request.session.clear()
    response = RedirectResponse(url="/")
    return response

#-----------------------------------------------------------------------------------------------------------------------
#prediction of model
@app.post("/predmod/")
async def prediction(file: UploadFile=File(...)):
    with  open(f'uploads/{file.filename}', 'wb+') as imgfile:
        imgfile.write(file.file.read())
        
    image_path = f'uploads/{file.filename}'
    new_image = image.load_img(image_path, target_size=(64, 64))
    new_image_array = image.img_to_array(new_image)
    new_image_array = np.expand_dims(new_image_array, axis=0)
    new_image_array /= 255.0
    prediction = loaded_model.predict(new_image_array)


    class_labels = ['healthy_leaf', 'target_spot', 'ToMV']
    predicted_class_index = np.argmax(prediction)
    predicted_class = class_labels[predicted_class_index]
    
    
    detc_disease=dis_col.find_one({'d_id': predicted_class})
    result=detc_disease['d_desc']
    confid=prediction.squeeze()
    
    

    print(f"The predicted class is: {predicted_class}")
    print(f"Confidence scores: {prediction.squeeze()}")
        
    return JSONResponse(content={"result": result, "confidence": confid.tolist()})