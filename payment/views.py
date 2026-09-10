from django.shortcuts import render
from .models import Payment
import qrcode
import os
from django.conf import settings

# Create your views here.


def payment_form(request):
    # Ye ek Django view function hai.
    # User jab payment page open karta hai,
    # Django is function ko execute karta hai.
    
    qr_url = None
    # None ka matlab hai ki abhi QR Code generate nahi hua.
    # Baad me jab QR generate hoga,
    # qr_url me QR image ka URL store karenge.
    
    if request.method == 'POST':
     # Check kar rahe hain ki user ne page par
    # POST request bheji hai ya nahi.
    # POST request normally tab aati hai
    # jab user form submit karta hai.
    
    
        upi_id = request.POST.get("upi_id")  # Form se 'upi_id' naam ke input ki value le rahe hain. 
        receiver_name = request.POST.get("receiver_name")  # Form se receiver name ki value le rahe hain.
        amount = request.POST.get("amount")  # Form se amount ki value le rahe hain.
        note = request.POST.get("note")  # Form se payment note ki value le rahe hain.
        
        
        # Payment model ka ek object create kar rahe hain.
        payment = Payment(
            upi_id = upi_id,                 # Payment object ke upi_id field me form se mili UPI ID store kar rahe hain.
            receiver_name = receiver_name,    # Payment object ke receiver_name field me receiver ka naam store kar rahe hain.
            amount = amount,                  # Payment object ke amount field me user dwara entered amount store kar rahe hain.
            note = note                       # Payment object ke note field me payment note store kar rahe hain.
        
        )
        payment.save()                        # Payment object ko database me permanently save kar rahe hain
        upi_url = f"upi://pay?pa={upi_id}&pn={receiver_name}&am={amount}&cu=INR&tn={note}"
        # Actual UPI payment URL create kar rahe hain.
        # f-string ki help se user ki actual information
        # UPI URL ke andar insert ho rahi hai.
        
        
        
        qr = qrcode.make(upi_url)               # qrcode.make() UPI URL ko QR Code image me convert karta hai.
        qr.save(os.path.join(settings.MEDIA_ROOT, "qr.png"))
        # os.path.join() do paths ko safely combine karta hai:
        
        
        qr_url = settings.MEDIA_URL + "qr.png"   # Isliye QR image media folder ke andar save hoti hai.
        
        
        # Ye debugging/checking ke liye useful hai.
        print("upi_id",upi_id)
        print("receiver_name",receiver_name)
        print("amount",amount)
        print("note",note)

    # return render (request, 'payment_form.html')
    return render(request,'payment_form.html',{"qr_url":qr_url})
    # User ko HTML template return/render kar rahe hain
