BOOK = {
    "title": "Winnie-the-Pooh",
    "author": "A. A. Milne",
    "year": "1926",
    "edition": "Standard Ebooks edition",
    "source": "https://github.com/standardebooks/a-a-milne_winnie-the-pooh",
    "characters": [
        {
            "name": "Winnie-the-Pooh",
            "aka": "Pooh; \"Edward Bear\"",
            "description": (
                "Christopher Robin's bear: \"Edward Bear, known to his friends as Winnie-the-Pooh, or Pooh for short.\" He loves honey (\"the only "
                "reason for making honey is so as I can eat it\"), makes up little hums, and calls himself \"a Bear of Very Little Brain, and long "
                "words Bother me.\" He floats up to a bees' nest on a balloon, trying \"to look like a small black cloud,\" and eats so much at "
                "Rabbit's that he gets stuck in the front door, \"a Wedged Bear in Great Tightness.\" To Christopher Robin he is \"the Best Bear in "
                "All the World.\" Tigger is not in this book; he first appears in the sequel."
            ),
            "evidence": [
                {"quote": "Edward Bear, known to his friends as Winnie-the-Pooh, or Pooh for short, was walking through the forest one day, humming proudly to himself. He had made up a little hum that very morning", "supports": "name, hums"},
                {"quote": "picked his Bear up by the leg, and walked off to the door, trailing Pooh behind him", "supports": "Christopher Robin's bear"},
                {"quote": "And then he got up, and said: \"And the only reason for making honey is so as I can eat it.\"", "supports": "honey"},
                {"quote": "\"For I am a Bear of Very Little Brain, and long words Bother me.\"", "supports": "very little brain"},
                {"quote": "\"I wonder if you've got such a thing as a balloon about you?\"", "supports": "the balloon"},
                {"quote": "\"I shall try to look like a small black cloud. That will deceive them", "supports": "tricks the bees"},
                {"quote": "\"Then would you read a Sustaining Book, such as would help and comfort a Wedged Bear in Great Tightness?\"", "supports": "stuck"},
                {"quote": "\"It all comes,\" said Rabbit sternly, \"of eating too much.", "supports": "eating too much"},
                {"quote": "that Rabbit might never be able to use his front door again", "supports": "stuck in Rabbit's door"},
                {"quote": "\"You're the Best Bear in All the World,\" said Christopher Robin soothingly.", "supports": "Christopher Robin's view"},
            ],
            "absent": [r"\bTigger\b"],
            "allow_terms": ["Tigger"],
        },
        {
            "name": "Piglet",
            "aka": "",
            "description": (
                "Pooh's small, timid friend, who \"lived in a very grand house in the middle of a beech-tree\" beside a broken sign reading "
                "\"Trespassers W,\" which he says was his grandfather's name. He admits \"It is hard to be brave... when you're only a Very Small "
                "Animal.\" When a flood leaves him \"Entirely Surrounded by Water,\" he sends a message in a bottle, and Christopher Robin and Pooh "
                "sail to him in \"The Brain of Pooh.\""
            ),
            "evidence": [
                {"quote": "The Piglet lived in a very grand house in the middle of a beech-tree", "supports": "home"},
                {"quote": "Next to his house was a piece of broken board which had: \"Trespassers W\" on it.", "supports": "the sign"},
                {"quote": "he said it was his grandfather's name, and had been in the family for a long time", "supports": "his explanation"},
                {"quote": "\"It is hard to be brave,\" said Piglet, sniffing slightly, \"when you're only a Very Small Animal.\"", "supports": "timid"},
                {"quote": "IX In Which Piglet Is Entirely Surrounded by Water", "supports": "the flood"},
                {"quote": "a man on a desert island who had written something in a bottle and thrown it in the sea; and Piglet thought", "supports": "message in a bottle"},
                {"quote": "\"I shall call this boat The Brain of Pooh,\" said Christopher Robin", "supports": "the rescue"},
            ],
        },
        {
            "name": "Eeyore",
            "aka": "",
            "description": (
                "\"The Old Grey Donkey,\" who \"stood by himself in a thistly corner of the forest\" and is always gloomy (\"I don't seem to have felt "
                "at all how for a long time\"). He loses his tail, which Pooh finds hanging on Owl's door as a \"bell-rope\"; Christopher Robin nails "
                "it back on. For his birthday he gets \"a Useful Pot to Keep Things In\" and a balloon that Piglet has burst on the way."
            ),
            "evidence": [
                {"quote": "The Old Grey Donkey, Eeyore, stood by himself in a thistly corner of the forest", "supports": "who he is"},
                {"quote": "\"I don't seem to have felt at all how for a long time.\"", "supports": "gloomy"},
                {"quote": "\"Why, what's happened to your tail?\" he said in surprise.", "supports": "loses his tail"},
                {"quote": "and when Christopher Robin had nailed it on in its right place again, Eeyore frisked about the forest", "supports": "tail nailed back"},
                {"quote": "\"I'm giving him a Useful Pot to Keep Things In", "supports": "birthday present"},
                {"quote": "\"No, but I-I-oh, Eeyore, I burst the balloon!\"", "supports": "the burst balloon"},
            ],
        },
        {
            "name": "Owl",
            "aka": "",
            "description": (
                "The wise-seeming bird who lives at \"The Chestnuts, an old-world residence of great charm.\" He can \"read and write and spell his "
                "own name Wol,\" but \"went all to pieces over delicate words like measles and buttered toast,\" so Christopher Robin writes his door "
                "notices. He likes long words, such as \"the customary procedure,\" and has been using Eeyore's lost tail as his \"Handsome "
                "bell-rope.\""
            ),
            "evidence": [
                {"quote": "lived at The Chestnuts, an old-world residence of great charm", "supports": "home"},
                {"quote": "for Owl, wise though he was in many ways, able to read and write and spell his own name Wol, yet somehow went all to pieces over delicate words like measles and buttered toast.", "supports": "spelling"},
                {"quote": "These notices had been written by Christopher Robin, who was the only one in the forest who could spell", "supports": "his notices"},
                {"quote": "\"Well,\" said Owl, \"the customary procedure in such cases is as follows.\"", "supports": "long words"},
                {"quote": "\"Handsome bell-rope, isn't it?\" said Owl.", "supports": "Eeyore's tail as a bell-rope"},
            ],
        },
        {
            "name": "Rabbit",
            "aka": "",
            "description": (
                "The forest's organiser, with a whole crowd of \"friends-and-relations.\" Pooh gets stuck in his front door. When Kanga arrives he "
                "writes a \"Plan to Capture Baby Roo,\" which starts from the facts that \"Kanga runs faster than any of Us, even Me.\""
            ),
            "evidence": [
                {"quote": "and, at the end, in a long line, all Rabbit's friends-and-relations.", "supports": "his relations"},
                {"quote": "Now by this time Rabbit wanted to go for a walk too, and finding the front door full, he went out by the back door", "supports": "Pooh in his door"},
                {"quote": "This was what Rabbit read out: Plan to Capture Baby Roo", "supports": "the plan"},
                {"quote": "Kanga runs faster than any of Us, even Me.", "supports": "his planning"},
            ],
        },
        {
            "name": "Kanga and Baby Roo",
            "aka": "",
            "description": (
                "A mother kangaroo and her baby who suddenly appear in the forest. To Rabbit she is \"a Strange Animal\": \"An animal who carries her "
                "family about with her in her pocket!\" Rabbit's plan swaps Piglet for Roo in Kanga's pocket, but Kanga pretends not to notice and "
                "gives Piglet a bath instead."
            ),
            "evidence": [
                {"quote": "Nobody seemed to know where they came from, but there they were in the Forest: Kanga and Baby Roo.", "supports": "arrival"},
                {"quote": "We find a Strange Animal among us.", "supports": "Rabbit's view"},
                {"quote": "An animal who carries her family about with her in her pocket!", "supports": "the pocket"},
                {"quote": "VII In Which Kanga and Baby Roo Come to the Forest, and Piglet Has a Bath", "supports": "Piglet's bath"},
                {"quote": "Of course as soon as Kanga unbuttoned her pocket, she saw what had happened.", "supports": "Kanga sees the swap"},
                {"quote": "So she said to herself, \"If they are having a joke with me, I will have a joke with them.\"", "supports": "plays along"},
                {"quote": "\"Bath first,\" said Kanga in a cheerful voice.", "supports": "the bath"},
                {"quote": "then Kanga, with Roo in her pocket, and Owl", "supports": "Roo in her pocket"},
            ],
        },
        {
            "name": "Christopher Robin",
            "aka": "",
            "description": (
                "The boy who owns Pooh and to whom the stories are told (the narrator calls him \"you\"). He is \"the only one in the forest who could "
                "spell,\" calls Pooh \"silly old Bear\" \"in such a loving voice,\" leads an \"Expotition to the North Pole,\" and rescues Piglet from the "
                "flood."
            ),
            "evidence": [
                {"quote": "picked his Bear up by the leg, and walked off to the door, trailing Pooh behind him", "supports": "owns Pooh"},
                {"quote": "\"Good morning, Winnie-ther-Pooh,\" said you.", "supports": "the stories are told to him"},
                {"quote": "These notices had been written by Christopher Robin, who was the only one in the forest who could spell", "supports": "can spell"},
                {"quote": "he said, \"Silly old Bear,\" in such a loving voice that everybody felt quite hopeful again.", "supports": "silly old Bear"},
                {"quote": "VIII In Which Christopher Robin Leads an Expotition to the North Pole", "supports": "the Expotition"},
                {"quote": "\"I shall call this boat The Brain of Pooh,\" said Christopher Robin", "supports": "rescues Piglet"},
            ],
        },
    ],
}
