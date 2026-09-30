BOOK = {
    "title": "The Adventures of Pinocchio",
    "author": "Carlo Collodi",
    "year": "1883",
    "edition": "Standard Ebooks edition of an early English translation (the translator is not named; the wording is close to Mary Alice Murray's 1892 version)",
    "source": "https://github.com/standardebooks/carlo-collodi_the-adventures-of-pinocchio",
    "characters": [
        {
            "name": "Pinocchio",
            "aka": "",
            "description": (
                "A wooden puppet that Geppetto carves from a piece of wood that can already cry and laugh. His nose grows while it is still being "
                "carved (\"no sooner had he made it than it began to grow\"), and later it grows whenever he lies to the Fairy: \"his nose, which was "
                "already long, grew at once two inches longer.\" Lazy and easily tricked, he is robbed by the Fox and the Cat, runs off to the \"Land "
                "of Boobies\" with Candlewick, and wakes up with \"a magnificent pair of donkey's ears.\" He finds Geppetto inside the Dogfish (\"Oh, "
                "my dear papa! I have found you at last!\") and at the end becomes \"a well-behaved little boy.\""
            ),
            "evidence": [
                {"quote": "Is it possible that this piece of wood can have learned to cry and to lament like a child?", "supports": "the wood cries"},
                {"quote": "he heard the same little voice say, laughing: \"Stop! you are tickling me all over!\"", "supports": "the wood laughs"},
                {"quote": "\"What name shall I give him?\" he said to himself; \"I think I will call him Pinocchio.", "supports": "named by Geppetto"},
                {"quote": "He then proceeded to carve the nose, but no sooner had he made it than it began to grow.", "supports": "the nose grows as it is carved"},
                {"quote": "He had scarcely told the lie when his nose, which was already long, grew at once two inches longer.", "supports": "the nose grows when he lies"},
                {"quote": "There are lies that have short legs, and lies that have long noses. Your lie, as it happens, is one of those that have a long nose.", "supports": "the Fairy explains"},
                {"quote": "\"Ah!\" said that lazy Pinocchio at once, \"I see that this village will never suit me! I wasn't born to work!\"", "supports": "lazy"},
                {"quote": "of you who are simple enough to believe that money can be sown and gathered in fields in the same way as beans and gourds.", "supports": "easily tricked"},
                {"quote": "while you were in the town the Fox and the Cat returned to the field; they took the buried money and then fled like the wind.", "supports": "robbed"},
                {"quote": "It is called the 'Land of Boobies.' Why do you not come, too?", "supports": "the Land of Boobies"},
                {"quote": "He saw his head embellished with a magnificent pair of donkey's ears!", "supports": "turns into a donkey"},
                {"quote": "\"Oh, my dear papa! I have found you at last! I will never leave you more, never more, never more!\"", "supports": "finds Geppetto"},
                {"quote": "\"How ridiculous I was when I was a puppet! And how glad I am that I have become a well-behaved little boy!\"", "supports": "becomes a boy"},
            ],
            "absent": [r"real boy"],
        },
        {
            "name": "Geppetto",
            "aka": "nicknamed \"Pudding\"",
            "description": (
                "\"A lively little old man\" whom the neighbourhood boys tease as \"Pudding,\" because \"his yellow wig greatly resembled a pudding made "
                "of Indian corn\"; he is \"very fiery\" and flies into a rage at the name. He is so poor that the fire in his room is only painted on "
                "the wall. He carves Pinocchio and sells his old coat to buy him a spelling-book. At sea he is \"swallowed by the terrible Dogfish,\" "
                "where Pinocchio finds him."
            ),
            "evidence": [
                {"quote": "A lively little old man immediately walked into the shop. His name was Geppetto, but when the boys of the neighborhood wished to make him angry they called him Pudding, because his yellow wig greatly resembled a pudding made of Indian corn.", "supports": "appearance, nickname"},
                {"quote": "Geppetto was very fiery. Woe to him who called him Pudding!", "supports": "temper"},
                {"quote": "At the end of the room there was a fireplace with a lighted fire; but the fire was painted", "supports": "poverty"},
                {"quote": "He returned shortly, holding in his hand a spelling-book for Pinocchio, but the old coat was gone. The poor man was in his shirtsleeves and out of doors it was snowing. \"And the coat, papa?\" \"I have sold it.\"", "supports": "sells his coat"},
                {"quote": "He must have been swallowed by the terrible Dogfish", "supports": "swallowed"},
            ],
        },
        {
            "name": "The Talking-Cricket",
            "aka": "",
            "description": (
                "An old cricket who has \"lived in this room a hundred years or more\" and warns Pinocchio about disobedient boys. Pinocchio, angry "
                "at being called a puppet with \"a wooden head,\" throws a hammer at him, and the Cricket is left \"dried up and flattened against the "
                "wall.\" He comes back as \"the ghost of the Talking-Cricket\" to warn Pinocchio again. The name \"Jiminy\" comes from the Disney film."
            ),
            "evidence": [
                {"quote": "\"I am the Talking-Cricket, and I have lived in this room a hundred years or more.\"", "supports": "who he is"},
                {"quote": "Woe to those boys who rebel against their parents and run away from home. They will never come to any good in the world, and sooner or later they will repent bitterly.", "supports": "the warning"},
                {"quote": "\"Because you are a puppet and, what is worse, because you have a wooden head.\"", "supports": "insults Pinocchio"},
                {"quote": "snatching a wooden hammer from the bench, he threw it at the Talking-Cricket.", "supports": "the hammer"},
                {"quote": "so that the poor Cricket had scarcely breath to cry \"Cri-cri-cri!\" and then he remained dried up and flattened against the wall.", "supports": "killed"},
                {"quote": "\"I am the ghost of the Talking-Cricket,\" answered the insect", "supports": "returns as a ghost"},
                {"quote": "\"I want to give you some advice. Go back and take the four sovereigns that you have left to your poor father", "supports": "warns him again"},
            ],
            "absent": [r"Jiminy"],
            "not_quotes": ["Jiminy"],
            "allow_terms": ["Disney"],
        },
        {
            "name": "The Fairy with Blue Hair",
            "aka": "first seen as \"a beautiful Child\"",
            "description": (
                "When Pinocchio runs from the assassins, \"a beautiful Child\" appears at a window: \"She had blue hair and a face as white as a waxen "
                "image.\" As \"the little Fairy with blue hair\" she cares for him \"with all the patience of a good mamma,\" tricks him into taking his "
                "medicine with sugar, and shows him that lies are easy to spot, because some lies \"have long noses.\""
            ),
            "evidence": [
                {"quote": "The window then opened and a beautiful Child appeared at it. She had blue hair and a face as white as a waxen image", "supports": "first appearance"},
                {"quote": "At first the good little woman maintained that she was not the little Fairy with blue hair", "supports": "the Fairy"},
                {"quote": "The Fairy then, with all the patience of a good mamma, put another lump of sugar in his mouth", "supports": "motherly care"},
                {"quote": "There are lies that have short legs, and lies that have long noses.", "supports": "catches his lies"},
            ],
        },
        {
            "name": "The Fox and the Cat",
            "aka": "",
            "description": (
                "Two swindlers Pinocchio meets on the road: \"a Fox lame of one foot, and a Cat blind of both eyes.\" Both are faking, because at the "
                "sound of his gold the Fox \"stretched out the paw that seemed crippled, and the Cat opened wide two eyes.\" They tell him to bury "
                "his coins in \"the Field of Miracles\" so they will grow. Disguised as assassins in charcoal sacks, they hang him from the Big Oak. "
                "At the end they are begging, and the Cat \"had so long feigned blindness that she had become blind in reality.\""
            ),
            "evidence": [
                {"quote": "he met on the road a Fox lame of one foot, and a Cat blind of both eyes", "supports": "who they are"},
                {"quote": "the Fox, with an involuntary movement, stretched out the paw that seemed crippled, and the Cat opened wide two eyes that looked like two green lanterns", "supports": "faking"},
                {"quote": "in the land of the Owls there is a sacred field called by everybody the Field of Miracles", "supports": "the swindle"},
                {"quote": "two evil-looking black figures completely enveloped in charcoal sacks", "supports": "the assassins"},
                {"quote": "Imagine his astonishment when instead of a hand he perceived that a cat's paw lay on the ground.", "supports": "the assassin is the Cat"},
                {"quote": "\"He must be hung! let us hang him!\"", "supports": "they hang him"},
                {"quote": "They were the Cat and the Fox, but they were scarcely recognizable. Fancy! the Cat had so long feigned blindness that she had become blind in reality", "supports": "their end"},
            ],
        },
        {
            "name": "Fire-Eater",
            "aka": "the showman",
            "description": (
                "The owner of the puppet theatre, \"very big, and so ugly that the sight of him was enough to frighten anyone,\" with a beard \"as "
                "black as ink\" so long that \"he trod upon it when he walked.\" He looks wicked but is soft-hearted: when he feels pity he sneezes "
                "(\"The showman has sneezed and that is a sign that he pities you\"). He spares Pinocchio and gives him \"five gold pieces\" for "
                "Geppetto."
            ),
            "evidence": [
                {"quote": "He was very big, and so ugly that the sight of him was enough to frighten anyone. His beard was as black as ink, and so long that it reached from his chin to the ground. I need only say that he trod upon it when he walked.", "supports": "appearance"},
                {"quote": "The showman, Fire-Eater-for that was his name-looked like a wicked man", "supports": "name"},
                {"quote": "The showman has sneezed and that is a sign that he pities you, and consequently you are saved.", "supports": "the pitying sneeze"},
                {"quote": "Here are five gold pieces. Go at once and take them to him with my compliments.", "supports": "the gift"},
            ],
        },
        {
            "name": "Candlewick",
            "aka": "real name Romeo",
            "description": (
                "Pinocchio's favourite schoolfellow, called Candlewick \"because he was so thin, straight and bright, like the new wick of a little "
                "nightlight,\" and \"the laziest and the naughtiest boy in the school.\" He persuades Pinocchio to come to the \"Land of Boobies,\" "
                "where both boys turn into donkeys; Candlewick is sold to a peasant."
            ),
            "evidence": [
                {"quote": "amongst Pinocchio's friends and schoolfellows there was one that he greatly preferred and was very fond of.", "supports": "his favourite"},
                {"quote": "This boy's name was Romeo, but he always went by the nickname of Candlewick, because he was so thin, straight and bright, like the new wick of a little nightlight.", "supports": "name, looks"},
                {"quote": "Candlewick was the laziest and the naughtiest boy in the school", "supports": "character"},
                {"quote": "It is called the 'Land of Boobies.' Why do you not come, too?", "supports": "tempts Pinocchio"},
                {"quote": "Candlewick was bought by a peasant whose donkey had died the previous day.", "supports": "a donkey, sold"},
            ],
        },
        {
            "name": "The Dogfish",
            "aka": "",
            "description": (
                "A huge sea monster that \"has been spreading devastation and ruin\" and swallows Geppetto and later Pinocchio. Inside it, Pinocchio "
                "finds his father, and they escape while \"the Dogfish is sleeping like a dormouse.\" In the book it is a dogfish, not a whale."
            ),
            "evidence": [
                {"quote": "He must have been swallowed by the terrible Dogfish, who for some days past has been spreading devastation and ruin in our waters.", "supports": "who it is"},
                {"quote": "the Dogfish is sleeping like a dormouse, the sea is calm, and it is as light as day. Follow me, dear papa", "supports": "the escape"},
            ],
            "absent": [r"\bwhale\b"],
        },
    ],
}
