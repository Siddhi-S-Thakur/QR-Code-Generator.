import qrcode

#taking upi id as input
upi_id=input("Enter your UPI Id:")

phonepe_url = f'upi://pay?pa={upi_id}&pn=Recipient%20Nam&am=1&cu=INR'
paytm_url = f'upi://pay?pa={upi_id}&pn=Recipient%20Name&am=1&cu=INR'
gpay_url = f'upi://pay?pa={upi_id}&pn=Recipient%20Name&am=1&cu=INR'

#creating QR code for each payment app
phonepe_qr= qrcode.make(phonepe_url)
paytm_qr= qrcode.make(paytm_url)
gpay_qr= qrcode.make(gpay_url)


#displaying the QR code
phonepe_qr.show()
paytm_qr.show()
gpay_qr.show()
