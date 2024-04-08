'''
Author: hibana2077 hibana2077@gmail.com
Date: 2024-04-07 23:39:59
LastEditors: hibana2077 hibana2077@gmail.com
LastEditTime: 2024-04-08 10:56:49
FilePath: \llm_agent_flow_lab\lab\better_question_disq\main.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
# Work flow: user input(Template 1) -> answer generation(Template 1) -> self answer check(Template 2) -> answer output(Template 1)  
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
    llm = ChatGroq(api_key=CHATGROQ_API_KEY)
    logger.info("Init ChatPromptTemplate")
    prompt1 = ChatPromptTemplate.from_messages([
        ('system', "You are a helpful AI assistant who can answer questions about any topic. Please answer the following question:"),
    ])
    prompt2 = ChatPromptTemplate.from_messages([
        ('system', "Please check the answer below that you provided and think twice before you confirm it."),
        ('system', "If there is nothing need to be changed, please say 'Yes', otherwise, please provide the correct answer."),
        ('system', "Is the answer correct?")
    ])
    logger.info("Start the conversation")
    while True:
        human_message = HumanMessage(input("=> "))
        logger.info("Human: {}".format(human_message.content))
        prompt1.append(human_message)
        chain1 = prompt1 | llm
        response1 = chain1.invoke({})
        prompt2_copy = prompt2.copy()
        prompt2_copy.append(AIMessage(response1.content))
        tmp_response = response1.content
        chain2 = prompt2_copy | llm
        response2:AIMessage = chain2.invoke({})
        if response2.content.startswith("Yes") or response2.content.startswith("yes"):
            logger.info("AI: {}".format(tmp_response))
            prompt1.append(AIMessage(tmp_response))
        else:
            logger.warning("Previous answer is not correct, use the new answer")
            logger.info("AI: {}".format(response2.content))
            prompt1.append(AIMessage(response2.content))

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        logger.info("Exit the program")
        exit(0)