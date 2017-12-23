# coding:gb18030

from django.http import HttpResponse
from django import template
import sys, os

if 'SERVER_SOFTWARE' in os.environ:
    sys.setdefaultencoding('gb18030')


def load_html( html_pth, **kw ):
    """
    2015/5/23 23:07 suny
    
    ͨ��htmlģ��·��������һ��HttpResponse����
    """
    fp   = open( html_pth )
    t    = template.Template( fp.read() )
    fp.close()
    html = t.render(template.Context( kw ))
    return HttpResponse(html)

def e_string( value , buflen = 0 , align='L' , fillchar = ' ' ):
    """
    ������ַ����ֶ����
    �����б�value:       �ֶ�����
              buflen:      �����ܳ��� 
              align: �ֶζ���(Ĭ�������) L:����� R:�Ҷ��� C:����
              fillchar:    ����ַ�(Ĭ�Ͽո��)
    """
    if value is None:
        value = ''
    elif type( value ) != str:
        value = str(value)
    if len(fillchar) != 1:
        raise RuntimeError( '����ַ�����[fillchar]��ʽ����' )  
    if buflen > 0:
        if len(value) > buflen:
            raise RuntimeError( '����ֶ�[%s]����Խ�磬Ҫ�󳤶�Ϊ��%d��ʵ�ʳ���Ϊ��%d' % ( value , buflen , len(value) ) )
        if align == 'L':
            return value.ljust(buflen,fillchar)
        elif align == 'R':
            return value.rjust(buflen,fillchar)
        elif align == 'C':
            return value.center(buflen,fillchar)
        else:
            raise RuntimeError( '��䷽�����[align]��ʽ���󣬺Ϸ��Ĳ���ΪL��R��C'  )
    else:
        return value

def e_datetime(value ,  buflen = 0 , align = 'L' , fmt = '%Y%m%d%H%M%S', fillchar = ' ' ):
    """
    ��������� ʱ���ʹ��Ϊ��ʽ�ַ���
    �����б�value:       �ֶ�����
              buflen:      �����ܳ��� 
              align: �ֶζ���(Ĭ�������) L:����� R:�Ҷ��� C:����
              format:      ת����ʽ(Ĭ��'%Y%m%d%H%M%S')
              fillchar:    ����ַ�(Ĭ�Ͽո��)
    """
    try:
        if value:
            tmpstr = value.strftime( fmt )
        else:
            tmpstr = ''
        return e_string( tmpstr , buflen , align , fillchar )
    except:
        raise RuntimeError( '��������[%s]���ǺϷ��ĸ�ʽ' % value )

def e_now( buflen = 0 , align = 'L' , fmt = '%Y%m%d%H%M%S' ,fillchar = ' ' ):
    """
    2015/5/24 22:07
    ��ȡ��ǰʱ��
    """
    import datetime
    n = datetime.datetime.now()
    return e_datetime( n , buflen , align , fmt , fillchar )