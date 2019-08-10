#TASK-1





#TASK-2
n=[{'model': 'auth_api.user', 'pk': 199, 'fields': {'password':
'pbkdf2_sha256$120000$ZWsTOyx6pAdj$o2YzlAyLus5dCXKc6wyYTSQcTFU8oNRP54kwE6lOfys=',
'last_login': None, 'is_superuser': False, 'username': 'price', 'first_name': '', 'last_name': '', 'email':
'prfe@price.com', 'is_staff': False, 'is_active': True, 'date_joined': '2019-05-09T07:00:47.721Z',
'user_type': 'Admin', 'company_name': None, 'phone_num': None, 'Des': None, 'owner': None, 'plan':
None, 'groups': [], 'user_permissions': []}},
{'model': 'auth_api.user', 'pk': 200, 'fields': {'password':
'pbkdf2_sha256$120000$ZWsTOyx6pAdj$o2YzlAyLus5dCXKc6wyYTSQcTFU8oNRP54kwE6lOfys=',
'last_login': None, 'is_superuser': False, 'username': 'price', 'first_name': '', 'last_name': '', 'email':
'prfe@price.com', 'is_staff': False, 'is_active': True, 'date_joined': '2019-05-09T07:00:47.721Z',
'user_type': 'Admin', 'company_name': None, 'phone_num': None, 'Des': None, 'owner': None, 'plan':
None, 'groups': [], 'user_permissions': []}}, {'model': 'auth_api.user', 'pk': 199, 'fields': {'password':
'pbkdf2_sha256$120000$ZWsTOyx6pAdj$o2YzlAyLus5dCXKc6wyYTSQcTFU8oNRP54kwE6lOfys=',
'last_login': None, 'is_superuser': False, 'username': 'price', 'first_name': '', 'last_name': '', 'email':
'prfe@price.com', 'is_staff': False, 'is_active': True, 'date_joined': '2019-05-09T07:00:47.721Z',
'user_type': 'Admin', 'company_name': None, 'phone_num': None, 'Des': None, 'owner': None, 'plan':
None, 'groups': [], 'user_permissions': []}},
{'model': 'auth_api.user', 'pk': 201, 'fields': {'password':
'pbkdf2_sha256$120000$ZWsTOyx6pAdj$o2YzlAyLus5dCXKc6wyYTSQcTFU8oNRP54kwE6lOfys=',
'last_login': None, 'is_superuser': False, 'username': 'price', 'first_name': '', 'last_name': '', 'email':
'prfe@price.com', 'is_staff': False, 'is_active': True, 'date_joined': None, 'Des': None, 'owner': None,
'plan': None, 'groups': [], 'user_permissions': []}}]
print([i for x, i in enumerate(n) if i not in n[x + 1:]])
#TASK-3
#Q1
import datetime
d=datetime.date(2019, 5, 8)
tdelta = datetime.timedelta(days=1)
print(d + tdelta)

#Q2
import datetime
d=datetime.date(2019, 5, 8)
print(d)
d=datetime.date(2019, 5, 9)

print(d.strftime("%d/%m/%y"))

#Q3
def leapyear(year):
    if (year%4==0):
        if (year%100==0):
            if (year%400==0):
                print('leap year:')
            else:
                print('Not leap year:')
        else:
            print('leap year:')
    else:
        print('not a leap year:')
year=int(input('enter a year:'))
leapyear(year)
# your all date are not a leap year:

#Q4
import datetime
d=datetime.date(2019, 12, 31)
tdelta = datetime.timedelta(days=1)
print(d + tdelta)












