from docx import Document
from pathlib import Path
import os

def convert_docx_to_html(input_file: str, output_file: str):
    
    doc = Document(input_file)
    
    level = 0
    html_content = [
        "<!DOCTYPE html>", "<html lang='en'>", "\t<head>", "\t\t<meta charset='UTF-8'>", 
        "\t\t<title>Title</title>", "\t</head>", "\t<body>"
    ]

    for paragraph in doc.paragraphs:
        if not paragraph.text.strip():
            continue

        if paragraph.style.name.startswith("Heading"):
            level = int(paragraph.style.name[-1])
            html_content.append((level + 1) * "\t" + f'<h{level} class="article-header{level}">{format_runs(paragraph.runs)}</h{level}>')
        else:
            if paragraph.runs != "":
                html_content.append((level + 2) * "\t" + f'<p class="artile-paragraph">{format_runs(paragraph.runs)}</p>')
            else:
                html_content.append("\n")
    
    html_content.append("\t</body>")
    html_content.append("</html>")
    
    with open(output_file, "w", encoding="utf-8") as f:
        f.write("\n".join(html_content))

def format_runs(runs):
    """
    Обрабатывает фрагменты текста (runs) и применяет HTML-стили (жирный, курсив, подчеркивание).
    """
    formatted_text = ""
    for run in runs:
        text = run.text
        if run.bold:
            text = f'<b class="bold-text">{text}</b>'
        if run.italic:
            text = f'<i class="italic-text">{text}</i>'
        if run.underline:
            text = f'<u class="underline-text">{text}</u>'
        formatted_text += text
    return formatted_text

if __name__ == "__main__":
    input_path = os.path.abspath("parsing/article.docx")
    output_path = "parsing/article.html"
    
    if Path(input_path).suffix.lower() != ".docx":
        print("Скрипт поддерживает только .docx файлы")
    else:
        convert_docx_to_html(input_path, output_path)
        print(f"Файл успешно преобразован в HTML и сохранён в {output_path}")
