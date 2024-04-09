'''
Author: hibana2077 hibana2077@gmail.com
Date: 2024-04-07 23:39:59
LastEditors: hibana2077 hibana2077@gmail.com
LastEditTime: 2024-04-09 09:28:33
FilePath: \llm_agent_flow_lab\lab\better_question_disq\main.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
from tqdm import tqdm
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.messages.ai import AIMessage
from langchain_core.messages.human import HumanMessage
import logging
import time
import os

CHATGROQ_API_KEY = os.getenv("CHATGROQ_API_KEY", "")

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def main():
    logger.info("Start the program")
    logger.info("Init ChatGroq")
    logger.info("API_KEY: {}".format(CHATGROQ_API_KEY))

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        logger.info("Exit the program")
        exit(0)