# coding: utf-8
import os
from sqlalchemy import create_engine
from phlaskr.models import AppUser,UserProfile,Email,Post,Tag,Comment
from phlaskr.app import application as api
from redis import Redis

print '\n'.join(os.environ.keys())

def convert_uri_to_args(uri):
    if uri is None:
        return False
    trash,remainder = uri.split('://')
    login,host_info = remainder.split('@')
    user,pw = login.split(':')
    host,port = host_info.split(':')
    return dict(
        host=host,
        port=port,
        db=0,
        password=pw
    )

redis_args =\
    os.environ.get('REDISCLOUD_URL') and\
    convert_uri_to_args(
        os.environ.get('REDISCLOUD_URL')
    ) or {}
cache = Redis(
        **redis_args
)
key = os.environ.get('DATABASE_URL')


def start():
    AppUser._engine = create_engine(os.environ.get('DATABASE_URL'),echo=True)
    AppUser.metadata.bind = AppUser._engine

def seed():
    if not cache.get(key):
        cache.set(key,1)

        content = {
            '1':'''
    Wow Youll never Guess !!!

    OMG!!!!
            ''',
            '2':'''
    Sometimes i think about all kinds of things

    I just never know where to start
            ''',
            '3':'''
    This was soooooo
    crazy, Im not sure
    if i beleive it myself.
            ''',
            '4':'''
    
    Now for some real magixc



    !!!!!!!
            '''
        }

        kyle = AppUser.get_new(username='test',password='test')
        email = Email(address='test@test.com',app_user_id=kyle.id,user_type='app')
        email.save()
        tag = Tag.get_new(name='tag')
        post = Post.get_new(title='test post',content='fsfsfwsd',author_id=kyle.id,tags=[tag.id])
        post = Post.get_new(title='test post2',content='fsfsfwsd',author_id=kyle.id,tags=[tag.id])
        post = Post.get_new(title='test post3',content='fsfsfwsd',author_id=kyle.id,tags=[tag.id])
        post = Post.get_new(title='test post4',content='fsfsfwsd',author_id=kyle.id,tags=[tag.id])
        joel = AppUser.get_new(username='admin',password=os.environ.get('ADMIN_PASSWORD'))
        email = Email(address=os.environ.get('ADMIN_EMAIL'),app_user_id=joel.id,user_type='app')
        email.save()
        tag = Tag.get_new(name='tags')
        post = Post.get_new(title='First test post',content=content['1'],author_id=joel.id,tags=[tag.id])
        post = Post.get_new(title='Just my thoughts',content=content['2'],author_id=joel.id,tags=[tag.id])
        post = Post.get_new(title='Some crazy stuff',content=content['3'],author_id=joel.id,tags=[tag.id])
        post = Post.get_new(title='You Wont Beleive This',content=content['4'],author_id=joel.id,tags=[tag.id])

def reset():
    ctx = api.test_request_context()
    ctx.push()
    start()
    AppUser.metadata.create_all(checkfirst=True)
    seed()
    ctx.pop()

if __name__ == "__main__":
    reset()
