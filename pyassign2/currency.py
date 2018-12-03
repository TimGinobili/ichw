#!/usr/bin/env python3

"""currency.py: exchange currency
__author__ = "niuxiao"
__pkuid__  = "1800011701"
__email__  = "1800011701@pku.edu.cn"
"""

#调用URL和json库
from urllib.request import urlopen
import json

#合法输入货币列表
list = ['AED', 'AFN', 'ALL', 'AMD', 'ANG', 'AOA', 'ARS', 'AUD', 'AWG', 'AZN',
        'BAM', 'BBD', 'BDT', 'BGN', 'BHD', 'BIF', 'BMD', 'BND', 'BOB', 'BRL',
        'BSD', 'BTC', 'BTN', 'BWP', 'BYR', 'BZD', 'CAD', 'CDF', 'CHF', 'CLF',
        'CLP', 'CNY', 'COP', 'CRC', 'CUC', 'CUP', 'CVE', 'CZK', 'DJF', 'DKK',
        'DOP', 'DZD', 'EEK', 'EGP', 'ERN', 'ETB', 'EUR', 'FJD', 'FKP', 'GBP',
        'GEL', 'GGP', 'GHS', 'GIP', 'GMD', 'GNF', 'GTQ', 'GYD', 'HKD', 'HNL',
        'HRK', 'HTG', 'HUF', 'IDR', 'ILS', 'IMP', 'INR', 'IQD', 'IRR', 'ISK',
        'JEP', 'JMD', 'JOD', 'JPY', 'KES', 'KGS', 'KHR', 'KMF', 'KPW', 'KRW',
        'KWD', 'KYD', 'KZT', 'LAK', 'LBP', 'LKR', 'LRD', 'LSL', 'LTL', 'LVL',
        'LYD', 'MAD', 'MDL', 'MGA', 'MKD', 'MMK', 'MNT', 'MOP', 'MRO', 'MTL',
        'MUR', 'MVR', 'MWK', 'MXN', 'MYR', 'MZN', 'NAD', 'NGN', 'NIO', 'NOK',
        'NPR', 'NZD', 'OMR', 'PAB', 'PEN', 'PGK', 'PHP', 'PKR', 'PLN', 'PYG',
        'QAR', 'RON', 'RSD', 'RUB', 'RWF', 'SAR', 'SBD', 'SCR', 'SDG', 'SEK',
        'SGD', 'SHP', 'SLL', 'SOS', 'SRD', 'STD', 'SVC', 'SYP', 'SZL', 'THB',
        'TJS', 'TMT', 'TND', 'TOP', 'TRY', 'TTD', 'TWD', 'TZS', 'UAH', 'UGX',
        'USD', 'UYU', 'UZS', 'VEF', 'VND', 'VUV', 'WST', 'XAF', 'XAG', 'XAU',
        'XCD', 'XDR', 'XOF', 'XPD', 'XPF', 'XPT', 'YER', 'ZAR', 'ZMK', 'ZMW', 
        'ZWL']

#分解字符串函数：取出一给定字符串第一个空格前的部分
def before_space(str):
    l = str.split()
    str = l[0]
    return str

#URL转化函数：访问URL，从中取出字符串并将之转化为字典
def turn_dict(site):
    doc = urlopen(site)
    docstr = doc.read()
    doc.close()
    jstr = docstr.decode('ascii')
    jstr = str(json.loads(jstr))
    dict = eval(jstr)
    return dict

#exchange 函数:实现货币的转换
def exchange(currency_from, currency_to, amount_from):
    dict1 = turn_dict(
            'http://cs1110.cs.cornell.edu/2016fa/a1server.php?from='
        + currency_from + '&to=' + currency_to + '&amt=' + amount_from
            )
    amount_to = dict1['to']
    amount = before_space(amount_to)
    return(amount)

# 输入函数
def items_input():
    global currency_from
    global currency_to
    global amount_from
    currency_from = input('请输入源货币:')
    currency_to = input('请输入目标货币:')
    amount_from = input('请输入源货币数目:')

#测试函数部分:
#字符串分解测试函数
def test_before_space():
    assert ('2.5' == before_space('2.5 USD'))
    assert ('2.5' == before_space('2.5 EUR'))
    assert ('3.5' == before_space('3.5 XCD'))
    assert ('9' == before_space('9 USD'))

#URL转化测试函数
def test_turn_dict():
    assert(
        {
            'from': '2.5 United States Dollars', 'to': '2.1589225 Euros', 'success': True, 'error': ''
        } == turn_dict(
            'http://cs1110.cs.cornell.edu/2016fa/a1server.php?from='
        + 'USD' + '&to=' + 'EUR' + '&amt=' + '2.5'
            )
    )
    assert (
            {
                'from': '3 United Arab Emirates Dirhams', 'to': '1.3818380458036 Bulgarian Levs', 'success': True,
                'error': ''
            } == turn_dict(
              'http://cs1110.cs.cornell.edu/2016fa/a1server.php?from='
              + 'AED' + '&to=' + 'BGN' + '&amt=' + '3'
            )
             )
    assert (
            {
                'from': '4 Jordanian Dinar', 'to': '7.7927403009982 Libyan Dinar', 'success': True, 'error': ''
            } == turn_dict(
             'http://cs1110.cs.cornell.edu/2016fa/a1server.php?from='
             + 'JOD' + '&to=' + 'LYD' + '&amt=' + '4'
            )
             )

#exchange测试函数
def test_exchange():
    assert(exchange('USD','EUR','2.5') == '2.1589225')
    assert(exchange('BSD','CLP','3') == '2077.2')
    assert(exchange('SGD','TJS','9') == '61.675575984606')

# 输入合法性检测函数
def test_items_input():
    if (currency_from in list) == False:
        return '源货币种类不合法。'
    elif (currency_to in list) == False:
        return '目标货币种类不合法。'
    elif currency_from in list and currency_to in list:
        try:
            x = float(amount_from)
        except ValueError:
            return '货币数目非法，请确认货币数目为数字。'
        else:
            return '输入合法。'
#测试所有函数
def test_All():
    test_before_space()
    test_turn_dict()
    test_exchange()
    print("All tests passed")

def main():
    test_All()
    items_input()
    test_items_input()
    if test_items_input() == '输入合法。':
        print(exchange(currency_from, currency_to, amount_from))
    else:
        print(test_items_input())

if __name__  ==  '__main__':
    main()

