# This file stores all the text content: events, chat messages, and endings.

DANMAKU_POOL = [
    # Positive & Hype
    "OMGGG", "W streamer", "peak", "ATE", "LMAOOO", "holy peak", "emotional damage",
    "marry me🌹🌹🌹", "cuteeee🥺", "poggers", "based", "W chat", "angel fr", "rent free",
    "so pretty", "sheesh", "main character energy", "awsl", "POG", "mother is mothering",
    "I WAS HERE", "VIP viewer here", "blessed stream", "she cooked", "slay", "kawaii ♡",
    "we love to see it", "₍ᐢ..ᐢ₎♡", "💖", "✨✨✨",
    "absolute cinema", "W vibes only", "take my energy ༼ つ ◕_◕ ༽つ", "tskrrrr",

    # Neutral & Confused
    "sus", "brainrot", "NPC behavior", "LOL", "we listening", "mods asleep", "awkward...",
    "what is happening", "bro?", "chat moving too fast", "context?", "any lore masters?",
    "literally me", "so real", "🤣🤣🤣",

    # Toxic & Negative
    "malding", "seething", "gigachad", "simp", "yikes", "unsubbing", "don't care",
    "ouch...", "mid stream", "Cringe", "final stream?", "L", "fell off", "ratio",
    "who?", "touch grass", "bot viewer", "industry plant", "💀💀💀", "🤢🤢🤢", "cap",
    "this is painful to watch🤮🤮🤮", "😓😓😓", "yawn 🥱"
]



