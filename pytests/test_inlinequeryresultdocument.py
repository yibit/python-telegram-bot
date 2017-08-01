#!/usr/bin/env python
#
# A library that provides a Python interface to the Telegram Bot API
# Copyright (C) 2015-2017
# Leandro Toledo de Souza <devs@python-telegram-bot.org>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see [http://www.gnu.org/licenses/].
import json

import pytest

from telegram import (InlineKeyboardButton, InputTextMessageContent, InlineQueryResultDocument,
                      InlineKeyboardMarkup, InlineQueryResultVoice)


@pytest.fixture(scope='class')
def inline_query_result_document():
    return InlineQueryResultDocument(TestInlineQueryResultDocument.id,
                                     TestInlineQueryResultDocument.document_url,
                                     TestInlineQueryResultDocument.title,
                                     TestInlineQueryResultDocument.mime_type,
                                     caption=TestInlineQueryResultDocument.caption,
                                     description=TestInlineQueryResultDocument.description,
                                     thumb_url=TestInlineQueryResultDocument.thumb_url,
                                     thumb_width=TestInlineQueryResultDocument.thumb_width,
                                     thumb_height=TestInlineQueryResultDocument.thumb_height,
                                     input_message_content=TestInlineQueryResultDocument.input_message_content,
                                     reply_markup=TestInlineQueryResultDocument.reply_markup)


class TestInlineQueryResultDocument:
    id = 'id'
    type = 'document'
    document_url = 'document url'
    title = 'title'
    caption = 'caption'
    mime_type = 'mime type'
    description = 'description'
    thumb_url = 'thumb url'
    thumb_width = 10
    thumb_height = 15
    input_message_content = InputTextMessageContent('input_message_content')
    reply_markup = InlineKeyboardMarkup([[InlineKeyboardButton('reply_markup')]])

    def test_expected_values(self, inline_query_result_document):
        assert inline_query_result_document.id == self.id
        assert inline_query_result_document.type == self.type
        assert inline_query_result_document.document_url == self.document_url
        assert inline_query_result_document.title == self.title
        assert inline_query_result_document.caption == self.caption
        assert inline_query_result_document.mime_type == self.mime_type
        assert inline_query_result_document.description == self.description
        assert inline_query_result_document.thumb_url == self.thumb_url
        assert inline_query_result_document.thumb_width == self.thumb_width
        assert inline_query_result_document.thumb_height == self.thumb_height
        assert inline_query_result_document.input_message_content.to_dict() == \
               self.input_message_content.to_dict()
        assert inline_query_result_document.reply_markup.to_dict() == self.reply_markup.to_dict()

    def test_to_json(self, inline_query_result_document):
        json.loads(inline_query_result_document.to_json())

    def test_to_dict(self, inline_query_result_document):
        inline_query_result_document_dict = inline_query_result_document.to_dict()

        assert isinstance(inline_query_result_document_dict, dict)
        assert inline_query_result_document_dict['id'] == self.id
        assert inline_query_result_document_dict['type'] == self.type
        assert inline_query_result_document_dict['document_url'] == self.document_url
        assert inline_query_result_document_dict['title'] == self.title
        assert inline_query_result_document_dict['caption'] == self.caption
        assert inline_query_result_document_dict['mime_type'] == self.mime_type
        assert inline_query_result_document_dict['description'] == self.description
        assert inline_query_result_document_dict['thumb_url'] == self.thumb_url
        assert inline_query_result_document_dict['thumb_width'] == self.thumb_width
        assert inline_query_result_document_dict['thumb_height'] == self.thumb_height
        assert inline_query_result_document_dict['input_message_content'] == \
               self.input_message_content.to_dict()
        assert inline_query_result_document_dict['reply_markup'] == \
               self.reply_markup.to_dict()

    def test_equality(self):
        a = InlineQueryResultDocument(self.id, self.document_url, self.title,
                                      self.mime_type)
        b = InlineQueryResultDocument(self.id, self.document_url, self.title,
                                      self.mime_type)
        c = InlineQueryResultDocument(self.id, "", self.title, self.mime_type)
        d = InlineQueryResultDocument("", self.document_url, self.title, self.mime_type)
        e = InlineQueryResultVoice(self.id, "", "")

        assert a == b
        assert hash(a) == hash(b)
        assert a is not b

        assert a == c
        assert hash(a) == hash(c)

        assert a != d
        assert hash(a) != hash(d)

        assert a != e
        assert hash(a) != hash(e)
