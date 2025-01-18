from docx import Document
from pathlib import Path
import os

def convert_docx_to_html(input_file: str, output_file: str):
    # Загружаем документ
    doc = Document(input_file)
    
    # Начинаем формировать HTML
    html_content = [
        "<!DOCTYPE html>", "<html lang='en'>", "\t<head>", "\t\t<meta charset='UTF-8'>", 
        "\t\t<title>Title</title>", "\t</head>", "\t<body>"
    ]
    
    for paragraph in doc.paragraphs:
        # Определяем стиль параграфа (например, заголовки)
        if paragraph.style.name.startswith("Heading"):
            level = int(paragraph.style.name[-1])  # Уровень заголовка (например, h1, h2)
            html_content.append(f"\t\t<h{level}>{format_runs(paragraph.runs)}</h{level}>")
        else:
            html_content.append(f"\t\t<p>{format_runs(paragraph.runs)}</p>")
    
    html_content.append("\t</body>")
    html_content.append("</html>")
    
    # Сохраняем HTML в файл
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
            text = f"<b>{text}</b>"
        if run.italic:
            text = f"<i>{text}</i>"
        if run.underline:
            text = f"<u>{text}</u>"
        formatted_text += text
    return formatted_text

if __name__ == "__main__":
    input_path = os.path.abspath("article.docx")
    output_path = "article.html"
    
    if Path(input_path).suffix.lower() != ".docx":
        print("Скрипт поддерживает только .docx файлы.")
    else:
        convert_docx_to_html(input_path, output_path)
        print(f"Файл успешно преобразован в HTML и сохранён в {output_path}")
