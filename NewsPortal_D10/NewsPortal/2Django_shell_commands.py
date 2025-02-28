#--------импорт модулей----------------

from django.contrib.auth.models import User
from news.models import *
from datetime import datetime
from posts_text import *


#--------создание объектов User-------------

user1 = User.objects.create_user(username = 'Иванов')
user2 = User.objects.create_user(username = 'Петров')


#--------создание объектов Author-------------

author1 = Author.objects.create(author_user = user1)
author2 = Author.objects.create(author_user = user2)


#--------создание объектов Category-------------

category1 = Category.objects.create(category_name = 'Спорт')
category2 = Category.objects.create(category_name = 'Техника')
category3 = Category.objects.create(category_name = 'ИТ')
category4 = Category.objects.create(category_name = 'Авто')


#--------создание объектов Post-------------

#---post1 (article) from author1
post1 = Post.objects.create(post_author = author1, post_type = 'ART', post_title = post1_title, post_text = post1_text)
post1.post_category.set([category2,category4])

#---post2 (article) from author2
post2 = Post.objects.create(post_author = author2, post_type = 'ART', post_title = post2_title, post_text = post2_text)
post2.post_category.set([category3,category4])

#---post3 (news) from author2
post3 = Post.objects.create(post_author = author2, post_type = 'NEW', post_title = post3_title, post_text = post3_text)
post3.post_category.set([category1,category4])


#--------создание объектов Comment-------------

#---comment1 for (post1, author1) from user2
comment1 = Comment.objects.create(comment_post = post1, comment_user = user2, comment_text = 'Like')

#---comment2 for (post2, author2) from user1
comment2 = Comment.objects.create(comment_post = post2, comment_user = user1, comment_text = 'Like')

#---comment3 for (post2, author2) from user1
comment3 = Comment.objects.create(comment_post = post2, comment_user = user1, comment_text = 'Like2')

#---comment4 for (post3, author2) from user1
comment4 = Comment.objects.create(comment_post = post3, comment_user = user1, comment_text = 'Like')


#--------Корректировка рейтингов-------------

post1.like()
post1.like()
post1.like()
post1.like()
post1.like()

post2.like()
post2.like()

post3.like()
post3.like()
post3.dislike()

comment1.like()
comment2.like()
comment3.like()
comment4.like()


#--------Обновление рейтингов-------------

author1.update_rating()
author2.update_rating()

#--------Вывод лучшего автора-------------

ba = Author.objects.order_by('-author_rating').first()
bu = User.objects.get(author = ba)
print('Лучший автор: ', bu.username, ', рейтинг: ', ba.author_rating)

#--------Вывод лучшей статьи-------------

bp = Post.objects.order_by('-post_rating').first()
print('Лучшая статья','\nДата: ',bp.post_time.strftime("%Y-%m-%d %H:%M:%S"),
      '\nАвтор:', User.objects.get(author = bp.post_author).username,
      '\nРейтинг статьи: ', bp.post_rating, '\nЗаголовок: ', bp.post_title,
      '\nПревью: ', bp.preview())


#--------Вывод комментариев-------------
print('Комментарии')
for c in Comment.objects.filter(comment_post = bp):
    print('\nДата: ',c.comment_time.strftime("%Y-%m-%d %H:%M:%S"),
          '\nПользователь:', c.comment_user,'\nРейтинг:', c.comment_rating,
          '\nТекст:', c.comment_text)
