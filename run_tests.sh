#!/bin/bash

test_case_path='tests/cases'
report_path='tests/reports'
lib_path='tests/lib'

# for anaconda install
/home/$(whoami)/anaconda3/bin/python -m robot \
                              --outputdir $report_path \
                              --pythonpath $lib_path \
                              $test_case_path
