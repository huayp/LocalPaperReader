# LocalPaperReader
A minimalist, secure local paper summarizer.

如果你的服务器没有 Root 权限，且主目录被加上了 noexec (禁止执行) 限制，可以按照以下步骤操作。
# 在不受限制的本地物理硬盘 /tmp 下创建环境隔离区
mkdir -p /tmp/my_env
cd /tmp/my_env

# 安装 Miniconda (假设安装包已上传至该目录)
bash Miniconda3-latest-Linux-x86_64.sh -b -p /tmp/my_env/miniconda3
/tmp/my_env/miniconda3/bin/conda init
source ~/.bashrc

# 创建并激活专属虚拟环境
conda create -n paper_reader python=3.10 -y
conda activate paper_reader

前往 Ollama GitHub Releases 手动下载 ollama-linux-amd64.tar.zst 文件，上传至服务器
# 解压文件
tar -xf ollama-linux-amd64.tar.zst

# 将执行文件和依赖库转移到虚拟环境目录
cp -r bin/* $CONDA_PREFIX/bin/
cp -r lib/* $CONDA_PREFIX/lib/
chmod +x $CONDA_PREFIX/bin/ollama

# 验证安装
ollama -v

# 在你安全的个人主目录创建模型库
mkdir -p ~/ollama_models_safe

# 设置环境变量，强制定向模型下载位置
export OLLAMA_MODELS="~/ollama_models_safe"

# 后台静默启动引擎
nohup ollama serve > /tmp/my_env/ollama.log 2>&1 &

# 拉取 Qwen2 大模型
ollama run qwen2

# 安装核心依赖
pip install PyMuPDF openai streamlit

# 进入安全的个人主目录，准备代码
cd ~
git clone https://github.com/你的用户名/LocalPaperReader.git
cd LocalPaperReader

在项目目录下运行
streamlit run app.py

打开本地电脑的浏览器，访问：👉 http://localhost:8501
尽情享受完全属于你自己的、毫秒级响应的文献阅读助手吧！
