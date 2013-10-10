#!/usr/bin/env python                                                           
# http://www.bryceboe.com/2012/02/14/python-multiprocessing-pool-and-keyboardinterrupt-revisited/
# http://www.bryceboe.com/2010/08/26/python-multiprocessing-and-keyboardinterrupt/
import multiprocessing, os, time
 
def do_work(i):
    try:
        print 'Work Started: %d %d' % (os.getpid(), i)
        time.sleep(2)
        return 'Success'
    except KeyboardInterrupt, e:
        pass
 
def main():
    pool = multiprocessing.Pool(3)
    p = pool.map_async(do_work, range(6))
    try:
        results = p.get(0xFFFF)
    except KeyboardInterrupt:
        print 'parent received control-c'
        return
 
    for i in results:
        print i
 
if __name__ == "__main__":
    main()
