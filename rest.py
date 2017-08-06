#!git  python3
# -*- coding: utf-8 -*-

class Chain(object):

    def __init__(self, path='GET'):
        self._path = path

    # 访问属性时触发(path为属性名)、调用方法时触发(path为方法名)
    def __getattr__(self, path):
        print(path)
        return Chain('%s/%s' % (self._path, path))

    # 调用方法时触发
    def __call__(self, attr):
        print(attr)
        return Chain('%s/%s' % (self._path, attr))

    def __str__(self):
        return self._path

    __repr__ = __str__

print(Chain().users('michael').group('student').repos)