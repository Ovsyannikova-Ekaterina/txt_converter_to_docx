from docx import Document


def txt_to_word(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as txt_file:
        text = txt_file.read()
    doc = Document()
    doc.add_paragraph(text)
    doc.save(output_file)


input_txt_file = 'input.txt'
output_word_file = 'output.docx'
txt_to_word(input_txt_file, output_word_file)
