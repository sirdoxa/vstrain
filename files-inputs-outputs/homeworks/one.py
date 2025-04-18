import re

while True:
    x = input('1)text:\n2)exit and show text:\n3)show word count:\n==> ')
    if x == '1':
        with open('one.txt','a') as f:
            f.write(input('enter your text: ') + '\n')
            
    elif x == '2':
        with open('one.txt','r') as o:
            for line in o:
                print(line.strip())

        print('\ngood luck!!')
        break
    elif x == '3':
        # شمارش کلمات بدون استفاده از فانکشن
        word_count = {}
        with open('one.txt', 'r') as f:
            text = f.read().lower()  # همه رو کوچیک کن

            # استخراج کلمات با استفاده از regular expression
            words = re.findall(r'\w+', text)

            for word in words:
                word_count[word] = word_count.get(word, 0) + 1

        print('\n==> Word count:')
        for word, count in word_count.items():
            print(f'{word}: {count}')
            print(12 * '*')
        
    else:
        print((4 * '*******')+'\nwrong choice! enter carefully\n'+(4 * '*******'))





