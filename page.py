from tkinter import ttk
from tkinter import *
import tkinter as tk
from tkinter import messagebox
import mysql.connector
import tkinter

root = Tk()
root.title("Restaurant Management")
root.geometry("1600x800")
root.configure(bg="#FF6103")
img= PhotoImage(file=r"C:\Users\Hp\OneDrive\Bureau\projet_python\icon-tajin.png")
root.iconphoto(False,img)

canv1 = Canvas(root,width=600 ,bg="#FF6103",height=390)
canv1.place(x=330,y=250)
item1= PhotoImage(file="ttt.gif")
canv1.create_image(1,1, anchor=NW, image=item1)



def page1():
    win1=Toplevel()
    win1.title("Restaurant Management")
    win1.geometry("1600x800")
    win1.configure(bg="white")
    img= PhotoImage(file=r"C:\Users\Hp\OneDrive\Bureau\projet_python\icon-tajin.png")
    win1.iconphoto(False,img)
   

    type_rese = StringVar()
    type_rese.set('Sureplace employe')

    style = ttk.Style()
    style.theme_use('clam')
# change selected color
    style.map('Treeview',background=[('selected',"#F4A460")])

    def suprime():
       selected_item = table.selection()[0]
       table.delete(selected_item)

       connection = mysql.connector.connect(host='localhost',user='root',password='Loutfi@123@',port='3306',database='resto')
       c= connection.cursor()
       Num_table = txtnumtable.get()
      

       txtprix.config(text=prixp+prixb)
       update_query = "DELETE FROM commande WHERE Num_table= "+ Num_table
       #  vals= (Num_table)
       c.execute(update_query)
       messagebox.showinfo("Confirmation", "La commande a été mise à jour avec succès.")
       connection.commit()


    def enrg(): 

       global prixp
       pl=txtnomplats.get()
       qt=int(txtplats.get())
       if pl == "Tajin" :
          prixp =  300 * qt
       elif pl =="Djaj Mhamar":
          prixp =  300 * qt
       elif pl =="Bastila Djaj":
          prixp =  400 * qt
       elif pl =="Bastila Hout":
          prixp=  750 * qt
       elif pl =="Couscous":
          prixp=  500 * qt
       elif pl =="Tanjia":
           prixp=  200 * qt
       elif pl =="Kabab":
          prixp =  150 * qt
       elif pl =="Lham bl Bar9ou9":
          prixp =  200 * qt
       elif pl =="Rien":
          prixp =  0 

       # txtprix.config(text=prixp)
       

       global prixb
       bs=txtboissan.get()
       qtb=int(txtnbrboissan.get())
       if bs == "Atai" :
         prixb =  100 * qtb
       elif bs =="Coca":
        prixb =  50 * qtb
       elif bs =="Fanta":
        prixb =  50 * qtb
       elif bs =="chwips":
        prixb =  50 * qtb
       elif bs =="Jus orange":
        prixb =  80  * qtb
       elif  bs =="Avoca":
        prixb =  80 * qtb
       elif bs =="Fraise":
        prixb =  80 * qtb
       elif bs =="Mangue":
        prixb =  80 * qtb
       elif bs =="Rien":
        prixb =  0 

       # txtprix.config(text=prixb)
       txtprix.config(text=prixp+prixb)
       
       Num_table = txtnumtable.get()
       Nom_plats = txtnomplats.get()
       Nom_boissan = txtboissan.get()
       Nombre_plats = txtplats.get()
       Nombre_boissan = txtnbrboissan.get()
       Type_de_commande = type_rese.get()
       Total = prixp+prixb

       table.insert('','end',values=(Num_table,Nom_plats,Nom_boissan,Nombre_plats,Nombre_boissan,Type_de_commande,Total))

       connection = mysql.connector.connect(host='localhost',user='root',password='Loutfi@123@',port='3306',database='resto')
       c= connection.cursor()
       Num_table = txtnumtable.get()
       Nom_plats = txtnomplats.get()
       Nom_boissan = txtboissan.get()
       Nombre_plats = txtplats.get()
       Nombre_boissan = txtnbrboissan.get()
       Type_de_commande = type_rese.get()
       Total = prixp+prixb
       insert_query = "INSERT INTO commande ( Num_table , Nom_plats , Nom_boissan ,Nombre_plats,Nombre_boissan,Type_commande,Total)VALUES(%s,%s,%s,%s,%s,%s,%s)"
       vals= (Num_table,Nom_plats,Nom_boissan,Nombre_plats,Nombre_boissan,Type_de_commande,Total)
       c.execute(insert_query,vals)
       messagebox.showinfo("Confirmation", "La commande a été insérée avec succès.")
       connection.commit()



       

    def actualise():
       txtnumtable.delete(0,END)
       txtnomplats.delete(0,END)
       txtboissan.delete(0,END)
       txtplats.delete(0,END)
       txtnbrboissan.delete(0,END)
       txtprix.config(text=0)

    def update_data():
       global prixp
       pl=txtnomplats.get()
       qt=int(txtplats.get())
       if pl == "Tajin" :
          prixp =  300 * qt
       elif pl =="Djaj Mhamar":
          prixp =  300 * qt
       elif pl =="Bastila Djaj":
          prixp =  400 * qt
       elif pl =="Bastila Hout":
          prixp=  750 * qt
       elif pl =="Couscous":
          prixp=  500 * qt
       elif pl =="Tanjia":
           prixp=  200 * qt
       elif pl =="Kabab":
          prixp =  150 * qt
       elif pl =="Lham bl Bar9ou9":
          prixp =  200 * qt
       elif pl =="Rien":
          prixp =  0 
      
       global prixb
       bs=txtboissan.get()
       qtb=int(txtnbrboissan.get())
       if bs == "Atai" :
         prixb =  100 * qtb
       elif bs =="Coca":
        prixb =  50 * qtb
       elif bs =="Fanta":
        prixb =  50 * qtb
       elif bs =="chwips":
        prixb =  50 * qtb
       elif bs =="Jus orange":
        prixb =  80  * qtb
       elif  bs =="Avoca":
        prixb =  80 * qtb
       elif bs =="Fraise":
        prixb =  80 * qtb
       elif bs =="Mangue":
        prixb =  80 * qtb
       elif bs =="Rien":
        prixb =  0 
      
       connection = mysql.connector.connect(host='localhost',user='root',password='Loutfi@123@',port='3306',database='resto')
       c= connection.cursor()
       Num_table = txtnumtable.get()
       Nom_plats = txtnomplats.get()
       Nom_boissan = txtboissan.get()
       Nombre_plats = txtplats.get()
       Nombre_boissan = txtnbrboissan.get()
       Type_de_commande = type_rese.get()
       Total = prixp+prixb
       txtboissan.delete(0,END)
      

       txtprix.config(text=prixp+prixb)
       update_query = "UPDATE commande SET  Num_table=%s , Nom_plats=%s, Nom_boissan=%s ,Nombre_plats=%s,Nombre_boissan=%s,Type_commande=%s,Total=%s WHERE Num_table=%s"
       vals= (Num_table,Nom_plats,Nom_boissan,Nombre_plats,Nombre_boissan,Type_de_commande,Total,Num_table)
       c.execute(update_query,vals)
       messagebox.showinfo("Confirmation", "La commande a été mise à jour avec succès.")
       connection.commit()


    lbltitre = Label( win1,bd=10, relief=RIDGE, text="Restaurant Management Systeme" ,font=("Vivaldi",40), bg="#FF6103" ,fg="white")
    lbltitre.place(x=0,y=0,width=1275,height=85) 
    lbltitrecom = Label(win1,text="Formulaire D'enregistrement De Commandes",font=("times new roman",22),background="white",fg="#8A360F")
    lbltitrecom.place (x=400,y=100) 
    numtable=Label(win1,text="Numero Table :",font=("times new roman",14),background="white",fg="#8A360F")
    numtable.place (x=100,y=150)
    txtnumtable=Entry(win1,bd=2,width=30)
    txtnumtable.place(x=300,y=150)

    plats= tk.StringVar() 
    txtnomplats= ttk.Combobox(win1, textvariable = plats ,width=27,cursor="hand2") 
    txtnomplats['values'] = ('Tajin','Djaj Mhamar','Bastila Djaj','Bastila Hout','Couscous','Tanjia','Kabab','Lham bl Bar9ou9',"Rien")
    txtnomplats.place(x=300,y=200)
    txtnomplats.current()


    nomnomplats=Label(win1,text="Nom plats :",font=("times new roman",14),background="white",fg="#8A360F")
    nomnomplats.place (x=100,y=200)
    # txtnomplats=Entry(win1,bd=3,width=30)
    # txtnomplats.place(x=300,y=200)

    prixb=0
    boissan= tk.StringVar() 
    txtboissan= ttk.Combobox(win1, textvariable = boissan ,width=27,text=prixb,cursor="hand2") 
    txtboissan['values'] = ('Atai','Coca','Fanta','chwips','Jus orange','Avoca','Fraise','Mangue',"Rien")
    txtboissan.place(x=300,y=250)
    txtboissan.current()

    nomboissan=Label(win1,text="Nom Boissan :" ,font=("times new roman",14),background="white",fg="#8A360F")
    nomboissan.place (x=100,y=250)
    # txtboissan=Entry(win1,bd=3,width=30)
    # txtboissan.place(x=300,y=250)



    nbrplats=Label(win1,text="Nombre Des Plats :",font=("times new roman",14),background="white",fg="#8A360F")
    nbrplats.place (x=100,y=300)
    txtplats=Entry(win1,bd=2,width=30)
    txtplats.place(x=300,y=300)

    nbrboissan=Label(win1,text="Nombre Des boissan :",font=("times new roman",14),background="white",fg="#8A360F")
    nbrboissan.place (x=100,y=340)
    txtnbrboissan=Entry(win1,bd=2,width=30)
    txtnbrboissan.place(x=300,y=340)

    TYPE=Label(win1,text="Type De Commande :",font=("times new roman",14),background="white",fg="#8A360F")
    TYPE.place(x=100,y=380)
    Surplace= Radiobutton(win1,text="Sureplace",font=("times new roman",14),background="white",fg="#8A360F",value="Sureplace",variable=type_rese)
    Surplace.place(x=300,y=380)
    emporte =Radiobutton(win1,text="emporte",font=("times new roman",14),background="white",fg="#8A360F",value="emporte",variable=type_rese)
    emporte.place(x=440,y=380)

    prixp=0
    Nbprix=Label(win1,text="TOTAL :",font=("times new roman",14),background="white",fg="#8A360F")
    Nbprix.place (x=100,y=420)
    txtprix=Label(win1,bd=2,width=30,text=prixp)
    txtprix.place(x=300,y=420)



    # canv1 = Canvas(win1,width=600 ,bg="white",height=260)
    # canv1.place(x=600,y=130)
    # item1= PhotoImage(file="tajine-marocain2.gif")
    # canv1.create_image(1,1, anchor=NW, image=item1)

    #treeview commande
    table = ttk.Treeview(win1,columns=(1,2,3,4,5,6,7),height=10, show="headings",cursor="hand2")
    

    table.heading(1,text="Num table")
    table.heading(2,text="Nom plats") 
    table.heading(3,text="Nom Boissan")
    table.heading(4,text="Nombre des Plats")
    table.heading(5,text="Nombre des boissan")
    table.heading(6,text="Type de commande")
    table.heading(7,text="Total")




    table.column(1,width=10,anchor=CENTER)
    table.column(2,width=10,anchor=CENTER)     
    table.column(3,width=10,anchor=CENTER)
    table.column(4,width=10,anchor=CENTER)
    table.column(5,width=40,anchor=CENTER)
    table.column(6,width=5,anchor=CENTER)
    table.column(7,width=10,anchor=CENTER)
    table.place(x=100,y=460,width=1050,height=180)

    connection = mysql.connector.connect(host='localhost',user='root',password='Loutfi@123@',port='3306',database='resto')
    c= connection.cursor()
    c.execute('select * from commande')
    commande =  c.fetchall()
    for com in commande:
       table.insert ('','end',value =(com[0],com[1],com[2],com[3],com[4],com[5],com[6]) )

    btnenrgcom=Button(win1,text="Enregistrer",font=("times new roman",16),bg="#FF6103",fg="white",bd=4,relief=GROOVE,command=enrg,cursor="hand2")
    btnenrgcom.place(x=680,y=200,width=200,height=40)

    btnsupprcom=Button(win1,text="Actualiser",font=("times new roman",16),bg="#FF6103",bd=4,relief=GROOVE,fg="white",command=actualise,cursor="hand2")
    btnsupprcom.place(x=950,y=200,width=200,height=40)

    btnsupprACT=Button(win1,text="Update",font=("times new roman",16),bg="#FF6103",bd=4,relief=GROOVE,fg="white",command=update_data,cursor="hand2")
    btnsupprACT.place(x=680,y=300,width=200,height=40)

    btnsmodifie=Button(win1,text="Delete",font=("times new roman",16),bg="#FF6103",bd=4,relief=GROOVE,fg="white",command=suprime,cursor="hand2")
    btnsmodifie.place(x=950,y=300,width=200,height=40)

    btnexitt=Button(win1,text="EXIT ~ >",font=("times new roman",16),bg="white",fg="#FF6103",bd=0,command=win1.quit)
    btnexitt.place(x=1170,y=600,width=100,height=40)

