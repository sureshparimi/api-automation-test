import ast
import os
from urllib.parse import urlparse

from behavex_web.steps.web import *
from os import environ


def before_all(context):
    """ before_all behave hook """
    if os.environ.get('APP_URL', None):
        app_url = os.environ.get('APP_URL')
        # Storing all variables in a context variable
        context.env_config = {
            'app_url': app_url,
            }
    else:
        raise Exception("Some env. variables are missing (APP_URL")
    context.failures_summary_filename = 'failures_summary.txt'


def before_feature(context, feature):
    """ before_feature behave hook """
    for scenario in feature.scenarios:
        if "DEPRECATED" in scenario.tags:
            scenario.skip("This scenario has been deprecated...")
        


def before_scenario(context, scenario):
    """ before_scenario behave hook """
    context.record_network_event_api_logs = False
    context.performance_logs = {}
    if 'NON_ENABLED' in scenario.tags:          
        print("------------------------------------------")
        scenario.skip("Scenario not enabled to run...")
        print("------------------------------------------")
        return
    else:
        for tag in scenario.tags:
            if "ONLY_" in tag:
                if tag in "ONLY_PRODUCTION":
                    print("------------------------------------------")
                    scenario.skip("Scenario only enabled to run in {}...".format("Production"))
                    print("------------------------------------------")
                    return
            if "NON_" in tag:
                if  tag in "NON_PRODUCTION":
                    print("------------------------------------------")
                    scenario.skip("Scenario not enabled to run in '{}'".format("NON PRODUCTION"))
                    print("------------------------------------------")
                    return
    context.performance_scenario = True if "PERFORMANCE" in scenario.tags else False
    print("------------------------------------------")
    print("Running Scenario: {}".format(scenario.name))
    print("------------------------------------------")


def before_step(context, step):
    """ before_step behave hook """
    context.step = step


def after_step(context, step):
    """ after_step behave hook """
    pass


def after_scenario(context, scenario):
    """ after_scenario behave hook """
    if scenario.status == "failed":
        failures_summary_file = os.path.join(os.environ.get('OUTPUT'), context.failures_summary_filename)
        with open(failures_summary_file, 'a+') as f:
            f.write("{}: {}\n".format(scenario.feature.name, scenario.name))


def after_feature(context, feature):
    """ after_feature behave hook """
    pass


def after_all(context):
    """ after_all behave hook """
    pass


