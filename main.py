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
from datetime import datetime, timezone,timedelta
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
from bson import ObjectId 
from pydantic import BaseModel
#-----------------------------------------------------------------------------------------------------------------------
#loading tomato madel---------------------------------------------------------------------------------------------------

# mod='tomato_model.keras'
# loaded_model = load_model(mod)


# mod_pump='pumpkin_model.keras'
# load_model_pumpkin=load_model(mod_pump)

#-----------------------------------------------------------------------------------------------------------------------
class OtpRequest(BaseModel):
    email: str
#--------------------------------------------------------------for appointment submission data--------------------------
from typing import List
from pydantic import BaseModel
from datetime import date

class AppointmentFormData(BaseModel):
    hid: str
    fullname: str
    dob: str
    contact: str
    plant: str
    description: str
    visitType: str
    houseNumber: str
    street: str
    city: str
    state: str
    pincode: str
    timestamp:str
    
    
class VAppointmentFormData(BaseModel):
    vfid: str
    vfullname: str
    vdob: str
    vcontact: str
    vplant: str
    vdescription: str
    vvisitType: str
    
class ptype(BaseModel):
    plant_type: str
#----------------------------------------------------database-----------------------------------------------------------
# http://127.0.0.1:8000/docs
uri = "mongodb+srv://harveal:harveal2024@cluster0.25sb0oo.mongodb.net/?retryWrites=true&w=majority"

client = MongoClient(uri, server_api=ServerApi('1'))
db = client["harveal"]
collection = db["users"]
dis_col=db['disease']
appointdb=db["appointments"]
admin_collection=db["admin"]
queries=db["queries"]
#----------------------------------------------------database-------------------------------------------------------------

#-------------------------------------------------------email-----------------------------------------------------------------

sender_email = "harvealsup628@gmail.com"
sender_password = "pcla mrfa myju mdtp"

#-------------------------------------------------------email-----------------------------------------------------------------
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
SECRET_KEY = secrets.token_hex(32)

# Session timeout in minutes
SESSION_TIMEOUT_MINUTES = 30

app.add_middleware(SessionMiddleware, secret_key=SECRET_KEY)

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


def get_session(request: Request):
    print("this is session:",request.session)
    return request.session

async def get_current_user(session: dict = Depends(get_session)):
    user_id = session.get("user_id")
    print("thiss is uid in session:",user_id)
    if user_id:
        user = collection.find_one({"HARV_ID": user_id})
        if user:
            return user
    return None





