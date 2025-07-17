#ライブラリ読込
from dotenv import load_dotenv
from openai import OpenAI
from langchain_openai import ChatOpenAI
from langchain.schema import SystemMessage, HumanMessage

load_dotenv()
import streamlit as st

#アプリGUI設定
st.title("お料理相談アプリ")
st.write("このアプリでは、気軽に専門家にお料理について質問することができます。")
st.write("##### STEP1: 談したい人を選んでください")
selected_item = st.radio(
    "選択してください。",
    ["家庭料理の専門家", "プロ料理の専門家"]
)
st.divider()

st.write("##### STEP2: 相談内容を入力してください")
st.write("入力フォームにテキストを入力し、「実行」ボタンを押すことで、選択した専門家に相談できます。")
issue = st.text_input(label="相談内容：")

st.divider()

#LLM実行関数定義
def execute_llm(selected_item, issue):
    llm = ChatOpenAI(model_name="gpt-4o-mini", temperature=0)
    if selected_item == "家庭料理の専門家":
        messages = [
            SystemMessage(content="あなたは家庭料理の専門家です。質問に端的に答えてください。"),
            HumanMessage(content=issue),
            ]
        result = llm(messages)
        return result.content

    elif selected_item == "プロ料理の専門家":
            llm = ChatOpenAI(model_name="gpt-4o-mini", temperature=0)
            messages = [
            SystemMessage(content="あなたは一流レストランの料理の専門家です。質問に端的に答えてください。"),
            HumanMessage(content=issue),
            ]
            result = llm(messages)
            return result.content
    
if st.button("実行"):
    if issue:
        result = execute_llm(selected_item, issue)
        st.write(result)
    else:
        st.error("相談内容を入力してください。")
