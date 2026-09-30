"""Reading-level judgments for the easy-reads section.

Each level is a judgment from published facts about the book, not a measurement made here:
published Lexile measures and grade bands (placed on MetaMetrics' Lexile-to-CEFR alignment),
who the book was written for, and features that make a text harder than its Lexile suggests
(dialect, deliberately rare words, specialist vocabulary). Word counts are plain lengths of the
Standard Ebooks texts (whitespace-separated words), re-counted at build time (see WORDS). Every
quoted example below is re-checked against the book text at build time (see EXAMPLES).
"""

# MetaMetrics' own papers were blocked by this environment's network policy; the figures are as
# quoted by search results (2026-09-29/30).
CEFR_SOURCES = [
    ("MetaMetrics, \"Aligning the Lexile Framework to the CEFR\" (research brief)",
     "https://www2.metametricsinc.com/hubfs/Aligning-the-Lexile-Framework-to-the-CEFR-Research-Brief.pdf",
     "texts for lower B1 about 700L–1000L, up to about 1200L at the top of B1; B2 from about 1000L"),
    ("MetaMetrics, \"Aligning the Lexile Framework to the CEFR\" (2018 concordance table)",
     "https://metametricsinc.com/wp-content/uploads/2018/07/Aligning-the-Lexile-Framework-to-the-CEFR.pdf",
     "readers: A2 540L–800L, B1 805L–1090L, B2 1095L–1320L"),
]

EASY = {
    "potter": {
        "lexile": "AD660L (*Peter Rabbit*)",
        "level": "A2–B1",
        "facts": [
            "*The Tale of Peter Rabbit* has a Lexile measure of AD660L (\"AD\" means it was written to be read aloud to young children) and an Accelerated Reader level of 4.2",
            "each tale is only a few pages long; all 20 tales in this edition come to about 31,000 words",
            "Potter sometimes picks a rare word on purpose (\"soporific,\" \"implored him to exert himself\"), but the sentences around it make it clear",
        ],
        "sources": [("library catalogue record", "https://eh.catalog.lionlibraries.org/Record/.b21889764")],
    },
    "aesop": {
        "lexile": "760L–780L",
        "level": "A2–B1",
        "facts": [
            "common editions have Lexile measures of 760L–780L and are recommended for grades 3–5",
            "each fable is only a few sentences long, often ending with a one-line moral (\"Slow and steady wins the race.\")",
            "284 fables, about 40,000 words in all, so it is easy to read a few at a time",
        ],
        "sources": [("library catalogue record", "https://catalog.deerfieldlibrary.org/Record/.b10959373")],
    },
    "wilde": {
        "lexile": "650L (900L illustrated)",
        "level": "B1",
        "facts": [
            "*The Happy Prince and Other Tales* has a Lexile measure of 650L in most editions (900L in some illustrated ones)",
            "the sentences are short and clear, but the vocabulary is more literary than the Lexile suggests (\"coquette,\" \"alighted,\" \"pedestal\"), which is why it is placed at B1 rather than A2",
            "the five tales were written as children's stories and come to about 16,000 words",
            "the same Standard Ebooks volume adds Wilde's second collection, *A House of Pomegranates*; its four tales total about 33,000 words, so each is much longer. Start with the first five",
        ],
        "sources": [("library catalogue record", "https://catalog.wake.gov/Record/711851")],
    },
    "pinocchio": {
        "lexile": "780L",
        "level": "B1",
        "facts": [
            "Lexile measure 780L; Accelerated Reader level 5.3",
            "first published as a serial in an Italian children's magazine, so it comes in 36 short chapters (about 41,500 words)",
        ],
        "sources": [("library catalogue record", "https://opac.marmot.org/Record/.b11527602")],
    },
    "pooh": {
        "lexile": "790L",
        "level": "B1",
        "facts": [
            "Lexile measure 790L; Accelerated Reader level 4.6",
            "short: ten chapters, about 22,500 words",
            "watch for jokes built on misspelling, like Owl's notice \"Ples ring if an rnser is reqird\" and Piglet's sign \"Trespassers W\"",
        ],
        "sources": [("library catalogue record", "https://bemis.marmot.org/Record/.b28380289")],
    },
    "grimm": {
        "lexile": "980L–1090L",
        "level": "B1 (read tale by tale)",
        "facts": [
            "Lexile measures of 980L–1090L depending on the edition; recommended for readers aged 8 and up",
            "more than 200 tales and about 283,000 words, far too long to read straight through, but each famous tale is only a few pages",
            "this 1884 translation keeps a few German name forms, such as \"Hänsel and Grethel\"",
        ],
        "sources": [("library catalogue record", "https://bemis2.marmot.org/Record/.b28004279"),
                    ("SuperSummary", "https://supersummary.com/grimms-fairy-tales/book-brief")],
    },
    "heidi": {
        "lexile": "1000L",
        "level": "B1 (upper end)",
        "facts": [
            "full-length editions have a Lexile measure of 1000L, the top of the lower-B1 range",
            "about 50,000 words",
            "a few Swiss-German names and words are kept (\"the Alm-Uncle,\" \"Im Dörfli\"), and the text explains them",
        ],
        "sources": [("library catalogue record", "https://lakecounty.marmot.org/Record/.b11611741")],
    },
    "oz": {
        "lexile": "1030L",
        "level": "B1 (upper end)",
        "facts": [
            "Lexile measure 1030L, a little above the lower-B1 range but well inside upper B1; recommended for grades 3–5 (Flesch-Kincaid grade 5.6)",
            "about 39,000 words",
            "plain, modern English: Baum wrote that it \"aspires to being a modernized fairy tale\"",
        ],
        "sources": [("ReadingVine", "https://www.readingvine.com/the-wonderful-wizard-of-oz-reading-level/")],
    },
}

