# Copyright (c) 2016-2021 Martin Donath <martin.donath@squidfunk.com>

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to
# deal in the Software without restriction, including without limitation the
# rights to use, copy, modify, merge, publish, distribute, sublicense, and/or
# sell copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NON-INFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS
# IN THE SOFTWARE.

from html import escape
from html.parser import HTMLParser
from mkdocs.contrib.search import SearchPlugin as BasePlugin
from mkdocs.contrib.search.search_index import SearchIndex as BaseIndex

# -----------------------------------------------------------------------------
# Class
# -----------------------------------------------------------------------------

# Search plugin with custom search index
class SearchPlugin(BasePlugin):

    # Override: use custom search index
    def on_pre_build(self, config):
        super().on_pre_build(config)
        self.search_index = SearchIndex(**self.config)

# -----------------------------------------------------------------------------

# Search index with support for additional fields
class SearchIndex(BaseIndex):

    # Override: use custom content parser
    def add_entry_from_context(self, page):
        search = page.meta.get("search", {})
        if "exclude" in search and search["exclude"]:
            return

        # Divide page content into sections
        parser = ContentParser()
        parser.feed(page.content)
        parser.close()

        # Ensure presence of top-level section
        if len(parser.data) and parser.data[0].tag != "h1":
            section = ContentSection("h1")
            section.title.append(page.title)

            # Insert section at the start
            parser.data.insert(0, section)

        # Add sections to index
        for section in parser.data:
            self.create_entry_for_section(section, page.toc, page.url, page)

    # Override: graceful indexing and additional fields
    def create_entry_for_section(self, section, toc, url, page):
        item = self._find_toc_by_id(toc, section.id)
        if item and not section.tag == "h1":
            url = url + item.url

        # Compute text
        text = ""
        if self.config["indexing"] != "titles":
            text = "".join(section.text).strip()

        # Create entry for section
        entry = {
            "title": "".join(section.title),
            "text": text,
            "location": url
        }

        # Add document tags, if any
        if "tags" in page.meta:
            entry["tags"] = page.meta["tags"]

        # Add document boost for search, if any
        search = page.meta.get("search", {})
        if "boost" in search:
            entry["boost"] = search["boost"]

        # Add entry to index
        self._entries.append(entry)

# -----------------------------------------------------------------------------

# Content section
class ContentSection:
    """
    A content section is a block of text, preceded by a headline with a certain
    tag and title, optionally with an identifier. It's used by the parser.
    """

    # Intialize content section
    def __init__(self, tag):
        self.tag   = tag
        self.text  = []
        self.title = []
        self.id    = None

# -----------------------------------------------------------------------------

# Content parser
class ContentParser(HTMLParser):
    """
    This parser divides the given string of HTML into a list of sections, each
    of which are preceded by a h1-h6 level heading. A white- and blacklist of
    tags dictates which tags should be preserved as part of the index, and
    which should be ignored in its entirety.
    """

    # Initialize content parser
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Tags to skip
        self.skip = set([
            "img",                     # Images
            "object",                  # Objects
            "script",                  # Scripts
            "style"                    # Styles
        ])

        # Tags to keep
        self.keep = set([
            "p",                       # Paragraphs
            "code", "pre",             # Code blocks
            "li", "ol", "ul"           # Lists
        ])

        # Current context and section
        self.context = []
        self.section = None

        # All parsed sections
        self.data = []

    # Called at the start of every HTML tag
    def handle_starttag(self, tag, attrs):
        self.context.append(tag)

        # Handle headings
        if tag in ([f"h{x}" for x in range(1, 7)]):
            if not self.section or (
                tag != "h1" or
                tag != self.section.tag
            ):
                self.section = ContentSection(tag)
                self.data.append(self.section)

            # Set identifier on section for TOC resolution
            for attr in attrs:
                if attr[0] == "id":
                    self.section.id = attr[1]
                    break

        # Handle preface - ensure top-level section
        if not self.section:
            self.section = ContentSection("h1")
            self.data.append(self.section)

        # Render opening tag if kept
        if tag in self.keep:
            text = self.section.text
            if self.section.tag in self.context:
                text = self.section.title

            # Append to section title or text
            text.append("<{}>".format(tag))

    # Called at the end of every HTML tag
    def handle_endtag(self, tag):
        if self.context[-1] == tag:
            self.context.pop()

        # Render closing tag if kept
        if tag in self.keep:
            text = self.section.text
            if self.section.tag in self.context:
                text = self.section.title

            # Append to section title or text
            text.append("</{}>".format(tag))

    # Called for the text contents of each tag.
    def handle_data(self, data):
        if self.skip.intersection(self.context):
            return

        # Collapse whitespace in non-pre contexts
        if not "pre" in self.context:
            if not data.isspace():
                data = data.replace("\n", " ")
            else:
                data = " "

        # Handle preface - ensure top-level section
        if not self.section:
            self.section = ContentSection("h1")
            self.data.append(self.section)

        # Ignore section headline
        if self.section.tag in self.context:
            if not "a" in self.context:
                self.section.title.append(
                    escape(data, quote = False)
                )

        # Handle everything else
        else:
            self.section.text.append(
                escape(data, quote = False)
            )
