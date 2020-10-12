#!/usr/bin/python3
# coding:utf-8
##
#  Ecriture dans fichier "guestbook.html"
#  Paramèes reç par méode POST
#

import cgi, cgitb , datetime, os

# Lecture des donné formulaire
form = cgi.FieldStorage() 
xnom = form.getvalue('nom')
xprenom  = form.getvalue('prenom')
xemail = form.getvalue('email')
xcomment = form.getvalue('comment')
xip = ""
for key in os.environ.keys():
	if key == "REMOTE_ADDR":
		xip =os.environ[key]
# Création du fichier si n'existe pas et ouverture en mode append 
gb = open("/home/ginf2021/melmimouni/public_html/message.html", "a")
v = open("/home/ginf2021/melmimouni/public_html/nbrvisiteur.txt","r")
t =  str(v.read())
v.close()
v = open("/home/ginf2021/melmimouni/public_html/nbrvisiteur.txt","w+")
nbr = int(t)
nbr = nbr + 1
v.write(str(nbr))
# Ecriture des informations dans le fichier avec balisage HTML
gb.write('<div> <hr />')
gb.write ("<p><em>Post numero"+str(nbr)+" le</em>: "+str(datetime.date.today())+"<br />\n")
gb.write ("<em>Nom </em>: <strong>"+str(xnom)+"<br />")
gb.write ("<em>Email </em>: "+str(xemail)+"</p>\n")
gb.write("<em>Message </em>:")
gb.write("<blockquote>")
gb.write (str(xcomment)+"</blockquote>")
gb.write("<em>Connecte a partir de</em>: "+str(xip)+"<br/>")
gb.close()
print ("Content-type: text/plain")
print()
print ("Vous etes le ")
print (nbr)
print("e signataire de mon livre d'or")








