from docx import Document
from pathlib import Path
import os

def convert_docx_to_html(input_file: str, output_file: str):
    
    doc = Document(input_file)
    
    level = 0
    html_content = "<!DOCTYPE html>\n<html lang='en'>\n\t<head>\n\t\t<meta charset='UTF-8'>\n\t\t<title>Title</title>\n\t</head>\n\t<body>\n"

    read_time = doc.paragraphs[0].runs[0].text or 5

    for paragraph in doc.paragraphs[1:]:
        if not paragraph.text.strip():
            continue

        if paragraph.style.name.startswith("Heading"):
            level = int(paragraph.style.name[-1])
            if level == 1:
                theme = paragraph.runs[0].text
            elif level == 2:
                title = paragraph.runs[0].text
            else:
                html_content += ((level-1) * "\t" + f'<h{level} class="article-header{level}">{format_runs(paragraph.runs)}</h{level}>\n')
        else:
            if paragraph.runs != "":
                html_content += (level * "\t" + f'<p class="artile-paragraph">{format_runs(paragraph.runs)}</p>\n')
            else:
                html_content += ("\n")
    
    html_content += ("\t</body>\n")
    html_content += ("</html>\n")
    return {
        'read_time': read_time,
        'theme': theme,
        'title': title,
        'html_content': html_content
    }
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(html_content)

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
        # print(convert_docx_to_html(input_path, output_path))
        convert_docx_to_html(input_path, output_path)
        print(f"Файл успешно преобразован в HTML и сохранён в {output_path}")
