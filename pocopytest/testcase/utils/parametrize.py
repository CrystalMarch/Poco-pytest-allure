# -*- coding: utf-8 -*-


class Param(object):
    # text, error_msg
    TEST_INPUT = [
        ('123Abc', '数字大小写字母'),
        # ('简体中文', '简体中文'),
        # ('繁體', '繁体'),
        # ('ありがとう', '日文'),
        (' ab', '开头有空格'),
        # ('ab ', '结尾有空格'),
        # ('a b', '字母中间有空格'),
        # (r'ab\n', '有换行符'),
        (r',.;:"`~!@#$%^&*()-_+=', '普通特殊字符'),
        # (r'null', '特殊字符串'),
        # (r'&nbsp', '特殊字符串'),
        ('¹ ² ³ ⁰ ⁱ ⁴ ⁵ ⁶ ⁷ ⁸ ⁹ ', '特殊字符'),
        # ('<color=#ff0000>红色</color>', '颜色字符'),
        # ('a' * 5, '5个字母'),
        # ('a' * 10, '10个字母'),
        # ('a' * 15, '15个字母'),
        # ('a' * 20, '20个字母'),
        ('a' * 25, '25个字母'),
        ('a' * 30, '30个字母'),
    ]