def page2():
       win2=Toplevel()
       win2.title("Restaurant Management")
       win2.geometry("1600x800")
       win2.configure(bg="white")
       img= PhotoImage(file=r"C:\Users\Hp\OneDrive\Bureau\projet_python\icon-tajin.png")
       win2.iconphoto(False,img)


       style2 = ttk.Style()
       style2.theme_use('clam')
      # change selected color
       style2.map('Treeview',background=[('selected',"#F4A460")])

       def ajouter():
          Nom_client = txtclient.get()
          Numero_table = txttable.get()
          Num_Tele = txttele.get()
          Date_time = txtReservation.get()
          Nombre_de_personnes = txtchaise.get()
          table.insert('','end',values=(Nom_client,Numero_table,Num_Tele,Date_time,Nombre_de_personnes,Nombre_de_personnes))

          txttable.delete(0,END)
          txtclient.delete(0,END)
          txttele.delete(0,END)
          txtReservation.delete(0,END)  
          txtchaise.delete(0,END)

          connection = mysql.connector.connect(host='localhost',user='root',password='Loutfi@123@',port='3306',database='resto')
          c= connection.cursor()
         #  Numero_table = txttable.get()
         #  Nom_client = txtclient.get()
         #  Num_Tele = txttele.get()
         #  Date_time = txtReservation.get()
         #  Nombre_de_personnes = txtchaise.get()
          insert_query = "INSERT INTO reservation ( Nom_client, Numero_table , Num_tele ,Date_time,Nombre_per)VALUES(%s,%s,%s,%s,%s)"
          vals= (Nom_client,Numero_table,Num_Tele,Date_time,Nombre_de_personnes)
          c.execute(insert_query,vals)
          messagebox.showinfo("Confirmation", "La commande a été mise à jour avec succès.")
          connection.commit()

       def suprime():
             selected_item = table.selection()[0]
             table.delete(selected_item)

             connection = mysql.connector.connect(host='localhost',user='root',password='Loutfi@123@',port='3306',database='resto')
             c= connection.cursor()
             Nom_client = txtclient.get()
            #  Numero_table = txttable.get()
            #  Num_Tele = txttele.get()
            #  Date_time = txtReservation.get()
            #  Nombre_de_personnes = txtchaise.get()
       
             update_query = "DELETE FROM reservation WHERE Nom_client = %s"
            #  vals= (Nom_client)
             c.execute(update_query,(Nom_client,))
             messagebox.showinfo("Confirmation", "La commande a été mise à jour avec succès.")
             connection.commit()

       def update_data():
          connection = mysql.connector.connect(host='localhost',user='root',password='Loutfi@123@',port='3306',database='resto')
          c= connection.cursor()
          Numero_table = txttable.get()
          Nom_client = txtclient.get()
          Num_Tele = txttele.get()
          Date_time = txtReservation.get()
          Nombre_de_personnes = txtchaise.get()
       
          update_query = "UPDATE reservation SET Nom_client=%s, Numero_table=%s , Num_tele=%s ,Date_time=%s,Nombre_per=%s WHERE Nom_client=%s"
          vals= (Nom_client,Numero_table,Num_Tele,Date_time,Nombre_de_personnes,Nom_client)
          c.execute(update_query,vals)
          messagebox.showinfo("Confirmation", "La commande a été mise à jour avec succès.")
          connection.commit()

       lbltitre = Label( win2,bd=10, relief=RIDGE, text="Restaurant Management Systeme" ,font=("Vivaldi",40), bg="#FF6103" ,fg="white")
       lbltitre.place(x=0,y=0,width=1275,height=85)
       lbltitrefor = Label(win2,text="Formulaire D'enregistrement De Réservation",font=("times new roman",23),background="white",fg="#8A360F")
       lbltitrefor.place (x=400,y=150)

       client=Label(win2,text="Nom de client :",font=("times new roman",14),background="white",fg="#8A360F")
       client.place (x=75,y=250)
       txtclient=Entry(win2,bd=3,width=30)
       txtclient.place(x=270,y=250)

       numtable=Label(win2,text="Numero Table :",font=("times new roman",14),background="white",fg="#8A360F")
       numtable.place (x=75,y=300)
       txttable=Entry(win2,bd=3,width=30)
       txttable.place(x=270,y=300)


       numtele=Label(win2,text="Numero Tele :",font=("times new roman",14),background="white",fg="#8A360F")
       numtele.place (x=75,y=350)
       txttele=Entry(win2,bd=3,width=30)
       txttele.place(x=270,y=350)


       dateReservation=Label(win2,text="Date de Reservation :",font=("times new roman",14),background="white",fg="#8A360F")
       dateReservation.place (x=55,y=400)
       txtReservation=Entry(win2,bd=3,width=30)
       txtReservation.place(x=270,y=400)


       chaise=Label(win2,text="Nombre de Personnes :",font=("times new roman",14) ,background="white",fg="#8A360F")
       chaise.place(x=50,y=450)
       txtchaise=Entry(win2,bd=3,width=30)
       txtchaise.place(x=270,y=450)

       btnenregistrertable=Button(win2,text="Enregistrer",font=("times new roman",16),bg="#FF6103",bd=4,relief=GROOVE,fg="white",command=ajouter,cursor="hand2") 
       btnenregistrertable.place(x=270,y=530,width=200,height=40)

       btnsupprimertable=Button(win2,text="Delete",font=("times new roman",16),bg="#FF6103",bd=4,relief=GROOVE,fg="white",command=suprime,cursor="hand2")
       btnsupprimertable.place(x=505,y=530,width=200,height=40)

   
       btnsmodifie=Button(win2,text="Update",font=("times new roman",16),bg="#FF6103",bd=4,relief=GROOVE,fg="white",command=update_data,cursor="hand2")
       btnsmodifie.place(x=740,y=530,width=200,height=40)

       btnexitt=Button(win2,text="EXIT ~ >",font=("times new roman",16),bg="white",fg="#FF6103",bd=0,command=win2.quit)
       btnexitt.place(x=1105,y=600,width=150,height=30)

      

       table = ttk.Treeview(win2,columns=(1,2,3,4,5),height=10, show="headings",cursor="hand2")
       table.place(x=540,y=250,width=690,height=230)
       
       
       

       
       table.heading(1,text="Nom_client")
       table.heading(2,text="Numero_table")
       table.heading(3,text="Num_Tele")
       table.heading(4,text="Date_time")
       table.heading(5,text="Nombe_de_personnes")

       table.column(1,width=30,anchor=CENTER)
       table.column(2,width=30,anchor=CENTER)
       table.column(3,width=30,anchor=CENTER)
       table.column(4,width=30,anchor=CENTER)
       table.column(5,width=30,anchor=CENTER)

       connection = mysql.connector.connect(host='localhost',user='root',password='Loutfi@123@',port='3306',database='resto')
       c= connection.cursor()
       c.execute('select * from reservation')
       reservation = c.fetchall()
       for res in reservation:
           table.insert ('','end',value =(res[0],res[1],res[2],res[3],res[4]) )
  


#ajouter le titre
lbltitre = Label( root,bd=0, relief=RIDGE, text="Welcome To My Restaurant" ,font=("Vivaldi",70),fg="white",bg="#FF6103")
lbltitre.place(x=100,y=100,width=1090,height=85)

btncom=Button(root,text="Commande",font=("times new roman",16),bg="white",fg="#8A360F",command=page1,cursor="hand2")
btncom.place(x=440,y=200,width=180,height=30)

btnrese=Button(root,text="Reservation",font=("times new roman",16),bg="white",fg="#8A360F",command=page2,cursor="hand2")
btnrese.place(x=650,y=200,width=180,height=30)


root.mainloop()