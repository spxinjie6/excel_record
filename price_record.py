#!usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author: xinjie
@file: price_record.py
@time: 2020/03/02
"""
import openpyxl

extend_records = [
    {
        "disk_type": "高性能",
        "pay_method": "每天",
        "extend_disk_price": 0.99,
        "extend_disk_base": 100,
        "min_extend_disk_size": 100,
        "max_extend_disk_size": 4000,
        "iops_price": 0.0,
        "min_iops_number": 0,
        "max_iops_number": 0,
        "iops_base": 0
    },
    {
        "disk_type": "高性能",
        "pay_method": "每月",
        "extend_disk_price": 50.0,
        "extend_disk_base": 100,
        "min_extend_disk_size": 100,
        "max_extend_disk_size": 4000,
        "iops_price": 0.0,
        "min_iops_number": 0,
        "max_iops_number": 0,
        "iops_base": 0
    },
    {
        "disk_type": "高性能",
        "pay_method": "每年",
        "extend_disk_price": 510.0,
        "extend_disk_base": 100,
        "min_extend_disk_size": 100,
        "max_extend_disk_size": 4000,
        "iops_price": 0.0,
        "min_iops_number": 0,
        "max_iops_number": 0,
        "iops_base": 0
    },
    {
        "disk_type": "高IO",
        "pay_method": "每天",
        "extend_disk_price": 0.71,
        "extend_disk_base": 50,
        "min_extend_disk_size": 50,
        "max_extend_disk_size": 4000,
        "iops_price": 0.07,
        "min_iops_number": 1,
        "max_iops_number": 50,
        "iops_base": 1
    },
    {
        "disk_type": "高IO",
        "pay_method": "每月",
        "extend_disk_price": 50.0,
        "extend_disk_base": 50,
        "min_extend_disk_size": 50,
        "max_extend_disk_size": 4000,
        "iops_price": 4,
        "min_iops_number": 1,
        "max_iops_number": 50,
        "iops_base": 1
    },
    {
        "disk_type": "高IO",
        "pay_method": "每年",
        "extend_disk_price": 1200.0,
        "extend_disk_base": 50,
        "min_extend_disk_size": 50,
        "max_extend_disk_size": 4000,
        "iops_price": 40.8,
        "min_iops_number": 1,
        "max_iops_number": 50,
        "iops_base": 1
    },
    {
        "disk_type": "标准型",
        "pay_method": "每天",
        "extend_disk_price": 0.99,
        "extend_disk_base": 100,
        "min_extend_disk_size": 100,
        "max_extend_disk_size": 4000,
        "iops_price": 0.0,
        "min_iops_number": 0,
        "max_iops_number": 0,
        "iops_base": 0
    },
    {
        "disk_type": "标准型",
        "pay_method": "每月",
        "extend_disk_price": 50.0,
        "extend_disk_base": 100,
        "min_extend_disk_size": 100,
        "max_extend_disk_size": 4000,
        "iops_price": 0.0,
        "min_iops_number": 0,
        "max_iops_number": 0,
        "iops_base": 0
    },
    {
        "disk_type": "标准型",
        "pay_method": "每年",
        "extend_disk_price": 510.0,
        "extend_disk_base": 100,
        "min_extend_disk_size": 100,
        "max_extend_disk_size": 4000,
        "iops_price": 0.0,
        "min_iops_number": 0,
        "max_iops_number": 0,
        "iops_base": 0
    }
]

def write_excel(header, keys, data, title, path, add_sheet=True):
    if add_sheet:
        wb = openpyxl.Workbook()
        ws = wb.active
        ws.title = title
    else:
        wb = openpyxl.load_workbook(path)
        wb.create_sheet(title)
        ws = wb[title]
    for field in range(1, len(header) + 1):  # 写入表头
        _ = ws.cell(row=1, column=field, value=str(header[field - 1]))

    for row1 in range(2, len(data) + 2):  # 写入数据
        for col1 in range(1, len(data[row1 - 2]) + 1):
            key = keys[col1 - 1]
            _ = ws.cell(row=row1, column=col1, value=str(data[row1 - 2][key]))

    wb.save(filename=path)


if __name__ == "__main__":
    header = ["机房", "CPU", "内存", "性能", "支付方式", "支付价格", "系统盘价格"]
    keys = ["room", "cpu", "ram", "disk_type", "pay_method", "price", "disk_price"]
    title = "CDS 价格表"
    path = "/Users/xinjie/Desktop/cds.xlsx"
    write_excel(header, keys, record, title, path)
    header = ["性能", "支付方式", "扩展盘单价", "最小拓展盘G", "最大拓展盘G", "扩展盘基数", "性能包单价", "最小性能包", "最大性能包", "性能包基数"]
    keys = ["disk_type", "pay_method", "extend_disk_price", "min_extend_disk_size", "max_extend_disk_size", "extend_disk_base", "iops_price", "min_iops_number", "max_iops_number", "iops_base"]
    title = "CDS 拓展盘价格表"
    # path = "/Users/xinjie/Desktop/cds.xlsx"
    write_excel(header, keys, extend_records, title, path, False)
