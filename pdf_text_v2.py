import fitz
from bs4 import BeautifulSoup

# pick the document
path = "/Users/beneverman/Documents/Coding/PYTHON/summarize-article-GPT-3/article-pdfs/penetrance.pdf"
output_text_file = "penetrance.txt"

# open it with PyMuPDF
doc = fitz.open(path)

# whole doc
# html_pages = ''
# for page in doc:
#     html_page = page.get_text("html", "html.parser")
#     html_pages += str(html_page)

#! certain number of pages
# how many pages to parse
pagelimit = len(doc)
# other setup
pagelimit_converted = pagelimit - 1
html_pages = ''
x = 0
# iterate over each page and get its html, store to "html_pages"
for pages in doc:
    while x <= pagelimit_converted:
        page = doc[x]
        html_page = page.get_text("html", "html.parser")
        html_pages += str(html_page)  
        x = x + 1

# stick the html into bs
html = BeautifulSoup(html_pages, features = 'html.parser')

# remove images
for tag in html:
    for img in html('img'):
        img.decompose()

# iterate over each p tag and add its text to var "p_text" to get the entire documents text
ptag = html.find_all('p')
p_text = ''
for ptag in html:
    p_text += ptag.text

# write it to a file
with open(f'article-txt/{output_text_file}', 'w') as f:
    f.write(p_text)

exit()

x = 0
pdf_text = ""
pagelimit = 12
pagelimit_converted = pagelimit - 1

while page in pdf.pages <= pagelimit_converted:
    page = pdf.pages[x]
    text = page.extract_text()
    pdf_text += text
    print(f'Page {x+1} indexed')
    x = x + 1

with open('wsj_article_v2.txt', 'w') as f:
    f.write(pdf_text)

print("finished")