import fitz  # PyMuPDF
from openai import OpenAI

def extract_text_from_pdf(file_path):
    """解析 PDF 并提取纯文本"""
    doc = fitz.open(file_path)
    text = ""
    for page in doc:
        text += page.get_text()
    return text

def analyze_paper(text):
    """调用本地 Ollama(Qwen2) 进行文献解析"""
    client = OpenAI(base_url="http://localhost:11434/v1", api_key="ollama")
    
    truncated_text = text[:6000] 
    
    response = client.chat.completions.create(
        model="qwen2",
        messages=[
            {"role": "system", "content": "你是一个严谨的学术科研助手。请帮我深度解析这篇文献，提取出：1. 核心贡献，2. 研究方法，3. 主要结论。"},
            {"role": "user", "content": f"请分析以下论文内容：\n\n{truncated_text}"}
        ],
        temperature=0.3
    )
    return response.choices[0].message.content