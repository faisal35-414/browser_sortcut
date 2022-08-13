
name = input("What's your name?\n")

if name == "faisal":
    print("Welcome " + name + ", select your option")


    i = 0
  
 # Using while loop
    while True:
        if i==100:
            break
        print("""
        1. Github
        2. Email
        3. Facebook
        4. Youtube
        5. exit """)
        
        number = input()
    
        if number == "1":
            print("Open git")
    
            import webbrowser
            get_url= webbrowser.open('https://github.com/')


        elif number == "2":
            print("Open Email")
    
            import webbrowser
            get_url= webbrowser.open('https://mail.google.com/')


        elif number == "3":
            print("Open facebook")
            
            import webbrowser
            get_url= webbrowser.open('https://www.facebook.com/')

        elif number == "4":
            print("Open youtube")
    
            import webbrowser
            get_url= webbrowser.open('https://www.youtube.com/')
 
        elif number == "5":
            break

        else : 
            print("Please write right word")

    i += 1
else :
    print("Please write right name")


    