EVENTS = {
    "positive": [
        {
            "text": "[SUPER CHAT $1k] Angel-chan you look SO gorgeous tonight!! Here's my entire month of lunch money, just take it!!",
            "options": [
                {
                    "label": "<Overdrive Fanservice> Awww thank you!! I'll literally be thinking about you before I sleep tonight~",
                    "effect": {"stress": 16, "edge": -7, "followers": 32, "money": 2},
                    "sfx": "coin",
                    "desc": "You force the perfect parasocial smile. Your wallet is happy, but your soul is exhausted."
                },
                {
                    "label": "<Self-Roast> Hey stop that, I can't call myself an angel anymore after this lmao",
                    "effect": {"stress": -3, "edge": -3, "followers": 15, "money": 1},
                    "sfx": "coin",
                    "desc": "Self-deprecating humor lands perfectly. Chat goes wild for the bit, tipping rolls in."
                },
                {
                    "label": "<Nuclear Meltdown> I DON'T WANT YOUR MONEY. GET OUT OF MY STREAM!!!",
                    "effect": {"stress": -6, "edge": 18, "followers": -25, "money": -4},
                    "sfx": "damage",
                    "desc": "You snap at a supporter. Stunned silence, then a mass unfollow wave. You feel weirdly free."
                },
            ]
        },
        {
            "text": "A huge clip channel just posted your most unhinged highlight! A massive wave of new viewers is flooding in!",
            "options": [
                {
                    "label": "<Welcome Ceremony> Hello new friendsss~ to join the Angel Army you must subscribe first okay??",
                    "effect": {"stress": 22, "edge": -6, "followers": 42, "money": 2},
                    "sfx": "heal",
                    "desc": "You perform perfectly for the newcomers. Maintaining this energy leaves you bone-tired."
                },
                {
                    "label": "<Self-Destruct> oh great everyone's here to witness my crimes huh (hands up)",
                    "effect": {"stress": -3, "edge": -2, "followers": 17, "money": 1},
                    "sfx": "click",
                    "desc": "The self-roast goes viral in chat. Old fans donate to 'protect' you from the newcomers."
                },
                {
                    "label": "<Gatekeep Mode> Tourists move aside!! This is sacred OG territory, not a tourist trap!!",
                    "effect": {"stress": -4, "edge": 12, "followers": -10, "money": -2},
                    "sfx": "damage",
                    "desc": "You gatekeep aggressively. New viewers leave instantly. Edge spikes dangerously."
                },
            ]
        },
        {
            "text": "Angel how are you SO full of energy, glowing, and adorable literally every single day?!",
            "options": [
                {
                    "label": "<Idol Mode> Because YOU are watching me!! Your smiles are my infinite power source ♡",
                    "effect": {"stress": 23, "edge": -5, "followers": 35, "money": 3},
                    "sfx": "heal",
                    "desc": "A flawless idol answer. So perfect it rings hollow. The performance slowly suffocates you."
                },
                {
                    "label": "<Doomer Hours> real answer? caffeine and the fear of unemployment. same time tomorrow lol",
                    "effect": {"stress": -1, "edge": -3, "followers": 22, "money": 1},
                    "sfx": "click",
                    "desc": "The relatable doomer humor hits hard. Chat floods with 'SAME' and surprise gifts."
                },
                {
                    "label": "<Mask Off> honestly? filters. if you're unsatisfied please exit accordingly (goodbye wave)",
                    "effect": {"stress": -10, "edge": 17, "followers": -20, "money": -5},
                    "sfx": "damage",
                    "desc": "The brutal honesty nukes the mood. Casual fans leave. You feel weirdly authentic for once."
                },
            ]
        },
        {
            "text": "Your latest selfie is going viral for being too aesthetically perfect!",
            "options": [
                {
                    "label": "<Humble Lie> omg really?? I literally just rolled out of bed, no filter or anything haha",
                    "effect": {"stress": 2, "edge": -3, "followers": 12, "money": 0},
                    "sfx": "click",
                    "desc": "A blatant lie. Remembering the 3 hours of editing makes you cringe at yourself."
                },
                {
                    "label": "<Credit Where Due> don't believe her!! Photoshop is the REAL beauty angel here (pour one out)",
                    "effect": {"stress": 13, "edge": 4, "followers": 28, "money": 0},
                    "sfx": "click",
                    "desc": "Self-deprecating humor about beauty standards hits home. The clip goes viral again."
                },
                {
                    "label": "<Ego Arc> Obviously. I'm literally the prettiest person on this entire platform and you know it.",
                    "effect": {"stress": -8, "edge": 21, "followers": 38, "money": 3},
                    "sfx": "damage",
                    "desc": "Full narcissist mode. Haters flood in but fans call you iconic. Edge skyrockets."
                },
            ]
        },
        {
            "text": "I survived 12 hours of online classes today and your stream is literally the only reason I'm still breathing...",
            "options": [
                {
                    "label": "<Healing Saint> You worked so hard today! Throw all your suffering into my stream, I'll handle it ♡",
                    "effect": {"stress": 24, "edge": -10, "followers": 42, "money": 4},
                    "sfx": "heal",
                    "desc": "You absorb their emotional baggage with a warm smile. Your own stress quietly climbs."
                },
                {
                    "label": "<Solidarity Post> I'm barely holding on too!! Two disasters supporting each other, let's GOOO tonight!!",
                    "effect": {"stress": 3, "edge": -4, "followers": 11, "money": 1},
                    "sfx": "click",
                    "desc": "Shared suffering is instantly relatable. The bonding energy makes chat erupt with gifts."
                },
                {
                    "label": "<Unhinged> ME TOO let's drop out together RIGHT NOW I'm serious I'm hitting the button",
                    "effect": {"stress": -7, "edge": 12, "followers": -12, "money": -2},
                    "sfx": "damage",
                    "desc": "The unhinged solidarity freaks out worried parents in chat. Normies mass-unfollow."
                },
            ]
        },
        {
            "text": "[SUPER CHAT $1k] I've been here since you had 10 followers. Watching you grow feels a little bittersweet...",
            "options": [
                {
                    "label": "<VIP Treatment> No matter how many followers I get, you will ALWAYS be number one in my heart! Always!!",
                    "effect": {"stress": 19, "edge": -4, "followers": 43, "money": 2},
                    "sfx": "coin",
                    "desc": "Textbook old-fan retention tactic. You feel like a professional liar tracking all these promises."
                },
                {
                    "label": "<Real Talk> ngl I miss the tiny 5-person streams sometimes... it felt less lonely back then",
                    "effect": {"stress": -3, "edge": -5, "followers": -15, "money": 1},
                    "sfx": "heal",
                    "desc": "The nostalgic honesty makes old fans flood the donation box. Your mixed feelings are painfully real."
                },
                {
                    "label": "<Cold Exit> then leave?? I can't stop growing for your comfort, sorry not sorry",
                    "effect": {"stress": -12, "edge": 17, "followers": -30, "money": 1},
                    "sfx": "damage",
                    "desc": "You snap at a loyal OG fan. Several publicly unfollow. You immediately regret it."
                },
            ]
        },
        {
            "text": "The internet is such a toxic garbage fire. Your stream is genuinely the last clean corner of the web.",
            "options": [
                {
                    "label": "<Cult Leader Energy> In this sinking world, let us build our own cyber utopia together. Follow me forever ♡",
                    "effect": {"stress": 23, "edge": -4, "followers": 44, "money": 0},
                    "sfx": "click",
                    "desc": "An intensely magnetic speech. Fan loyalty surges but the cult pressure feels terrifying."
                },
                {
                    "label": "<Mudslide Theory> lmaooo I'm from the garbage fire too, we can be gross together in solidarity",
                    "effect": {"stress": -3, "edge": 4, "followers": 14, "money": 1},
                    "sfx": "click",
                    "desc": "The relatable mudslide analogy becomes a meme. The chat is chaotically joyful."
                },
                {
                    "label": "<Reality Check> clean corner?? buddy this is also a landfill, you've been bamboozled",
                    "effect": {"stress": -8, "edge": 13, "followers": -25, "money": -1},
                    "sfx": "damage",
                    "desc": "You shatter their illusion without mercy. Dreamy fans feel betrayed and leave en masse."
                },
            ]
        },
        {
            "text": "Your late-night ASMR accidentally went viral everywhere. People are calling your voice 'dangerously comforting.'",
            "options": [
                {
                    "label": "<Soft Angel> If my voice can make your night a little less lonely... then stay with me a while longer ♡",
                    "effect": {"stress": 19, "edge": 2, "followers": 38, "money": 1},
                    "sfx": "heal",
                    "desc": "The chat melts. You quietly carry thousands of lonely souls home every single night."
                },
                {
                    "label": "<Sleep-Deprived> dangerous?? good. I also haven't slept in 36 hours, who's gonna comfort who lmao",
                    "effect": {"stress": -3, "edge": -3, "followers": 12, "money": 1},
                    "sfx": "click",
                    "desc": "Sleep-deprived solidarity humor lands perfectly. Clips get reposted everywhere."
                },
                {
                    "label": "<Tsundere Snob> Dangerous? Good. Thank me for it. Don't like it? Uninstall. Next.",
                    "effect": {"stress": -8, "edge": 14, "followers": -22, "money": -2},
                    "sfx": "damage",
                    "desc": "Snapping at your listeners shatters the ASMR magic completely. Overnight fans quietly leave."
                },
            ]
        },
        {
            "text": "[SUPER CHAT $2k] Angel noticed me... I can die happy now",
            "options": [
                {
                    "label": "<Parasocial Lock> Don't say that okay?? Stay with me forever instead ♡",
                    "effect": {"stress": 17, "edge": 2, "followers": 38, "money": 4},
                    "sfx": "coin",
                    "desc": "A dangerously sweet reply. Money secured but the emotional dependency is suffocating."
                },
                {
                    "label": "<Gremlin Redirect> bold of you to die before the stream ends, wait at least another hour lmao",
                    "effect": {"stress": -2, "edge": 3, "followers": 10, "money": 2},
                    "sfx": "click",
                    "desc": "You defuse the heavy parasocial energy with comedy. The mood stays light and giggly."
                },
                {
                    "label": "<Ice Queen> sure whatever, you'll be back tomorrow anyway (shrug)",
                    "effect": {"stress": -5, "edge": 5, "followers": -10, "money": 2},
                    "sfx": "damage",
                    "desc": "The cold dismissal wounds the fan visibly. Chat goes icy. Long-time viewers unfollow."
                },
            ]
        },
        {
            "text": "the future of the internet!!",
            "options": [
                {
                    "label": "<Idol Promise> Ahh?! Thank you so much... I'll work even harder from now on! Please keep watching!",
                    "effect": {"stress": 17, "edge": -6, "followers": 33, "money": 2},
                    "sfx": "heal",
                    "desc": "A thousand expectations land on your shoulders all at once. The weight is crushing."
                },
                {
                    "label": "<Galaxy Brain> hm. the future of the internet is me. so the internet is doomed. makes sense.",
                    "effect": {"stress": -3, "edge": -3, "followers": 15, "money": 1},
                    "sfx": "click",
                    "desc": "The self-deprecating punchline goes viral. Chat erupts and gift storms flood in."
                },
                {
                    "label": "<Arrogant Angel> Obviously. I've BEEN the future. You're just finally catching up. (hair flip)",
                    "effect": {"stress": -8, "edge": 22, "followers": 40, "money": 2},
                    "sfx": "damage",
                    "desc": "Arrogance becomes your whole personality now. The haters are sharpening their knives."
                },
            ]
        },
        {
            "text": "This stream feels like home.",
            "options": [
                {
                    "label": "<Stay Till Dawn> Then let's stay together until morning, okay? I'm not going anywhere ♡",
                    "effect": {"stress": 19, "edge": -4, "followers": 38, "money": 4},
                    "sfx": "heal",
                    "desc": "The stream becomes a warm sanctuary. But being everyone's home drains every drop of you."
                },
                {
                    "label": "<Chaos Mom> home?? then where are your parents?? please tell me they're not also in this chat",
                    "effect": {"stress": -4, "edge": 3, "followers": -12, "money": -1},
                    "sfx": "click",
                    "desc": "The absurd improvised joke cracks up the whole chat. Mood instantly becomes warm chaos."
                },
                {
                    "label": "<Hard Boundary> Home?? This is a livestream not your living room, please log off and go outside",
                    "effect": {"stress": -7, "edge": 12, "followers": -30, "money": -5},
                    "sfx": "damage",
                    "desc": "You shatter the cozy illusion aggressively. Emotionally invested fans feel humiliated and leave."
                },
            ]
        },
        {
            "text": "Your streams genuinely kept me alive through a really horrible year.",
            "options": [
                {
                    "label": "<Heartfelt> I'm really glad you're still here. Truly. Thank you for surviving.",
                    "effect": {"stress": 13, "edge": -7, "followers": 32, "money": 0},
                    "sfx": "heal",
                    "desc": "The entire chat pauses in silence. Beautiful, but carrying their weight slowly crushes you."
                },
                {
                    "label": "<Deflect Humor> omg... so I'm responsible for everyone's mental health lore now??? no pressure I guess",
                    "effect": {"stress": -3, "edge": 6, "followers": 10, "money": 1},
                    "sfx": "click",
                    "desc": "You laugh the emotion away before your chest gets too heavy. Cowardly but merciful."
                },
                {
                    "label": "<Exploitation Mode> Then you OWE me a subscription. Prove your gratitude. Right now.",
                    "effect": {"stress": -7, "edge": 14, "followers": -25, "money": 2},
                    "sfx": "coin",
                    "desc": "You weaponize their gratitude for profit. Several loyal fans unfollow in disgust."
                },
            ]
        },
        {
            "text": "ur laugh literally cured my depression LOL",
            "options": [
                {
                    "label": "<Eternal Idol Promise> Then I'll keep laughing forever just for you all!!",
                    "effect": {"stress": 18, "edge": -4, "followers": 37, "money": 4},
                    "sfx": "heal",
                    "desc": "You promise more than you can give. Forcing smiles every single day hollows you out."
                },
                {
                    "label": "<Side Effects Warning> warning: may cause emotional damage and temporary delusion (official disclaimer)",
                    "effect": {"stress": -3, "edge": 3, "followers": 10, "money": 1},
                    "sfx": "click",
                    "desc": "The absurd pharmaceutical warning becomes a meme. Chat floods with clipped reactions."
                },
                {
                    "label": "<Vending Machine Logic> great, now that you're cured please subscribe and pay up ty byeee",
                    "effect": {"stress": -6, "edge": 9, "followers": -24, "money": -2},
                    "sfx": "damage",
                    "desc": "The transactional response after a vulnerable moment shocks everyone. Fans feel used and leave."
                },
            ]
        },
    ],
    "negative": [
        {
            "text": "Did you gain weight recently? Your face looks kind of wide on camera...",
            "options": [
                {
                    "label": "<Sad Girl> ugh... I've really been trying to diet lately... please don't be mean to me...",
                    "effect": {"stress": 5, "edge": -2, "followers": -15, "money": -1},
                    "sfx": "damage",
                    "desc": "You showed weakness. White knights donate out of pity, but your self-esteem is shattered."
                },
                {
                    "label": "<Body Confident> and?? this is called being well-nourished, stay jealous honestly (laugh)",
                    "effect": {"stress": 4, "edge": 7, "followers": 12, "money": 1},
                    "sfx": "click",
                    "desc": "Owning the insult with humor completely flips the energy. Chat cheers and gifts pour in."
                },
                {
                    "label": "<Scorched Earth> Is your keyboard soaked in the grease from YOUR face?? Mind your own business!!!",
                    "effect": {"stress": -5, "edge": 21, "followers": 35, "money": 4},
                    "sfx": "damage",
                    "desc": "The savage clapback goes viral. Haters pour in to watch the chaos. Donations spike hard."
                },
            ]
        },
        {
            "text": "A massive hate raid from a rival's fanbase just invaded your chat! They are spamming garbage everywhere!",
            "options": [
                {
                    "label": "<Cry on Stream> Why are you all doing this to me?! I just want to stream in peace!!",
                    "effect": {"stress": 5, "edge": -2, "followers": -20, "money": -2},
                    "sfx": "damage",
                    "desc": "Your tears go viral. It's humiliating, but the pity donations quietly cover the damage."
                },
                {
                    "label": "<Comedy Gold> wow chat quality really nose-dived tonight huh, excellent, please continue (laugh-cry)",
                    "effect": {"stress": 4, "edge": 6, "followers": 17, "money": 2},
                    "sfx": "click",
                    "desc": "Turning a hate raid into comedy gold is legendary. Neutral viewers side with you and sub."
                },
                {
                    "label": "<Declare War> GO TELL YOUR STREAMER I SAID WHAT I SAID. Full internet war, starting now!!",
                    "effect": {"stress": -4, "edge": 17, "followers": 32, "money": 3},
                    "sfx": "damage",
                    "desc": "You declare full internet war. Drama-hungry viewers flood in. Your soul is now stained black."
                },
            ]
        },
        {
            "text": "Your audio quality dropped to scratchy garbage. Are you streaming from an actual toaster right now?",
            "options": [
                {
                    "label": "<Panic Spending> I'M SORRY I'M BUYING A NEW MIC LIVE RIGHT NOW PLEASE WAIT",
                    "effect": {"stress": 12, "edge": -6, "followers": 16, "money": -12},
                    "sfx": "coin",
                    "desc": "You panic-buy to save face on stream. Audio is fixed, but financial ruin looms closer."
                },
                {
                    "label": "<Gaslight> this isn't low quality, it's lo-fi underground aesthetic. you simply lack the culture.",
                    "effect": {"stress": 6, "edge": 3, "followers": -15, "money": 0},
                    "sfx": "click",
                    "desc": "You gaslight them into accepting it as a deliberate choice. Some actually start to believe you."
                },
                {
                    "label": "<Mic Check Violence> my mic costs more than your rent, come back when you have ears that work!!",
                    "effect": {"stress": -5, "edge": 21, "followers": 36, "money": 2},
                    "sfx": "damage",
                    "desc": "The unhinged confidence makes drama-tourists pile in. Chaos is somehow profitable tonight."
                },
            ]
        },
        {
            "text": "Someone dug up your super cringe middle school posts. The entire chat is laughing at you.",
            "options": [
                {
                    "label": "<Full Denial> That is CLEARLY AI-generated deep fake propaganda! Do NOT trust what you see online!!",
                    "effect": {"stress": 8, "edge": -2, "followers": -14, "money": -5},
                    "sfx": "damage",
                    "desc": "The paranoid denial backfires spectacularly. Chat splits into conspiracy chaos. Stress maxes out."
                },
                {
                    "label": "<Own It Completely> yep that's me. I was weird then. I'm weird now. zero notes, zero regrets (shrug)",
                    "effect": {"stress": 4, "edge": 2, "followers": 12, "money": 1},
                    "sfx": "click",
                    "desc": "Owning your embarrassing past with humor is iconic. Every outcast online relates and subscribes."
                },
                {
                    "label": "<Counter Attack> you're seriously digging up MY past?? show me YOUR search history first. I'll wait.",
                    "effect": {"stress": 5, "edge": 14, "followers": 32, "money": 1},
                    "sfx": "damage",
                    "desc": "The aggressive counter-offense works. Defenders and drama fans flood in and tip generously."
                },
            ]
        },
        {
            "text": "Your eyes look so dead now. All corporate smiles, the pure magical spark you had at the start is completely gone.",
            "options": [
                {
                    "label": "<Quiet Admission> everyone has to grow up... I'm just trying not to get buried alive by reality.",
                    "effect": {"stress": 15, "edge": -4, "followers": 20, "money": 0},
                    "sfx": "damage",
                    "desc": "The reality check lands hard. Sympathy flows, but a crushing wave of depression rolls over you."
                },
                {
                    "label": "<Bit Recovery> dead eyes?? hold on let me fix that (begins completely unhinged interpretive dance)",
                    "effect": {"stress": 5, "edge": 4, "followers": -23, "money": 0},
                    "sfx": "click",
                    "desc": "The chaotic comedic response becomes a classic clip. Chat forgets what they were criticizing."
                },
                {
                    "label": "<Sweet Dismissal> don't like what you see? feel free to find another stream. byeee~ (gentle ban)",
                    "effect": {"stress": -4, "edge": 13, "followers": 25, "money": 3},
                    "sfx": "damage",
                    "desc": "The icy sweet dismissal terrifies the chat. Fans donate in nervous solidarity."
                },
            ]
        },
        {
            "text": "Other streamers do dance covers and gaming challenges. You just sit there reading chat. So lazy.",
            "options": [
                {
                    "label": "<Submissive Apology> I'm so sorry... I'll plan better content next time, please don't give up on me!",
                    "effect": {"stress": 16, "edge": -3, "followers": 28, "money": 0},
                    "sfx": "damage",
                    "desc": "Extremely submissive apology. You feel humiliated bowing to a random stranger online."
                },
                {
                    "label": "<Signature Brand> yep. lazy is the brand. lazy is the content. you can't buy this kind of charisma.",
                    "effect": {"stress": -2, "edge": -2, "followers": -31, "money": -8},
                    "sfx": "click",
                    "desc": "Ironically owning laziness as a brand identity becomes iconic. Chat adopts it as their religion."
                },
                {
                    "label": "<Real Talk> I can hold your attention by just SITTING HERE. what does that say about you?? think about it.",
                    "effect": {"stress": -5, "edge": 21, "followers": 38, "money": 3},
                    "sfx": "damage",
                    "desc": "The arrogant shutdown lands perfectly. Angry sharers spread the clip. Chaos tourism pays big."
                },
            ]
        },
        {
            "text": "Rumor says you talk like a sailor IRL and secretly have a boyfriend. Personas are such a scam.",
            "options": [
                {
                    "label": "<Total Denial> IMPOSSIBLE!! I check my DMs every second of every day, I haven't even touched a DOG!!",
                    "effect": {"stress": 12, "edge": -2, "followers": -21, "money": 0},
                    "sfx": "damage",
                    "desc": "You desperately defend your pure image. Maintaining this lie is suffocating and exhausting."
                },
                {
                    "label": "<Absurdist Arc> boyfriend?? I have an entire HAREM. application forms drop next week. stay tuned.",
                    "effect": {"stress": 3, "edge": 2, "followers": -26, "money": -4},
                    "sfx": "click",
                    "desc": "You turn the rumor into an absurd comedy sketch. The haters are completely stunned."
                },
                {
                    "label": "<Confession Bomb> YEAH I swear and I have a boyfriend and this was NEVER a fantasy paradise!! Surprise!!",
                    "effect": {"stress": 8, "edge": 19, "followers": 36, "money": -1},
                    "sfx": "damage",
                    "desc": "The confession bomb detonates the parasocial bubble. Chaos fans pour in screaming. Ka-ching."
                },
            ]
        },
        {
            "text": "A clip titled 'streamer has a complete mental breakdown live' is trending on every platform right now.",
            "options": [
                {
                    "label": "<Fall Apart> maybe... I really am broken beyond fixing at this point...",
                    "effect": {"stress": 14, "edge": -5, "followers": -13, "money": 1},
                    "sfx": "damage",
                    "desc": "The internet feeds on your pain. Sympathy and voyeurism merge as you visibly break."
                },
                {
                    "label": "<Monetize the Moment> had a breakdown?? obviously, that's the content. please sub before you scroll on.",
                    "effect": {"stress": 7, "edge": 8, "followers": 25, "money": 0},
                    "sfx": "coin",
                    "desc": "You monetize your own meltdown with dark humor. The viral moment becomes a fundraiser."
                },
                {
                    "label": "<Chaos Convert> yeah I'm falling apart, and?? SUBSCRIBE FIRST then come back to judge me!!",
                    "effect": {"stress": -6, "edge": 21, "followers": 32, "money": 4},
                    "sfx": "coin",
                    "desc": "You transform public humiliation into pure engagement farming. You are a monster. It works."
                },
            ]
        },
        {
            "text": "People on a forum say your entire personality is just recycled anime girl behavior.",
            "options": [
                {
                    "label": "<Identity Crisis> ...maybe they're right. I don't even know who I actually am anymore.",
                    "effect": {"stress": 13, "edge": -4, "followers": -5, "money": 1},
                    "sfx": "damage",
                    "desc": "Letting the existential crisis play out publicly earns pity tips, but crushes you mentally."
                },
                {
                    "label": "<Which Anime Though> recycled?? wait. which character am I?? someone help me figure this out rn",
                    "effect": {"stress": 4, "edge": 4, "followers": 17, "money": -2},
                    "sfx": "click",
                    "desc": "The meta-humor immediately flips the situation. Chat floods with anime character nominations."
                },
                {
                    "label": "<Steal Everything> all great creators steal. I'm stealing your attention right now. what are you gonna do about it?",
                    "effect": {"stress": -2, "edge": 12, "followers": 25, "money": 3},
                    "sfx": "damage",
                    "desc": "The savage intellectual flip goes viral. Haters quote-repost in anger. Numbers climb fast."
                },
            ]
        },
        {
            "text": "People are accusing you of only caring about donations and money now.",
            "options": [
                {
                    "label": "<Idol Defense> That's not true!! I stream because I genuinely love all of you, I promise ♡",
                    "effect": {"stress": 15, "edge": -5, "followers": -8, "money": -2},
                    "sfx": "click",
                    "desc": "The forced idol voice leaves a bitter taste. The long-timers don't believe a word of it."
                },
                {
                    "label": "<Rent Is Real> streaming IS my rent money... what else am I supposed to do here (nervous laugh)",
                    "effect": {"stress": 4, "edge": 2, "followers": -23, "money": -5},
                    "sfx": "coin",
                    "desc": "Honest self-deprecation about money struggles is painfully relatable. Sympathy tips roll in."
                },
                {
                    "label": "<Unfiltered> Correct. I love money. I have always loved money. Next question.",
                    "effect": {"stress": -6, "edge": 17, "followers": 33, "money": 2},
                    "sfx": "coin",
                    "desc": "Shameless honesty becomes weirdly hilarious. You are a villain, but a self-aware profitable one."
                },
            ]
        },
        {
            "text": "Someone posted side-by-side screenshots of your selfies - heavily edited vs the raw originals.",
            "options": [
                {
                    "label": "<Breakdown> please... stop looking at me that closely... it's terrifying...",
                    "effect": {"stress": 13, "edge": -4, "followers": -20, "money": -5},
                    "sfx": "damage",
                    "desc": "You become terrified of every camera angle. The paranoia quietly destroys you from inside."
                },
                {
                    "label": "<Art Defense> reality is ugly. editing is art. can you accept that? (sincere face)",
                    "effect": {"stress": 5, "edge": 8, "followers": 8, "money": -2},
                    "sfx": "click",
                    "desc": "The unashamed artistic defense becomes a rallying cry. Fans actually respect the boldness."
                },
                {
                    "label": "<Counter Challenge> show me YOUR unedited selfies first. no filter. I'll wait right here. go ahead.",
                    "effect": {"stress": -3, "edge": 14, "followers": 27, "money": 3},
                    "sfx": "damage",
                    "desc": "The counter-offensive challenge goes viral instantly. Drama views pump the numbers hard."
                },
            ]
        },
        {
            "text": "Your smile looks so fake now.",
            "options": [
                {
                    "label": "<Quiet Hurt> ...is it really that obvious?",
                    "effect": {"stress": 10, "edge": -6, "followers": -13, "money": 0},
                    "sfx": "damage",
                    "desc": "The comment sticks in your brain like poison. Sympathy tips carry you, barely."
                },
                {
                    "label": "<Premium Service> fake?? no no no, this is called a PROFESSIONAL smile. it's actually very expensive.",
                    "effect": {"stress": 6, "edge": 8, "followers": 17, "money": 1},
                    "sfx": "click",
                    "desc": "Framing your exhaustion as a luxury product is bizarrely funny. Chat tips the 'service fee'."
                },
                {
                    "label": "<Nihilist Drop> of course it's fake. everything online is fake. welcome to the internet, enjoy your stay.",
                    "effect": {"stress": -3, "edge": 16, "followers": 28, "money": 2},
                    "sfx": "damage",
                    "desc": "The nihilistic reveal explodes as edgy quote content. Your edge climbs dangerously fast."
                },
            ]
        },
        {
            "text": "is anyone else genuinely worried about her or is it just me",
            "options": [
                {
                    "label": "<Fragile Angel> it's okay... as long as you're all here with me, I can keep going.",
                    "effect": {"stress": 17, "edge": -3, "followers": 21, "money": 1},
                    "sfx": "coin",
                    "desc": "You monetize their concern with fragile-girl energy. The emotional dependency intensifies."
                },
                {
                    "label": "<Certified Disaster> I've been 'not okay' since middle school, this is just my normal state lol",
                    "effect": {"stress": 3, "edge": 2, "followers": -23, "money": -2},
                    "sfx": "click",
                    "desc": "Self-aware humor about your perpetual mess of a life lands warmly. Chat visibly relaxes."
                },
                {
                    "label": "<Deflect and Attack> worried about ME?? have you looked at yourself lately?? I'm fine, unfollow yourself first",
                    "effect": {"stress": -6, "edge": 22, "followers": 36, "money": 3},
                    "sfx": "damage",
                    "desc": "Turning the concern into a wild counter-accusation is unhinged comedy. Chaos viewers love it."
                },
            ]
        },
        {
            "text": "u changed after getting big",
            "options": [
                {
                    "label": "<Nostalgia Bait> ...honestly I miss those tiny streams sometimes too. I haven't forgotten.",
                    "effect": {"stress": 15, "edge": -7, "followers": 12, "money": 2},
                    "sfx": "heal",
                    "desc": "You play the nostalgia card expertly. It works, but you feel deeply hollow afterwards."
                },
                {
                    "label": "<Growing Pains> yeah old me was also broker, sadder, and more confused, somehow that version was cuter huh",
                    "effect": {"stress": 7, "edge": 2, "followers": 8, "money": 0},
                    "sfx": "click",
                    "desc": "Turning growing pains into relatable humor is cathartic. The chat softens immediately."
                },
                {
                    "label": "<Ice Cold> growing changes people. adapt or unfollow. (yawns)",
                    "effect": {"stress": -5, "edge": 17, "followers": 11, "money": -2},
                    "sfx": "damage",
                    "desc": "The cold detachment sounds almost cruel. Veteran fans leave. Drama-watchers take their seats."
                },
            ]
        },
        {
            "text": "this stream feels kinda cursed tonight ngl",
            "options": [
                {
                    "label": "<Scared Cutie> STOP IT you're literally freaking me out, everyone spam cute emotes RIGHT NOW please",
                    "effect": {"stress": -3, "edge": -5, "followers": -30, "money": -5},
                    "sfx": "heal",
                    "desc": "Cute scared-girl energy resets the creepy mood. Chat floods with protective emotes."
                },
                {
                    "label": "<Method Actor> perfect, horror arc unlocked. I'll play dead. who wants to be the villain? (hand up)",
                    "effect": {"stress": 5, "edge": 6, "followers": 12, "money": 1},
                    "sfx": "click",
                    "desc": "Leaning into the cursed energy makes this the best stream segment of the night."
                },
                {
                    "label": "<Chaos Brand> YES. the best clips ALWAYS come from cursed streams. keep the vibe going. subscribe.",
                    "effect": {"stress": -4, "edge": 17, "followers": 38, "money": 2},
                    "sfx": "damage",
                    "desc": "You weaponize the chaos vibes for engagement. The cursed stream gets clipped absolutely everywhere."
                },
            ]
        },
    ],
}

