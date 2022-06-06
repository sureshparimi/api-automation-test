import logging
from multiprocessing import context, managers
from select import select
import time
from urllib import request, response
from urllib.parse import urljoin
import os
import requests

from behave import step


@step(u'I send the parameters "{date_min}","{date_max}","{dist_min}","{dist_max}" and "{fullname}" and "{sort}" to retrive the close approach data')
def get_close_approach_data(context,date_min,date_max,dist_min,dist_max,fullname,sort):
    try:
        
        query_param = "date-min={param1}&date-max={param2}&dist-min={param3}&dist-max={param4}&fullname={param5}&sort={param6}".format(param1=date_min,param2=date_max,param3=dist_min,param4=dist_max,param5="true",param6=sort)
        # query_param = "des={param0}&date-min={param1}&date-max={param2}&dist-min={param3}&dist-max={param4}".format(param0=object,param1=date_min,param2=date_max,param3=dist_min,param4=dist_max)
        app_url=os.environ['app_url']
        url="{}?{}".format(app_url,query_param)
        logging.info("The api end point used:{}".format(url))
        logging.info("Querying to get the close approach data with parameters {param_1},{param_2},{param_3},{param_4},{param_5}".format(param_1=date_min,param_2=date_max,param_3=dist_min,param_4=dist_max,param_5=fullname))
        response = requests.request("GET",url=url)
        context.data = response.json()
        context.status_code = response.status_code
        logging.info('API responded with the status code {}'.format(response.status_code))
    except Exception as e:
        logging.info(e)

@step(u'I verify the response for Signature and count and fields and data')
def  verify_response_status(context):
    try:
        status_code = ["200","400","405","500","503"]
        logging.info('API responded with the status code {}'.format(context.status_code))
        assert context.data.get('signature',{}).get('version','') == '1.4'
        assert str(context.status_code) in status_code
    except Exception as e:
        logging.info(e)

@step(u'I verify the data contains "{dist_min}","{dist_max}" and "{fullname}"')
def  verify_response_data(context,dist_min,dist_max,fullname):
    data=context.data
    logging.info("The response from the end point is")
    logging.info(data)
    fields = ["des","orbit_id","jd","cd","dist","dist_min","dist_max","v_rel","v_inf","t_sigma_f","body","h","diameter","diameter_sigma","fullname"]
    try:
        if data.get('count',0) != "0":            
            assert str(len(data.get('data',[]))) == data.get('count','0')
            assert (data.get('data',[])[0][-1]).strip() == fullname 
            assert (data.get('data',[])[0][5]) >= dist_min
            assert (data.get('data',[])[0][6]) <= dist_max
            assert any(i for i in fields if i in data.get('fields'))
        else:
            logging.info("API returned no data!!.May be the query is too restrictive")
    except Exception as e:
        logging.info(e)
