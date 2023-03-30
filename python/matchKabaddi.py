
'''
در ورودی نمونه داده شده، بازیکنانی که 5 و 4 بازی داشته‌اند، طبق صورت سوال نمی‌توانند در گروهی باشند؛ بنابراین فقط 4 بازیکنی که 0 و 2و 1و 0  بازی داشته‌اند ،می‌توانند در گروه‌ها باشند. با 4 نفر هم تنها می‌توان 1 گروه 3 نفره تشکیل داد. دقت کنید که لازم نیست تعداد حالت‌(جایگشت)هایی را حساب کنید.
input 
6
4 3 5 0 1 2
output
1

6
4 4 5 6 8 9
2
'''

n=int(input())
data_list = [ int(x) for x in input().split() ]
new_list=[] # use list
for i in data_list:
    if i >= 2:
        new_list.append(i)
        data_list = new_list

l=len(new_list)
j= (l//3) # limit team 3 player
print(j)

