### pptx2txt
extract raw text content from ppts

### run below in CLI to create an envmt
conda create -n streamlit python=3.9

### run below in CLI to activate said envmt
conda activate streamlit
pip install python-pptx

### run below in CLI
streamlit run https://raw.githubusercontent.com/sudhir-voleti/pptx2txt/main/app.py

## for html2mdtxt
pip install streamlit beautifulsoup4 markdownify
streamlit run https://raw.githubusercontent.com/sudhir-voleti/pptx2txt/main/app1.py

## for MarkItDown
conda create -n streamlit1 python=3.10

conda activate streamlit1

pip install streamlit markitdown[all]

streamlit run https://raw.githubusercontent.com/sudhir-voleti/pptx2txt/main/app2.py
