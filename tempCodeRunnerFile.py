@app.post("/sendotp/")
async def send_otp(email: str = Form(...)):
  
   send_mail(email,otp_user)
   return{"its done"}