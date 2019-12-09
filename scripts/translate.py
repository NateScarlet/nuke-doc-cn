#!/usr/bin/env python

import pathlib
from concurrent import futures
from itertools import chain
import json

from aliyunsdkalimt.request.v20190107 import TranslateGeneralRequest
from aliyunsdkcore.client import AcsClient
import bs4
import environs
import fire


def get_client() -> AcsClient:
    ENV = environs.Env()
    ENV.read_env()
    return AcsClient(
        ENV('ALIYUN_ACCESS_KEY_ID'),
        ENV('ALIYUN_ACCESS_KEY_SECRET'),
        "cn-hangzhou"
    )


def translate_html(client, content) -> str:
    request = TranslateGeneralRequest.TranslateGeneralRequest()
    request.set_SourceLanguage("en")
    request.set_SourceText(content)
    request.set_FormatType("html")
    request.set_TargetLanguage("zh")
    response = client.do_action_with_exception(request)
    result = json.loads(response)
    assert result["Code"] == "200", result.get("Message")
    return result['Data']['Translated']


def translate_html_file(client, path):
    soup = bs4.BeautifulSoup(open(path, 'r', encoding='utf8'), 'html.parser')

    translated_tags = set()

    def is_translated(tag: bs4.Tag) -> bool:
        if tag in translated_tags:
            return True
        if tag.parent:
            return is_translated(tag.parent)
        return False

    def translate_tag(i):
        if is_translated(i):
            return
        translated = translate_html(client, str(i))
        i.replace_with(bs4.BeautifulSoup(translated, 'html.parser'))
        translated_tags.add(i)

    def select_html_text(tag: bs4.Tag):
        if tag.name in ['script']:
            return False
        return len(str(tag)) < 2000 and len(tag.get_text()) > 2

    for i in chain(
            soup.find_all('title'),
            soup.find('body').find_all(select_html_text)):
        translate_tag(i)

    with open(path, 'w', encoding='utf8') as f:
        f.write(soup.prettify())


if __name__ == '__main__':
    class CLI:
        def __init__(self) -> None:
            self._client = get_client()

        def html(self, path):
            path = pathlib.Path(path).as_posix()
            with open('translated_files', 'r') as f:
                if path + '\n' in f:
                    return

            translate_html_file(self._client, path)
            with open('translated_files', 'a') as f:
                f.write(path + '\n')
            print(path)

        def html_dir(self, path):
            with futures.ThreadPoolExecutor() as executor:
                executor.map(self.html, pathlib.Path(path).glob('**/*.html'))

    fire.Fire(CLI())
