#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2024/10/18 17:14
# @Author  : 兵
# @email    : 1747193328@qq.com
import os
import re
import threading

import numpy as np

from loguru import logger


def read_nep_in(  file_name):
    run_in={}
    with open(file_name, 'r', encoding="utf8") as f:

        groups = re.findall("^([A-Za-z_]+)\s+(.*)", f.read(), re.MULTILINE)

        for group in groups:
            run_in[group[0].strip()] = group[1].strip()
    return run_in
def check_fullbatch(nep_in_path,structure_num):

    run_in = read_nep_in(nep_in_path)
    if run_in.get("prediction")=="1":
        return True
    if int(run_in.get("batch",1000))>=structure_num:
        return True
    return False


def read_atom_num_from_xyz(path):
    with open(path, 'r') as file:

        nums=re.findall("^(\d+)$",file.read(),re.MULTILINE)

        return [int(num) for num in nums]




def read_nep_out_file(file_path):
    logger.info("读取文件{}".format(file_path))
    if os.path.exists(file_path):
        data = np.loadtxt(file_path)

        return data
    else:
        return np.array([])



