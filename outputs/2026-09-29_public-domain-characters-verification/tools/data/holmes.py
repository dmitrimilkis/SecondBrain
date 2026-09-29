BOOK = {
    "title": "The Adventures of Sherlock Holmes",
    "author": "Arthur Conan Doyle",
    "year": "1892",
    "edition": "Standard Ebooks edition (the twelve stories of the 1892 collection)",
    "source": "https://github.com/standardebooks/arthur-conan-doyle_the-adventures-of-sherlock-holmes",
    "characters": [
        {
            "name": "Sherlock Holmes",
            "aka": "",
            "description": (
                "The detective of 221B Baker Street, \"the most perfect reasoning and observing machine that the world has seen,\" with a mind that "
                "finds emotions \"abhorrent.\" Tall and gaunt, with a \"hawk-like nose\" and \"long, thin fingers\"; he smokes a black clay pipe (\"quite "
                "a three pipe problem\"), is \"an enthusiastic musician,\" swings between \"cocaine and ambition,\" and is a master of disguise (a "
                "drunken groom, a clergyman). He wears a \"close-fitting cloth cap,\" but the word \"deerstalker\" never appears, and he never says "
                "\"Elementary, my dear Watson.\""
            ),
            "evidence": [
                {"quote": "applying at 6:30 this evening at 221B, Baker Street", "supports": "address"},
                {"quote": "He was, I take it, the most perfect reasoning and observing machine that the world has seen", "supports": "reasoning machine"},
                {"quote": "All emotions, and that one particularly, were abhorrent to his cold, precise but admirably balanced mind.", "supports": "cold mind"},
                {"quote": "You see, but you do not observe.", "supports": "method"},
                {"quote": "his tall, gaunt figure made even gaunter and taller by his long grey travelling-cloak and close-fitting cloth cap", "supports": "figure, cap"},
                {"quote": "with his thin knees drawn up to his hawk-like nose, and there he sat with his eyes closed and his black clay pipe thrusting out like the bill of some strange bird", "supports": "nose, pipe"},
                {"quote": "It is quite a three pipe problem, and I beg that you won't speak to me for fifty minutes.", "supports": "pipe-smoking thought"},
                {"quote": "My friend was an enthusiastic musician, being himself not only a very capable performer but a composer of no ordinary merit.", "supports": "music"},
                {"quote": "gently waving his long, thin fingers in time to the music", "supports": "fingers"},
                {"quote": "alternating from week to week between cocaine and ambition, the drowsiness of the drug, and the fierce energy of his own keen nature", "supports": "cocaine"},
                {"quote": "a drunken-looking groom, ill-kempt and side-whiskered, with an inflamed face and disreputable clothes", "supports": "disguise 1"},
                {"quote": "in the character of an amiable and simple-minded Nonconformist clergyman", "supports": "disguise 2"},
            ],
            "absent": [r"Elementary, my dear Watson", r"\bdeerstalker\b"],
            "not_quotes": ["deerstalker", "Elementary, my dear Watson"],
        },
        {
            "name": "Dr. Watson",
            "aka": "the narrator",
            "description": (
                "Holmes's \"intimate friend and associate\" and the narrator of the stories: a doctor who has \"returned to civil practice\" and "
                "married, so he now sees less of Holmes. He still carries \"the Jezail bullet\" from his \"Afghan campaign.\" Holmes relies on him "
                "(\"someone with me on whom I can thoroughly rely\"). His first name is not given in this collection, and in \"The Man with the "
                "Twisted Lip\" his wife calls him \"James.\""
            ),
            "evidence": [
                {"quote": "This is my intimate friend and associate, Dr. Watson, before whom you can speak as freely as before myself.", "supports": "role"},
                {"quote": "I was returning from a journey to a patient (for I had now returned to civil practice)", "supports": "doctor"},
                {"quote": "My marriage had drifted us away from each other.", "supports": "married"},
                {"quote": "the Jezail bullet which I had brought back in one of my limbs as a relic of my Afghan campaign throbbed with dull persistence", "supports": "war wound"},
                {"quote": "It makes a considerable difference to me, having someone with me on whom I can thoroughly rely.", "supports": "Holmes relies on him"},
                {"quote": "Or should you rather that I sent James off to bed?", "supports": "the 'James' slip"},
            ],
            "absent": [r"John.{0,3}Watson|\bJohn H\."],
        },
        {
            "name": "Irene Adler",
            "aka": "\"the woman\"",
            "description": (
                "An opera singer (\"Born in New Jersey in the year 1858. Contralto ... Prima donna Imperial Opera of Warsaw\") and the woman who "
                "outwits Holmes, so that to him \"she is always the woman.\" The King of Bohemia says she has \"the face of the most beautiful of "
                "women, and the mind of the most resolute of men.\" A trained actress, she sees through Holmes's disguise, disguises herself in "
                "men's clothes, marries the lawyer Godfrey Norton and slips away."
            ),
            "evidence": [
                {"quote": "Born in New Jersey in the year 1858. Contralto-hum! La Scala, hum! Prima donna Imperial Opera of Warsaw-yes!", "supports": "biography"},
                {"quote": "To Sherlock Holmes she is always the woman.", "supports": "the woman"},
                {"quote": "She has the face of the most beautiful of women, and the mind of the most resolute of men.", "supports": "beauty and resolve"},
                {"quote": "I have been trained as an actress myself. Male costume is nothing new to me.", "supports": "actress, male disguise"},
                {"quote": "Even after I became suspicious, I found it hard to think evil of such a dear, kind old clergyman.", "supports": "sees through his disguise"},
                {"quote": "Good night, Mister Sherlock Holmes.", "supports": "greets him in disguise"},
                {"quote": "so you will find the nest empty when you call tomorrow", "supports": "slips away"},
                {"quote": "This Godfrey Norton was evidently an important factor in the matter. He was a lawyer.", "supports": "Godfrey Norton, lawyer"},
                {"quote": "the best plans of Mr. Sherlock Holmes were beaten by a woman's wit", "supports": "outwits Holmes"},
                {"quote": "Irene Norton, nee Adler.", "supports": "marries Godfrey Norton"},
            ],
        },
        {
            "name": "Inspector Lestrade",
            "aka": "Lestrade, of Scotland Yard",
            "description": (
                "The Scotland Yard detective, whom Watson describes as \"A lean, ferret-like man, furtive and sly-looking.\" Self-satisfied about his "
                "own theories, he scoffs at Holmes's methods, yet refers puzzling cases to him. In \"The Boscombe Valley Mystery\" he insists the son "
                "is the killer, and the real murderer later confesses to Holmes."
            ),
            "evidence": [
                {"quote": "A lean, ferret-like man, furtive and sly-looking, was waiting for us upon the platform.", "supports": "appearance"},
                {"quote": "I had no difficulty in recognising Lestrade, of Scotland Yard", "supports": "Scotland Yard"},
                {"quote": "Lestrade, being rather puzzled, has referred the case to me", "supports": "refers cases to Holmes"},
                {"quote": "Lestrade laughed indulgently. \"You have, no doubt, already formed your conclusions from the newspapers,\" he said.", "supports": "condescension"},
                {"quote": "That McCarthy senior met his death from McCarthy junior and that all theories to the contrary are the merest moonshine.", "supports": "his wrong theory"},
                {"quote": "I did it, Mr. Holmes. I would do it again.", "supports": "the real killer, old Turner, confesses"},
            ],
        },
        {
            "name": "Mrs. Hudson",
            "aka": "the landlady",
            "description": (
                "Holmes's landlady, who gets woken early for clients and lights the fire for them. In \"A Scandal in Bohemia\" the landlady is called "
                "\"Mrs. Turner\" instead."
            ),
            "evidence": [
                {"quote": "Mrs. Hudson has been knocked up, she retorted upon me, and I on you.", "supports": "woken for a client"},
                {"quote": "I am glad to see that Mrs. Hudson has had the good sense to light the fire.", "supports": "looks after visitors"},
                {"quote": "When Mrs. Turner has brought in the tray I will make it clear to you.", "supports": "'Mrs. Turner' slip"},
            ],
        },
    ],
}
