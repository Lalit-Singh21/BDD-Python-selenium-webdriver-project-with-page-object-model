#!/usr/bin/env python
# A customized test runner for behave BDD test automation to run on different browsers on docker
#################################################################################################

import os
import argparse
from argparse import RawTextHelpFormatter
import subprocess as sp
from multiprocessing import Process


def worker_scenario(scenario_names, feature_files, output, browser_name):
    """Runs a given scenario a single time"""
    cmd = ["behave.exe"]
    # print(f"feature file, {type(feature_files)}---{feature_files}")
    # print(f"scenario_names file, {type(scenario_names)}---{scenario_names}")
    browser_dict = {'c': 'chrome', 'f': 'firefox', 'o': 'opera'}
    if feature_files is not None:
        for i in range(len(feature_files)):
            cmd = cmd + [feature_files[i]]
        if scenario_names is not None:
            for i in range(len(scenario_names)):
                cmd = cmd + ["-t"] + [scenario_names[i]]
    else:
        print("Running whole testsuite\n")
    if output is not None:
        cmd = cmd + ["-o"] + [output]
    if browser_name is not None:
        cmd += ['--define']+[browser_dict[browser_name]]
    print("cmd:::", cmd)
    sp.call(cmd)
    print("\n\n\n")


def runner_scenario_x_times(repetitions, scenario_names, feature_files, out):
    """
    Runs 'repetitions' are browser numbers combination to cover given behave scenarios, features, or
    the whole testsuite.

    :param repetitions: (int) number of times that a given test scenario,
                        feature file, or whole test suite, shall be run on given browser
    :param scenario_names: (seq) list of scenario names to be run a given
                           'repetitions' times
    :param feature_files: (seq) list of feature-files to be run a given
                          'repetitions' times
    """
    if scenario_names is not None:
        to_test = scenario_names
    elif feature_files is not None:
        to_test = feature_files
    else:
        to_test = "tests" #folder for all tests
    # browser_dict = dict()
    if repetitions is not None:
        browser_dict = eval(repetitions)
    msg = ("\nRunning " + str(repetitions) + " times test(s):\n " 
           + str(to_test) + "\n")
    print(msg)
    if out:
        out_name = os.path.splitext(out)[0]
        ext = os.path.splitext(out)[1]

    for browser in browser_dict.keys():
        for i in range(int(browser_dict[browser])):
            print (f"Iteration number:  {str(i+1)} for browser - {browser}")
            p = Process(target=worker_scenario,
                            args=(scenario_names, feature_files,out, browser))
            p.start()
            p.join()

def main():

    parser = argparse.ArgumentParser(
                 description="Test Runner allowing to run n test scenarios",
                 formatter_class=RawTextHelpFormatter)

    parser.add_argument(
        "-b", "--repeat_browser_type", type=str, default='{c:1}',
        help="provide the browser type to run test in docker multiple times, {c:2, f:3, o:3} means" \
             "8 repetitions. 2 in chrome, 3 in firefox and 3 in opera, write {c:5} for 5 repetition in chrome\n"
             + "(default=None)")
    parser.add_argument(
        "-t", "--scenario-names", type=str, nargs="+", default=None,
        help="Name of the scenario/s to be run 'x' times\n"
             + "(default=None)")
    parser.add_argument(
        "-f", "--feature-files", type=str, nargs="+", default=None,
        help="Name of the behave feature-file/s to be run 'x' times\n"
             + "(default=None)")
    parser.add_argument(
        "-o", "--output", type=str, default=None,
        help="Write output on specified file instead of stdout\n"
             + "(default=None)")

    args = parser.parse_args()

    runner_scenario_x_times(args.repeat_browser_type,
                            args.scenario_names,
                            args.feature_files,
                            args.output)


if __name__ == "__main__":
    main()

