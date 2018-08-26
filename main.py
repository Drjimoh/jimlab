import tkinter
from tkinter import ttk
from tkinter import messagebox


app = tkinter.Tk()
app.configure(background='#a1dbcd')
app.geometry('1500x1000')
messagebox.showinfo(title= 'Jimoh Lab', message='Welcome to AI with Drug research, this software is currently under development by Jimoh Waliu')

text = tkinter.Label(app, text='''Terms and Conditions ("Terms")

Last updated: (26/08/2018)

Please read these Terms carefully before using the Jimoh Lab software  operated by ITSmart.

Your access to and use of the Service is conditioned on your acceptance of and compliance with these Terms. These Terms apply to all visitors, users and others who access or use the Service.

By accessing or using the Service you agree to be bound by these Terms. If you disagree with any part of the terms then you may not access the Service.

Purchases

If you wish to purchase any product or service made available through the Service, you may be asked to supply certain information relevant to your Purchase.''', bg='#a1dbcd')
text.grid(column=1, row=1)

#text2 = tkinter.Label(text='Jimoh Lab', bg='#a1dbcd')
#text2.grid(column=2, row=2)

app.mainloop()