ENDINGS = {
    "stress": {
        "title": "ENDING 1: ANGEL NOT FOUND",
        "text": (
            "A thousand eyes crushed you, donation by donation.\n"
            "Mid-laugh, you smashed your monitor and pulled the plug.\n"
            "Chat spammed 'F' for a minute, then forgot you ever existed."
        )
    },
    "edge": {
        "title": "ENDING 2: TOXIC ROYALTY",
        "text": (
            "You learned hate-clicks pay the rent.\n"
            "Your chat is a dumpster fire, your merch sells out, but your DMs are empty.\n"
            "Congratulations, you're the villain everyone loves to hate."
        )
    },
    "money": {
        "title": "ENDING 3: CONNECTION LOST",
        "text": (
            "Turns out follower count doesn't keep the lights on.\n"
            "Mid-sentence, the screen went black - power cut.\n"
            "You sat in the dark, phone buzzing 'stream??' while real life evicted you."
        )
    },
    "dream": {
        "title": "✦ DREAM END: INTERNET ANGEL ✦",
        "text": (
            "You walked the razor's edge and never fell.\n"
            "A million genuine fans, zero scandals, and your sanity intact.\n"
            "The perfect Internet Angel - too bad angels don't exist. But for now? Pog."
        )
    },
    "dark_lord": {
        "title": "ENDING: DARK LORD",
        "text": (
            "You learned the dark truth: hate-clicks pay the bills.\n"
            "Your chat is a beautiful dumpster fire, your merch sells out, but your reflection makes you flinch.\n"
            "Congrats - you're the villain everyone loves to hate, and that's the only love you'll ever get.\n"
        )
    },
    "mid_crisis": {
        "title": "ENDING: SCREAMING IN THE MIDDLE",
        "text": (
            "You're too unwell to grow, but not broken enough to go viral.\n"
            "A few thousand regulars watch you slowly unravel, posting 'you ok?' between shitposts.\n"
            "You're not a cautionary tale. You're just... stuck on the dashboard forever."
        )
    },
    "normal_streamer": {
        "title": "ENDING: MID TIER PURGATORY",
        "text": (
            "No meteoric rise, no spectacular crash - just a few hundred loyal weirdos.\n"
            "You pay the rent, dodge panic attacks, and log off before midnight.\n"
            "In a world that worships extremes, being 'meh' is the quietest rebellion."
        )
    }
}


