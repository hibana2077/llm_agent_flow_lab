'''
Author: hibana2077 hibana2077@gmail.com
Date: 2024-04-07 23:39:59
LastEditors: hibana2077 hibana2077@gmail.com
LastEditTime: 2024-04-08 08:27:15
FilePath: \llm_agent_flow_lab\lab\better_question_disq\main.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
from tqdm import tqdm
from langchain_groq import ChatGroq
from langchain_community.document_loaders import ArxivLoader, PyMuPDFLoader, _module_lookup
# more document loaders see _module_lookup in langchain_community.document_loaders
from langchain_core.documents import Document
import logging
import time

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def main():
    pass

if __name__ == '__main__':
    main()