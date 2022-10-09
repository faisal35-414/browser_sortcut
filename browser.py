import webbrowser
name = input("What's your name?\n")

if name == "faisal":
    print("Welcome " + name + ", select your option")

    f = 0
 
 # Using while loop
    while True:
        if f==100:
            print("Time out")
            break

        print("""
        1. Github
        2. Email
        3. Facebook
        4. Youtube
        5. Google classroom
        6. Student portal
        7. Linkedin
        8. Whatsapp
        9. Noureldinehab
        10. Udemy
        e. exit """)
        
        number = input()
    
        if number == "1":
            print("Open git")
            get_url= webbrowser.open('https://github.com/')

        elif number == "2":
            print("Open Email")
            get_url= webbrowser.open('https://mail.google.com/')

        elif number == "3":
            print("Open facebook")
            get_url= webbrowser.open('https://www.facebook.com/')

        elif number == "4":
            print("Open youtube")
            get_url= webbrowser.open('https://www.youtube.com/')
 
        elif number == "5":
            print("Open classroom")
            get_url= webbrowser.open('https://classroom.google.com/')
        
        elif number == "6":
            print("Open studentportal")
            get_url= webbrowser.open('http://studentportal.diu.edu.bd/#/dashboard1')
        
        elif number == "7":
            print("Open linkedin")
            get_url= webbrowser.open('https://www.linkedin.com/feed/')

        elif number == "8":
            print("Open whatsapp")
            get_url= webbrowser.open('https://web.whatsapp.com/')   

        elif number == "9":
            print("Open noureldinehab")
            get_url= webbrowser.open('https://noureldinehab.medium.com/')  

        elif number == "10":
            print("Open udemy")
            get_url= webbrowser.open('https://www.udemy.com/')

        elif number == "e":
            break

        else : 
            print("Please write right word")

    f += 1
else :
    print("Please write right name")
