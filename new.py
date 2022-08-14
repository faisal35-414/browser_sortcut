name = input("What's ypur name?\n")

print("Welcome " + name + ", select your option")

print("""
      1. Github
      2. Email
      3. Facebook
      4. Youtube""")



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
    print("open facebook")
    
    import webbrowser
    get_url= webbrowser.open('https://www.facebook.com/')

elif number == "4":
    print("open youtube")
    
    import webbrowser
    get_url= webbrowser.open('https://www.youtube.com/')
 


else : 
    print("please write right word")
