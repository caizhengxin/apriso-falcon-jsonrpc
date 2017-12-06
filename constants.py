# -*- coding: utf-8 -*-
# @Author: caixin
# @Date:   2017-12-05 17:00:27
# @Last Modified by:   1249614072@qq.com
# @Last Modified time: 2017-12-06 10:40:34
from utils.utils import get_conf

CONF = get_conf(r'config.toml')


APRISO_URL = 'http://%s/Apriso/BusinessWebServices/JobExecutor.asmx?WSDL'

DATAXMLS = r"""<?xml version="1.0" encoding="utf-8"?>
<OperationInterpretationParameters
  xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
  xmlns:xsd="http://www.w3.org/2001/XMLSchema">
    <OperationID>0</OperationID>
    <OperationCode>%s</OperationCode>
    <OperationResolutionMethod>ByOperationCode</OperationResolutionMethod>
    <Inputs>
            <PropertyBagItem Key="Json_str" name = "Json_str">
                <Value xsi:type="xsd:string">%s</Value>
            </PropertyBagItem>
    </Inputs>
    <Outputs/>
    <InputsType/>
    <OutputsType/>
    <SystemVariables/>
    <ExecuteRemote>false</ExecuteRemote>
    <EmployeeID>-1</EmployeeID>
    <TestRun>false</TestRun>
</OperationInterpretationParameters>"""
