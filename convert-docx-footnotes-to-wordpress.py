from docx2python import docx2python

docx_content = docx2python('test.docx') # Enter the name of the document here

footnotes = docx_content.footnotes[0][0]

ft_array = []

for ft in footnotes:
    ft_array.append(ft[0].split(')\t '))

text = docx_content.text

for footnote in ft_array:
    if len(footnote) > 1:
        text = text.replace('----' + footnote[0] + '----', '[ref]' + footnote[1] + '[/ref]')

text = text.split('footnote1)')[0]

with open('test.txt', 'w') as f: # Enter the name of the intended file name here
    f.write(text)

docx_content.close()
