test_case_path='tests/cases'
report_path='tests/reports'

# for anaconda install
/home/$(whoami)/anaconda3/bin/python -m robot $test_case_path

# not sure how to config this stuff when executing earlier. --outputdir didn't seem to work for me
mv log.html report.html output.xml ./tests/reports/