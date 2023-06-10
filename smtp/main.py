import smtplib as s
from tkinter import *
import tkinter as tk
import csv
from time import strftime
from datetime import datetime as dt
from email.message import EmailMessage


def my_time():
    t2=dt.now()
    show=t2.strftime("%m/%d/%Y\n %H:%M:%S")
    t1.config(text=show)

def send_message():
    from_msg=send.get()
    from_pass="oyefedyeujqznfph"
    msg=EmailMessage()
    msg["To"]=address.get()
    msg["From"]=send.get()
    msg["Subject"]=sub.get()
    msg.set_content(msg_entry.get('1.0',END))
    
    
    with open("emails.csv", "w") as file:
        writer = csv.writer(file)
        writer.writerow([msg["From"],msg["To"],msg["Subject"],])
       
        
    ob=s.SMTP("smtp.gmail.com",587)
    ob.starttls()
    ob.login(from_msg,from_pass)
    ob.send_message(msg)    
    print("send successfully")
    ob.quit()



wb=Tk()
wb.geometry("500x500")
wb.title("Email App")
wb.iconbitmap('email (1).ico')

heading = Label(text="Email Sender Option",bg="yellow",fg="black",font=("Bold",15),width="500",height="3")
heading.pack()
wb.configure(background = "light blue")
  
t1=tk.Label(wb,font=('times',12,'bold'),bg="yellow")
t1.place(x=380,y=15)
my_time()


address=StringVar()
send=StringVar()
sub=StringVar()

address_lbl=Label(wb,text="To",font=15)
address_lbl.place(x=30,y=80)

address_entry=Entry(wb,textvariable=address,font=("Calibri",15),width="30")
address_entry.place(x=180,y=80)

send_lbl = Label(wb,text="From",font=15)
send_lbl.place(x=30,y=130)
  
send_entry=Entry(wb,textvariable=send,width="30",font=("Calibri",15))
send_entry.place(x=180,y=130)

send_lbl = Label(wb,text="Subject",font=15)
send_lbl.place(x=30,y=180)  

send_entry=Entry(wb,textvariable=sub,width="30",font=("Calibri",15))
send_entry.place(x=180,y=180)

msg_lbl = Label(wb,text="Message :",font=15)
msg_lbl.place(x=30,y=230)

msg_entry=Text(wb,width="40",font=("Calibri",15))
msg_entry.place(x=30,y=260,height=85)

buton=Button(wb,text="Send",bg="green",width=30,height=2,command=send_message)
buton.place(x=120,y=390)

mainloop()