# coding:gb18030

from django.http import HttpResponse
from django import template
import sys, os

if 'SERVER_SOFTWARE' in os.environ:
    sys.setdefaultencoding('gb18030')


def load_html( html_pth, **kw ):
    """
    2015/5/23 23:07 suny
    
    通过html模板路径，返回一个HttpResponse对象
    """
    fp   = open( html_pth )
    t    = template.Template( fp.read() )
    fp.close()
    html = t.render(template.Context( kw ))
    return HttpResponse(html)

def e_string( value , buflen = 0 , align='L' , fillchar = ' ' ):
    """
    打包，字符型字段填充
    参数列表：value:       字段内容
              buflen:      填充后总长度 
              align: 字段对齐(默认左对齐) L:左对齐 R:右对齐 C:居中
              fillchar:    填充字符(默认空格符)
    """
    if value is None:
        value = ''
    elif type( value ) != str:
        value = str(value)
    if len(fillchar) != 1:
        raise RuntimeError( '填充字符参数[fillchar]格式错误' )  
    if buflen > 0:
        if len(value) > buflen:
            raise RuntimeError( '打包字段[%s]长度越界，要求长度为：%d，实际长度为：%d' % ( value , buflen , len(value) ) )
        if align == 'L':
            return value.ljust(buflen,fillchar)
        elif align == 'R':
            return value.rjust(buflen,fillchar)
        elif align == 'C':
            return value.center(buflen,fillchar)
        else:
            raise RuntimeError( '填充方向参数[align]格式错误，合法的参数为L、R、C'  )
    else:
        return value

def e_datetime(value ,  buflen = 0 , align = 'L' , fmt = '%Y%m%d%H%M%S', fillchar = ' ' ):
    """
    打包，日期 时间型打包为格式字符串
    参数列表：value:       字段内容
              buflen:      填充后总长度 
              align: 字段对齐(默认左对齐) L:左对齐 R:右对齐 C:居中
              format:      转换格式(默认'%Y%m%d%H%M%S')
              fillchar:    填充字符(默认空格符)
    """
    try:
        if value:
            tmpstr = value.strftime( fmt )
        else:
            tmpstr = ''
        return e_string( tmpstr , buflen , align , fillchar )
    except:
        raise RuntimeError( '输入内容[%s]不是合法的格式' % value )

def e_now( buflen = 0 , align = 'L' , fmt = '%Y%m%d%H%M%S' ,fillchar = ' ' ):
    """
    2015/5/24 22:07
    获取当前时间
    """
    import datetime
    n = datetime.datetime.now()
    return e_datetime( n , buflen , align , fmt , fillchar )