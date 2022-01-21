class Post:
    id = ''
    title = ''
    author = ''
    content = ''

post1 = Post()

post1.id = '그냥 아이디'
post1.title = '게시글'
post1.author = '윤소현'
post1.content = '파이썬 클래스 이용한 숙제'

print(post1)
print('<게시글>')
print('id :',post1.id)
print('title :',post1.title)
print('author :',post1.author)
print('content :',post1.content)
