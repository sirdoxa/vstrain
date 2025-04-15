'''
't' = text file
'b' = binary file
'r' (rt) ==>  اشاره گر در ابتدای فایله و فایل متنی عه و برای خواندنه و درصورت عدم وجود خطا میده
'w' (wt) ==> برای نوشتن و محتوای قبلی پاک میشه اشاره گر در ابتدای فایل و اگر فایل نباشد اول ایجاد و سپس باز میشود
'a' (at) ==> برای نوشتن در انتهای فایل و نشانه گر در انتهای فایل و اگر فایل نباشد اول ایجاد و سپس باز میشود
'x' (xt) ==>  اشاره گر در ابتدای فایله و فایل متنی عه و برای خواندنه و درصورت وجود خطا میده
'rb' , 'wb' , 'ab' , 'xb'
'r+' (r+t , rt+) ==> برای خواندن و نوشتن ، درصورت عدم وجود فایل خطا
'w+' (w+t , wt+) ==> برای خواندن و نوشتن ، متن قبلی پاک میشه
'a+' (a+t , at+) ==> برای خواندن و نوشتن و از انتهای فایل مینویسه
'x+' (x+t , xt+) ==> درصورت وجود فایل خطا ، برای خواندن و نوشتن
'rb+' , 'wb+' , 'ab+' , 'xb+'

'''
# f = open('new.txt','r')    

# print(f.readline())
# print(f.readline())
# f = open('w-test.txt','w')   
# print(f.write('mahdi')) 

# f = open('w-test.txt','a')   
# print(f.write('\nnabavi')) 
# print(f.write('\npython')) 
# print(f.readline())

# x = open('new.txt','a',encoding='utf-8')

# print(x.write('🂮'))

# o = open('note.txt','ab')
# s = bytes('🂢 🂣 🂤 🂥 🂦 🂧 🂨 🂩 🂪 🂫','utf-8')
# print(o.write(s))

# import os
# f = open('mahdi.txt','a')
# f.write('mahdi\n')
# f.flush()
# os.fsync(f)
# f.write('taha\n')
# input('x: ')
# f.close()

# import io
# print(io.DEFAULT_BUFFER_SIZE)



# POINTER
# 0 ==> ابتدای فایل
# 1 ==> موقعیت فعلی فایل
# 2 ==> انتهای فایل



f = open('main.txt','rb')

print(f.tell())
print(f.read(3))
f.seek(2,1)
print(f.tell())
print(f.read(5))




