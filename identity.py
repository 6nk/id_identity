#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random
import re
import datetime

import constant as const

class IdNumber(str):

    def __init__(self, id_number):
        super(IdNumber, self).__init__()
        self.id = id_number
        self.area_id = int(self.id[0:6])
        self.birth_year = int(self.id[6:10])
        self.birth_month = int(self.id[10:12])
        self.birth_day = int(self.id[12:14])

    def get_area_name(self):
        """根据区域编号取出区域名称"""
        return const.AREA_INFO[self.area_id]

    def get_check_digit(self):
        """通过身份证号获取校验码"""
        check_sum = 0
        for i in range(0, 17):
            check_sum += ((1 << (17 - i)) % 11) * int(self.id[i])
        check_digit = (12 - (check_sum % 11)) % 11
        return check_digit if check_digit < 10 else 'X'

    @classmethod
    def verify_id(cls, id_number):
        """校验身份证是否正确"""
        if re.match(const.ID_NUMBER_18_REGEX, id_number):
            check_digit = cls(id_number).get_check_digit()
            return str(check_digit) == id_number[-1]
        else:
            return bool(re.match(const.ID_NUMBER_15_REGEX, id_number))

if __name__ == '__main__':
#    print(IdNumber('410326199507103197').area_id)  # 地址编码:410326
#    print(IdNumber('410326199507103197').get_area_name())  # 地址:河南省洛阳市汝阳县
#    print(IdNumber('410326199507103197').get_birthday())  # 生日:1995-7-10
#    print(IdNumber('410326199507103197').get_age())  # 年龄:23(岁)
#    print(IdNumber('410326199507103197').get_sex())  # 性别:1(男)
#    print(IdNumber('410326199507103197').get_check_digit())  # 校验码:7
    str1 = "123456"  #身份证前6位
    str2 = "1234"    #身份证后4位
    count = 0
    begin = datetime.date(1990,1,1)
    end = datetime.date(1999,12,31)
    for i in range((end-begin).days + 1):
        day = begin + datetime.timedelta(days = i)
        birthday = day.strftime("%Y%m%d")
        id_num = str1 + birthday + str2
        if(IdNumber.verify_id(id_num)):  # 检验身份证是否正确:False
            print id_num, True
            count = count + 1
    print "total:", count
