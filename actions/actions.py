from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

def determine_prakriti(bodyBuilt,joints,bodyOrgans,skin,hair,eyes,lips,teeth,initiation_capabilities,speech,memory,diseaseTendency,diseaseSuseptibility):
    x = [bodyBuilt,joints,bodyOrgans,skin,hair,eyes,lips,teeth,initiation_capabilities,speech,memory,diseaseTendency,diseaseSuseptibility]
    props = ["bodyBuilt","joints","bodyOrgans","skin","hair","eyes","lips","teeth","initiation_capabilities","speech","memory","diseaseTendency","diseaseSuseptibility"]
    vatta_score = 0
    pitta_score = 0
    kapha_score = 0
    info = {'vata':{},'pitta':{},'kapha':{}}
    info = {
    "vata": {
        "bodyBuilt": [
            "thin", "slender", "athletic", "lean", "muscular", "fit", "curvy", "shapely", "robust", "sturdy", "voluptuous",
            "full", "petite", "dainty", "strong", "muscular", "healthy", "well-proportioned", "slim", "graceful",
            "underdeveloped", "prominent veins", "curvy", "prominent veins", "athletic", "visible muscles",
            "well-proportioned", "distinct features", "defined", "visible contours", "muscular", "prominent veins",
            "toned", "striking features", "healthy", "noticeable lines", "slim", "visible contours",
        ],
        "joints": [
            "unstable", "stiff", "unsteady", "rigid", "insecure", "tense", "wobbly", "hard", "shaky", "inflexible",
            "unbalanced", "stiff", "volatile", "firm", "unsettled", "solid", "unanchored", "taut",
        ],
        "bodyOrgans": [
            "short", "cracked", "thin", "stiff", "brief", "damaged", "slim", "rigid", "small", "broken", "narrow", "firm",
            "limited", "fractured", "lean", "unyielding", "abbreviated", "impaired", "slender", "inflexible",
            "diminished", "shrunken", "sturdy", "scarce", "frail", "scant", "ruptured", "tense", "compressed", "slight",
        ],
        "skin": [
            "dry", "rough", "dark", "cracked", "cold", "black", "dehydrated", "coarse", "deep", "chapped", "chilly",
            "darker", "weathered", "brown", "blemished", "cool", "ebony", "parched", "harsh", "dim", "split", "frigid",
            "charcoal", "sallow", "flawed", "frosty", "somber", "rough", "chilled", "swarthy", "imperfections", "icy",
            "dusky", "pitted", "brisk", "darkened", "gelid", "black", "bleak", "tanned", "ashen", "shadowy", "frozen",
            "bronzed", "parched", "harsh", "somber", "split", "brisk", "tawny",
        ],
        "hair": [
            "thin", "dry", "split ends", "scanty", "rough", "less", "cracked", "delicate", "sparse", "impaired tips",
            "limited", "dehydrated", "coarse", "weathered", "frayed tips", "slim", "scarce", "meager", "arid",
            "frizzed tips", "restricted", "worn-out", "fine", "constrained", "damaged tips", "parched", "frayed ends",
        ],
        "eyes": [
            "dry", "unsteady", "moisturized", "blinking", "tired", "teary", "watery", "irritated", "itchy",
        ],
        "lips": [
            "deep-colored", "moisturized", "intensely shaded", "hydrated", "shadowed", "well-moisturized", "dark", "smooth",
            "soft", "richly pigmented", "well-hydrated", "dark-hued", "nourished", "deep-toned", "properly moisturized",
            "supple", "dark-shaded", "adequately moisturize", "well-maintained", "deeply tinted", "kept moisturized",
        ],
        "teeth": [
            "small", "straight", "resilient", "crooked", "charming", "easily cracked", "maintain good oral hygiene",
            "small and neat", "slightly crooked", "tiny", "misaligned", "susceptible to cracking", "tiny but strong",
            "compact", "sturdy", "small, misshapen, prone to cracking", "small yet strong, not easily cracked",
            "dainty, slightly crooked, prone to being easily cracked", "small, crooked, surprisingly resistant to cracking",
            "compact, misaligned, easily cracked", "tiny and unique, crooked, resilient",
            "small, crooked, not easily cracked, good dental care", "small and crooked, hardy, not easily cracked",
            "compact, slightly crooked, susceptible to cracking", "small and crooked, resistant to cracking",
            "delicate, crooked, prone to being easily cracked",
        ],
        "initiation_capabilities": [
            "quick", "responsive", "enthusiastic", "quick thinking", "responsiveness", "enthusiasm", "decision-making",
            "quick mindset", "initiating style", "initiation of projects", "effective initiation", "action",
            "initiation of tasks", "known for", "key to", "forte", "strengths", "blend of", "always responsive",
            "characterize",
        ],
        "speech": [
            "chatty", "verbose", "loquacious", "garrulous", "communicative", "voluble", "effusive", "expressive",
            "articulate", "outspoken", "vocal", "talky", "gabby", "effervescent", "glib", "chatterbox",
        ],
        "memory": [
            "swift", "rapid", "prompt", "nimble", "speedily", "efficient", "quickly", "agile", "effortless", "quick-witted",
            "speedy", "prompt", "retaining", "limited", "poor", "subpar", "inadequate", "weak", "sustaining", "deficient",
            "insufficient", "impaired", "substandard", "below-average", "low", "faulty", "limited", "inferior",
            "unsatisfactory", "suboptimal", "unobtrusive", "low-key", "gentle", "quiet", "reserved", "taciturn", "retiring",
            "introspective", "muted", "pensive", "soft-spoken", "hushed", "demure", "subdued", "subtle", "quiet",
            "low-profile",
        ],
        "diseaseTendency": [
            "catch diseases", "disease resistance", "low resistance", "contract illnesses easily", "limited immunity",
            "diminished resistance", "propensity for contracting diseases", "inclination toward diseases",
            "disposed to illnesses", "proneness to ailments", "subpar immunity", "tendency to acquire illnesses",
            "vulnerability to diseases", "weakened immunity", "frequent bouts of illness", "limited disease resistance",
            "acquires diseases easily", "prone to infections", "suffer from ailments frequently",
            "vulnerability to infections", "frequently falling ill", "low immunity level",
            "tendency to contract infections", "easily acquiring diseases", "proneness to ailments",
            "feeble immune system", "frequent sickness", "prone to acquiring diseases", "susceptible to ailments",
            "weakened disease immunity", "frequently falling ill", "acquire ailments easily", "susceptibility to diseases",
            "prone to infections", "low disease resistance", "frequently suffering from ailments",
            "easily contracting illnesses", "feeble immunity", "prone to acquiring infections",
            "frequently afflicted by diseases", "susceptible to ailments", "low disease resistance",
            "easily acquiring infections", "frequent susceptibility to diseases", "prone to ailments",
            "susceptibility to infections", "limited resistance to diseases", "frequently getting sick",
            "easily acquiring diseases", "weak immune system", "prone to infections", "susceptibility to ailments",
        ],
        "diseaseSuseptibility": [
            "reduced", "diminished", "decreased", "lower", "weakened", "subdued", "lessened", "lowered", "limited",
            "protection", "resistance", "demonstrate", "exhibit", "maintenance", "immunity", "defense", "vulnerability",
            "sedate", "laid-back", "methodical", "careful", "easygoing", "strong", "exceptional", "remarkable",
            "impressive", "outstanding", "top-notch", "excellent", "superior", "good", "high", "effective", "noteworthy",
            "superb", "robust", "exemplary", "high-level", "notable",
        ],
    },
    "pitta":{
        "bodyBuilt": [
            "good-looking", "delicately shaped", "well-proportioned", "gracefully contoured", "handsome",
            "elegantly sculpted", "attractive", "finely crafted", "pleasing", "beautifully structured", "captivating",
            "tastefully designed", "alluring", "artistically shaped", "charming", "skillfully molded",
            "delightfully contoured", "handsome", "elegantly crafted", "captivating", "captivatingly shaped", "pleasing",
            "delicately outlined", "attractive", "tastefully designed", "charming", "skillfully molded", "graceful",
            "exquisitely formed", "compact", "good-looking", "well-proportioned", "visually appealing", "trim", "handsome",
            "neatly shaped", "attractive", "efficiently designed", "pleasing to the eye", "tidily structured", "charming",
            "concisely built", "aesthetically pleasing", "well-arranged", "good-looking",
        ],
        "joints": [
            "soft", "loose", "softness", "looseness", "supple", "flexible", "flexibility", "suppleness", "pliable",
            "limber", "limberness", "pliability", "pliant", "malleable", "malleability", "pliancy", "yielding", "elastic",
            "elasticity", "yield", "resilient", "pliable", "resilience", "pliancy", "limber", "supple", "suppleness",
            "limberness", "elastic", "flexible", "flexibility", "elasticity", "malleable", "yielding", "yield",
            "malleability", "resilient", "pliant", "pliancy", "resilience", "bendable", "loosened", "bendability", "loosening",
        ],
        "bodyOrgans": [
            "coppery", "bronze", "rusty", "copper-toned", "reddish-brown", "earthy", "metallic", "brownish-red", "tawny",
        ],
        "skin": [
            "warm", "soft", "freckles", "moles", "wrinkled", "fair", "reddish", "heated", "gentle", "beauty marks", "creased",
            "pale", "rosy", "mild", "silken", "speckles", "beauty spots", "temperate", "velvety", "aging", "roseate",
            "cosseted", "tender", "blemishes", "soothing", "rose-colored", "blushing",
        ],
        "hair": [
            "thin", "fine", "blonde", "oily", "red", "early greying", "texture", "delicate", "sparse", "impaired tips",
            "limited", "dehydrated", "coarse", "weathered", "frayed tips", "slim", "scarce", "meager", "arid", "frizzed tips",
            "restricted", "worn-out", "damaged tips", "parched", "frayed ends", "strands",
        ],
        "eyes": [
            "sharp", "penetrating", "blonde", "intense", "copper-toned", "copper-colored",
        ],
        "lips": [
            "plush", "softly pink", "velvety", "subtle pink", "tender", "naturally pink", "soft", "delicately colored",
            "pillowy", "rosy", "gentle", "pinkish",
        ],
        "teeth": [
            "moderate size", "pearly white", "yellowish", "healthy", "subtly yellowish enamel", "naturally yellowish",
            "lightly yellowish", "robust", "neither too small nor too large", "subtle yellowish tint", "straight",
            "soft yellowish glow", "well-maintained", "warm and friendly appearance", "gentle yellowish tint",
            "pleasantly yellowish", "reflecting dental health", "gives them character", "radiant smile", "slightly yellowish",
            "exude a friendly charm", "natural yellowish shade", "unique appeal", "adds warmth", "mild yellowish tint",
            "showcasing a healthy radiance",
        ],
        "initiation_capabilities": [
            "moderate", "upon conviction", "understanding", "conviction-driven", "moderation", "balanced approach",
            "thoughtful moderation", "clear understanding", "deep understanding", "measured approach", "context",
        ],
        "speech": [
            "authoritative", "contending debater", "assertive", "leadership approach", "decisive", "managerial approach",
            "approachable", "guidance", "leadership roles", "public speaking engagements", "team leader", "negotiations",
            "professional collaborations", "persuasive",
        ],
        "memory": [
            "balanced", "middle-of-the-road", "moderated", "average", "middling", "intermediate", "tempered", "standard",
            "moderate", "proficient", "regular", "ordinary", "median", "steady", "middle-ground",
        ],
        "diseaseTendency": [
            "moderate resistance", "average resistance", "moderate immunity", "intermediate resistance", "typical resistance",
            "average disease resistance", "standard resistance", "intermediate resistance to diseases", "typical resistance to illnesses",
            "moderate disease resistance", "intermediate immunity", "typical resistance to diseases",
        ],
        "diseaseSuseptibility": [
            "medium", "moderate", "balanced", "middling", "intermediate", "reasonable",
        ],
    },
    "kapha":{
        "bodyBuilt": [
            "well-formed", "majestic gait", "sculpted", "toned", "fit", "athletic", "strong", "healthy", "chiseled",
            "muscular", "trim", "well-proportioned", "robust", "powerful", "defined", "sturdy", "proportionate", "glossy",
            "stable movement", "defined", "radiant", "athletic", "smooth", "toned", "lustrous", "fit", "polished", "sculpted",
            "gleaming", "healthy", "sleek", "muscular", "shimmering", "strong", "lustrous", "robust", "glowing", "trim",
            "shimmering", "powerful", "polished", "well-proportioned", "radiant", "defined", "smooth", "athletic", "shiny",
            "toned", "lustrous", "fit", "polished", "sculpted", "gleaming", "healthy", "sleek", "muscular", "shimmering",
            "strong", "lustrous", "robust", "glowing", "trim", "shimmering", "powerful", "polished", "well-proportioned",
            "radiant", "defined", "smooth", "athletic", "shiny", "toned", "lustrous", "fit", "polished", "sculpted",
            "gleaming", "healthy", "sleek", "muscular", "shimmering", "strong", "lustrous", "robust", "glowing", "trim",
            "shimmering", "powerful", "polished", "well-proportioned", "radiant", "defined", "smooth", "athletic", "shiny",
            "toned", "lustrous", "fit", "polished", "sculpted", "gleaming", "healthy", "sleek", "muscular", "shimmering",
            "strong", "lustrous", "robust", "glowing", "trim", "shimmering", "powerful", "polished", "well-proportioned",
            "radiant",
        ],
        "joints": [
            "strong", "well-hidden", "well-protected", "strong", "robust", "concealed", "secure", "sturdy", "powerful",
            "disguised", "well-defended", "resilient", "vigorous", "camouflaged", "guarded", "mighty", "stalwart", "veiled",
            "well-shielded", "forceful", "potent", "covert", "well-armored", "tenacious", "stout", "hidden", "well-safeguarded",
            "hardy", "firm", "concealed", "well-secured", "muscular", "resistant", "disguised", "well-fortified", "forceful",
            "tenacious", "camouflaged", "well-guarded", "sturdy", "enduring", "veiled", "well-protected", "powerful", "solid",
            "covert", "well-defended", "mighty", "hidden", "resilient", "well-shielded", "sturdy", "powerful", "veiled",
            "well-safeguarded", "hardy", "muscular", "disguised", "well-secured", "firm", "forceful", "hidden",
            "well-fortified", "resistant", "camouflaged", "covert", "well-guarded", "solid", "veiled", "mighty",
            "well-protected", "tenacious", "resilient", "concealed", "well-armored", "powerful", "hardy", "veiled",
            "well-safeguarded", "hidden", "disguised", "firm", "well-secured", "sturdy", "forceful", "camouflaged",
            "well-fortified", "resilient", "tenacious", "hidden", "well-guarded", "powerful", "enduring", "veiled",
            "well-protected", "mighty", "solid", "covert", "well-defended", "hardy",
        ],
        "bodyOrgans": [
            "compact", "firm", "big", "elevated", "long arms", "efficiently structured", "solid", "substantial", "raised",
            "extended arms", "well-organized", "sturdy", "spacious", "uplifted", "elongated arms", "neatly arranged",
            "resilient", "expansive", "lifted", "lengthy arms", "well-compact", "stalwart", "generous", "heightened",
            "toned", "ample", "roomy", "lengthened arms", "sizeable", "substantial", "elongated arms",
        ],
        "skin": [
            "smooth", "moist", "light", "clear", "oily", "non-wrinkled", "whitish", "slick", "pale", "rosy", "soft",
            "glossy", "silky", "radiant", "supple", "non-creased", "glistening", "smooth-textured", "luminous", "satin-like",
        ],
        "hair": [
            "thick", "glossy", "black", "firmly rooted", "wavy", "beeblack", "dense", "shiny", "ebony", "firmly anchored",
            "undulating", "lustrous", "inky", "securely rooted",
        ],
        "eyes": [
            "sparkling", "expressive", "radiant with thick eyelashes", "captivating and alluring eyes", "enchanting",
            "lush with thick eyelashes", "supple", "mesmerizing and attractive eyes", "long and voluminous eyelashes",
            "magnetic", "compelling", "striking and enticing eyes", "charming", "full with voluminous eyelashes", "hydrated",
            "captivating and attractive eyes", "dense eyelashes", "hypnotic", "appealing", "alluring and enchanting eyes",
            "bewitching",
        ],
        "lips": [
            "full", "naturally pink", "thick", "moist", "pillowy", "pinkish", "plush", "oily",
        ],
        "teeth": [
            "strong", "large", "radiantly white", "robust", "stunningly white", "impeccably white", "powerful",
            "substantial size", "gleaming white", "sturdy", "impressively large", "brilliantly white", "pearly white luster",
            "strikingly white", "straight", "naturally strong", "generously large", "whiter than snow", "dazzling white brilliance",
            "teeth with great strength and size", "purely white", "healthy", "impressive", "blindingly white", "well-maintained",
            "resilient", "sparkling white", "flawlessly white", "teeth of substantial size", "exceptionally strong",
            "dazzlingly white", "pure white", "considerable size", "shining white",
        ],
        "initiation_capabilities": [
            "slow", "deliberate", "steady", "thorough", "methodical", "intentionally slow", "thoughtful",
            "comprehensive understanding", "quality over speed",
        ],
        "speech": [
            "serene", "tranquil", "composed", "placid", "equanimous", "unflappable", "peaceful", "cool-headed", "balanced",
            "soothing", "calm", "reassuring", "gentle", "quiet", "unobtrusive", "level-headed", "equanimity", "collected",
            "measured", "unperturbed", "reserved", "taciturn", "retiring", "introspective", "muted", "low-key", "pensive",
            "soft-spoken", "hushed", "demure", "subdued", "subtle", "quiet", "low-profile",
        ],
        "memory": [
            "deliberate", "gradual", "leisurely", "sluggish", "tardy", "prolonged", "relaxed", "languid", "slow", "moderate",
            "measured", "steady", "sedate", "unhurried", "laid-back", "methodical", "careful", "easygoing", "strong",
            "exceptional", "remarkable", "impressive", "outstanding", "top-notch", "excellent", "superior", "good", "high",
            "effective", "noteworthy", "superb", "robust", "exemplary", "high-level", "notable",
        ],
        "diseaseTendency": [
            "good resistance", "immunity is strong", "excellent resistance", "robust resistance", "immunity is vigorous",
            "exceptional resistance", "disease resistance", "resilient immunity", "strong resistance", "vigorous immunity",
            "strong disease resistance", "strong immunity", "resilient resistance", "robust disease resistance",
        ],
        "diseaseSuseptibility": [
            "significant", "intensely", "heightened", "high", "substantial", "elevated", "increased", "pronounced",
            "extreme", "intense",
        ],
    }
    }

    for i in range(len(props)):

        vata_list = info["vata"][props[i]]
        pitta_list = info["pitta"][props[i]]
        kapha_list = info["kapha"][props[i]]

        for k in x:
            if k is None:
                continue
            if k in kapha_list:
                kapha_score += 1
            elif k in pitta_list:
                pitta_score += 1
            elif k in vata_list:
                vatta_score += 1
    
    print('vatta_score',vatta_score,'pitta_score',pitta_score,'kapha_score',kapha_score)

    if kapha_score == vatta_score and vatta_score == pitta_score:
        return "Kapha"

    if kapha_score > vatta_score:

        if kapha_score > pitta_score:
            return "Kapha"

        else:
            return "Pitta"

    else:

        if vatta_score > pitta_score:
            return "Vatta"

        else:
            return "Pitta"

class ActionDeterminePrakriti(Action):
    def name(self) -> Text:
        return "action_determinePrakriti"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:

        # Get the values of the entities
        bodyBuilt = tracker.get_slot("bodyBuilt")
        joints = tracker.get_slot("joints")
        skin = tracker.get_slot("skin")
        hair = tracker.get_slot("hair")
        bodyOrgans = tracker.get_slot("bodyOrgans")
        eyes = tracker.get_slot("eyes")
        lips = tracker.get_slot("lips")
        teeth = tracker.get_slot("teeth")
        initiation_capabilities = tracker.get_slot("initiation_capabilities")
        speech = tracker.get_slot("speech")
        memory = tracker.get_slot("memory")
        diseaseTendency = tracker.get_slot("diseaseTendency")
        diseaseSuseptibility = tracker.get_slot("diseaseSuseptibility")

        # Use these values to determine the prakriti
        prakriti = determine_prakriti(bodyBuilt,joints,bodyOrgans,skin,hair,eyes,lips,teeth,initiation_capabilities,speech,memory,diseaseTendency,diseaseSuseptibility)

        # Send a message to the user with the result
        dispatcher.utter_message(text=f"Your prakriti is {prakriti}.")

        return []

