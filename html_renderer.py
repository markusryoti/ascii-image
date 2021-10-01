from bs4 import BeautifulSoup


class HtmlRenderer:
    def __init__(self):
        self.html_name = 'ascii.html'
        self.html_template = 'template.html'
        self.soup = BeautifulSoup(self.read_template(), 'html.parser')

    def img_to_html(self, img):
        img_tag = self.soup.new_tag('div')
        for row in img:
            row_element = self.soup.new_tag('div')
            row_text = ''.join(map(lambda x: str(x), row))
            row_element.append(row_text)
            img_tag.append(row_element)
        return img_tag

    def render(self, img):
        img_as_html = self.img_to_html(img)
        self.soup.find_all(id='render')[0].append(img_as_html)
        self.write_file()

    def read_template(self):
        with open(self.html_template, 'r') as f:
            content = f.read()
        return content

    def write_file(self):
        with open(self.html_name, 'w') as f:
            f.write(self.soup.prettify())
