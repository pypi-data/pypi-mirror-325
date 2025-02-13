# -*- coding:utf-8 -*-
import os
from nose.tools import assert_equal

from pyconn.wx.wechat import WechatMessage, Token, Wechat


def test_send_msg():
    msg = WechatMessage("7", "liucb", "aa")
    corp_id = ""
    corp_secret = ""
    token = Token(corp_id, corp_secret).get_token()
    ret = Wechat(token).send(msg)
    assert_equal(0, ret['errcode'])


def test_send_file():
    filepath = '/tmp/pyconn_wechat_send_file_test.txt'
    with open(os.path.join('/tmp', filepath), 'w') as file_handle:
        file_handle.write('pyconn wechat send file test.')
    corp_id = ""
    corp_secret = ""
    token = Token(corp_id, corp_secret).get_token()
    ret = Wechat(token).send_file('luoan', filepath)
    assert_equal(0, ret['errcode'])
