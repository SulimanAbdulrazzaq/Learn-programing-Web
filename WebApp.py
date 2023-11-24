import pywebio
from pywebio.output import *
from pywebio.input import *
from pywebio.session import *
from pywebio.pin import *
import webbrowser
import os
import sqlite3
import datetime
def App():
    db = sqlite3.connect("WebCustmors1.db")
    cr = db.cursor()
    cr.execute("CREATE TABLE if not exists WebApp( name text,email text,PhoneNumber int,password int)")
            
    popup(" افضل موقع لتعلم البرمجة ",
        put_text("اظغت هنا لتعرف كم عدد المشتركين").style("color:blue").onclick(lambda:toast("عدد المشتركين في الموقع 1000 مشترك"))
    )
    put_html("<center><h3> نظام التسجيل في الموقع المتعدد الخدمات</h3><img src=https://www.iconpacks.net/icons/2/free-user-icon-3296-thumb.png width=250></center>")
    put_html("<h3><marquee>اهلا وسهلا بكم في موقع كوديف نجلب لك الكورسات مكان ما انت جالس</marquee></h3>").style("background:#00005C;padding:25px;color:gold")
    def SignUp():
            
            def check_password(Data):
                if len(Data["pass"])<5:
                    return("pass","Sorry too short")

            Data = input_group("ادخل بياناتك",
                            [
                                input("اسم المشترك",name="name"),
                                input("ادخل رقم الهاتف خاصتك",type="number",name="PhoneNumber"),
                                input("ادخل البريد الالكتروني",name="email"),
                                input("ادخل كلمة المرور الخاصة بك",type="password",name="pass"),
                                checkbox('لغات البرمجة التي تعرفها',options = ["python","javascript","c++","c","java","HTML,CSS","C#"],inline=True,name="lan"),
                                checkbox('اللغات التي تعرفها',options=["Arabic","English","Spain","France"],inline=True,name="lan2"),
                            ],validate=check_password
                            )
            
            import sqlite3


                    
                    
            db = sqlite3.connect("WebCustmors1.db")
            cr = db.cursor()
            cr.execute("CREATE TABLE if not exists WebApp(name text,email text,PhoneNumber int,password int)")
            cr.execute(f"insert into WebApp(name,email,PhoneNumber,password) values({Data['name']!r},{Data['email']!r} ,{Data['PhoneNumber']!r},{Data['pass']!r})")
            cr.execute('Select email,password FROM WebApp WHERE email=? and password=?', (email, password))
            result = cr.fetchone()
                    
                    



            

            db.commit()
            db.close()
            
            if "@" and ".com" not in Data["email"]:
                put_text("Sorry Invalid email")
                put_text("Refresh the page to do email agin")
            else:
                
                
                def toGo():
                    
                            img = file_upload("حمل صورتك",
                                "images/*")

                        
                    
                    
                            
                            put_text("ولكن قبل الاشتراك في الموقع سيكون هناك سوألين لتشترك")

                            data1=radio("في اي من المكاتب التالية في بايثون تستخدم في تطوير الويب",
                                        options=["tkinter","Pywebio","TensorFlow"])

                            if data1== "Pywebio" :
                                put_text("Correct")
                                data2=radio("اي من اللغات تفضل",
                                        options=["Python","javaScript","C++"])
                            
                            
                                    
                                def d2():
                                    webbrowser.open("https://docs.python.org/3/")
                                if img:
                                    put_image(img["content"],title= img["filename"]).style("margin-center:50px")
                                # put_text("Email:",Data["email"])
                                # put_text("Password:",Data["pass"])
                                
                                def Python():
                                    webbrowser.open("https://www.youtube.com/watch?v=smKHKgedkP4&ab_channel=%D8%B1%D8%A7%D9%83%D9%88%D8%A7%D9%86%D9%84%D9%84%D8%A8%D8%B1%D9%85%D8%AC%D8%A9-CodeRK")
                                if data2 == "Python":
                                    put_button("You love python So Click me to go to python docs",
                                            onclick=d2)
                                
                                put_button("Click me to open Python course",onclick=Python)
                                def C():
                                    webbrowser.open("https://www.youtube.com/watch?v=M_DD16C2C64&ab_channel=%D8%B1%D8%A7%D9%83%D9%88%D8%A7%D9%86%D9%84%D9%84%D8%A8%D8%B1%D9%85%D8%AC%D8%A9-CodeRK")

                                put_button("Click me to open C++ course",onclick=C)
                                def java():
                                    webbrowser.open("https://www.youtube.com/watch?v=e-a7OiTmA64&ab_channel=%D8%B1%D8%A7%D9%83%D9%88%D8%A7%D9%86%D9%84%D9%84%D8%A8%D8%B1%D9%85%D8%AC%D8%A9-CodeRK")
                                put_button("Click me to open Java course",onclick=java)
                                def C1():
                                    webbrowser.open("https://www.youtube.com/watch?v=ELglVujXcNQ&ab_channel=%D8%B1%D8%A7%D9%83%D9%88%D8%A7%D9%86%D9%84%D9%84%D8%A8%D8%B1%D9%85%D8%AC%D8%A9-CodeRK")
                                put_button("Click me to open C# course",onclick=C1)
                                def php():
                                    webbrowser.open("https://www.youtube.com/watch?v=Lf406ZnxvQg&ab_channel=%D8%B1%D8%A7%D9%83%D9%88%D8%A7%D9%86%D9%84%D9%84%D8%A8%D8%B1%D9%85%D8%AC%D8%A9-CodeRK")
                                put_button("Click me to open php course",onclick=php)
                            if data1!= "Pywebio":
                                put_html("<h3><marquee>Sorry incorrect we cannot help you</marquee></h3>")
                                def close():
                                    os.system("taskkill /im chrome.exe /f")
                                put_button("Close",onclick=close)
                            
            put_button(" اذا تريد الكورسات المجانية اضغط هنا",onclick=toGo)
            

            



    def folog():
                        def d2():
                            webbrowser.open("https://docs.python.org/3/")

                        # put_text("Email:",Data["email"])
                        # put_text("Password:",Data["pass"])
                        
                        def Python():
                            webbrowser.open("https://www.youtube.com/watch?v=smKHKgedkP4&ab_channel=%D8%B1%D8%A7%D9%83%D9%88%D8%A7%D9%86%D9%84%D9%84%D8%A8%D8%B1%D9%85%D8%AC%D8%A9-CodeRK")
                            
                        put_button("You love python So Click me to go to python docs",
                                    onclick=d2)
                        
                        put_button("Click me to open Python course",onclick=Python)
                        def C():
                            webbrowser.open("https://www.youtube.com/watch?v=M_DD16C2C64&ab_channel=%D8%B1%D8%A7%D9%83%D9%88%D8%A7%D9%86%D9%84%D9%84%D8%A8%D8%B1%D9%85%D8%AC%D8%A9-CodeRK")

                        put_button("Click me to open C++ course",onclick=C)
                        def java():
                            webbrowser.open("https://www.youtube.com/watch?v=e-a7OiTmA64&ab_channel=%D8%B1%D8%A7%D9%83%D9%88%D8%A7%D9%86%D9%84%D9%84%D8%A8%D8%B1%D9%85%D8%AC%D8%A9-CodeRK")
                        put_button("Click me to open Java course",onclick=java)
                        def C1():
                            webbrowser.open("https://www.youtube.com/watch?v=ELglVujXcNQ&ab_channel=%D8%B1%D8%A7%D9%83%D9%88%D8%A7%D9%86%D9%84%D9%84%D8%A8%D8%B1%D9%85%D8%AC%D8%A9-CodeRK")
                        put_button("Click me to open C# course",onclick=C1)
                        def php():
                            webbrowser.open("https://www.youtube.com/watch?v=Lf406ZnxvQg&ab_channel=%D8%B1%D8%A7%D9%83%D9%88%D8%A7%D9%86%D9%84%D9%84%D8%A8%D8%B1%D9%85%D8%AC%D8%A9-CodeRK")
                        put_button("Click me to open php course",onclick=php)
                        
                        def close():
                            os.system("taskkill /im chrome.exe /f")
                        put_button("Close",onclick=close)
        

        
    
    Data2 = input_group("تسجيل دخول",
                        [
                            input("ادخل الايميل ",name='email'),
                            input("ادخل كلمة المرور الخاصة بك",type=PASSWORD,name='pwd')
                        ])
    email = Data2['email']
    password =Data2['pwd']

    db = sqlite3.connect("WebCustmors1.db")
    cr = db.cursor()
    cr.execute('Select email,password FROM WebApp WHERE email=? and password=? ', (email, password))
    result = cr.fetchone()
    if result :
        put_button("To go to courses",onclick=folog)
    else:
        put_text("Invalid email")
        put_button("SignUp",onclick=SignUp)
    

v = "LearnProgramingInArabic"
pywebio.start_server(App,port=1111,debug=True)

