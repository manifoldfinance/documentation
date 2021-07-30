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

import os
import re
import requests

from cairosvg import svg2png
from cssutils import parseString
from hashlib import md5
from io import BytesIO
from mkdocs.config.config_options import Type
from mkdocs.plugins import BasePlugin
from PIL import Image, ImageDraw, ImageFont
from shutil import copyfile

# -----------------------------------------------------------------------------
# Class
# -----------------------------------------------------------------------------

# Social plugin
class SocialPlugin(BasePlugin):

    # Configuration scheme
    config_scheme = (
        ("cards", Type(bool, default = True)),
        ("cards_directory", Type(str, default = "assets/images/social"))
    )

    # Initialize plugin
    def __init__(self):
        self.color = colors.get("indigo")

        # Resolve and create cache directory
        self.cache = ".cache"
        if not os.path.isdir(self.cache):
            os.makedirs(self.cache)

    # Retrieve configuration for rendering
    def on_config(self, config):
        theme = config.get("theme")

        # Retrieve palette from theme configuration
        if "palette" in theme:
            palette = theme["palette"]

            # Use first palette, if multiple are defined
            if isinstance(palette, list):
                palette = palette[0]

            # Set colors according to palette
            if "primary" in palette:
                primary = palette["primary"].replace(" ", "-")
                self.color = colors.get(primary, self.color)

        # Retrieve logo and font
        self.logo = self.__load_logo(config)
        self.font = self.__load_font(config)

    # Create social cards
    def on_page_markdown(self, markdown, page, config, **kwargs):
        directory = self.config.get("cards_directory")
        file, _ = os.path.splitext(page.file.src_path)

        # Resolve path of image
        path = "{}.png".format(os.path.join(
            config.get("site_dir"),
            directory,
            file
        ))

        # Resolve path of image directory
        directory = os.path.dirname(path)
        if not os.path.isdir(directory):
            os.makedirs(directory)

        # Compute site name
        site_name = config.get("site_name")

        # Compute page title and description
        title = page.meta.get("title", page.title)
        description = config.get("site_description") or ""
        if "description" in page.meta:
            description = page.meta["description"]

        # Compute hash and try to copy from cache
        hash = md5("".join([site_name, title, description]).encode("utf-8"))
        file = os.path.join(self.cache, "{}.png".format(hash.hexdigest()))
        if os.path.isfile(file):
            copyfile(file, path)

        # Render card and save to file
        else:
            image = self.__render_card(site_name, title, description)
            image.save(path)

        # Inject meta tags into page
        meta = page.meta.get("meta", [])
        page.meta["meta"] = meta + self.__generate_meta(page, config)

    # -------------------------------------------------------------------------

    # Render social card
    def __render_card(self, site_name, title, description):
        logo = self.logo

        # Render background and logo
        image = self.__render_card_background((1200, 630), self.color["bg"])
        image.alpha_composite(
            logo.resize((144, int(144 * logo.height / logo.width))),
            (1200 - 228, 64 - 4)
        )

        # Render site name
        font = ImageFont.truetype(self.font.get(700), 36)
        image.alpha_composite(
            self.__render_text((826, 48), font, site_name),
            (64 + 4, 64)
        )

        # Render page title
        font = ImageFont.truetype(self.font.get(700), 92)
        image.alpha_composite(
            self.__render_text((826, 328), font, title, 20),
            (64, 160)
        )

        # Render page description
        font = ImageFont.truetype(self.font.get(400), 28)
        image.alpha_composite(
            self.__render_text((826, 80), font, description, 14),
            (64 + 4, 512)
        )

        # Return social card image
        return image

    # Render social card background
    def __render_card_background(self, size, fill):
        return Image.new(mode = "RGBA", size = size, color = fill)

    # Render social card text
    def __render_text(self, size, font, text, spacing = 0):
        lines, words = [], []

        # Create temporary image
        image = Image.new(mode = "RGBA", size = size)

        # Create drawing context and split text into lines
        context = ImageDraw.Draw(image)
        for word in text.split(" "):
            combine = " ".join(words + [word])
            textbox = context.textbbox((0, 0), combine, font = font)
            if textbox[2] <= image.width:
                words.append(word)
            else:
                lines.append(words)
                words = [word]

        # Balance words on last line
        if len(lines) > 0:
            prev = len(" ".join(lines[-1]))
            last = len(" ".join(words))

            # Heuristic: try to find a good ratio
            if last / prev < 0.6:
                words.insert(0, lines[-1].pop())

        # Join words for each line and create image
        lines.append(words)
        lines = [" ".join(line) for line in lines]
        image = Image.new(mode = "RGBA", size = size)

        # Create drawing context and split text into lines
        context = ImageDraw.Draw(image)
        context.text(
            (0, 0), "\n".join(lines),
            font = font, fill = self.color["fg"], spacing = spacing
        )

        # Return text image
        return image

    # -------------------------------------------------------------------------

    # Generate meta tags
    def __generate_meta(self, page, config):
        directory = self.config.get("cards_directory")
        file, _ = os.path.splitext(page.file.src_path)

        # Compute page title
        title = page.meta.get("title", page.title)
        if not page.is_homepage:
            title = "{} - {}".format(title, config.get("site_name"))

        # Compute page description
        description = config.get("site_description")
        if "description" in page.meta:
            description = page.meta["description"]

        # Resolve image URL
        url = "{}.png".format(os.path.join(
            config.get("site_url"),
            directory,
            file
        ))

        # Return meta tags
        return [

            # Meta tags for Open Graph
            { "property": "og:type", "content": "website" },
            { "property": "og:title", "content": title },
            { "property": "og:description", "content": description },
            { "property": "og:image", "content": url },
            { "property": "og:image:type", "content": "image/png" },
            { "property": "og:image:width", "content": "1200" },
            { "property": "og:image:height", "content": "630" },
            { "property": "og:url", "content": page.canonical_url },

            # Meta tags for Twitter
            { "name": "twitter:card", "content": "summary_large_image" },
            # { "name": "twitter:site", "content": user },
            # { "name": "twitter:creator", "content": user },
            { "name": "twitter:title", "content": title },
            { "name": "twitter:description", "content": description },
            { "name": "twitter:image", "content": url }
        ]

    # Retrieve logo image or icon
    def __load_logo(self, config):
        theme = config.get("theme")

        # Handle images (precedence over icons)
        if "logo" in theme:
            _, extension = os.path.splitext(theme["logo"])

            # Load SVG and convert to PNG
            path = os.path.join(config.get("docs_dir"), theme["logo"])
            if extension == ".svg":
                return self.__load_logo_svg(path)

            # Load PNG, JPEG, etc.
            return Image.open(path).convert("RGBA")

        # Handle icons
        logo = "material/library"
        icon = theme["icon"] or {}
        if "logo" in icon and icon["logo"]:
            logo = icon["logo"]

        # Resolve path of package
        base = os.path.abspath(os.path.join(
            os.path.dirname(__file__),
            "../.."
        ))

        # Load icon data and fill with color
        path = "{}/.icons/{}.svg".format(base, logo)
        return self.__load_logo_svg(path, self.color["fg"])

    # Load SVG file and convert to PNG
    def __load_logo_svg(self, path, fill = None):
        file = BytesIO()
        data = open(path).read()

        # Fill with color, if given
        if fill:
            data = data.replace(
                "<svg",
                "<svg fill=\"{}\"".format(fill)
            )

        # Convert to PNG and return image
        svg2png(bytestring = data, write_to = file, scale = 10)
        return Image.open(file)

    # Retrieve fonts
    def __load_font(self, config):
        theme = config.get("theme")

        # Retrieve font name (use Roboto, if disabled)
        name = "Roboto"
        if theme["font"]:
            name = theme["font"]["text"]

        # Retrieve font files, if not already done
        if not all(os.path.isfile(
            os.path.join(self.cache, "{}.{}.ttf".format(name, weight))
        ) for weight in ["400", "700"]):
            self.__load_font_webfont(name)

        # Return paths associated with font weights
        return {
            400: os.path.join(self.cache, "{}.400.ttf".format(name)),
            700: os.path.join(self.cache, "{}.700.ttf".format(name))
        }

    # Retrieve font from Google Fonts
    def __load_font_webfont(self, name):
        url = "https://fonts.googleapis.com/css?family={}:400,700"
        res = requests.get(url.format(name.replace(" ", "+")))

        # Parse font declarations from stylesheet
        sheet = parseString(res.text)
        fonts = dict((
            rule.style["font-weight"],
            rule.style["src"]
        ) for rule in sheet)

        # Fetch referenced fonts
        for weight, url in fonts.items():
            url = re.search("url\((.+?)\)", url).group(1)
            res = requests.get(url)

            # Save font to file
            font = "{}.{}.ttf".format(name, weight)
            file = open(os.path.join(self.cache, font), "wb")
            file.write(res.content)
            file.close()

