import requests
import json
def store(filename,url):
    f=open(filename,"w")
    json.dump(url,f,indent=4)
    return f
def store1(filename,url):
    f=open(filename,"w")
    json.dump(url,f,indent=4)
    return f
def slug(filename,url):
    f=open(filename,"w")
    json.dump(url,f,indent=4)
    return f
def options(b1,user,b,res1):
    x=user
    while True:
        opt1=input("enter a option next or up or back:")
        if opt1=="next":
            req1=requests.get("http://saral.navgurukul.org/api/courses/"+str(b1)+"/exercise/getBySlug?slug="+str(b[x]))
            r=req1.json()
            #slug1=slug("slug.json",r)
            print("content:",r["content"])
            x=x+1
        elif opt1=="up":
            req1=requests.get("http://saral.navgurukul.org/api/courses/"+str(b1)+"/exercise/getBySlug?slug="+str(b[x-2]))
            r=req1.json()
            slug1=slug("slug.json",r)
            print("content:",r["content"])
            x=x-1
        elif opt1=="back":
            b=[]
            c1=1
            for parent in res1["data"]:
                print(c1,parent["name"])
                b.append(parent["slug"])
                c1=c1+1
                for child in parent["childExercises"]:
                    print("        ",c1,"C_E_N:",child["name"])
                    b.append(child["slug"])
                    c1=c1+1
        elif opt1=="quit":
            break
def reqest_1():
    result=requests.get("https://saral.navgurukul.org/api/courses")
    a=result.json()
    s_t1=store("req.json",a)
    c=1
    for course in a["availableCourses"]:
        print(c,course["name"],course["id"])
        c=c+1
    select_course=int(input("select ur course no...:"))
    print("course-Name:",a["availableCourses"][select_course-1]["name"])
    b1=a["availableCourses"][select_course-1]["id"]
    res=requests.get("http://saral.navgurukul.org/api/courses/"+str(b1)+"/exercises" )
    res1=res.json()
    s_t=store1("req2.json",res1)
    print("the below excersise names are belogns to above couser_name")
    b=[]
    c1=1
    for parent in res1["data"]:
        print(c1,parent["name"])
        b.append(parent["slug"])
        c1=c1+1
        for child in parent["childExercises"]:
            print("        ",c1,"C_E_N:",child["name"])
            b.append(child["slug"])
            c1=c1+1
    user=int(input("enter a slug no:"))
    req1=requests.get("http://saral.navgurukul.org/api/courses/"+str(b1)+"/exercise/getBySlug?slug="+str(b[user-1]))
    r=req1.json()
    slug1=slug("slug.json",r)
    print("content:",r["content"])
    opt=options(b1,user,b,res1)




    
    
            
        



    
reqest_1()




