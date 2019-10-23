#!/usr/bin/env python
# _*_ coding:utf-8 _*_
import csv
import logging
import os
from xmind2testcase.utils import get_xmind_testcase_list, get_absolute_path

"""
Convert XMind fie to Zentao testcase csv file 

Zentao official document about import CSV testcase file: https://www.zentao.net/book/zentaopmshelp/243.mhtml 
"""


def xmind_to_zentao_csv_file(xmind_file):
    """Convert XMind file to a zentao csv file"""
    xmind_file = get_absolute_path(xmind_file)
    logging.info('Start converting XMind file(%s) to zentao file...', xmind_file)
    testcases = get_xmind_testcase_list(xmind_file)

    fileheader = ["所属模块", "用例类型", "相关需求", "用例标题", "优先级", "前置条件", "步骤", "预期", "关键词", "用例状态"]
    zentao_testcase_rows = [fileheader]
    for testcase in testcases:
        row = gen_a_testcase_row(testcase)
        zentao_testcase_rows.append(row)

    zentao_file = xmind_file[:-6] + '.csv'
    if os.path.exists(zentao_file):
        logging.info('The zentao csv file already exists, return it directly: %s', zentao_file)
        return zentao_file

    with open(zentao_file, 'w', encoding='gbk',newline='') as f: # fengtao 1,modify encoding to GBK 2,add paremater newline=''
        writer = csv.writer(f)
        writer.writerows(zentao_testcase_rows)
        logging.info('Convert XMind file(%s) to a zentao csv file(%s) successfully!', xmind_file, zentao_file)

    return zentao_file


def gen_a_testcase_row(testcase_dict):
    case_module = gen_case_module(testcase_dict['suite'])
    case_title = testcase_dict['name']
    case_precondition = testcase_dict['preconditions']['precondition']
    case_step, case_expected_result = gen_case_step_and_expected_result(testcase_dict['steps'],testcase_dict['expects'])
    case_keyword = testcase_dict['execution_type']  # fengtao：indicate case is manual or auto exec
    #case_priority = gen_case_priority(testcase_dict['importance']) # fengtao：zentao version is low,use number as priority
    case_priority = testcase_dict['importance']
    case_type = testcase_dict['case_type']
    case_status = '正常'
    case_req = testcase_dict['case_req']
    row = [case_module, case_type, case_req, case_title, case_priority, case_precondition, case_step, case_expected_result, case_keyword, case_status]
    return row


def gen_case_module(module_name):
    if module_name:
        module_name = module_name.replace('（', '(')
        module_name = module_name.replace('）', ')')
    else:
        module_name = '/'
    return module_name


def gen_case_precondition(testcase_dict):
    return testcase_dict['preconditions']['precondition']


def gen_case_step_and_expected_result(steps,expects):
    case_step = ''
    case_expected_result = ''

    for step_dict in steps:
        case_step += str(step_dict['step_number']) + '. ' + step_dict['action'].replace('\n', '').strip() + '\n'

    for expect_dict in expects:
        case_expected_result += str(expect_dict['expect_number']) + '. ' + \
        expect_dict['expect'].replace('\n', '').strip() + '\n' \
        if expect_dict.get('expect', '') else ''


    return case_step, case_expected_result


def gen_case_priority(priority):   #  禅道版本太低，使用1/2/3/4 作为优先级，此方法目前不使用
    mapping = {1: '高', 2: '中', 3: '低'}
    if priority in mapping.keys():
        return mapping[priority]
    else:
        return '中'


def gen_case_type(case_type):   # 从case_dict 中的execution_type中获取，此方法不使用
    mapping = {1: '手动', 2: '自动'}
    if case_type in mapping.keys():
        return mapping[case_type]
    else:
        return '手动'


if __name__ == '__main__':
    xmind_file = '../docs/zentao_testcase_template.xmind'
    zentao_csv_file = xmind_to_zentao_csv_file(xmind_file)
    print('Conver the xmind file to a zentao csv file succssfully: %s', zentao_csv_file)