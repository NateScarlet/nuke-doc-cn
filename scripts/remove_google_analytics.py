import pathlib
import fire

import bs4


def remove_ga_from_html_file(path) -> None:
    doc = bs4.BeautifulSoup(open(path, 'r', encoding='utf8'), 'html.parser')

    def _select(tag: bs4.Tag) -> bool:
        return tag.name == 'script' and ("ga('send'" in tag.text or "ga('create'" in tag.text)
    is_need_write = False
    for i in doc.find_all(_select):  # type: bs4.Tag
        i.extract()
        is_need_write = True
    if not is_need_write:
        return
    with open(path, 'w', encoding='utf-8') as f:
        f.write(doc.prettify())


def cli(folder_path: str) -> None:
    for i in pathlib.Path(folder_path).glob('**/*.html'):
        remove_ga_from_html_file(i)
        print(i)


if __name__ == '__main__':
    fire.Fire(cli)
