#!/usr/bin/env python
# -*- coding: utf8 -*-

import time
import sys, getopt
from pymongo import MongoClient

kid = 306537937891354

mongo_url = 'mongodb://curriculum:banyu2017@10.106.74.21:26047/curriculum'
conn = MongoClient(mongo_url)
db = conn.curriculum

# 获取第n节课的secid
def get_classroom_info(idx):
    coll = db.curriculum_classroom_info
    cond = {'kid':kid, 'idx':int(idx), 'ver':4, 'enable':True}
    return list(coll.find(cond))

def set_progress(uid, classroom_info):
    coll = db.curriculum_classroom_secidx
    cond = {'kid':kid, 'uid':int(uid)}
    new_data = {
        'secid':classroom_info['secid'],
        'level':classroom_info['level'],
        'idx':classroom_info['idx'],
        'ver':classroom_info['ver'],
        'ltype':classroom_info['ltype'],
        'ut':int(time.time())
    }
    update = {'$set': new_data}
    coll.update(cond, update, True, False)

def main(argv):
    uids = ''
    idx = ''
    try:
        opts, args = getopt.getopt(argv,"hu:i:",["uids=","idx="])
    except getopt.GetoptError:
        print 'set_interactive_class_progress.py -uids <uids> -idx <idx>'
        sys.exit(2)
    for opt, arg in opts:
        if opt in ("-u", "--uids"):
            uids = arg
        elif opt in ("-i", "--idx"):
            idx = arg
    infos = get_classroom_info(idx)
    if not infos:
        print '此课节不存在，请重新选择课节序号'
    uids = uids.split(',')
    info = infos[0]
    for uid in uids:
        set_progress(uid, info)
    print '互动绘本课进度设置完成'

if __name__ == '__main__':
    main(sys.argv[1:])