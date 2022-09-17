# from datetime import datetime
#
# contacts=[]
# while True:
#     print("Welcome to my Phonebook\nPress 1 to add new contact\nPress 2 to show contacts\nPress 3 to Delete Data \nPress 0 exits program.")
#     ch = input("Enter Your Choise:")
#     if ch=="0":
#         break
#     if ch=="1":
#         count=1
#         if contacts:
#             count =contacts[-1]['id']+1
#         print("New Contact")
#         name =input("Enter Name:")
#
#         mobile =input("Enter Number:")
#
#         date = datetime.today().strftime( "%y-%m-%d" )
#         data={'id':count,'name':name,'mobile':mobile,"Date":date}
#         contacts.append(data)
#     if ch=='2':
#         print("Your Contact list")
#         for c in contacts:
#             print(c)
#
#     if ch=='3':
#         print(contacts)
#         sid=int(input('Enter Id for  delete:'))
#         for c in contacts:
#             if sid==c.get('id'):
#                 c.clear()
#                 print("delete SuccessFully")
#
# print(contacts)
#
#
#












# auth=('neetu12','neetu12')


# import requests
# data ={
#     'username':"neetu12",
#     'password':'neetu12',
#     'email': 'neetu12@gmail.com'
#
# }
# data =requests.post("  http://127.0.0.1:8000/project/api/signup/",data=data)
#
# print(data.text)