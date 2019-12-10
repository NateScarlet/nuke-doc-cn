#!/usr/bin/env python

from cached_property import threaded_cached_property
import json
import pathlib
from concurrent import futures
from itertools import chain
from threading import Lock

import bs4
import environs
import fire
from aliyunsdkalimt.request.v20190107 import TranslateGeneralRequest
from aliyunsdkcore.client import AcsClient


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


class CLI:
    record_file = 'translated_files'

    def __init__(self) -> None:
        self._client = get_client()
        self._record_lock = Lock()

    @threaded_cached_property
    def _translated_files(self):
        with self._record_lock:
            with open(self.record_file, 'r') as f:
                return f.readlines()

    def _add_translated_file(self, path):
        path = pathlib.Path(path).as_posix()
        with self._record_lock:
            with open(self.record_file, 'a') as f:
                f.write(path + '\n')
            print(path)

    def _is_translated_file(self, path) -> bool:
        path = pathlib.Path(path).as_posix()
        return path + '\n' in self._translated_files

    def html(self, path):
        if self._is_translated_file(path):
            return
        translate_html_file(self._client, path)
        self._add_translated_file(path)

    def html_dir(self, path):
        with futures.ThreadPoolExecutor() as executor:
            executor.map(self.html, pathlib.Path(path).glob('**/*.html'))


if __name__ == '__main__':
    fire.Fire(CLI())
