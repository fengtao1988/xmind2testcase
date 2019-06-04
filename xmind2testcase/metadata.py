#!/usr/bin/env python
# _*_ coding:utf-8 _*_

"""
testlink.testlink
"""
# 构造测试元数据模板

class TestSuite(object):  # 构造测试套字典模板

    def __init__(self, name='', details='', testcase_list=None, sub_suites=None, statistics=None):
        """
        TestSuite
        :param name: test suite name
        :param details: test suite detail infomation
        :param testcase_list: test case list
        :param sub_suites: sub test suite list
        :param statistics: testsuite statistics info {'case_num': 0, 'non_execution': 0, 'pass': 0, 'failed': 0, 'blocked': 0, 'skipped': 0}
        """
        self.name = name
        self.details = details
        self.testcase_list = testcase_list
        self.sub_suites = sub_suites
        self.statistics = statistics

    def to_dict(self):
        data = {
            'name': self.name,
            'details': self.details,
            'testcase_list': [],
            'sub_suites': []
        }

        if self.sub_suites:
            for suite in self.sub_suites:
                data['sub_suites'].append(suite.to_dict())

        if self.testcase_list:
            for case in self.testcase_list:
                data['testcase_list'].append(case.to_dict())

        if self.statistics:
            data['statistics'] = self.statistics

        return data


class TestCase(object):   # 构造测试用例字典模板

    def __init__(self, name=None, version=1, preconditions=None, execution_type='手动', importance=2, estimated_exec_duration=3, status=7, result=0, steps=None, expects=None):
        """
        TestCase
        :param name: test case name
        :param version: test case version information
        :param preconditions: test case pre condition
        :param execution_type: manual or automate
        :param importance: high:1, middle:2, low:3
        :param estimated_exec_duration: estimated execution duration
        :param status: draft:1, ready ro review:2, review in progress:3, rework:4, obsolete:5, future:6, final:7
        :param result: non-execution:0, pass:1, failed:2, blocked:3, skipped:4
        :param steps: test case step list
        :param expects: test case result list
        """
        self.name = name
        self.version = version
        self.preconditions = preconditions
        self.execution_type = execution_type
        self.importance = importance
        self.estimated_exec_duration = estimated_exec_duration
        self.status = status
        self.result = result
        self.steps = steps
        self.expects = expects

    def to_dict(self):
        data = {
            'name': self.name,
            'version': self.version,  # TODO(devin): get version content
            'preconditions': self.preconditions,
            'execution_type': self.execution_type,
            'importance': self.importance,
            'estimated_exec_duration': self.estimated_exec_duration,  # TODO(devin): get estimated content
            'status': self.status,  # TODO(devin): get status content
            'result': self.result,
            'steps': [],
            'expects': []
        }

        if self.preconditions:
            data['preconditions'] = self.preconditions.to_dict()

        if self.steps:
            for step in self.steps:
                data['steps'].append(step.to_dict())

        if self.expects:
            for expect in self.expects:
                data['expects'].append(expect.to_dict())

        return data


class TestPre(object):  # 构造测试用例预制条件字典模板

    def __init__(self, precondition='', script=''):
        '''
        TestPre
        :param precondition: test case precondition
        :param script: script of test precondition
        '''
        self.precondition = precondition
        self.script = script  # 预留作为自动生成自动化脚本

    def to_dict(self):
        data = {
            'precondition': self.precondition,
            'script': self.script
        }
        return data


class TestStep(object):   # 构造测试用例步骤字典模板

    def __init__(self, step_number=1, action='', script=''):
        """
        TestStep
        :param step_number: test step number
        :param action: test step actions
        :param script: script of teststep
        """
        self.step_number = step_number
        self.action = action
        self.script = script  # 预留作为自动生成自动化脚本

    def to_dict(self):
        data = {
            'step_number': self.step_number,
            'action': self.action,
            'script': self.script
        }

        return data


class TestExpect(object):   # 构造测试用例预期结果字典模板

    def __init__(self, expect_number=1, expect='', script='', result=0):
        '''
        TestExpect
        :param expect_number:
        :param expects: test step expected results
        :param scripts: script of test expect
        :param result: non-execution:0, pass:1, failed:2, blocked:3, skipped:4
        '''
        self.expect_number = expect_number
        self.expect = expect
        self.script = script   # 预留作为自动生成自动化脚本
        self.result = result

    def to_dict(self):
        data = {
            'expect_number': self.expect_number,
            'expect': self.expect,
            'script': self.script,
            'result': self.result
        }
        return data




