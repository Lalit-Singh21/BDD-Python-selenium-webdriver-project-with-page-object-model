#!/usr/bin/env python
# A customized test runner for behave BDD tests to run parallelely
# on different browser versions on number of docker containers
####################################################################
import os
import argparse
from argparse import RawTextHelpFormatter
import subprocess as sp
import multiprocessing
from multiprocessing import pool
import time
browser_dict = {'c': 'chrome', 'f': 'firefox', 'o': 'opera'}
t = time.time()
def get_behave_command(scenario_names, feature_files, output, browser_name):
    """Returns a command line string for behave """
    cmd = ["behave.exe"]
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
    return cmd # ("cmd:::", cmd)

def run_cli(cmd):
    sp.call(cmd)

def parallel_runner(repetitions, scenario_names, feature_files, out):
    """
    :param repetitions: dict input is browser name with number of instances
    :param scenario_names: (seq) list of scenario names to be run for number of times for specific browsers
    :param feature_files: (seq) list of feature-files to be run
    """
    dict_repetitions = dict()
    if repetitions is not None:
        dict_repetitions = eval(repetitions)
    if out:
        out_name = os.path.splitext(out)[0]
        ext = os.path.splitext(out)[1]
    list_of_process = []
    for browser in dict_repetitions.keys():
        for i in range(int(dict_repetitions[browser])):
            list_of_process.append(get_behave_command(scenario_names, feature_files,out, browser))
    # print(list_of_process)
    # *(10) number of sessions (MAX_SESSIONS: browser sessions to run at same time in docker hub)
    p = multiprocessing.Pool(10)
    p.map(run_cli, list_of_process)



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
    parallel_runner(args.repeat_browser_type,
                            args.scenario_names,
                            args.feature_files,
                            args.output)

    print("time taken: ", time.time()-t)

if __name__ == "__main__":
    main()