@app.get("/sig_log/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("LogReg.html", {"request": request})

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("Home.html", {"request": request})




otp_user = random.randint(10000, 99999)

@app.post("/sendotp/")
async def send_otp(data: OtpRequest):
    email = data.email  
    
    
    existing_user = db.users.find_one({"email": email})
    if existing_user:
        return JSONResponse({"error": "User already exists"}, status_code=400)
    
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
        
    welcome_message =  f"""
<html>
  <head>
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Didact+Gothic&family=Quicksand:wght@300&display=swap');
       body {{  
       font-family: 'Didact Gothic', sans-serif;
    }}
      .header {{
        background-color: rgb(13, 202, 76);
        text-align: center
        padding: 25px;
      }}
      .logo {{
        width: 150px; /* Adjust the size as needed */
        height: auto;
      }}
      .headname {{
        color: white;
        font-size: 24px;
        font-weight: bold;
      }}
      .footer {{
  background-color: rgb(13, 202, 76);
  color: white;

  text-align: center;
  padding: 20px 0;
  
  bottom: 0;
  width: 100%;
}}

.footer-content {{
  display: flex;
  flex-direction: column;
}}

.footer-label {{
  font-weight: bold;
  font-size: 35px;
  margin-bottom: 10px;
}}

.footer-copyright {{
  font-size: 14px;
  color: black;
}}
    </style>
  </head>
  <body>
    <div class="header">
      <label for="" class="headname"><strong>Harveal</strong></label>
    </div>
    <p>Dear {log_user},</p>
    <p>Use this OTP to login: <strong>{log_otp_user}</strong></p>
    <p>Thank you for choosing Harveal. We look forward to being a part of your journey.</p>
    <p>Best regards,<br/>The Harveal Team.</p>
     <footer class="footer">
          <div class="footer-content">
              <p class="footer-label">Harveal, Your Plant Specialist.</p>
              <p class="footer-copyright">&#169; 2023 Harveal. All rights reserved.</p>
          </div>
      </footer>
  </body>
</html>
"""
    msg.attach(MIMEText(welcome_message, 'html'))
        
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
async def register(request: Request,phone: str = Form(...), email: str = Form(...),otp:int=Form(...)):
    # Insert the received data into MongoDB
    user_data = {
        "phone_number":phone,
        "email":email,
        "HARV_ID":Id_user
    }       
    find=db.users.find_one({"email": email})
    print(find)
    if find:
        return JSONResponse({"error": "User already exists"}, status_code=400)
    elif (otp != otp_user):
        return JSONResponse({"error": "Incorrect OTP"}, status_code=400)
    else:
        collection.insert_one(user_data)
        session_id = str(datetime.now(timezone.utc).timestamp())
        request.session["user_id"] = Id_user
        print(request.session["user_id"])
  
    # Store the session ID in a cookie
        response= templates.TemplateResponse("Inhome.html", {"request": request})
        response.set_cookie(key="session_id", value=session_id, expires=timedelta(minutes=SESSION_TIMEOUT_MINUTES))
        return response
        


   
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
        print("dem:",request.session["user_id"] )
        
        response = templates.TemplateResponse("Inhome.html", {"request": request})
        response.set_cookie(key="session_id", value=session_id, expires=timedelta(minutes=SESSION_TIMEOUT_MINUTES))
        return response
    else:
        return {"what a waste!"}  
    

class LogOtpRequest(BaseModel):
    uid: str
@app.post("/send_log_otp/") 
async def send_log_otp(lgdata:LogOtpRequest):
    log_ID = get_user_by_id(lgdata.uid)
    
    if log_ID is None:
        raise HTTPException(status_code=404, detail="User not found") 
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
    # text to Marathi
    translator = Translator(to_lang="mr")
    translated_text = translator.translate(text)
    chunk_size = 200
    text_chunks = [text[i:i+chunk_size] for i in range(0, len(text), chunk_size)]

    # Translate each chunk separately
    translated_text = ""
    for chunk in text_chunks:
        translator = Translator(to_lang="mr")
        translated_chunk = translator.translate(chunk)
        translated_text += translated_chunk 
        translated_text.replace('br', '\n')

    return JSONResponse(content={"translatedText": translated_text.strip()})
   
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
        translated_text += translated_chunk
        translated_text.replace('br', '\n')

    return JSONResponse(content={"translatedText":translated_text.strip()})

#-----------------------------------------------------------------------------------------------------------------------
#read out loud feature
@app.post("/read_out_loud/")
async def read_out_loud(text: str = Form(...)):

    detected_lang = detect(text)

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
@app.get("/logout/", response_class=HTMLResponse)
async def logout(request: Request, response: JSONResponse):
    response.delete_cookie(key="session_id")
    request.session.clear()
    response = RedirectResponse(url="/")
    return response

#-----------------------------------------------------------------------------------------------------------------------
#prediction of model

@app.post("/predmod/")
async def prediction(file: UploadFile = File(...),plant_type: str = Form(...)):
    # Load the appropriate model based on the selected plant type
    if plant_type == 'Pumpkin':
        print(plant_type)
        model_path = 'pumpkin_model.keras'
        class_labels = ['Alt_cucu', 'Alt_b', 'Aphid', 'ArmW', 'Bact_LS', 'Bact_wilt', 'Cucum_beet', 'Flee_beet', 'Fusa', 'Gum_stem', 'Phy_bli', 'Sqau_bg', 'Sq_vb','Thirps', 'Hlty_pump']
    elif plant_type == 'Tomato':
        model_path = 'tomato_model.keras'
        class_labels = ['Bacspot', 'Eblight', 'LateB', 'LeafM', 'septLeaf', 'SpidM', 'TarSpot', 'YellowLeaf', 'ToMV', 'Hlty']
    else:
        return JSONResponse(content={"error": "Invalid plant type"})
    
    loaded_model = load_model(model_path)

    # Save the uploaded image
    with open(f'uploads/{file.filename}', 'wb+') as imgfile:
        imgfile.write(file.file.read())
        
    image_path = f'uploads/{file.filename}'
    new_image = image.load_img(image_path, target_size=(64, 64))
    new_image_array = image.img_to_array(new_image)
    new_image_array = np.expand_dims(new_image_array, axis=0)
    new_image_array /= 255.0
    prediction = loaded_model.predict(new_image_array)

    predicted_class_index = np.argmax(prediction)
    predicted_class = class_labels[predicted_class_index]
    
    # Assuming dis_col is your MongoDB collection for disease descriptions
    detc_disease = dis_col.find_one({'d_id': predicted_class})
    result = detc_disease['d_desc']
    
    confidence = prediction.squeeze()

    print(f"The predicted class is: {predicted_class}")
    print(f"Confidence scores: {confidence}")
        
    return JSONResponse(content={"result": result, "confidence": confidence.tolist()})

#-----------------------------header.html------------------------------------------------------------------
@app.get("/header/", response_class=HTMLResponse)
async def render_header(request: Request):
    return templates.TemplateResponse("header.html", {"request": request})
#---------------------------appointment----------------------------------------------------------------------
@app.get("/appointment/", response_class=HTMLResponse)
async def appointment(request: Request, current_user: dict = Depends(get_current_user)):
    if current_user:
        return templates.TemplateResponse("appoint.html", {"request": request})
    else:
         return RedirectResponse(url="/sig_log/")
 
#----------------------------------------mainpage--------------dignose------------------------------------
@app.get("/diagnose/", response_class=HTMLResponse)
async def appointment(request: Request,current_user: dict = Depends(get_current_user)):
    if current_user:
        return templates.TemplateResponse("mainP.html", {"request": request})
    else:
         return RedirectResponse(url="/sig_log/")
#-----------------------------------------------home_aft_log_sig--------------------------------------------------------
@app.get("/Inhome/", response_class=HTMLResponse)
async def appointment(request: Request,current_user: dict = Depends(get_current_user)):
    if current_user:
        return templates.TemplateResponse("Inhome.html", {"request": request})
    else:
         return RedirectResponse(url="/sig_log/")
#-------------------------------------------contactus-------------------------------------------------------------------
@app.get("/contactus/", response_class=HTMLResponse)
async def appointment(request: Request,current_user: dict = Depends(get_current_user)):
    if current_user:
        return templates.TemplateResponse("contactus.html", {"request": request})
    else:
         return RedirectResponse(url="/sig_log/")
#----------------------------------------------------news------------------------------------------------------------------------
@app.get("/news/", response_class=HTMLResponse)
async def appointment(request: Request,current_user: dict = Depends(get_current_user)):
    if current_user:
        return templates.TemplateResponse("news.html", {"request": request})
    else:
         return RedirectResponse(url="/sig_log/")
#---------------------------------------admin(displaying appts)----------------------------------------------------

#---------------------------------------admin login page-------------------------------------------------------------

#---------------------------------------appointment_submit----------------------------------------------------------
@app.post("/submit_appn/")
async def submit_appointment(
    hid: str = Form(...),
    fullname: str = Form(...),
    dob: str = Form(...),
    contact: str = Form(...),
    plant: str = Form(...),
    description: str = Form(...),
    visitType: str = Form(...),
    houseNumber: str = Form(...),
    street: str = Form(...),
    city: str = Form(...),
    state: str = Form(...),
    pincode: str = Form(...),

):
    try:
      
        # Validate the form data using the Pydantic model
        appointment_data = AppointmentFormData(
            hid=hid,
            fullname=fullname,
            dob=dob,
            contact=contact,
            plant=plant,
            description=description,
            visitType=visitType,
            houseNumber=houseNumber,
            street=street,
            city=city,
            state=state,
            pincode=pincode,
            timestamp=str(datetime.now().strftime("%Y-%m-%d %H:%M:%S")),
        )
        print(appointment_data.model_dump())
        ald=appointdb.find_one({"hid": hid})
        print(ald)
        if ald:
            raise HTTPException(status_code=400, detail="Already booked a appointment!") 
        
        if(ald==None):    
            appointdb.insert_one(appointment_data.model_dump())
            user_data = collection.find_one({"HARV_ID": hid})
            receiver_email = user_data["email"]
            send_appointment_confirmation_email(appointment_data, receiver_email)
    except Exception as e:
        # Handle other exceptions
        print(f"Error: {str(e)}")
        raise HTTPException(
            status_code=500, detail=f"Internal Server Error: {str(e)}"
        )

def send_appointment_confirmation_email(appointment_data, receiver_email):
    # Email configuration
    sender_email = "harvealsup628@gmail.com"
    sender_password = "pcla mrfa myju mdtp"

    # Constructing the message
    message = MIMEMultipart()
    message['From'] = sender_email
    message['To'] = receiver_email
    message['Subject'] = "Harveal-Appointment Confirmation"

    # Message body
    body = f"Dear {appointment_data.fullname},\n\n"\
           "Thank you for booking your appointment with us.\n"\
           "Here are the details of your appointment:\n"\
           f"Appointment ID: {appointment_data.hid}\n"\
           f"Name: {appointment_data.fullname}\n"\
           f"Plant: {appointment_data.plant}\n"\
           f"Description: {appointment_data.description}\n"\
           f"Address: {appointment_data.houseNumber}, {appointment_data.street}, "\
           f"{appointment_data.city}, {appointment_data.state}, {appointment_data.pincode}\n\n"\
           "If any changes are needed, please contact us at our toll-free number: 1800-XXX-XXXX.\n\n"\
           "We look forward to seeing you.\n"\
           "Best regards,\nYour Organization"

    message.attach(MIMEText(body, 'plain'))

    # Sending the email
    try:
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, receiver_email, message.as_string())
        print("Email sent successfully!")
    except Exception as e:
        print(f"An error occurred while sending the email: {str(e)}")


