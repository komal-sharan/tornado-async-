#!/usr/bin/env python
import time
from tornado import gen
from tornado.ioloop import IOLoop
from tornado.httpclient import AsyncHTTPClient
from tornado.gen import sleep

@gen.coroutine
def some_task(g):
        g=g-1
        yield fetch_task(g)
        
@gen.coroutine
def fetch_task(g):
   
   g=yield some_task(g)
   g=g-1
   yield blocking()     
   if(g==0):
        print('fetch_task finished')

@gen.coroutine
def blocking():
   start_time = time.time()
   counter = 1
   while True:
       time.sleep(2)
       print('blocking for %f' % (time.time() - start_time))
       yield gen.moment
       print('gen.moment counter %d' % counter)
       counter += 1

@gen.coroutine
def main(g):
   fetch_task(g)
   
   
g=10
IOLoop.instance().run_sync(lambda:main(g))
