#!/usr/bin/env python
# -*-coding:utf-8 -*-
# __author__ = 'jiang'

from qiniu import Auth, put_file, etag
import qiniu.config

access_key = 'vlSHnQer2_XLm3NyZeQ5-GhiymkMjmkSnHIAlEO5'
secret_key = 'KZPRrzZMROt9oFIu-V13yBZnxMbFNZ0kf2yqL9ud'

q = Auth(access_key, secret_key)

bucket_name = 'zyouzz'

key = 'my-python-logo2.png';

#上传文件到七牛后， 七牛将文件名和文件大小回调给业务服务器。
# policy={
#  'callbackUrl':'http://your.domain.com/callback.php',
#  'callbackBody':'filename=$(fname)&filesize=$(fsize)'
#  }

token = q.upload_token(bucket_name, key, 3600)

localfile = 'http://101.201.40.144:81/uploads/article/20170414/3110c949c60880453f14cbe49ce0ba53.png'

ret, info = put_file(token, key, localfile)
print(info)
assert ret['key'] == key
assert ret['hash'] == etag(localfile)

