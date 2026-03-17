import streamlit as st
import os
from core import extract_text_from_pdf, analyze_paper

# 设置网页全宽和标题
st.set_page_config(page_title="本地文献解析器", layout="wide")
st.title("📚 LocalPaper-Reader: 100% 隐私安全的文献助手")

# 文件上传组件
uploaded_file = st.file_uploader("请上传一篇 PDF 格式的论文", type="pdf")

if uploaded_file is not None:
    if st.button("开始深度解析"):
        with st.spinner("AI 正在疯狂阅读中..."):
            with open("temp.pdf", "wb") as f:
                f.write(uploaded_file.getbuffer())
            
            text = extract_text_from_pdf("temp.pdf")
            result = analyze_paper(text)
            
            st.success("解析完成！")
            st.markdown(result)
            
            os.remove("temp.pdf")