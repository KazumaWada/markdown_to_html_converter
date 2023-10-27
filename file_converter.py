import sys
import os
import markdown

hint = """
##↓TYPE THIS COMMAND↓##

python3 file-converter.py markdown inputfile.md outputfile.html
"""

# convert md to html


def converter():
    print("do convert md to html here")
    with open('inputfile.md', 'r') as markdown_file:
        markdown_text = markdown_file.read()

    converted = markdown.markdown(markdown_text)

    with open('outputfile.html', 'w') as html_file:
        html_file.write(converted)


# python3 file_converter.py markdown inputfile outputfile
# validation
# "file_converter.py"と入力されないと、そもそもこのファイルに到達できないからhintが実行されない。
if len(sys.argv) >= 4 and sys.argv[0] == "file_converter.py" and sys.argv[1] == "markdown" and sys.argv[2] and sys.argv[3]:
    print("validation passed!")
    converter()
else:
    print(hint)
