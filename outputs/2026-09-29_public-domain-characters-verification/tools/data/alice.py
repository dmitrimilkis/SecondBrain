BOOK = {
    "title": "Alice's Adventures in Wonderland",
    "author": "Lewis Carroll",
    "year": "1865",
    "edition": "Standard Ebooks edition",
    "source": "https://github.com/standardebooks/lewis-carroll_alices-adventures-in-wonderland",
    "characters": [
        {
            "name": "Alice",
            "aka": "",
            "description": (
                "A curious, well-mannered little girl who, \"burning with curiosity,\" follows a rabbit underground and keeps growing and shrinking "
                "after drinking and eating things labelled \"Drink Me\" and \"Eat Me.\" She tries to curtsey even while falling down the rabbit-hole, "
                "talks to herself constantly (she \"generally gave herself very good advice\" but \"very seldom followed it\"), misses her cat Dinah, "
                "and finally wakes up from \"such a curious dream.\" The book never gives her age or hair colour. All it says is that her hair "
                "\"doesn't go in ringlets at all\"; the blonde hair and blue dress come from illustrations and films."
            ),
            "evidence": [
                {"quote": "burning with curiosity, she ran across the field after it", "supports": "curiosity"},
                {"quote": "she tried to curtsey as she spoke-fancy curtseying as you're falling through the air!", "supports": "polite"},
                {"quote": "She generally gave herself very good advice, (though she very seldom followed it), and sometimes she scolded herself so severely as to bring tears into her eyes", "supports": "talks to herself"},
                {"quote": "with the words \"Drink Me\" beautifully printed on it in large letters", "supports": "Drink Me"},
                {"quote": "a very small cake, on which the words \"Eat Me\" were beautifully marked in currants", "supports": "Eat Me"},
                {"quote": "\"Curiouser and curiouser!\" cried Alice", "supports": "famous line"},
                {"quote": "\"Dinah'll miss me very much tonight, I should think!\" (Dinah was the cat.)", "supports": "her cat"},
                {"quote": "for her hair goes in such long ringlets, and mine doesn't go in ringlets at all", "supports": "only hair detail"},
                {"quote": "\"Oh, I've had such a curious dream!\" said Alice", "supports": "dream ending"},
            ],
            "absent": [r"seven years", r"\bblonde?\b|golden hair|yellow hair|fair hair", r"blue (dress|frock)|pinafore"],
        },
        {
            "name": "The White Rabbit",
            "aka": "W. Rabbit",
            "description": (
                "A nervous, fussy \"White Rabbit with pink eyes\" who wears a waistcoat, checks his pocket watch and cries \"Oh dear! Oh dear! I shall "
                "be late!\" He carries white kid gloves and a fan, has a housemaid called Mary Ann (he mistakes Alice for her), and acts as the "
                "herald at the trial."
            ),
            "evidence": [
                {"quote": "a White Rabbit with pink eyes ran close by her", "supports": "appearance"},
                {"quote": "\"Oh dear! Oh dear! I shall be late!\"", "supports": "catchphrase"},
                {"quote": "the Rabbit actually took a watch out of its waistcoat-pocket", "supports": "waistcoat, watch"},
                {"quote": "with a pair of white kid gloves in one hand and a large fan in the other", "supports": "gloves and fan"},
                {"quote": "\"Why, Mary Ann, what are you doing out here?", "supports": "mistakes Alice for his maid"},
                {"quote": "\"Herald, read the accusation!\" said the King. On this the White Rabbit blew three blasts on the trumpet", "supports": "herald"},
            ],
        },
        {
            "name": "The Cheshire Cat",
            "aka": "",
            "description": (
                "The Duchess's cat, a large cat \"grinning from ear to ear\" that can appear and vanish at will, once fading away until only its grin "
                "is left (\"a grin without a cat!\"). It tells Alice, \"we're all mad here. I'm mad. You're mad.\""
            ),
            "evidence": [
                {"quote": "a large cat which was sitting on the hearth and grinning from ear to ear", "supports": "grin"},
                {"quote": "\"It's a Cheshire cat,\" said the Duchess", "supports": "the Duchess's cat"},
                {"quote": "we're all mad here. I'm mad. You're mad.", "supports": "famous line"},
                {"quote": "this time it vanished quite slowly, beginning with the end of the tail, and ending with the grin, which remained some time after the rest of it had gone", "supports": "vanishing"},
                {"quote": "but a grin without a cat!", "supports": "grin without a cat"},
            ],
        },
        {
            "name": "The Hatter",
            "aka": "never called \"the Mad Hatter\" in the book",
            "description": (
                "A rude, riddling hat-seller (\"I keep them to sell ... I'm a hatter\") who hosts the \"Mad Tea-Party\" with the March Hare and the "
                "Dormouse and greets Alice with \"Your hair wants cutting.\" He asks the unanswered riddle \"Why is a raven like a writing-desk?\" He "
                "has quarrelled with Time, so tea-time never ends: \"It's always six o'clock now.\" The book never calls him \"the Mad Hatter,\" and "
                "the \"10/6\" price tag is only in the pictures."
            ),
            "evidence": [
                {"quote": "\"I keep them to sell,\" the Hatter added as an explanation; \"I've none of my own. I'm a hatter.\"", "supports": "profession"},
                {"quote": "all he said was, \"Why is a raven like a writing-desk?\"", "supports": "riddle"},
                {"quote": "\"Your hair wants cutting,\" said the Hatter.", "supports": "rude"},
                {"quote": "\"You should learn not to make personal remarks,\" Alice said with some severity; \"it's very rude.\"", "supports": "Alice calls it rude"},
                {"quote": "It's always six o'clock now.", "supports": "stopped time"},
                {"quote": "it's always teatime, and we've no time to", "supports": "endless tea"},
                {"quote": "the March Hare and the Hatter were having tea at it", "supports": "tea party"},
            ],
            "absent": [r"mad hatter", r"10/6"],
            "not_quotes": ["the Mad Hatter", "10/6"],
        },
        {
            "name": "The March Hare",
            "aka": "",
            "description": (
                "The Hatter's tea-party partner. Alice hopes that \"as this is May it won't be raving mad,\" but it offers her wine when there is "
                "only tea (\"Have some wine\")."
            ),
            "evidence": [
                {"quote": "perhaps as this is May it won't be raving mad-at least not so mad as it was in March", "supports": "mad as a March hare"},
                {"quote": "\"Have some wine,\" the March Hare said in an encouraging tone. Alice looked all round the table, but there was nothing on it but tea.", "supports": "nonsense hospitality"},
            ],
        },
        {
            "name": "The Dormouse",
            "aka": "",
            "description": (
                "A sleepy guest at the tea party, \"fast asleep\" between the Hatter and the March Hare, who use it as a cushion. It wakes to tell a "
                "story about sisters who live in a \"treacle-well,\" and when Alice leaves they are \"trying to put the Dormouse into the teapot.\""
            ),
            "evidence": [
                {"quote": "a Dormouse was sitting between them, fast asleep, and the other two were using it as a cushion", "supports": "asleep, cushion"},
                {"quote": "\"It was a treacle-well.\"", "supports": "treacle-well story"},
                {"quote": "they were trying to put the Dormouse into the teapot", "supports": "teapot"},
            ],
        },
        {
            "name": "The Queen of Hearts",
            "aka": "",
            "description": (
                "The furious playing-card queen who \"had only one way of settling all difficulties, great or small\": \"Off with his head!\" She plays "
                "croquet with live flamingoes as mallets and hedgehogs as balls. Her death sentences are never carried out: the Gryphon says \"they "
                "never executes nobody,\" and the King quietly pardons everyone \"in a low voice.\""
            ),
            "evidence": [
                {"quote": "The Queen had only one way of settling all difficulties, great or small. \"Off with his head!\" she said, without even looking round.", "supports": "temper"},
                {"quote": "The Queen turned crimson with fury, and, after glaring at her for a moment like a wild beast, screamed \"Off with her head! Off-\"", "supports": "rage"},
                {"quote": "the balls were live hedgehogs, the mallets live flamingoes", "supports": "croquet"},
                {"quote": "\"Why, she,\" said the Gryphon. \"It's all her fancy, that: they never executes nobody, you know.", "supports": "no executions"},
                {"quote": "Alice heard the King say in a low voice, to the company generally, \"You are all pardoned.\"", "supports": "the King pardons"},
            ],
        },
        {
            "name": "The Caterpillar",
            "aka": "",
            "description": (
                "The book introduces him as \"a large blue caterpillar,\" sitting on a mushroom \"with its arms folded, quietly smoking a long "
                "hookah,\" who asks Alice in a \"languid, sleepy voice\": \"Who are you?\" It tells her that one side of the mushroom makes you taller "
                "and the other shorter."
            ),
            "evidence": [
                {"quote": "a large blue caterpillar, that was sitting on the top with its arms folded, quietly smoking a long hookah", "supports": "appearance"},
                {"quote": "addressed her in a languid, sleepy voice. \"Who are you?\" said the Caterpillar.", "supports": "manner, question"},
                {"quote": "One side will make you grow taller, and the other side will make you grow shorter.", "supports": "mushroom advice"},
            ],
        },
        {
            "name": "The Duchess",
            "aka": "",
            "description": (
                "A \"very ugly\" noblewoman with a pepper-filled kitchen and a howling baby that turns into a pig in Alice's arms. Later she turns "
                "oddly affectionate (\"you dear old thing!\") and insists \"Everything's got a moral, if only you can find it.\""
            ),
            "evidence": [
                {"quote": "the Duchess was very ugly", "supports": "looks"},
                {"quote": "\"There's certainly too much pepper in that soup!\" Alice said to herself, as well as she could for sneezing.", "supports": "pepper"},
                {"quote": "it was neither more nor less than a pig", "supports": "baby becomes a pig"},
                {"quote": "\"You can't think how glad I am to see you again, you dear old thing!\" said the Duchess, as she tucked her arm affectionately into Alice's", "supports": "affectionate"},
                {"quote": "\"Tut, tut, child!\" said the Duchess. \"Everything's got a moral, if only you can find it.\"", "supports": "morals"},
            ],
        },
        {
            "name": "The Mock Turtle",
            "aka": "",
            "description": (
                "A tearful creature, \"the thing Mock Turtle Soup is made from,\" whom Alice finds \"sighing as if his heart would break\"; with the "
                "Gryphon he tells of his school in the sea and performs the Lobster Quadrille."
            ),
            "evidence": [
                {"quote": "\"It's the thing Mock Turtle Soup is made from,\" said the Queen.", "supports": "what he is"},
                {"quote": "Alice could hear him sighing as if his heart would break", "supports": "sorrow"},
                {"quote": "\"This here young lady,\" said the Gryphon, \"she wants for to know your history, she do.\" \"I'll tell it her,\" said the Mock Turtle", "supports": "tells his story to the Gryphon and Alice"},
                {"quote": "we went to school in the sea. The master was an old Turtle-we used to call him Tortoise-", "supports": "school in the sea"},
                {"quote": "so you can have no idea what a delightful thing a Lobster Quadrille is!", "supports": "Lobster Quadrille"},
                {"quote": "began solemnly dancing round and round Alice", "supports": "they dance it"},
            ],
        },
    ],
}
