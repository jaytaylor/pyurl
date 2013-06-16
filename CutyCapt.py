#!/usr/bin/env python

import time

import Image

try:
    from pyurl import settings
    DEFAULT_WIDTH = getattr(settings, 'PREVIEW_WIDTH', 480)
    from pyurl.killableprocess import call, check_call, CalledProcessError
except ImportError:
    DEFAULT_WIDTH = 480
    from killableprocess import call, check_call, CalledProcessError

#url = 'http://gmail.com'
#dest = '/tmp/image.png'

def cuty_capt(url, dest_lg, dest_sm):
    #command_line = '''xvfb-run --server-args="--server-args=terminate -screen 0, 1024x768x24" CutyCapt --url="%s" --out="%s"''' % (url, dest_lg)
    command_line = '''xvfb-run --server-args=" -screen 0, 1024x768x24" CutyCapt --url="%s" --out="%s"''' % (url, dest_lg)
    #with open('/tmp/test.txt', 'w+') as fh:
    #    fh.write('%s\n' % command_line)
    import shlex, subprocess
    args = shlex.split(command_line)
    #check_call(args, timeout=20)
    try:
        check_call(args, timeout=20)
    except CalledProcessError:
        pass

    #p = subprocess.check_call(args)
    #p = subprocess.Popen(args)
    #timeout = 10
    #waited = 0
    #while True:
    #    time.sleep(1)
    #    waited += 1
    #    retcode = p.Poll()
    #    if retcode:
    #        break
    #    if waited > timeout:
    #        raise Exception('xvfb timeout occurred')
    src_img = Image.open(dest_lg)
    width = DEFAULT_WIDTH
    import math
    height = int(math.floor(src_img.size[1] / (src_img.size[0]/float(width))))
    #height = getattr(settings, 'PREVIEW_HEIGHT', 480)
    #base_name = dest[0:dest.rindex('.')]
    #ext = dest[dest.rindex('.'):]
    resized_img = src_img.resize((width, height), Image.ANTIALIAS)
    #resized_img.save('%s_sm%s' % (base_name, ext))
    resized_img.save(dest_sm)


if __name__ == '__main__':
    cuty_capt('http://willowvillagesquare.com', '/tmp/wvs_lg.png', '/tmp/wvs_sm.png')
    #cuty_capt('http://google.com', '/tmp/goog_lg.png', '/tmp/goog_sm.png')
