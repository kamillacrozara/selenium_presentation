#!/usr/bin/python
# -*- coding: utf-8 *-*
from threading import Thread
import sys, os, fnmatch
from datetime import datetime

class SRDStartSuites(Thread):
	def __init__(self, testName, logNumber):
		self.testName = testName
		self.logName = "log/selenium_srd_tests_%s.log" %(datetime.now().strftime('%m-%d-%y-%H:%M'))
		Thread.__init__(self)
	
	def run(self):
		os.system('python %s >> %s 2>&1 ' %(self.testName, self.logName))

def grab_files(dir):
	tests = []
	for root, dirnames, filenames in os.walk(dir):
		for filename in fnmatch.filter(filenames, '*_test.py'):
			tests.append(os.path.join(root, filename))
	return tests

def start_threads(tests):
	logNumber = 1
	for test in tests:
		thread = SRDStartSuites(test, logNumber)
		thread.start()
		logNumber +=1

def execute_rg_tests(args):
	rg_args = ""
	i = 2
	while i < len(args):
		rg_args = rg_args + args[i] + " "
		i += 1
	print rg_args
	os.system('cd regression_tests && php %s' %rg_args)


def verify_log_folder():
	try:
		os.makedirs("log")
	except OSError:
		if os.path.exists("log"):
			pass
		else:
			print "Log folder doesn't exist and can't be created. Please verify the user permissions to the execution folder."
			raise

def log_execution(test_type = 'default'):
	config = {}
	execfile("srd_test_suite.conf", config)
	
	test_options = {
					'ui': "User Interface", 
					'ck': "Check Links",
					'sd': "Search/Download tab",
					'lt': "Light",
					'default': "SRD Test Suite",
					'rg': "Regression"
					}

	print "****************************************************************"
	print "Starting %s tests." %test_options.get(test_type)
	print "Base URL: %s" %config["BASE_URL"]
	print "Logging folder: %s" %os.getcwd() +  "/log"
	print "****************************************************************"

if __name__ == '__main__':
	if len(sys.argv) == 1:
		verify_log_folder()
		tests = grab_files(os.getcwd())
		os.system('cd regression_tests && php RunAll.php -g')
		log_execution()
		start_threads(tests)
	elif ((len(sys.argv) == 2) and (sys.argv[1] == "ui")):
		verify_log_folder()
		log_execution(sys.argv[1])
		tests = grab_files(os.getcwd() + "/srd_ui_tcs")
		start_threads(tests)
	elif ((len(sys.argv) == 2) and (sys.argv[1] == "sd")):
		verify_log_folder()
		log_execution(sys.argv[1])
		tests = grab_files(os.getcwd() + "/srd_sd_tcs")
		start_threads(tests)
	elif ((len(sys.argv) == 2) and (sys.argv[1] == "lt")):
		verify_log_folder()
		log_execution(sys.argv[1])
		tests = grab_files(os.getcwd() + "/srd_light_tcs")
		start_threads(tests)
	elif ((len(sys.argv) == 2) and (sys.argv[1] == "ck")):
		verify_log_folder()
		log_execution(sys.argv[1])
		tests = grab_files(os.getcwd() + "/srd_checklinks_tcs")
		start_threads(tests)
	elif sys.argv[1] == "rg":
		execute_rg_tests(sys.argv)
	else:
		print "\nOops... wrong number of arguments and/or invalid option.\n"
		print "Please, choose a valid option:\n"
		print "[ui] for User Interface tests."
		print "[sd] for Search/Download tab tests."
		print "[lt] for light tests."
		print "[ck] for check the SRD download links."
		print "[rg] [aditional arguments] for regression tests.\n"