# Daily Diary Lines 
# These are Angel-chan's private inner thoughts, written once per in-game day.
# They are picked based on the player's current stress and edge levels.
# Low stress/edge = soft dreamy tone. High stress = cracking. High edge = sinister.

DIARY_LINES = {
    # Feeling okay — soft, hopeful, a little delusional
    "calm": [
        "Today was... actually kind of okay. Chat was nice. I smiled for real once.",
        "I bought strawberry milk after stream. Small things. They still count.",
        "Someone said I looked pretty today. I saved that message. Don't judge me.",
        "The BGM playlist I made is so good. I listened to it three times while editing.",
        "I think I'm getting better at this. Maybe. Probably. Hopefully.",
        "Fell asleep at my desk again. Dreamed of a stream with only 5 viewers. It felt warm.",
        "I keep a sticky note that says 'you are loved' on my monitor. I wrote it myself.",
        "Rent is scary but the chat said goodnight tonight. Even trade, maybe.",
        "The moon was really pretty when I finally logged off. I took a photo for no one.",
        "I told chat I was fine and actually meant it today. A rare occurrence.",
    ],
    # Stress is climbing — tired, fraying, still holding on
    "stressed": [
        "My hands were shaking after stream. I told chat it was cold. It wasn't cold.",
        "I don't remember what I ate today. I think I ate. I should eat.",
        "Someone clipped the part where I almost cried and posted it as funny content. Cool.",
        "I refreshed my follower count fourteen times between sets. I need help.",
        "The performance face is getting heavier. Like wearing a smile made of glass.",
        "I cancelled plans again. My friends probably stopped making them for me.",
        "Three energy drinks and I still feel nothing. Just static behind my eyes.",
        "The chat loves me so much tonight. I wish I could feel that from the inside.",
        "I keep thinking about what happens if I stop. Then I open the stream anyway.",
        "Stress recovery is just: pretend hard enough until it becomes true. Day 47.",
    ],
    # Edge is climbing — detached, sharp, a little scary
    "edgy": [
        "I said something mean in my head during donations tonight. I kept smiling.",
        "The parasocial thing is getting weird. They act like they know me. They don't.",
        "Caught myself calculating which fans are worth keeping. That's not normal, right?",
        "Someone said 'don't change' and I wanted to ask them which version they meant.",
        "The algorithm is a slot machine and I am the lever. Very fun. Great job everyone.",
        "I watched my own VOD and didn't recognize the person talking. Interesting.",
        "I said something I meant as a joke. Chat took it seriously. I'm not sure which one I was.",
        "The 'real me' is somewhere under the persona. I'll dig her out eventually. Maybe.",
        "My editor said the footage looks great. I said thanks. We are both lying professionally.",
        "I have 400k people watching a character I invented. She's more popular than I am.",
    ],
    # Both high — the cracking point, dreamy-dark yandere mode
    "breaking": [
        "If I disappeared from the internet tomorrow, how long before they'd notice? Asking for a friend.",
        "The smile doesn't come off anymore. It just stays. Like a mask that forgot to be a mask.",
        "I thought about shutting everything down tonight. I opened a new tab instead. Same thing.",
        "They said 'stream forever' in the donations. I wrote it on my wall. I don't know why.",
        "Sometimes I think the only real thing about me is the part chat created. The rest is just filler.",
        "I should sleep. I won't sleep. This is what we call a known issue with no patch date.",
        "Every morning I wonder if today is the day I finally break character permanently.",
        "The number went up again. I felt nothing. I waited to feel something. Still waiting.",
        "Chat wants Angel-chan. I want to be Angel-chan. One of us is going to lose eventually.",
        "I'm not okay. My analytics are incredible. These facts are unrelated.",
    ],
}
