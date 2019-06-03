from bs4 import BeautifulSoup
from pprint import pprint as p

SIMPLE_HTML = ''' <html>
<head></head>
<body>
    <h1>This is a title</h1>
    <p class="subtitle">I am a paragraph with nothing to say</p>
    <p>Im a paragraph with no class</p>
        <u1>
            <li>Rolf</li>  
            <li>Charlie</li>
            <li>Pop</li>
            <li>Noah</li>
        </ul>
</body>
</html>     
'''


def find_title():
    return soup.find('h1')


def find_list_items():
    return [i.string for i in soup.find_all('li')]


def find_subtitle():
    subtitle = soup.find('p', {'class': 'subtitle'})
    return subtitle.string


def find_para():
    return [para.string for para in soup.find_all('p') if 'subtitle' not in para.attrs.get('class', [])]


soup = BeautifulSoup(SIMPLE_HTML, 'html.parser')

p(find_title())
p(find_list_items())
p(find_subtitle())
p(find_para())



