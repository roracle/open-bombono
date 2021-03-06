#!/usr/bin/env python
# coding: utf-8

import SConsTwin
import ASettings

def MakeMenu(env, is_moving):
    if not is_moving:
        # 1 - m2v
        # '-a' - аспект: (1 - 1:1) 2 - 4:3, 3 - 16:9 (4 - 2.21:1)
        aspect = '2'
        if not ASettings.Is4_3:
            aspect = '3'
        # возможные опции оптимизации: -b <kbps>, -q <num>, -H
        # однако отображение в totem все равно гораздо хуже, чем снимок того же кадра, сделанного в totem! 
        options = "-f 8"
        # 'n -1' sucks: need to generate two frames (n -2) 
        # for much better encoding quality with mpeg2enc (thanks to stagediverr)
        env.Command('Menu.m2v', 'Menu.png', "png2yuv -n 2 -I p -f 25 -j $SOURCE | mpeg2enc -a " + aspect + " " + options + " -o $TARGET")
        
        # 2 - mpg
        env.Command('Menu.mpg', ['Menu.m2v', '#Silent.mp2'], "mplex -f 8 -o $TARGET $SOURCES")
    
    # 3 - menu subpictures
    import SCons.Action
    # очень нужно выполнить команду именно внутри каталога меню, из-за ссылок внутри Menu.xml
    cur_dir = env.Dir('.').path
    
    def GenerateSAFunc(stream_id):
        def GenerateSACmd(source, target, env, for_signature):
            cd_str = 'cd "' + cur_dir + '" && '
            spumux_str = 'spumux -s%s %s < %s > %s' % (stream_id, source[0].name, source[1].name, target[0].name)
            return cd_str + spumux_str
        return GenerateSACmd
    def GenerateSA(stream_id):
        return SConsTwin.MakeGenAction(GenerateSAFunc(stream_id))
    
    # в версии SCons >= 0.96.90 можно пользоваться аргументом chdir (правда, будет конфликтовать с опцией -j :( )
    #Command('MenuSub.mpg', ['Menu.xml', 'Menu.mpg'], 
    #        "spumux ${SOURCES[0].file} < ${SOURCES[1].file} > ${TARGET.file}", chdir=1)
    if ASettings.Is4_3:
        env.Command('MenuSub.mpg', ['Menu.xml', 'Menu.mpg'], GenerateSA(0))
    else:
        env.Command('MenuSub0.mpg', ['Menu.xml', 'Menu.mpg'], GenerateSA(0))
        env.Command('MenuSub.mpg', ['MenuLB.xml', 'MenuSub0.mpg'], GenerateSA(1))

