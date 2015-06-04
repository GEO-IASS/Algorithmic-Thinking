import pos_simpletest

def run_test(format_function):
    #some informal testing code
    #create a TestSuite object
    suite=poc_simpletest.TestSuite()
    suite.run_test(format_function(0),"0:00.0","Test #1:")
    suite.run_test(format_function(214),"0:21.4","Test #2:")

    suite.report_results()