#-----------------------------------adminlogin------------------------------------------------------------------------
@app.get("/adminlog/", response_class=HTMLResponse)
async def appointment(request: Request):
    return templates.TemplateResponse("admin.html", {"request": request})




class AdminLoginRequest(BaseModel):
    admin_id: str
    password: str

@app.post("/admin-login/", response_class=HTMLResponse)
async def admin_login(request: Request, admin_id: str = Form(...), password: str = Form(...)):
    admin = admin_collection.find_one({"admin_id": admin_id})
    if admin:
        return templates.TemplateResponse("adminapp.html", {"request": request}) 
    else:
        return templates.TemplateResponse("admin.html", {"request": request})
    

#-------------------------------------------------------------get appnt------------------------------------------------
@app.get("/api/appointments")
async def get_appointments():
    appointments = list(appointdb.find({}))
    
    # Convert ObjectId to string in each appointment
    for appointment in appointments:
        appointment["_id"] = str(appointment["_id"])  # Convert ObjectId to string
    
    return appointments
#---------------------------------------deletion app-----------------------------------------------------------------
@app.post("/api/appointments/{hid}/delete")
async def delete_appointment(hid: str):
    try:
        # Delete the appointment from the database based on the provided hid
        result = appointdb.delete_one({"hid": hid})
        
        if result.deleted_count == 1:
            return {"message": "Appointment deleted successfully"}

        
        else:
            raise HTTPException(status_code=404, detail="Appointment not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
#---------------------------------------------contact us submit---------------------------------------------------

class con_sub(BaseModel):
    name : str
    email:str
    message:str

@app.post("/sub_contact/")
async def submitcontact(request:Request,name:str=Form(...),email:str=Form(...),message:str=Form(...)):
    
    subdata={
        "name":name,
        "email":email,
        "date":datetime.now(),
        "message":message
    }
    
    queries.insert_one(subdata)
    return {"success"}

