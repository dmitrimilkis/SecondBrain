BOOK = {
    "title": "Frankenstein; or, The Modern Prometheus",
    "author": "Mary Shelley",
    "year": "1818 (revised 1831)",
    "edition": "Standard Ebooks edition, based on the revised 1831 text",
    "source": "https://github.com/standardebooks/mary-shelley_frankenstein",
    "characters": [
        {
            "name": "Victor Frankenstein",
            "aka": "",
            "description": (
                "A young Genevese scientist from one of the republic's leading families who, as a student at the University of Ingolstadt, "
                "discovers how to \"infuse a spark of being into the lifeless thing\" and builds a living man. He is a student, never called "
                "\"Doctor.\" Horrified by what he has made, he runs from it (\"I rushed out of the room\"), and the Creature later kills his little "
                "brother, his best friend and his bride. When the explorer Walton finds him adrift \"on a large fragment of ice,\" his eyes have \"an "
                "expression of wildness, and even madness.\""
            ),
            "evidence": [
                {"quote": "I am by birth a Genevese; and my family is one of the most distinguished of that republic.", "supports": "origin"},
                {"quote": "my parents resolved that I should become a student at the university of Ingolstadt", "supports": "student at Ingolstadt"},
                {"quote": "I collected the instruments of life around me, that I might infuse a spark of being into the lifeless thing that lay at my feet", "supports": "creation"},
                {"quote": "breathless horror and disgust filled my heart. Unable to endure the aspect of the being I had created, I rushed out of the room", "supports": "flees his creation"},
                {"quote": "It was, in fact, a sledge, like that we had seen before, which had drifted towards us in the night, on a large fragment of ice. Only one dog remained alive; but there was a human being within it", "supports": "found on the ice"},
                {"quote": "his eyes have generally an expression of wildness, and even madness", "supports": "Walton's view of him"},
            ],
            "absent": [r"\b(Dr\.?|Doctor) Frankenstein\b"],
        },
        {
            "name": "The Creature",
            "aka": "never named; called \"daemon,\" \"fiend,\" \"wretch,\" \"monster\"",
            "description": (
                "Victor's creation, built \"about eight feet in height\" with features chosen \"as beautiful,\" but hideous when alive: \"yellow skin\" "
                "barely covering \"muscles and arteries,\" flowing \"lustrous black\" hair, teeth \"of a pearly whiteness,\" \"watery eyes,\" a \"shrivelled "
                "complexion and straight black lips.\" He has no name. By secretly listening to a cottager family he teaches himself to speak and "
                "read (Paradise Lost, Plutarch's Lives, Werther); shut out by everyone (\"Everywhere I see bliss, from which I alone am irrevocably "
                "excluded\"), he turns to revenge: \"I was benevolent and good; misery made me a fiend.\" He kills Victor's little brother William, "
                "then Clerval and Elizabeth. The book has no neck bolts, green skin or Igor."
            ),
            "evidence": [
                {"quote": "to make the being of a gigantic stature; that is to say, about eight feet in height, and proportionably large", "supports": "height"},
                {"quote": "His limbs were in proportion, and I had selected his features as beautiful. Beautiful!-Great God! His yellow skin scarcely covered the work of muscles and arteries beneath; his hair was of a lustrous black, and flowing; his teeth of a pearly whiteness; but these luxuriances only formed a more horrid contrast with his watery eyes, that seemed almost of the same colour as the dun white sockets in which they were set, his shrivelled complexion and straight black lips.", "supports": "appearance"},
                {"quote": "While I improved in speech, I also learned the science of letters, as it was taught to the stranger", "supports": "learns to speak and read"},
                {"quote": "they consisted of Paradise Lost, a volume of Plutarch's Lives, and the Sorrows of Werther", "supports": "self-education"},
                {"quote": "Everywhere I see bliss, from which I alone am irrevocably excluded.", "supports": "excluded"},
                {"quote": "I ought to be thy Adam; but I am rather the fallen angel", "supports": "his self-image"},
                {"quote": "I was benevolent and good; misery made me a fiend. Make me happy, and I shall again be virtuous.", "supports": "turn to evil"},
                {"quote": "William is dead!-that sweet child", "supports": "William, Victor's little brother"},
                {"quote": "'Frankenstein! you belong then to my enemy-to him towards whom I have sworn eternal revenge; you shall be my first victim.'", "supports": "targets William as a Frankenstein"},
                {"quote": "I grasped his throat to silence him, and in a moment he lay dead at my feet.", "supports": "kills William"},
                {"quote": "After the murder of Clerval, I returned to Switzerland", "supports": "kills Clerval (his own words)"},
                {"quote": "The murderous mark of the fiend's grasp was on her neck", "supports": "kills Elizabeth"},
                {"quote": "You must create a female for me", "supports": "demands a mate"},
            ],
            "absent": [r"\bIgor\b", r"neck.{0,20}bolts?|bolts?.{0,20}neck", r"green (skin|complexion|face)"],
            "allow_terms": ["Igor"],
        },
        {
            "name": "Elizabeth Lavenza",
            "aka": "",
            "description": (
                "Victor's adopted \"more than sister\" and later his bride. In this 1831 text she is a foundling Victor's parents find in a poor "
                "cottage on \"the shores of the Lake of Como\": \"thin, and very fair,\" with hair of \"the brightest living gold\" and \"blue eyes "
                "cloudless.\" The Creature murders her on the wedding night, as he had threatened (\"I shall be with you on your wedding night\")."
            ),
            "evidence": [
                {"quote": "they passed a week on the shores of the Lake of Como. Their benevolent disposition often made them enter the cottages of the poor.", "supports": "found near Lake Como"},
                {"quote": "this child was thin, and very fair. Her hair was the brightest living gold", "supports": "appearance"},
                {"quote": "her blue eyes cloudless", "supports": "blue eyes"},
                {"quote": "Elizabeth Lavenza became the inmate of my parents' house-my more than sister", "supports": "adopted"},
                {"quote": "I go; but remember, I shall be with you on your wedding night.", "supports": "the threat"},
                {"quote": "She was there, lifeless and inanimate, thrown across the bed", "supports": "murdered"},
            ],
        },
        {
            "name": "Henry Clerval",
            "aka": "",
            "description": (
                "Victor's boyhood best friend, \"the son of a merchant of Geneva\" and \"a boy of singular talent and fancy\" who loved \"books of "
                "chivalry and romance.\" He nurses Victor through months of fever and is later murdered by the Creature."
            ),
            "evidence": [
                {"quote": "Henry Clerval was the son of a merchant of Geneva. He was a boy of singular talent and fancy. He loved enterprise, hardship, and even danger, for its own sake. He was deeply read in books of chivalry and romance.", "supports": "background, character"},
                {"quote": "This was the commencement of a nervous fever, which confined me for several months. During all that time Henry was my only nurse.", "supports": "nurses Victor for months"},
                {"quote": "I saw the lifeless form of Henry Clerval stretched before me", "supports": "murdered"},
            ],
        },
        {
            "name": "Robert Walton",
            "aka": "",
            "description": (
                "An ambitious, lonely explorer (\"I have no friend, Margaret\") on \"a voyage of discovery towards the northern pole,\" whose letters "
                "to his sister Margaret Saville in England frame the story. He takes Victor aboard from the ice, hears his tale, and finally agrees "
                "to turn back when his crew demands it."
            ),
            "evidence": [
                {"quote": "To Mrs. Saville, England.", "supports": "letters addressed to England"},
                {"quote": "Your affectionate brother, R. Walton.", "supports": "she is his sister"},
                {"quote": "I try in vain to be persuaded that the pole is the seat of frost and desolation", "supports": "polar goal"},
                {"quote": "we were on a voyage of discovery towards the northern pole", "supports": "polar voyage"},
                {"quote": "I have no friend, Margaret", "supports": "loneliness"},
                {"quote": "The die is cast; I have consented to return, if we are not destroyed.", "supports": "turns back"},
                {"quote": "Alas! yes; I cannot withstand their demands. I cannot lead them unwillingly to danger, and I must return.", "supports": "the crew's demand"},
            ],
        },
    ],
}
