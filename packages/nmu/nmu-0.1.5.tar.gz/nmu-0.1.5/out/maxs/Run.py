from nmu.maxs.Operation import Operation
from nmu.utils.PostgreSQLTool import PostgreSQLTool
from nmu.common.Browser import Browser
import json
import os
import logging

# 日志配置
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger()

# 数据库配置
db_config = {
    "host": os.getenv("DB_HOST", "172.16.200.139"),
    "port": int(os.getenv("DB_PORT", 5432)),
    "database": os.getenv("DB_NAME", "datav"),
    "user": os.getenv("DB_USER", "usr_netsec"),
    "password": os.getenv("DB_PASSWORD", "o3h&sCas5vsK!gh@")
}

browser = Browser(isHeadless=True, chrome_location="/app/chrome-linux64/chrome")
driver = browser.get_driver()
operation = Operation(driver)
postgresql_tool = PostgreSQLTool(db_config)


def insert_data(data_list, query, fields):
    for record in data_list:
        try:
            values = tuple(record[field] for field in fields)
            postgresql_tool.execute_query(query, values)
            logger.info(f"插入成功: {record}")
        except Exception as e:
            logger.error(f"插入失败: {record} - 错误: {e}")

def get_grade():
    insert_query = """
        INSERT INTO usr_netsec.t_wlaqzt_maxs (gradeName, score)
        VALUES (%s, %s)
    """
    result = operation.get_grade()
    print(result)
    if isinstance(result, str):
        result = json.loads(result)
    data_dict = result.get("data", {})
    insert_data([data_dict], insert_query, ["gradeName", "score"])

def get_safe_event():
    insert_query = """
        INSERT INTO usr_netsec.t_aqsj_maxs (pendingCnt, solvedCnt)
        VALUES (%s, %s)
    """
    result = operation.get_safe_event()
    print(result)
    if isinstance(result, str):
        result = json.loads(result)
    data_dict = result.get("data", {})
    insert_data([data_dict], insert_query, ["pendingCnt", "solvedCnt"])

def get_safe_warnnings():
    insert_query = """
        INSERT INTO usr_netsec.t_aqgj_maxs (pendingCnt, solvedCnt)
        VALUES (%s, %s)
    """
    result = operation.get_safe_warnnings()
    print(result)
    if isinstance(result, str):
        result = json.loads(result)
    data_dict = result.get("data", {})
    insert_data([data_dict], insert_query, ["pendingCnt", "solvedCnt"])

def get_top5_attacks():
    insert_query = """
        INSERT INTO usr_netsec.t_zctop5_gjzsj_maxs (srcIp, srcArea, dstIpCnt, alarmCnt)
        VALUES (%s, %s, %s, %s)
    """
    result = operation.get_top5_attacks()
    print(result)
    if isinstance(result, str):
        result = json.loads(result)
    data_list = result.get("data", [])
    insert_data(data_list, insert_query, ["srcIp", "srcArea", "dstIpCnt", "alarmCnt"])

def get_top5_casualty():
    insert_query = """
        INSERT INTO usr_netsec.t_zctop5_shzsj_maxs (ip, dstAssetName, dstAssetGroup, dstAssetOrg, srcIpCnt, alarmCnt)
        VALUES (%s, %s, %s, %s, %s, %s)
    """
    result = operation.get_top5_casualty()
    print(result)
    if isinstance(result, str):
        result = json.loads(result)
    data_list = result.get("data", [])
    insert_data(data_list, insert_query, ["ip", "dstAssetName", "dstAssetGroup", "dstAssetOrg", "srcIpCnt", "alarmCnt"])

def post_safe_event_list():
    insert_query = """
        INSERT INTO usr_netsec.t_aqsjlb_maxs (riskLevel, riskLevelDesc, quantity, securityEventTypeId, securityEventType, eventQuantity)
        VALUES (%s, %s, %s, %s, %s, %s)
    """
    result = operation.post_safe_event_list()
    print(result)
    if isinstance(result, str):
        result = json.loads(result)
    data_list = result.get("data", {}).get("securityEventList", [])
    insert_data(data_list, insert_query, ["riskLevel", "riskLevelDesc", "quantity", "securityEventTypeId", "securityEventType", "eventQuantity"])


if __name__ == '__main__':
    try:
        get_grade()
        get_safe_event()
        get_safe_warnnings()
        get_top5_attacks()
        get_top5_casualty()
        post_safe_event_list()
    finally:
        browser.close_browser()