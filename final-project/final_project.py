#Step 1: Import necessary package
import smtplib #Python provides smtplib module, which defines an SMTP client session object that can be used to send mail to any Internet machine with an SMTP or ESMTP listener daemon
#email.mime module is required to craft the email messages
from email.mime.multipart import MIMEMultipart #untuk menambahkan lebih beberapa part pada email
from email.mime.text import MIMEText #untuk menambahkan teks pada email
from email.mime.base import MIMEBase
from email import encoders #Encoder akan mengkodekan setiap jalur input yang aktif menjadi kode bilangan biner.
import json #format data yang digunakan untuk pertukaran dan penyimpanan data

#Step 2: Menambahkan variabel subjek, body email dan email penerima
email_sender = input("Sender email: ")
daftar_email = []

email = int(input("Berapa banyak email: "))
for i in range(email):
    email_receiver = input("masukkan alamat email: ")
    daftar_email.append(email_receiver)

rec =  ', '.join(daftar_email) #mengkonversi atau mengubah variabel yang nilainya berformat array menjadi berformat string 

#mengcopy unit dalam list ke file txt
with open('receiver_list.txt', 'w') as f:
    f.write(json.dumps(daftar_email)) #encoding data

msg = MIMEMultipart()
msg['Subject'] = input("Subjek email: ")
msg['From'] = email_sender
msg['To'] = rec
    
body = input("Body email: ")
msg.attach(MIMEText(body, 'plain'))

#Step 3: Attachment Gambar
filename = "Kholilah Qultsum_CV for KI.pdf"
attachment = open("D:\\Kholilah Qultsum_CV for KI.pdf", "rb") #rb untuk file yang bersifat binary

#Step 4: Kirim email
part = MIMEBase('application', 'octet-stream')
part.set_payload((attachment).read())   
encoders.encode_base64(part)
part.add_header('Content-Disposition', "attachment; filename= %s" % filename)
msg.attach(part)
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
password = input("Masukkan password: ")
server.login(email_sender, password)
text = msg.as_string()
server.sendmail(email_sender, daftar_email, text)
server.quit()


#Referensi
#https://answer-id.com/id/53557096
#https://www.codegrepper.com/code-examples/python/how+to+append+a+list+to+a+text+file+in+python
#https://gist.github.com/wfng92/a36729f5d8a43652abe46b9ab944d64a
#https://code.tutsplus.com/id/tutorials/sending-emails-in-python-with-smtp--cms-29975
#https://stackoverflow.com/questions/38825943/mimemultipart-mimetext-mimebase-and-payloads-for-sending-email-with-file-atta
#https://betterprogramming.pub/how-to-send-an-email-with-attachments-in-python-abe3b957ecf3