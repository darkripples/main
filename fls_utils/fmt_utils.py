# coding:utf8
## Some Func About 'Format Obj'
# 2016/6/6 Add fmt_null_obj()

def __check_null( v ):
    # Check 'v' for None
    if v and v not in ('None', 'null', 'Null'):
        return True
    return False

def __fmt_null_ListTuple( l_t ):
    # Change 'None' to '' for List or Tuple
    return [ fmt_null_obj(i) if __check_null(i) else '' for i in l_t ]

def __fmt_null_Dict( d ):
    # Change 'None' to '' for Dict
    return dict( (k, fmt_null_obj(v)) if __check_null(v) else (k, '') for k, v in d.items() )

def fmt_null_obj( obj ):
    # Change None's obj to ''
    if not __check_null(obj): return ''
    if type(obj) in ( list, tuple ):
        # Change 'None' to ''
        obj_new = __fmt_null_ListTuple( obj )
    elif type(obj) == dict:
        # Change None's value to ''
        obj_new = __fmt_null_Dict( obj )
    else:
        obj_new = obj
    return obj_new

def fmt_date( fmt='%Y%m%d%H%M%S' ):
    # format DATE
    from datetime import datetime
    n = datetime.now().strftime( fmt )
    return n

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

def e_int(value , buflen = 0 , align = 'R' , fillchar = '0' ):
    """ 打包，整型数值字段打包格式字符串
        参数列表：value:       字段内容
                  buflen:      填充后总长度 
                  align: 字段对齐(默认左对齐) L:左对齐 R:右对齐 C:居中
                  fillchar:    填充字符(默认空格符)
    """
    if value is None:
        value = 0
    tmpstr = str(int(value))
    return e_string( tmpstr , buflen , align , fillchar )

def e_int_money( value , buflen = 0 , align = 'R' , fillchar = '0' ):
    """
     打包，以分为单位的金额格式话
     参数列表: value       字段内容，整形或浮点型，以元为单位
               buflen      填充后长度
               align 对齐方式(默认左对齐) L:左对齐 R:右对齐 C:居中
               fillchar    填充字符(默认空格符)
    """
    if value is None:
        value = 0
    if float(value) <0:
        s = '-'+ e_int( round(abs(value) * 100) , buflen-1 , align , fillchar )
        return s
    else:
        return e_int( round(value * 100) , buflen , align , fillchar )

def __test_2_fmt_null_obj():
    # Test for fmt_null_obj
    n = None
    a = [None,'asdf',123,'12']
    b = {'a':None,'b':'None','c':1,'d':'123'}
    c = [{'a':'None','b':None,'c':123},{'d':None,'e':'123'},b]
    d = [{'a':'None','b':None,'c':123},{'d':None,'e':'123'},c]
    old = d
    print(old)
    new_ = fmt_null_obj(old)
    print(new_)

def __test_2_fmt_date():
    # Test for fmt_date()
    a = fmt_date(fmt='%Y-%m-%d')
    import sys
    print(sys.argv)
    fmt = sys.argv[-1] if len(sys.argv)==2 else '%Y-%m-%d'
    a = fmt_date(fmt=fmt)
    print(a)

if __name__ == '__main__':
    # For test:
    #__test_2_fmt_null_obj()
    __test_2_fmt_date()