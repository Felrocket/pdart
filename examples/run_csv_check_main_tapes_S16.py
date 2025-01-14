#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Run initial checks on csv files - S16 (main tapes)

Make checked csv files (will drop some damaged data)
out of the raw csv files extracted from binary. 

Remember to run final_csv_check_main_tapes_all.py AFTER this file, 
which uses slightly different paramters for some of the files which 
didn't have good data recovery.

:copyright:
    The PDART Development Team & Ceri Nunn
:license:
    GNU Lesser General Public License, Version 3
    (https://www.gnu.org/copyleft/lesser.html)
"""
from __future__ import (absolute_import, division, print_function,
                        unicode_literals)
from future.builtins import *  # NOQA
from pdart.csv_check_work_tapes import call_csv_check_work_tapes
# from pdart.view import plot_from_stream
from obspy.core.stream import read
import pdart.config as config

import logging
# logging.handlers


import pandas as pd
import numpy as np

def run_csv_check_work_tapes():
    checked_dir='/Users/cnunn/lunar_data/PDART_CSV/S16'
    processed_dir='/Users/cnunn/lunar_data/PDART_PROCESSED'

    # example 1 with clock flag
    config.initial = False
    filenames=[
'pse.a16.1.1.csv.gz',
'pse.a16.1.10.csv.gz',
'pse.a16.1.100.csv.gz',
'pse.a16.1.101.csv.gz',
'pse.a16.1.102.csv.gz',
'pse.a16.1.103.csv.gz',
'pse.a16.1.104.csv.gz',
'pse.a16.1.105.csv.gz',
'pse.a16.1.106.csv.gz',
'pse.a16.1.107.csv.gz',
'pse.a16.1.108.csv.gz',
'pse.a16.1.109.csv.gz',
'pse.a16.1.11.csv.gz',
'pse.a16.1.110.csv.gz',
'pse.a16.1.111.csv.gz',
'pse.a16.1.112.csv.gz',
'pse.a16.1.113.csv.gz',
'pse.a16.1.114.csv.gz',
'pse.a16.1.115.csv.gz',
'pse.a16.1.116.csv.gz',
'pse.a16.1.117.csv.gz',
'pse.a16.1.118.csv.gz',
'pse.a16.1.119.csv.gz',
'pse.a16.1.12.csv.gz',
'pse.a16.1.120.csv.gz',
'pse.a16.1.121.csv.gz',
'pse.a16.1.122.csv.gz',
'pse.a16.1.123.csv.gz',
'pse.a16.1.124.csv.gz',
'pse.a16.1.125.csv.gz',
'pse.a16.1.126.csv.gz',
'pse.a16.1.127.csv.gz',
'pse.a16.1.128.csv.gz',
'pse.a16.1.129.csv.gz',
'pse.a16.1.13.csv.gz',
'pse.a16.1.130.csv.gz',
'pse.a16.1.131.csv.gz',
'pse.a16.1.132.csv.gz',
'pse.a16.1.133.csv.gz',
'pse.a16.1.134.csv.gz',
'pse.a16.1.135.csv.gz',
'pse.a16.1.136.csv.gz',
'pse.a16.1.137.csv.gz',
'pse.a16.1.138.csv.gz',
'pse.a16.1.139.csv.gz',
'pse.a16.1.14.csv.gz',
'pse.a16.1.140.csv.gz',
'pse.a16.1.141.csv.gz',
'pse.a16.1.142.csv.gz',
'pse.a16.1.143.csv.gz',
'pse.a16.1.144.csv.gz',
'pse.a16.1.145.csv.gz',
'pse.a16.1.146.csv.gz',
'pse.a16.1.147.csv.gz',
'pse.a16.1.148.csv.gz',
'pse.a16.1.149.csv.gz',
'pse.a16.1.15.csv.gz',
'pse.a16.1.150.csv.gz',
'pse.a16.1.151.csv.gz',
'pse.a16.1.152.csv.gz',
'pse.a16.1.153.csv.gz',
'pse.a16.1.154.csv.gz',
'pse.a16.1.155.csv.gz',
'pse.a16.1.156.csv.gz',
'pse.a16.1.157.csv.gz',
'pse.a16.1.158.csv.gz',
'pse.a16.1.159.csv.gz',
'pse.a16.1.16.csv.gz',
'pse.a16.1.160.csv.gz',
'pse.a16.1.161.csv.gz',
'pse.a16.1.162.csv.gz',
'pse.a16.1.163.csv.gz',
'pse.a16.1.164.csv.gz',
'pse.a16.1.165.csv.gz',
'pse.a16.1.166.csv.gz',
'pse.a16.1.167.csv.gz',
'pse.a16.1.168.csv.gz',
'pse.a16.1.169.csv.gz',
'pse.a16.1.17.csv.gz',
'pse.a16.1.18.csv.gz',
'pse.a16.1.19.csv.gz',
'pse.a16.1.2.csv.gz',
'pse.a16.1.20.csv.gz',
'pse.a16.1.21.csv.gz',
'pse.a16.1.22.csv.gz',
'pse.a16.1.23.csv.gz',
'pse.a16.1.24.csv.gz',
'pse.a16.1.25.csv.gz',
'pse.a16.1.26.csv.gz',
'pse.a16.1.27.csv.gz',
'pse.a16.1.28.csv.gz',
'pse.a16.1.29.csv.gz',
'pse.a16.1.3.csv.gz',
'pse.a16.1.30.csv.gz',
'pse.a16.1.31.csv.gz',
'pse.a16.1.32.csv.gz',
'pse.a16.1.33.csv.gz',
'pse.a16.1.34.csv.gz',
'pse.a16.1.35.csv.gz',
'pse.a16.1.36.csv.gz',
'pse.a16.1.37.csv.gz',
'pse.a16.1.38.csv.gz',
'pse.a16.1.39.csv.gz',
'pse.a16.1.4.csv.gz',
'pse.a16.1.40.csv.gz',
'pse.a16.1.41.csv.gz',
'pse.a16.1.42.csv.gz',
'pse.a16.1.43.csv.gz',
'pse.a16.1.44.csv.gz',
'pse.a16.1.45.csv.gz',
'pse.a16.1.46.csv.gz',
'pse.a16.1.47.csv.gz',
'pse.a16.1.48.csv.gz',
'pse.a16.1.49.csv.gz',
'pse.a16.1.5.csv.gz',
'pse.a16.1.50.csv.gz',
'pse.a16.1.51.csv.gz',
'pse.a16.1.52.csv.gz',
'pse.a16.1.53.csv.gz',
'pse.a16.1.54.csv.gz',
'pse.a16.1.55.csv.gz',
'pse.a16.1.56.csv.gz',
'pse.a16.1.57.csv.gz',
'pse.a16.1.58.csv.gz',
'pse.a16.1.59.csv.gz',
'pse.a16.1.6.csv.gz',
'pse.a16.1.60.csv.gz',
'pse.a16.1.61.csv.gz',
'pse.a16.1.62.csv.gz',
'pse.a16.1.63.csv.gz',
'pse.a16.1.64.csv.gz',
'pse.a16.1.65.csv.gz',
'pse.a16.1.66.csv.gz',
'pse.a16.1.67.csv.gz',
'pse.a16.1.68.csv.gz',
'pse.a16.1.69.csv.gz',
'pse.a16.1.7.csv.gz',
'pse.a16.1.70.csv.gz',
'pse.a16.1.71.csv.gz',
'pse.a16.1.72.csv.gz',
'pse.a16.1.73.csv.gz',
'pse.a16.1.74.csv.gz',
'pse.a16.1.75.csv.gz',
'pse.a16.1.76.csv.gz',
'pse.a16.1.77.csv.gz',
'pse.a16.1.78.csv.gz',
'pse.a16.1.79.csv.gz',
'pse.a16.1.8.csv.gz',
'pse.a16.1.80.csv.gz',
'pse.a16.1.81.csv.gz',
'pse.a16.1.82.csv.gz',
'pse.a16.1.83.csv.gz',
'pse.a16.1.84.csv.gz',
'pse.a16.1.85.csv.gz',
'pse.a16.1.86.csv.gz',
'pse.a16.1.87.csv.gz',
'pse.a16.1.88.csv.gz',
'pse.a16.1.89.csv.gz',
'pse.a16.1.9.csv.gz',
'pse.a16.1.90.csv.gz',
'pse.a16.1.91.csv.gz',
'pse.a16.1.92.csv.gz',
'pse.a16.1.93.csv.gz',
'pse.a16.1.94.csv.gz',
'pse.a16.1.95.csv.gz',
'pse.a16.1.96.csv.gz',
'pse.a16.1.97.csv.gz',
'pse.a16.1.98.csv.gz',
'pse.a16.1.99.csv.gz',
'pse.a16.12.29.csv.gz',
'pse.a16.12.30.csv.gz',
'pse.a16.12.31.csv.gz',
'pse.a16.2.1.csv.gz',
'pse.a16.2.10.csv.gz',
'pse.a16.2.100.csv.gz',
'pse.a16.2.101.csv.gz',
'pse.a16.2.102.csv.gz',
'pse.a16.2.103.csv.gz',
'pse.a16.2.104.csv.gz',
'pse.a16.2.105.csv.gz',
'pse.a16.2.106.csv.gz',
'pse.a16.2.107.csv.gz',
'pse.a16.2.108.csv.gz',
'pse.a16.2.109.csv.gz',
'pse.a16.2.11.csv.gz',
'pse.a16.2.110.csv.gz',
'pse.a16.2.111.csv.gz',
'pse.a16.2.112.csv.gz',
'pse.a16.2.113.csv.gz',
'pse.a16.2.114.csv.gz',
'pse.a16.2.115.csv.gz',
'pse.a16.2.116.csv.gz',
'pse.a16.2.117.csv.gz',
'pse.a16.2.118.csv.gz',
'pse.a16.2.119.csv.gz',
'pse.a16.2.12.csv.gz',
'pse.a16.2.120.csv.gz',
'pse.a16.2.121.csv.gz',
'pse.a16.2.122.csv.gz',
'pse.a16.2.123.csv.gz',
'pse.a16.2.124.csv.gz',
'pse.a16.2.125.csv.gz',
'pse.a16.2.126.csv.gz',
'pse.a16.2.127.csv.gz',
'pse.a16.2.128.csv.gz',
'pse.a16.2.129.csv.gz',
'pse.a16.2.13.csv.gz',
'pse.a16.2.130.csv.gz',
'pse.a16.2.131.csv.gz',
'pse.a16.2.132.csv.gz',
'pse.a16.2.133.csv.gz',
'pse.a16.2.134.csv.gz',
'pse.a16.2.135.csv.gz',
'pse.a16.2.136.csv.gz',
'pse.a16.2.137.csv.gz',
'pse.a16.2.138.csv.gz',
'pse.a16.2.139.csv.gz',
'pse.a16.2.14.csv.gz',
'pse.a16.2.140.csv.gz',
'pse.a16.2.141.csv.gz',
'pse.a16.2.142.csv.gz',
'pse.a16.2.143.csv.gz',
'pse.a16.2.144.csv.gz',
'pse.a16.2.145.csv.gz',
'pse.a16.2.146.csv.gz',
'pse.a16.2.147.csv.gz',
'pse.a16.2.148.csv.gz',
'pse.a16.2.149.csv.gz',
'pse.a16.2.15.csv.gz',
'pse.a16.2.150.csv.gz',
'pse.a16.2.151.csv.gz',
'pse.a16.2.152.csv.gz',
'pse.a16.2.153.csv.gz',
'pse.a16.2.154.csv.gz',
'pse.a16.2.155.csv.gz',
'pse.a16.2.156.csv.gz',
'pse.a16.2.157.csv.gz',
'pse.a16.2.158.csv.gz',
'pse.a16.2.159.csv.gz',
'pse.a16.2.16.csv.gz',
'pse.a16.2.160.csv.gz',
'pse.a16.2.161.csv.gz',
'pse.a16.2.162.csv.gz',
'pse.a16.2.163.csv.gz',
'pse.a16.2.164.csv.gz',
'pse.a16.2.165.csv.gz',
'pse.a16.2.166.csv.gz',
'pse.a16.2.167.csv.gz',
'pse.a16.2.168.csv.gz',
'pse.a16.2.169.csv.gz',
'pse.a16.2.17.csv.gz',
'pse.a16.2.170.csv.gz',
'pse.a16.2.171.csv.gz',
'pse.a16.2.172.csv.gz',
'pse.a16.2.173.csv.gz',
'pse.a16.2.174.csv.gz',
'pse.a16.2.175.csv.gz',
'pse.a16.2.176.csv.gz',
'pse.a16.2.177.csv.gz',
'pse.a16.2.18.csv.gz',
'pse.a16.2.19.csv.gz',
'pse.a16.2.2.csv.gz',
'pse.a16.2.20.csv.gz',
'pse.a16.2.21.csv.gz',
'pse.a16.2.22.csv.gz',
'pse.a16.2.23.csv.gz',
'pse.a16.2.24.csv.gz',
'pse.a16.2.25.csv.gz',
'pse.a16.2.26.csv.gz',
'pse.a16.2.27.csv.gz',
'pse.a16.2.28.csv.gz',
'pse.a16.2.29.csv.gz',
'pse.a16.2.3.csv.gz',
'pse.a16.2.30.csv.gz',
'pse.a16.2.31.csv.gz',
'pse.a16.2.32.csv.gz',
'pse.a16.2.33.csv.gz',
'pse.a16.2.34.csv.gz',
'pse.a16.2.35.csv.gz',
'pse.a16.2.36.csv.gz',
'pse.a16.2.37.csv.gz',
'pse.a16.2.38.csv.gz',
'pse.a16.2.39.csv.gz',
'pse.a16.2.4.csv.gz',
'pse.a16.2.40.csv.gz',
'pse.a16.2.41.csv.gz',
'pse.a16.2.42.csv.gz',
'pse.a16.2.43.csv.gz',
'pse.a16.2.44.csv.gz',
'pse.a16.2.45.csv.gz',
'pse.a16.2.46.csv.gz',
'pse.a16.2.47.csv.gz',
'pse.a16.2.48.csv.gz',
'pse.a16.2.49.csv.gz',
'pse.a16.2.5.csv.gz',
'pse.a16.2.50.csv.gz',
'pse.a16.2.51.csv.gz',
'pse.a16.2.52.csv.gz',
'pse.a16.2.53.csv.gz',
'pse.a16.2.54.csv.gz',
'pse.a16.2.55.csv.gz',
'pse.a16.2.56.csv.gz',
'pse.a16.2.57.csv.gz',
'pse.a16.2.58.csv.gz',
'pse.a16.2.59.csv.gz',
'pse.a16.2.6.csv.gz',
'pse.a16.2.60.csv.gz',
'pse.a16.2.61.csv.gz',
'pse.a16.2.62.csv.gz',
'pse.a16.2.63.csv.gz',
'pse.a16.2.64.csv.gz',
'pse.a16.2.65.csv.gz',
'pse.a16.2.66.csv.gz',
'pse.a16.2.67.csv.gz',
'pse.a16.2.68.csv.gz',
'pse.a16.2.69.csv.gz',
'pse.a16.2.7.csv.gz',
'pse.a16.2.70.csv.gz',
'pse.a16.2.71.csv.gz',
'pse.a16.2.72.csv.gz',
'pse.a16.2.73.csv.gz',
'pse.a16.2.74.csv.gz',
'pse.a16.2.75.csv.gz',
'pse.a16.2.76.csv.gz',
'pse.a16.2.77.csv.gz',
'pse.a16.2.78.csv.gz',
'pse.a16.2.79.csv.gz',
'pse.a16.2.8.csv.gz',
'pse.a16.2.80.csv.gz',
'pse.a16.2.81.csv.gz',
'pse.a16.2.82.csv.gz',
'pse.a16.2.83.csv.gz',
'pse.a16.2.84.csv.gz',
'pse.a16.2.85.csv.gz',
'pse.a16.2.86.csv.gz',
'pse.a16.2.87.csv.gz',
'pse.a16.2.88.csv.gz',
'pse.a16.2.89.csv.gz',
'pse.a16.2.9.csv.gz',
'pse.a16.2.90.csv.gz',
'pse.a16.2.91.csv.gz',
'pse.a16.2.92.csv.gz',
'pse.a16.2.93.csv.gz',
'pse.a16.2.94.csv.gz',
'pse.a16.2.95.csv.gz',
'pse.a16.2.96.csv.gz',
'pse.a16.2.97.csv.gz',
'pse.a16.2.98.csv.gz',
'pse.a16.2.99.csv.gz',
'pse.a16.3.1.csv.gz',
'pse.a16.3.10.csv.gz',
'pse.a16.3.100.csv.gz',
'pse.a16.3.101.csv.gz',
'pse.a16.3.102.csv.gz',
'pse.a16.3.103.csv.gz',
'pse.a16.3.104.csv.gz',
'pse.a16.3.105.csv.gz',
'pse.a16.3.106.csv.gz',
'pse.a16.3.107.csv.gz',
'pse.a16.3.108.csv.gz',
'pse.a16.3.109.csv.gz',
'pse.a16.3.11.csv.gz',
'pse.a16.3.110.csv.gz',
'pse.a16.3.111.csv.gz',
'pse.a16.3.112.csv.gz',
'pse.a16.3.113.csv.gz',
'pse.a16.3.114.csv.gz',
'pse.a16.3.115.csv.gz',
'pse.a16.3.116.csv.gz',
'pse.a16.3.117.csv.gz',
'pse.a16.3.118.csv.gz',
'pse.a16.3.119.csv.gz',
'pse.a16.3.12.csv.gz',
'pse.a16.3.120.csv.gz',
'pse.a16.3.121.csv.gz',
'pse.a16.3.122.csv.gz',
'pse.a16.3.123.csv.gz',
'pse.a16.3.124.csv.gz',
'pse.a16.3.125.csv.gz',
'pse.a16.3.126.csv.gz',
'pse.a16.3.127.csv.gz',
'pse.a16.3.128.csv.gz',
'pse.a16.3.129.csv.gz',
'pse.a16.3.13.csv.gz',
'pse.a16.3.130.csv.gz',
'pse.a16.3.131.csv.gz',
'pse.a16.3.132.csv.gz',
'pse.a16.3.133.csv.gz',
'pse.a16.3.134.csv.gz',
'pse.a16.3.135.csv.gz',
'pse.a16.3.136.csv.gz',
'pse.a16.3.137.csv.gz',
'pse.a16.3.138.csv.gz',
'pse.a16.3.139.csv.gz',
'pse.a16.3.14.csv.gz',
'pse.a16.3.140.csv.gz',
'pse.a16.3.141.csv.gz',
'pse.a16.3.142.csv.gz',
'pse.a16.3.143.csv.gz',
'pse.a16.3.144.csv.gz',
'pse.a16.3.145.csv.gz',
'pse.a16.3.146.csv.gz',
'pse.a16.3.147.csv.gz',
'pse.a16.3.148.csv.gz',
'pse.a16.3.149.csv.gz',
'pse.a16.3.15.csv.gz',
'pse.a16.3.150.csv.gz',
'pse.a16.3.151.csv.gz',
'pse.a16.3.152.csv.gz',
'pse.a16.3.153.csv.gz',
'pse.a16.3.154.csv.gz',
'pse.a16.3.155.csv.gz',
'pse.a16.3.156.csv.gz',
'pse.a16.3.157.csv.gz',
'pse.a16.3.158.csv.gz',
'pse.a16.3.159.csv.gz',
'pse.a16.3.16.csv.gz',
'pse.a16.3.160.csv.gz',
'pse.a16.3.161.csv.gz',
'pse.a16.3.162.csv.gz',
'pse.a16.3.163.csv.gz',
'pse.a16.3.164.csv.gz',
'pse.a16.3.165.csv.gz',
'pse.a16.3.166.csv.gz',
'pse.a16.3.167.csv.gz',
'pse.a16.3.168.csv.gz',
'pse.a16.3.169.csv.gz',
'pse.a16.3.17.csv.gz',
'pse.a16.3.170.csv.gz',
'pse.a16.3.171.csv.gz',
'pse.a16.3.172.csv.gz',
'pse.a16.3.173.csv.gz',
'pse.a16.3.174.csv.gz',
'pse.a16.3.175.csv.gz',
'pse.a16.3.176.csv.gz',
'pse.a16.3.177.csv.gz',
'pse.a16.3.178.csv.gz',
'pse.a16.3.18.csv.gz',
'pse.a16.3.19.csv.gz',
'pse.a16.3.2.csv.gz',
'pse.a16.3.20.csv.gz',
'pse.a16.3.21.csv.gz',
'pse.a16.3.22.csv.gz',
'pse.a16.3.23.csv.gz',
'pse.a16.3.24.csv.gz',
'pse.a16.3.25.csv.gz',
'pse.a16.3.26.csv.gz',
'pse.a16.3.27.csv.gz',
'pse.a16.3.28.csv.gz',
'pse.a16.3.29.csv.gz',
'pse.a16.3.3.csv.gz',
'pse.a16.3.30.csv.gz',
'pse.a16.3.31.csv.gz',
'pse.a16.3.32.csv.gz',
'pse.a16.3.33.csv.gz',
'pse.a16.3.34.csv.gz',
'pse.a16.3.35.csv.gz',
'pse.a16.3.36.csv.gz',
'pse.a16.3.37.csv.gz',
'pse.a16.3.38.csv.gz',
'pse.a16.3.39.csv.gz',
'pse.a16.3.4.csv.gz',
'pse.a16.3.40.csv.gz',
'pse.a16.3.41.csv.gz',
'pse.a16.3.42.csv.gz',
'pse.a16.3.43.csv.gz',
'pse.a16.3.44.csv.gz',
'pse.a16.3.45.csv.gz',
'pse.a16.3.46.csv.gz',
'pse.a16.3.47.csv.gz',
'pse.a16.3.48.csv.gz',
'pse.a16.3.49.csv.gz',
'pse.a16.3.5.csv.gz',
'pse.a16.3.50.csv.gz',
'pse.a16.3.51.csv.gz',
'pse.a16.3.52.csv.gz',
'pse.a16.3.53.csv.gz',
'pse.a16.3.54.csv.gz',
'pse.a16.3.55.csv.gz',
'pse.a16.3.56.csv.gz',
'pse.a16.3.57.csv.gz',
'pse.a16.3.58.csv.gz',
'pse.a16.3.59.csv.gz',
'pse.a16.3.6.csv.gz',
'pse.a16.3.60.csv.gz',
'pse.a16.3.61.csv.gz',
'pse.a16.3.62.csv.gz',
'pse.a16.3.63.csv.gz',
'pse.a16.3.64.csv.gz',
'pse.a16.3.65.csv.gz',
'pse.a16.3.66.csv.gz',
'pse.a16.3.67.csv.gz',
'pse.a16.3.68.csv.gz',
'pse.a16.3.69.csv.gz',
'pse.a16.3.7.csv.gz',
'pse.a16.3.70.csv.gz',
'pse.a16.3.71.csv.gz',
'pse.a16.3.72.csv.gz',
'pse.a16.3.73.csv.gz',
'pse.a16.3.74.csv.gz',
'pse.a16.3.75.csv.gz',
'pse.a16.3.76.csv.gz',
'pse.a16.3.77.csv.gz',
'pse.a16.3.78.csv.gz',
'pse.a16.3.79.csv.gz',
'pse.a16.3.8.csv.gz',
'pse.a16.3.80.csv.gz',
'pse.a16.3.81.csv.gz',
'pse.a16.3.82.csv.gz',
'pse.a16.3.83.csv.gz',
'pse.a16.3.84.csv.gz',
'pse.a16.3.85.csv.gz',
'pse.a16.3.86.csv.gz',
'pse.a16.3.87.csv.gz',
'pse.a16.3.88.csv.gz',
'pse.a16.3.89.csv.gz',
'pse.a16.3.9.csv.gz',
'pse.a16.3.90.csv.gz',
'pse.a16.3.91.csv.gz',
'pse.a16.3.92.csv.gz',
'pse.a16.3.93.csv.gz',
'pse.a16.3.94.csv.gz',
'pse.a16.3.95.csv.gz',
'pse.a16.3.96.csv.gz',
'pse.a16.3.97.csv.gz',
'pse.a16.3.98.csv.gz',
'pse.a16.3.99.csv.gz',
'pse.a16.4.1.csv.gz',
'pse.a16.4.10.csv.gz',
'pse.a16.4.100.csv.gz',
'pse.a16.4.101.csv.gz',
'pse.a16.4.102.csv.gz',
'pse.a16.4.103.csv.gz',
'pse.a16.4.104.csv.gz',
'pse.a16.4.105.csv.gz',
'pse.a16.4.106.csv.gz',
'pse.a16.4.107.csv.gz',
'pse.a16.4.108.csv.gz',
'pse.a16.4.109.csv.gz',
'pse.a16.4.11.csv.gz',
'pse.a16.4.110.csv.gz',
'pse.a16.4.111.csv.gz',
'pse.a16.4.112.csv.gz',
'pse.a16.4.113.csv.gz',
'pse.a16.4.114.csv.gz',
'pse.a16.4.115.csv.gz',
'pse.a16.4.116.csv.gz',
'pse.a16.4.117.csv.gz',
'pse.a16.4.118.csv.gz',
'pse.a16.4.119.csv.gz',
'pse.a16.4.12.csv.gz',
'pse.a16.4.120.csv.gz',
'pse.a16.4.121.csv.gz',
'pse.a16.4.122.csv.gz',
'pse.a16.4.123.csv.gz',
'pse.a16.4.124.csv.gz',
'pse.a16.4.125.csv.gz',
'pse.a16.4.126.csv.gz',
'pse.a16.4.127.csv.gz',
'pse.a16.4.128.csv.gz',
'pse.a16.4.129.csv.gz',
'pse.a16.4.13.csv.gz',
'pse.a16.4.130.csv.gz',
'pse.a16.4.131.csv.gz',
'pse.a16.4.132.csv.gz',
'pse.a16.4.133.csv.gz',
'pse.a16.4.134.csv.gz',
'pse.a16.4.135.csv.gz',
'pse.a16.4.136.csv.gz',
'pse.a16.4.137.csv.gz',
'pse.a16.4.138.csv.gz',
'pse.a16.4.139.csv.gz',
'pse.a16.4.14.csv.gz',
'pse.a16.4.140.csv.gz',
'pse.a16.4.141.csv.gz',
'pse.a16.4.142.csv.gz',
'pse.a16.4.143.csv.gz',
'pse.a16.4.144.csv.gz',
'pse.a16.4.145.csv.gz',
'pse.a16.4.146.csv.gz',
'pse.a16.4.147.csv.gz',
'pse.a16.4.148.csv.gz',
'pse.a16.4.149.csv.gz',
'pse.a16.4.15.csv.gz',
'pse.a16.4.150.csv.gz',
'pse.a16.4.151.csv.gz',
'pse.a16.4.152.csv.gz',
'pse.a16.4.153.csv.gz',
'pse.a16.4.154.csv.gz',
'pse.a16.4.155.csv.gz',
'pse.a16.4.156.csv.gz',
'pse.a16.4.157.csv.gz',
'pse.a16.4.158.csv.gz',
'pse.a16.4.159.csv.gz',
'pse.a16.4.16.csv.gz',
'pse.a16.4.160.csv.gz',
'pse.a16.4.161.csv.gz',
'pse.a16.4.162.csv.gz',
'pse.a16.4.163.csv.gz',
'pse.a16.4.164.csv.gz',
'pse.a16.4.165.csv.gz',
'pse.a16.4.166.csv.gz',
'pse.a16.4.167.csv.gz',
'pse.a16.4.168.csv.gz',
'pse.a16.4.169.csv.gz',
'pse.a16.4.17.csv.gz',
'pse.a16.4.170.csv.gz',
'pse.a16.4.171.csv.gz',
'pse.a16.4.172.csv.gz',
'pse.a16.4.173.csv.gz',
'pse.a16.4.174.csv.gz',
'pse.a16.4.175.csv.gz',
'pse.a16.4.176.csv.gz',
'pse.a16.4.177.csv.gz',
'pse.a16.4.178.csv.gz',
'pse.a16.4.179.csv.gz',
'pse.a16.4.18.csv.gz',
'pse.a16.4.180.csv.gz',
'pse.a16.4.19.csv.gz',
'pse.a16.4.2.csv.gz',
'pse.a16.4.20.csv.gz',
'pse.a16.4.21.csv.gz',
'pse.a16.4.22.csv.gz',
'pse.a16.4.23.csv.gz',
'pse.a16.4.24.csv.gz',
'pse.a16.4.25.csv.gz',
'pse.a16.4.26.csv.gz',
'pse.a16.4.27.csv.gz',
'pse.a16.4.28.csv.gz',
'pse.a16.4.29.csv.gz',
'pse.a16.4.3.csv.gz',
'pse.a16.4.30.csv.gz',
'pse.a16.4.31.csv.gz',
'pse.a16.4.32.csv.gz',
'pse.a16.4.33.csv.gz',
'pse.a16.4.34.csv.gz',
'pse.a16.4.35.csv.gz',
'pse.a16.4.36.csv.gz',
'pse.a16.4.37.csv.gz',
'pse.a16.4.38.csv.gz',
'pse.a16.4.39.csv.gz',
'pse.a16.4.4.csv.gz',
'pse.a16.4.40.csv.gz',
'pse.a16.4.41.csv.gz',
'pse.a16.4.42.csv.gz',
'pse.a16.4.43.csv.gz',
'pse.a16.4.44.csv.gz',
'pse.a16.4.45.csv.gz',
'pse.a16.4.46.csv.gz',
'pse.a16.4.47.csv.gz',
'pse.a16.4.48.csv.gz',
'pse.a16.4.49.csv.gz',
'pse.a16.4.5.csv.gz',
'pse.a16.4.50.csv.gz',
'pse.a16.4.51.csv.gz',
'pse.a16.4.52.csv.gz',
'pse.a16.4.53.csv.gz',
'pse.a16.4.54.csv.gz',
'pse.a16.4.55.csv.gz',
'pse.a16.4.56.csv.gz',
'pse.a16.4.57.csv.gz',
'pse.a16.4.58.csv.gz',
'pse.a16.4.59.csv.gz',
'pse.a16.4.6.csv.gz',
'pse.a16.4.60.csv.gz',
'pse.a16.4.61.csv.gz',
'pse.a16.4.62.csv.gz',
'pse.a16.4.63.csv.gz',
'pse.a16.4.64.csv.gz',
'pse.a16.4.65.csv.gz',
'pse.a16.4.66.csv.gz',
'pse.a16.4.67.csv.gz',
'pse.a16.4.68.csv.gz',
'pse.a16.4.69.csv.gz',
'pse.a16.4.7.csv.gz',
'pse.a16.4.70.csv.gz',
'pse.a16.4.71.csv.gz',
'pse.a16.4.72.csv.gz',
'pse.a16.4.73.csv.gz',
'pse.a16.4.74.csv.gz',
'pse.a16.4.75.csv.gz',
'pse.a16.4.76.csv.gz',
'pse.a16.4.77.csv.gz',
'pse.a16.4.78.csv.gz',
'pse.a16.4.79.csv.gz',
'pse.a16.4.8.csv.gz',
'pse.a16.4.80.csv.gz',
'pse.a16.4.81.csv.gz',
'pse.a16.4.82.csv.gz',
'pse.a16.4.83.csv.gz',
'pse.a16.4.84.csv.gz',
'pse.a16.4.85.csv.gz',
'pse.a16.4.86.csv.gz',
'pse.a16.4.87.csv.gz',
'pse.a16.4.88.csv.gz',
'pse.a16.4.89.csv.gz',
'pse.a16.4.9.csv.gz',
'pse.a16.4.90.csv.gz',
'pse.a16.4.91.csv.gz',
'pse.a16.4.92.csv.gz',
'pse.a16.4.93.csv.gz',
'pse.a16.4.94.csv.gz',
'pse.a16.4.95.csv.gz',
'pse.a16.4.96.csv.gz',
'pse.a16.4.97.csv.gz',
'pse.a16.4.98.csv.gz',
'pse.a16.4.99.csv.gz',
'pse.a16.5.1.csv.gz',
'pse.a16.5.10.csv.gz',
'pse.a16.5.100.csv.gz',
'pse.a16.5.101.csv.gz',
'pse.a16.5.102.csv.gz',
'pse.a16.5.103.csv.gz',
'pse.a16.5.104.csv.gz',
'pse.a16.5.105.csv.gz',
'pse.a16.5.106.csv.gz',
'pse.a16.5.107.csv.gz',
'pse.a16.5.108.csv.gz',
'pse.a16.5.109.csv.gz',
'pse.a16.5.11.csv.gz',
'pse.a16.5.110.csv.gz',
'pse.a16.5.111.csv.gz',
'pse.a16.5.112.csv.gz',
'pse.a16.5.113.csv.gz',
'pse.a16.5.114.csv.gz',
'pse.a16.5.115.csv.gz',
'pse.a16.5.116.csv.gz',
'pse.a16.5.117.csv.gz',
'pse.a16.5.118.csv.gz',
'pse.a16.5.119.csv.gz',
'pse.a16.5.12.csv.gz',
'pse.a16.5.120.csv.gz',
'pse.a16.5.121.csv.gz',
'pse.a16.5.122.csv.gz',
'pse.a16.5.123.csv.gz',
'pse.a16.5.124.csv.gz',
'pse.a16.5.125.csv.gz',
'pse.a16.5.126.csv.gz',
'pse.a16.5.127.csv.gz',
'pse.a16.5.128.csv.gz',
'pse.a16.5.129.csv.gz',
'pse.a16.5.13.csv.gz',
'pse.a16.5.130.csv.gz',
'pse.a16.5.131.csv.gz',
'pse.a16.5.132.csv.gz',
'pse.a16.5.133.csv.gz',
'pse.a16.5.134.csv.gz',
'pse.a16.5.135.csv.gz',
'pse.a16.5.136.csv.gz',
'pse.a16.5.137.csv.gz',
'pse.a16.5.138.csv.gz',
'pse.a16.5.139.csv.gz',
'pse.a16.5.14.csv.gz',
'pse.a16.5.140.csv.gz',
'pse.a16.5.141.csv.gz',
'pse.a16.5.142.csv.gz',
'pse.a16.5.143.csv.gz',
'pse.a16.5.144.csv.gz',
'pse.a16.5.145.csv.gz',
'pse.a16.5.146.csv.gz',
'pse.a16.5.147.csv.gz',
'pse.a16.5.148.csv.gz',
'pse.a16.5.149.csv.gz',
'pse.a16.5.15.csv.gz',
'pse.a16.5.150.csv.gz',
'pse.a16.5.151.csv.gz',
'pse.a16.5.152.csv.gz',
'pse.a16.5.153.csv.gz',
'pse.a16.5.154.csv.gz',
'pse.a16.5.155.csv.gz',
'pse.a16.5.156.csv.gz',
'pse.a16.5.157.csv.gz',
'pse.a16.5.158.csv.gz',
'pse.a16.5.159.csv.gz',
'pse.a16.5.16.csv.gz',
'pse.a16.5.160.csv.gz',
'pse.a16.5.161.csv.gz',
'pse.a16.5.162.csv.gz',
'pse.a16.5.163.csv.gz',
'pse.a16.5.164.csv.gz',
'pse.a16.5.165.csv.gz',
'pse.a16.5.166.csv.gz',
'pse.a16.5.167.csv.gz',
'pse.a16.5.168.csv.gz',
'pse.a16.5.169.csv.gz',
'pse.a16.5.17.csv.gz',
'pse.a16.5.170.csv.gz',
'pse.a16.5.171.csv.gz',
'pse.a16.5.172.csv.gz',
'pse.a16.5.173.csv.gz',
'pse.a16.5.174.csv.gz',
'pse.a16.5.175.csv.gz',
'pse.a16.5.176.csv.gz',
'pse.a16.5.177.csv.gz',
'pse.a16.5.178.csv.gz',
'pse.a16.5.179.csv.gz',
'pse.a16.5.18.csv.gz',
'pse.a16.5.180.csv.gz',
'pse.a16.5.19.csv.gz',
'pse.a16.5.2.csv.gz',
'pse.a16.5.20.csv.gz',
'pse.a16.5.21.csv.gz',
'pse.a16.5.22.csv.gz',
'pse.a16.5.23.csv.gz',
'pse.a16.5.24.csv.gz',
'pse.a16.5.25.csv.gz',
'pse.a16.5.26.csv.gz',
'pse.a16.5.27.csv.gz',
'pse.a16.5.28.csv.gz',
'pse.a16.5.29.csv.gz',
'pse.a16.5.3.csv.gz',
'pse.a16.5.30.csv.gz',
'pse.a16.5.31.csv.gz',
'pse.a16.5.32.csv.gz',
'pse.a16.5.33.csv.gz',
'pse.a16.5.34.csv.gz',
'pse.a16.5.35.csv.gz',
'pse.a16.5.36.csv.gz',
'pse.a16.5.37.csv.gz',
'pse.a16.5.38.csv.gz',
'pse.a16.5.39.csv.gz',
'pse.a16.5.4.csv.gz',
'pse.a16.5.40.csv.gz',
'pse.a16.5.41.csv.gz',
'pse.a16.5.42.csv.gz',
'pse.a16.5.43.csv.gz',
'pse.a16.5.44.csv.gz',
'pse.a16.5.45.csv.gz',
'pse.a16.5.46.csv.gz',
'pse.a16.5.47.csv.gz',
'pse.a16.5.48.csv.gz',
'pse.a16.5.49.csv.gz',
'pse.a16.5.5.csv.gz',
'pse.a16.5.50.csv.gz',
'pse.a16.5.51.csv.gz',
'pse.a16.5.52.csv.gz',
'pse.a16.5.53.csv.gz',
'pse.a16.5.54.csv.gz',
'pse.a16.5.55.csv.gz',
'pse.a16.5.56.csv.gz',
'pse.a16.5.57.csv.gz',
'pse.a16.5.58.csv.gz',
'pse.a16.5.59.csv.gz',
'pse.a16.5.6.csv.gz',
'pse.a16.5.60.csv.gz',
'pse.a16.5.61.csv.gz',
'pse.a16.5.62.csv.gz',
'pse.a16.5.63.csv.gz',
'pse.a16.5.64.csv.gz',
'pse.a16.5.65.csv.gz',
'pse.a16.5.66.csv.gz',
'pse.a16.5.67.csv.gz',
'pse.a16.5.68.csv.gz',
'pse.a16.5.69.csv.gz',
'pse.a16.5.7.csv.gz',
'pse.a16.5.70.csv.gz',
'pse.a16.5.71.csv.gz',
'pse.a16.5.72.csv.gz',
'pse.a16.5.73.csv.gz',
'pse.a16.5.74.csv.gz',
'pse.a16.5.75.csv.gz',
'pse.a16.5.76.csv.gz',
'pse.a16.5.77.csv.gz',
'pse.a16.5.78.csv.gz',
'pse.a16.5.79.csv.gz',
'pse.a16.5.8.csv.gz',
'pse.a16.5.80.csv.gz',
'pse.a16.5.81.csv.gz',
'pse.a16.5.82.csv.gz',
'pse.a16.5.83.csv.gz',
'pse.a16.5.84.csv.gz',
'pse.a16.5.85.csv.gz',
'pse.a16.5.86.csv.gz',
'pse.a16.5.87.csv.gz',
'pse.a16.5.88.csv.gz',
'pse.a16.5.89.csv.gz',
'pse.a16.5.9.csv.gz',
'pse.a16.5.90.csv.gz',
'pse.a16.5.91.csv.gz',
'pse.a16.5.92.csv.gz',
'pse.a16.5.93.csv.gz',
'pse.a16.5.94.csv.gz',
'pse.a16.5.95.csv.gz',
'pse.a16.5.96.csv.gz',
'pse.a16.5.97.csv.gz',
'pse.a16.5.98.csv.gz',
'pse.a16.5.99.csv.gz',
'pse.a16.6.1.csv.gz',
'pse.a16.6.10.csv.gz',
'pse.a16.6.100.csv.gz',
'pse.a16.6.101.csv.gz',
'pse.a16.6.102.csv.gz',
'pse.a16.6.103.csv.gz',
'pse.a16.6.104.csv.gz',
'pse.a16.6.105.csv.gz',
'pse.a16.6.106.csv.gz',
'pse.a16.6.107.csv.gz',
'pse.a16.6.108.csv.gz',
'pse.a16.6.109.csv.gz',
'pse.a16.6.11.csv.gz',
'pse.a16.6.110.csv.gz',
'pse.a16.6.111.csv.gz',
'pse.a16.6.112.csv.gz',
'pse.a16.6.113.csv.gz',
'pse.a16.6.114.csv.gz',
'pse.a16.6.115.csv.gz',
'pse.a16.6.116.csv.gz',
'pse.a16.6.117.csv.gz',
'pse.a16.6.118.csv.gz',
'pse.a16.6.119.csv.gz',
'pse.a16.6.12.csv.gz',
'pse.a16.6.120.csv.gz',
'pse.a16.6.121.csv.gz',
'pse.a16.6.122.csv.gz',
'pse.a16.6.123.csv.gz',
'pse.a16.6.124.csv.gz',
'pse.a16.6.125.csv.gz',
'pse.a16.6.126.csv.gz',
'pse.a16.6.127.csv.gz',
'pse.a16.6.128.csv.gz',
'pse.a16.6.129.csv.gz',
'pse.a16.6.13.csv.gz',
'pse.a16.6.130.csv.gz',
'pse.a16.6.131.csv.gz',
'pse.a16.6.132.csv.gz',
'pse.a16.6.133.csv.gz',
'pse.a16.6.134.csv.gz',
'pse.a16.6.135.csv.gz',
'pse.a16.6.136.csv.gz',
'pse.a16.6.137.csv.gz',
'pse.a16.6.138.csv.gz',
'pse.a16.6.139.csv.gz',
'pse.a16.6.14.csv.gz',
'pse.a16.6.140.csv.gz',
'pse.a16.6.141.csv.gz',
'pse.a16.6.142.csv.gz',
'pse.a16.6.143.csv.gz',
'pse.a16.6.144.csv.gz',
'pse.a16.6.145.csv.gz',
'pse.a16.6.146.csv.gz',
'pse.a16.6.147.csv.gz',
'pse.a16.6.148.csv.gz',
'pse.a16.6.149.csv.gz',
'pse.a16.6.15.csv.gz',
'pse.a16.6.150.csv.gz',
'pse.a16.6.151.csv.gz',
'pse.a16.6.152.csv.gz',
'pse.a16.6.153.csv.gz',
'pse.a16.6.154.csv.gz',
'pse.a16.6.155.csv.gz',
'pse.a16.6.156.csv.gz',
'pse.a16.6.157.csv.gz',
'pse.a16.6.158.csv.gz',
'pse.a16.6.159.csv.gz',
'pse.a16.6.16.csv.gz',
'pse.a16.6.160.csv.gz',
'pse.a16.6.161.csv.gz',
'pse.a16.6.162.csv.gz',
'pse.a16.6.163.csv.gz',
'pse.a16.6.164.csv.gz',
'pse.a16.6.165.csv.gz',
'pse.a16.6.166.csv.gz',
'pse.a16.6.167.csv.gz',
'pse.a16.6.168.csv.gz',
'pse.a16.6.169.csv.gz',
'pse.a16.6.17.csv.gz',
'pse.a16.6.170.csv.gz',
'pse.a16.6.171.csv.gz',
'pse.a16.6.172.csv.gz',
'pse.a16.6.173.csv.gz',
'pse.a16.6.174.csv.gz',
'pse.a16.6.18.csv.gz',
'pse.a16.6.19.csv.gz',
'pse.a16.6.2.csv.gz',
'pse.a16.6.20.csv.gz',
'pse.a16.6.21.csv.gz',
'pse.a16.6.22.csv.gz',
'pse.a16.6.23.csv.gz',
'pse.a16.6.24.csv.gz',
'pse.a16.6.25.csv.gz',
'pse.a16.6.26.csv.gz',
'pse.a16.6.27.csv.gz',
'pse.a16.6.28.csv.gz',
'pse.a16.6.29.csv.gz',
'pse.a16.6.3.csv.gz',
'pse.a16.6.30.csv.gz',
'pse.a16.6.31.csv.gz',
'pse.a16.6.32.csv.gz',
'pse.a16.6.33.csv.gz',
'pse.a16.6.34.csv.gz',
'pse.a16.6.35.csv.gz',
'pse.a16.6.36.csv.gz',
'pse.a16.6.37.csv.gz',
'pse.a16.6.38.csv.gz',
'pse.a16.6.39.csv.gz',
'pse.a16.6.4.csv.gz',
'pse.a16.6.40.csv.gz',
'pse.a16.6.41.csv.gz',
'pse.a16.6.42.csv.gz',
'pse.a16.6.43.csv.gz',
'pse.a16.6.44.csv.gz',
'pse.a16.6.45.csv.gz',
'pse.a16.6.46.csv.gz',
'pse.a16.6.47.csv.gz',
'pse.a16.6.48.csv.gz',
'pse.a16.6.49.csv.gz',
'pse.a16.6.5.csv.gz',
'pse.a16.6.50.csv.gz',
'pse.a16.6.51.csv.gz',
'pse.a16.6.52.csv.gz',
'pse.a16.6.53.csv.gz',
'pse.a16.6.54.csv.gz',
'pse.a16.6.55.csv.gz',
'pse.a16.6.56.csv.gz',
'pse.a16.6.57.csv.gz',
'pse.a16.6.58.csv.gz',
'pse.a16.6.59.csv.gz',
'pse.a16.6.6.csv.gz',
'pse.a16.6.60.csv.gz',
'pse.a16.6.61.csv.gz',
'pse.a16.6.62.csv.gz',
'pse.a16.6.63.csv.gz',
'pse.a16.6.64.csv.gz',
'pse.a16.6.65.csv.gz',
'pse.a16.6.66.csv.gz',
'pse.a16.6.67.csv.gz',
'pse.a16.6.68.csv.gz',
'pse.a16.6.69.csv.gz',
'pse.a16.6.7.csv.gz',
'pse.a16.6.70.csv.gz',
'pse.a16.6.71.csv.gz',
'pse.a16.6.72.csv.gz',
'pse.a16.6.73.csv.gz',
'pse.a16.6.74.csv.gz',
'pse.a16.6.75.csv.gz',
'pse.a16.6.76.csv.gz',
'pse.a16.6.77.csv.gz',
'pse.a16.6.78.csv.gz',
'pse.a16.6.79.csv.gz',
'pse.a16.6.8.csv.gz',
'pse.a16.6.80.csv.gz',
'pse.a16.6.81.csv.gz',
'pse.a16.6.82.csv.gz',
'pse.a16.6.83.csv.gz',
'pse.a16.6.84.csv.gz',
'pse.a16.6.85.csv.gz',
'pse.a16.6.86.csv.gz',
'pse.a16.6.87.csv.gz',
'pse.a16.6.88.csv.gz',
'pse.a16.6.89.csv.gz',
'pse.a16.6.9.csv.gz',
'pse.a16.6.90.csv.gz',
'pse.a16.6.91.csv.gz',
'pse.a16.6.92.csv.gz',
'pse.a16.6.93.csv.gz',
'pse.a16.6.94.csv.gz',
'pse.a16.6.95.csv.gz',
'pse.a16.6.96.csv.gz',
'pse.a16.6.97.csv.gz',
'pse.a16.6.98.csv.gz',
'pse.a16.6.99.csv.gz',
'pse.a16.7.1.csv.gz',
'pse.a16.7.10.csv.gz',
'pse.a16.7.100.csv.gz',
'pse.a16.7.101.csv.gz',
'pse.a16.7.102.csv.gz',
'pse.a16.7.103.csv.gz',
'pse.a16.7.104.csv.gz',
'pse.a16.7.105.csv.gz',
'pse.a16.7.106.csv.gz',
'pse.a16.7.107.csv.gz',
'pse.a16.7.108.csv.gz',
'pse.a16.7.109.csv.gz',
'pse.a16.7.11.csv.gz',
'pse.a16.7.110.csv.gz',
'pse.a16.7.111.csv.gz',
'pse.a16.7.112.csv.gz',
'pse.a16.7.113.csv.gz',
'pse.a16.7.114.csv.gz',
'pse.a16.7.115.csv.gz',
'pse.a16.7.116.csv.gz',
'pse.a16.7.117.csv.gz',
'pse.a16.7.118.csv.gz',
'pse.a16.7.119.csv.gz',
'pse.a16.7.12.csv.gz',
'pse.a16.7.120.csv.gz',
'pse.a16.7.121.csv.gz',
'pse.a16.7.122.csv.gz',
'pse.a16.7.123.csv.gz',
'pse.a16.7.124.csv.gz',
'pse.a16.7.125.csv.gz',
'pse.a16.7.126.csv.gz',
'pse.a16.7.127.csv.gz',
'pse.a16.7.128.csv.gz',
'pse.a16.7.129.csv.gz',
'pse.a16.7.13.csv.gz',
'pse.a16.7.130.csv.gz',
'pse.a16.7.131.csv.gz',
'pse.a16.7.132.csv.gz',
'pse.a16.7.133.csv.gz',
'pse.a16.7.134.csv.gz',
'pse.a16.7.135.csv.gz',
'pse.a16.7.136.csv.gz',
'pse.a16.7.137.csv.gz',
'pse.a16.7.138.csv.gz',
'pse.a16.7.139.csv.gz',
'pse.a16.7.14.csv.gz',
'pse.a16.7.140.csv.gz',
'pse.a16.7.141.csv.gz',
'pse.a16.7.142.csv.gz',
'pse.a16.7.143.csv.gz',
'pse.a16.7.144.csv.gz',
'pse.a16.7.145.csv.gz',
'pse.a16.7.146.csv.gz',
'pse.a16.7.147.csv.gz',
'pse.a16.7.148.csv.gz',
'pse.a16.7.149.csv.gz',
'pse.a16.7.15.csv.gz',
'pse.a16.7.150.csv.gz',
'pse.a16.7.151.csv.gz',
'pse.a16.7.152.csv.gz',
'pse.a16.7.153.csv.gz',
'pse.a16.7.154.csv.gz',
'pse.a16.7.155.csv.gz',
'pse.a16.7.156.csv.gz',
'pse.a16.7.157.csv.gz',
'pse.a16.7.158.csv.gz',
'pse.a16.7.159.csv.gz',
'pse.a16.7.16.csv.gz',
'pse.a16.7.160.csv.gz',
'pse.a16.7.161.csv.gz',
'pse.a16.7.162.csv.gz',
'pse.a16.7.163.csv.gz',
'pse.a16.7.164.csv.gz',
'pse.a16.7.165.csv.gz',
'pse.a16.7.166.csv.gz',
'pse.a16.7.167.csv.gz',
'pse.a16.7.168.csv.gz',
'pse.a16.7.169.csv.gz',
'pse.a16.7.17.csv.gz',
'pse.a16.7.170.csv.gz',
'pse.a16.7.171.csv.gz',
'pse.a16.7.172.csv.gz',
'pse.a16.7.173.csv.gz',
'pse.a16.7.174.csv.gz',
'pse.a16.7.175.csv.gz',
'pse.a16.7.18.csv.gz',
'pse.a16.7.19.csv.gz',
'pse.a16.7.2.csv.gz',
'pse.a16.7.20.csv.gz',
'pse.a16.7.21.csv.gz',
'pse.a16.7.22.csv.gz',
'pse.a16.7.23.csv.gz',
'pse.a16.7.24.csv.gz',
'pse.a16.7.25.csv.gz',
'pse.a16.7.26.csv.gz',
'pse.a16.7.27.csv.gz',
'pse.a16.7.28.csv.gz',
'pse.a16.7.29.csv.gz',
'pse.a16.7.3.csv.gz',
'pse.a16.7.30.csv.gz',
'pse.a16.7.31.csv.gz',
'pse.a16.7.32.csv.gz',
'pse.a16.7.33.csv.gz',
'pse.a16.7.34.csv.gz',
'pse.a16.7.35.csv.gz',
'pse.a16.7.36.csv.gz',
'pse.a16.7.37.csv.gz',
'pse.a16.7.38.csv.gz',
'pse.a16.7.39.csv.gz',
'pse.a16.7.4.csv.gz',
'pse.a16.7.40.csv.gz',
'pse.a16.7.41.csv.gz',
'pse.a16.7.42.csv.gz',
'pse.a16.7.43.csv.gz',
'pse.a16.7.44.csv.gz',
'pse.a16.7.45.csv.gz',
'pse.a16.7.46.csv.gz',
'pse.a16.7.47.csv.gz',
'pse.a16.7.48.csv.gz',
'pse.a16.7.49.csv.gz',
'pse.a16.7.5.csv.gz',
'pse.a16.7.50.csv.gz',
'pse.a16.7.51.csv.gz',
'pse.a16.7.52.csv.gz',
'pse.a16.7.53.csv.gz',
'pse.a16.7.54.csv.gz',
'pse.a16.7.55.csv.gz',
'pse.a16.7.56.csv.gz',
'pse.a16.7.57.csv.gz',
'pse.a16.7.58.csv.gz',
'pse.a16.7.59.csv.gz',
'pse.a16.7.6.csv.gz',
'pse.a16.7.60.csv.gz',
'pse.a16.7.61.csv.gz',
'pse.a16.7.62.csv.gz',
'pse.a16.7.63.csv.gz',
'pse.a16.7.64.csv.gz',
'pse.a16.7.65.csv.gz',
'pse.a16.7.66.csv.gz',
'pse.a16.7.67.csv.gz',
'pse.a16.7.68.csv.gz',
'pse.a16.7.69.csv.gz',
'pse.a16.7.7.csv.gz',
'pse.a16.7.70.csv.gz',
'pse.a16.7.71.csv.gz',
'pse.a16.7.72.csv.gz',
'pse.a16.7.73.csv.gz',
'pse.a16.7.74.csv.gz',
'pse.a16.7.75.csv.gz',
'pse.a16.7.76.csv.gz',
'pse.a16.7.77.csv.gz',
'pse.a16.7.78.csv.gz',
'pse.a16.7.79.csv.gz',
'pse.a16.7.8.csv.gz',
'pse.a16.7.80.csv.gz',
'pse.a16.7.81.csv.gz',
'pse.a16.7.82.csv.gz',
'pse.a16.7.83.csv.gz',
'pse.a16.7.84.csv.gz',
'pse.a16.7.85.csv.gz',
'pse.a16.7.86.csv.gz',
'pse.a16.7.87.csv.gz',
'pse.a16.7.88.csv.gz',
'pse.a16.7.89.csv.gz',
'pse.a16.7.9.csv.gz',
'pse.a16.7.90.csv.gz',
'pse.a16.7.91.csv.gz',
'pse.a16.7.92.csv.gz',
'pse.a16.7.93.csv.gz',
'pse.a16.7.94.csv.gz',
'pse.a16.7.95.csv.gz',
'pse.a16.7.96.csv.gz',
'pse.a16.7.97.csv.gz',
'pse.a16.7.98.csv.gz',
'pse.a16.7.99.csv.gz',
'pse.a16.8.1.csv.gz',
'pse.a16.8.10.csv.gz',
'pse.a16.8.100.csv.gz',
'pse.a16.8.101.csv.gz',
'pse.a16.8.102.csv.gz',
'pse.a16.8.103.csv.gz',
'pse.a16.8.104.csv.gz',
'pse.a16.8.105.csv.gz',
'pse.a16.8.106.csv.gz',
'pse.a16.8.107.csv.gz',
'pse.a16.8.108.csv.gz',
'pse.a16.8.109.csv.gz',
'pse.a16.8.11.csv.gz',
'pse.a16.8.110.csv.gz',
'pse.a16.8.111.csv.gz',
'pse.a16.8.112.csv.gz',
'pse.a16.8.113.csv.gz',
'pse.a16.8.114.csv.gz',
'pse.a16.8.115.csv.gz',
'pse.a16.8.116.csv.gz',
'pse.a16.8.117.csv.gz',
'pse.a16.8.118.csv.gz',
'pse.a16.8.119.csv.gz',
'pse.a16.8.12.csv.gz',
'pse.a16.8.120.csv.gz',
'pse.a16.8.121.csv.gz',
'pse.a16.8.122.csv.gz',
'pse.a16.8.123.csv.gz',
'pse.a16.8.124.csv.gz',
'pse.a16.8.125.csv.gz',
'pse.a16.8.126.csv.gz',
'pse.a16.8.127.csv.gz',
'pse.a16.8.128.csv.gz',
'pse.a16.8.129.csv.gz',
'pse.a16.8.13.csv.gz',
'pse.a16.8.130.csv.gz',
'pse.a16.8.131.csv.gz',
'pse.a16.8.132.csv.gz',
'pse.a16.8.133.csv.gz',
'pse.a16.8.134.csv.gz',
'pse.a16.8.135.csv.gz',
'pse.a16.8.136.csv.gz',
'pse.a16.8.137.csv.gz',
'pse.a16.8.138.csv.gz',
'pse.a16.8.139.csv.gz',
'pse.a16.8.14.csv.gz',
'pse.a16.8.140.csv.gz',
'pse.a16.8.141.csv.gz',
'pse.a16.8.142.csv.gz',
'pse.a16.8.143.csv.gz',
'pse.a16.8.144.csv.gz',
'pse.a16.8.145.csv.gz',
'pse.a16.8.146.csv.gz',
'pse.a16.8.147.csv.gz',
'pse.a16.8.148.csv.gz',
'pse.a16.8.149.csv.gz',
'pse.a16.8.15.csv.gz',
'pse.a16.8.150.csv.gz',
'pse.a16.8.151.csv.gz',
'pse.a16.8.152.csv.gz',
'pse.a16.8.153.csv.gz',
'pse.a16.8.154.csv.gz',
'pse.a16.8.155.csv.gz',
'pse.a16.8.156.csv.gz',
'pse.a16.8.157.csv.gz',
'pse.a16.8.158.csv.gz',
'pse.a16.8.159.csv.gz',
'pse.a16.8.16.csv.gz',
'pse.a16.8.160.csv.gz',
'pse.a16.8.161.csv.gz',
'pse.a16.8.162.csv.gz',
'pse.a16.8.163.csv.gz',
'pse.a16.8.164.csv.gz',
'pse.a16.8.165.csv.gz',
'pse.a16.8.166.csv.gz',
'pse.a16.8.167.csv.gz',
'pse.a16.8.168.csv.gz',
'pse.a16.8.169.csv.gz',
'pse.a16.8.17.csv.gz',
'pse.a16.8.170.csv.gz',
'pse.a16.8.171.csv.gz',
'pse.a16.8.172.csv.gz',
'pse.a16.8.173.csv.gz',
'pse.a16.8.174.csv.gz',
'pse.a16.8.175.csv.gz',
'pse.a16.8.18.csv.gz',
'pse.a16.8.19.csv.gz',
'pse.a16.8.2.csv.gz',
'pse.a16.8.20.csv.gz',
'pse.a16.8.21.csv.gz',
'pse.a16.8.22.csv.gz',
'pse.a16.8.23.csv.gz',
'pse.a16.8.24.csv.gz',
'pse.a16.8.25.csv.gz',
'pse.a16.8.26.csv.gz',
'pse.a16.8.27.csv.gz',
'pse.a16.8.28.csv.gz',
'pse.a16.8.29.csv.gz',
'pse.a16.8.3.csv.gz',
'pse.a16.8.30.csv.gz',
'pse.a16.8.31.csv.gz',
'pse.a16.8.32.csv.gz',
'pse.a16.8.33.csv.gz',
'pse.a16.8.34.csv.gz',
'pse.a16.8.35.csv.gz',
'pse.a16.8.36.csv.gz',
'pse.a16.8.37.csv.gz',
'pse.a16.8.38.csv.gz',
'pse.a16.8.39.csv.gz',
'pse.a16.8.4.csv.gz',
'pse.a16.8.40.csv.gz',
'pse.a16.8.41.csv.gz',
'pse.a16.8.42.csv.gz',
'pse.a16.8.43.csv.gz',
'pse.a16.8.44.csv.gz',
'pse.a16.8.45.csv.gz',
'pse.a16.8.46.csv.gz',
'pse.a16.8.47.csv.gz',
'pse.a16.8.48.csv.gz',
'pse.a16.8.49.csv.gz',
'pse.a16.8.5.csv.gz',
'pse.a16.8.50.csv.gz',
'pse.a16.8.51.csv.gz',
'pse.a16.8.52.csv.gz',
'pse.a16.8.53.csv.gz',
'pse.a16.8.54.csv.gz',
'pse.a16.8.55.csv.gz',
'pse.a16.8.56.csv.gz',
'pse.a16.8.57.csv.gz',
'pse.a16.8.58.csv.gz',
'pse.a16.8.59.csv.gz',
'pse.a16.8.6.csv.gz',
'pse.a16.8.60.csv.gz',
'pse.a16.8.61.csv.gz',
'pse.a16.8.62.csv.gz',
'pse.a16.8.63.csv.gz',
'pse.a16.8.64.csv.gz',
'pse.a16.8.65.csv.gz',
'pse.a16.8.66.csv.gz',
'pse.a16.8.67.csv.gz',
'pse.a16.8.68.csv.gz',
'pse.a16.8.69.csv.gz',
'pse.a16.8.7.csv.gz',
'pse.a16.8.70.csv.gz',
'pse.a16.8.71.csv.gz',
'pse.a16.8.72.csv.gz',
'pse.a16.8.73.csv.gz',
'pse.a16.8.74.csv.gz',
'pse.a16.8.75.csv.gz',
'pse.a16.8.76.csv.gz',
'pse.a16.8.77.csv.gz',
'pse.a16.8.78.csv.gz',
'pse.a16.8.79.csv.gz',
'pse.a16.8.8.csv.gz',
'pse.a16.8.80.csv.gz',
'pse.a16.8.81.csv.gz',
'pse.a16.8.82.csv.gz',
'pse.a16.8.83.csv.gz',
'pse.a16.8.84.csv.gz',
'pse.a16.8.85.csv.gz',
'pse.a16.8.86.csv.gz',
'pse.a16.8.87.csv.gz',
'pse.a16.8.88.csv.gz',
'pse.a16.8.89.csv.gz',
'pse.a16.8.9.csv.gz',
'pse.a16.8.90.csv.gz',
'pse.a16.8.91.csv.gz',
'pse.a16.8.92.csv.gz',
'pse.a16.8.93.csv.gz',
'pse.a16.8.94.csv.gz',
'pse.a16.8.95.csv.gz',
'pse.a16.8.96.csv.gz',
'pse.a16.8.97.csv.gz',
'pse.a16.8.98.csv.gz',
'pse.a16.8.99.csv.gz',

    ]
    call_csv_check_work_tapes(checked_dir=checked_dir,processed_dir=processed_dir,log_dir=checked_dir,
      filenames=filenames,logging_level=logging.INFO
        # ,single_station='12'
        # ,single_ground_station=10
        )
# 10 12



if __name__ == "__main__":

    run_csv_check_work_tapes()

