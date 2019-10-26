import urllib.request
import os, re, logging
from urllib.request import urlopen
from urllib.error import HTTPError, URLError
from bs4 import BeautifulSoup


logging.basicConfig(filename='getArticle.log',
                    format='%(asctime)s %(levelname)s:%(message)s',
                    level=logging.DEBUG, datefmt='%Y-%m-%d %I:%M:%S')

# 当前python文件的所在路径
path = os.path.split(os.path.realpath(__file__))[0]

def get_article(url):
    """获取文章url中的标题、正文、图片"""
    try:
        html = urlopen(url)
    except (HTTPError, URLError) as e:
        return None
    try:
        bs_obj = BeautifulSoup(html.read())
        title = bs_obj.title
        # print('title --> {}'.format(title))
        if str(title) == '<title>提示信息</title>':
            print('{} --> have not content.'.format(url))
            logging.info('{} --> have no content.'.format(url))
            return None
        content = bs_obj.findAll(name='div', attrs={'class': 'content'})[0]
        imgs = bs_obj.findAll(name='img')
        attachments = bs_obj.findAll(name='a')
    except AttributeError as e:
        return None
    return title, content, imgs, attachments


def get_article_name(url, article):
    """获取文章栏目及标题信息, 创建栏目为本地路径，标题为栏目下路径"""
    id = url.split('&')[-1]
    # print('article id --> {}'.format(id))
    article_name = str(article[0])[7:-8].split('-')[0].rstrip()
    dir = str(article[0])[7:-8].split('-')[1].split()
    # if os.path.exists(os.path.join(path, dir)):
    #     print('dir is exists.')
    # else:
    #     os.makedirs(os.path.join(path, dir))

    if not os.path.exists(os.path.join(path, id, dir[0], article_name)):
        os.makedirs(os.path.join(path, id, dir[0], article_name))
    else:
        print('dir exist --> {}'.format(
            os.path.join(path, id, dir[0], article_name)))

    return os.path.join(path, id, dir[0], article_name)


def save_img(url, article, article_path):
    """获取文章中的所有图片地址"""
    for img in article[2]:
        # pattern = re.compile(r'src="(.+?\.jpg)')
        pattern = "((http):[^\s]*?(jpge|jpg|png|PNG|JPG))"
        # img_src = pattern.findall(str(img))
        img_src = re.findall(pattern, str(img))
        if img_src:
            img_name = img_src[0][0].split('/')[-1]
            print('img_src --> {}'.format(str(img_src[0][0])))
            print('img_name --> {}'.format(img_name))
            print('img save to --> {}'.format(os.path.join(article_path, img_name)))

            # HTML图片保存本地
            try:
                urllib.request.urlretrieve(
                    img_src[0][0], os.path.join(article_path, img_name)
                )
            except HTTPError as e:
                logging.info('{} --> have pic can not find.'.format(url))
        else:
            logging.info('{} --> has pic out link.'.format(url))


def save_html(article, filename):
    """写入本地HTML文件"""
    with open('{}.html'.format(filename), 'w', encoding='utf-8') as html:
        # print('contents --> {}'.format(article))
        html.write(str(article[0]))
        html.write(str(article[1]))


def make_articles():
    articles = []
    # catid 并没有什么影响，指定一个存在的就可以取出所有文章
    for catid in [24]:
        for id in range(1, 921):
            url_template = (
                "http://www.c2.org.cn/index.php?m=content&c=index&a=show&"
                "catid={}&id={}".format(catid, id)
            )
            articles.append(url_template)
    return articles


def save_attachment(url, article, article_path):
    for attachments in article[3]:
        pattern = "((http):[^\s]*?(docx|Docx|DOCX|pdf|Pdf|PDF|doc|Doc|DOC))"
        attachment = re.findall(pattern, str(attachments))
        if attachment:
            logging.info('{} --> has attachment.'.format(url))
            attachment_src = attachment[0][0]
            attachment_name = attachment[0][0].split('/')[-1]
            print('attachment src --> {}'.format(attachment_src))
            print('attachment name --> {}'.format(attachment_name))
            print('attachment save --> {}'.format(
                os.path.join(article_path, attachment_name)
            ))

            # HTML附件保存本地
            try:
                urllib.request.urlretrieve(
                    attachment_src, os.path.join(article_path, attachment_name)
                )
            except URLError as e:
                logging.info('{} --> attachment save failed.'.format(url))
        else:
            logging.info('{} --> has not attachment.'.format(url))


def do_work(urls):
    """处理文章URL队列"""
    for url in urls:
        print('article url --> {}'.format(url))
        article = get_article(url)
        if article is not None:
            article_path = get_article_name(url, article)
            article_name = article_path.split('/')[-1].rstrip()
            save_html(article, os.path.join(article_path, article_name))
            save_img(url, article, article_path)
            save_attachment(url, article, article_path)


urls = make_articles()

# urls = [
#     "http://www.c2.org.cn/index.php?m=content&c=index&a=show&catid=24&id=617",
# ]

do_work(urls)

