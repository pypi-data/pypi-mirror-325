"""
Blocks module entry point. Used to cleanly organize blocks into
individual files based on purpose, but provide them all as a
single `blocks` module.
"""

from django.utils.translation import gettext_lazy as _

from .html_blocks import (
    ButtonBlock,
    ImageBlock,
    ImageLinkBlock,
    DownloadBlock,
    EmbedVideoBlock,
    PageListBlock,
    PagePreviewBlock,
    QuoteBlock,
    RichTextBlock,
    TableBlock,
    SearchableHTMLBlock,
)
from .content_blocks import (  # noqa
    AccordionBlock,
    CardBlock,
    CarouselBlock,
    FilmStripBlock,
    ImageGalleryBlock,
    ModalBlock,
    NavDocumentLinkWithSubLinkBlock,
    NavExternalLinkWithSubLinkBlock,
    NavPageLinkWithSubLinkBlock,
    PriceListBlock,
    ReusableContentBlock,
    HighlightBlock,
)
from .content.events import PublicEventBlock, EventCalendarBlock
from .content.countdown import CountdownBlock
from .layout_blocks import CardGridBlock, GridBlock, HeroBlock
from cjkcms.settings import cms_settings

# Collections of blocks commonly used together.

HTML_STREAMBLOCKS = [
    (
        "text",
        RichTextBlock(
            icon="font",
            features=cms_settings.CJKCMS_RICHTEXT_FEATURES["full"],
        ),
    ),
    ("button", ButtonBlock()),
    ("image", ImageBlock()),
    ("image_link", ImageLinkBlock()),
    (
        "html",
        SearchableHTMLBlock(
            icon="code",
            form_classname="monospace",
            label=_("HTML"),
        ),
    ),
    ("download", DownloadBlock()),
    ("embed_video", EmbedVideoBlock()),
    ("quote", QuoteBlock()),
    ("table", TableBlock()),
    ("page_list", PageListBlock()),
    ("page_preview", PagePreviewBlock()),
]

CONTENT_STREAMBLOCKS = HTML_STREAMBLOCKS + [
    ("accordion", AccordionBlock()),
    ("card", CardBlock()),
    ("carousel", CarouselBlock()),
    ("filmstrip", FilmStripBlock()),
    ("image_gallery", ImageGalleryBlock()),
    ("modal", ModalBlock(HTML_STREAMBLOCKS)),
    ("pricelist", PriceListBlock()),
    ("reusable_content", ReusableContentBlock()),
    ("event_calendar", EventCalendarBlock()),
    ("highlight", HighlightBlock()),
    ("countdown", CountdownBlock()),
]

NAVIGATION_STREAMBLOCKS = [
    ("page_link", NavPageLinkWithSubLinkBlock()),
    ("external_link", NavExternalLinkWithSubLinkBlock()),
    ("document_link", NavDocumentLinkWithSubLinkBlock()),
]

PUBLIC_EVENT_STREAMBLOCKS = [
    ("event", PublicEventBlock()),
]

BASIC_LAYOUT_STREAMBLOCKS = [
    ("row", GridBlock(HTML_STREAMBLOCKS)),
    (
        "html",
        SearchableHTMLBlock(icon="code", form_classname="monospace", label=_("HTML")),
    ),
]

LAYOUT_STREAMBLOCKS = [
    (
        "hero",
        HeroBlock(
            [
                ("row", GridBlock(CONTENT_STREAMBLOCKS)),
                (
                    "cardgrid",
                    CardGridBlock(
                        [
                            ("card", CardBlock()),
                        ]
                    ),
                ),
                (
                    "html",
                    SearchableHTMLBlock(
                        icon="code", form_classname="monospace", label=_("HTML")
                    ),
                ),
            ]
        ),
    ),
    ("row", GridBlock(CONTENT_STREAMBLOCKS)),
    (
        "cardgrid",
        CardGridBlock(
            [
                ("card", CardBlock()),
            ]
        ),
    ),
    (
        "html",
        SearchableHTMLBlock(icon="code", form_classname="monospace", label=_("HTML")),
    ),
]