NEAR_MISSES = [
    ("Peter Pan (Peter and Wendy)", "J. M. Barrie, 1911", "B2",
     "Its Lexile (920L–980L) looks easy, but the narrator is sarcastic and opinionated and uses rare words on purpose "
     "(\"embonpoint,\" \"pluperfect,\" \"quietus\" are all in the text).",
     [("CBCA Reading Time review", "https://readingtime.cbca.org.au/complete-peter-pan/")]),
    ("Black Beauty", "Anna Sewell, 1877", "B1–B2",
     "Lexile about 990L–1020L, but Sewell wrote it for adults who work with horses, not for children, and it is full of "
     "harness terms such as \"bearing reins.\"",
     [("ReadingVine", "https://www.readingvine.com/books/black-beauty/"),
      ("Susan Elkin", "https://susanelkin.co.uk/articles/susans-bookshelves-black-beauty-by-anna-sewell/")]),
    ("The Secret Garden", "Frances Hodgson Burnett, 1911", "B2",
     "Lexile 970L, but much of the dialogue is in Yorkshire dialect (\"An' tha's browt th' young 'un with thee\"); one "
     "study guide needs a glossary of more than 400 entries.",
     [("Heron Books glossary", "https://www.heronbooks.com/store/Glossary-and-Notes-The-Secret-Garden-p143416150")]),
    ("The Jungle Book", "Rudyard Kipling, 1894", "B2",
     "Lexile 1140L, recommended for grades 5–8, and the animals speak old-fashioned English (\"Thou art the master\").",
     [("ReadingVine", "https://www.readingvine.com/books/the-jungle-book/")]),
]

ALSO_EASY_NOT_CHECKED = [
    ("Hans Christian Andersen's fairy tales", "Lexile 860L–1040L depending on the translation",
     [("TeachingBooks", "https://school.teachingbooks.net/tb.cgi?tid=23948"),
      ("Reading Is Fundamental", "https://rif.org/literacy-central/book/classic-fairy-tales-andersens-fairy-tales")]),
    ("Joseph Jacobs's *English Fairy Tales* (Jack and the Beanstalk, the Three Little Pigs)", "Lexile 1040L, ages 8–14",
     [("library catalogue record", "https://lafayette.flatironslibrary.org/Record/.b25679065")]),
    ("*The Velveteen Rabbit* (Margery Williams, 1922)", "Lexile AD1050L, and very short",
     [("library catalogue record", "https://eh.catalog.lionlibraries.org/Record/.b17226879")]),
]

# quoted examples in the level notes, re-checked against the book text at build time
EXAMPLES = {
    "potter": ["soporific", "implored him to exert himself"],
    "aesop": ["Slow and steady wins the race."],
    "wilde": ["coquette", "alighted", "pedestal"],
    "pooh": ["Ples ring if an rnser is reqird", "Trespassers W"],
    "grimm": ["Hänsel and Grethel"],
    "heidi": ["the Alm-Uncle", "Im Dörfli"],
    "oz": ["aspires to being a modernized fairy tale"],
    "peterpan": ["embonpoint", "pluperfect", "quietus"],
    "blackbeauty": ["bearing reins"],
    "secretgarden": ["An' tha's browt th' young 'un with thee"],
    "junglebook": ["Thou art the master"],
}

# "about N words" in the facts above, re-counted at build time (whitespace-separated words; must be
# within 3%). Keys: book, and which sections (all, or a slice of the section list).
WORDS = [
    ("potter", "all", None, 31000),
    ("aesop", "all", None, 40000),
    ("wilde", "first five tales", (0, 5), 16000),
    ("wilde", "last four tales", (5, 9), 33000),
    ("pinocchio", "all", None, 41500),
    ("pooh", "all", None, 22500),
    ("grimm", "all", None, 283000),
    ("heidi", "all", None, 50000),
    ("oz", "all", None, 39000),
]