# -----------------------------------------------------------------------------
# Data
# -----------------------------------------------------------------------------

# Color palette
colors = dict({
    "red":         { "bg": "#ef5552", "fg": "#ffffff" },
    "pink":        { "bg": "#e92063", "fg": "#ffffff" },
    "purple":      { "bg": "#ab47bd", "fg": "#ffffff" },
    "deep-purple": { "bg": "#7e56c2", "fg": "#ffffff" },
    "indigo":      { "bg": "#4051b5", "fg": "#ffffff" },
    "blue":        { "bg": "#2094f3", "fg": "#ffffff" },
    "light-blue":  { "bg": "#02a6f2", "fg": "#ffffff" },
    "cyan":        { "bg": "#00bdd6", "fg": "#ffffff" },
    "teal":        { "bg": "#009485", "fg": "#ffffff" },
    "green":       { "bg": "#4cae4f", "fg": "#ffffff" },
    "light-green": { "bg": "#8bc34b", "fg": "#ffffff" },
    "lime":        { "bg": "#cbdc38", "fg": "#000000" },
    "yellow":      { "bg": "#ffec3d", "fg": "#000000" },
    "amber":       { "bg": "#ffc105", "fg": "#000000" },
    "orange":      { "bg": "#ffa724", "fg": "#000000" },
    "deep-orange": { "bg": "#ff6e42", "fg": "#ffffff" },
    "brown":       { "bg": "#795649", "fg": "#ffffff" },
    "grey":        { "bg": "#757575", "fg": "#ffffff" },
    "blue-grey":   { "bg": "#546d78", "fg": "#ffffff" },
    "black":       { "bg": "#000000", "fg": "#ffffff" },
    "white":       { "bg": "#ffffff", "fg": "#000000" }
})
