from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

class ActionDeterminePrakriti(Action):

    def name(self) -> Text:
        return "action_determinePrakriti"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        # Get the values of the entities
        bodyBuilt = tracker.get_slot('bodyBuilt')
        joints = tracker.get_slot('joints')
        skin = tracker.get_slot('skin')
        hair = tracker.get_slot('hair')
        bodyOrgans = tracker.get_slot('bodyOrgans')
        eyes = tracker.get_slot('eyes')
        lips = tracker.get_slot('lips')
        teeth = tracker.get_slot('teeth')
        initiation_capabilities = tracker.get_slot('initiation_capabilities')
        speech = tracker.get_slot('speech')
        memory = tracker.get_slot('memory')
        diseaseTendency = tracker.get_slot('diseaseTendency')
        diseaseSuseptibility = tracker.get_slot('diseaseSuseptibility')


        # Use these values to determine the prakriti
        prakriti = self.determine_prakriti(bodyBuilt, joints, bodyOrgans, skin, hair, eyes, lips, teeth, initiation_capabilities, speech, memory, diseaseTendency, diseaseSuseptibility)

        # Send a message to the user with the result
        dispatcher.utter_message(text=f"Your prakriti is {prakriti}.")

        return []
    
    def determine_prakriti(bodyBuilt, joints, bodyOrgans, skin, hair, eyes, lips, teeth, initiation_capabilities, speech, memory, diseaseTendency, diseaseSuseptibility):
        x = [bodyBuilt, joints, bodyOrgans, skin, hair, eyes, lips, teeth, initiation_capabilities, speech, memory, diseaseTendency, diseaseSuseptibility]
        props = ['bodyBuilt', 'joints', 'bodyOrgans', 'skin', 'hair', 'eyes', 'lips', 'teeth', 'initiation_capabilities', 'speech', 'memory', 'diseaseTendency', 'diseaseSuseptibility']
        vatta_score=0
        pitta_score=0
        kapha_score =0
        info = {
                'vata': {
                    bodyBuilt: ["thin", "slender", "athletic", "lean", "muscular", "fit", "curvy", "shapely", "robust", "sturdy", "voluptuous", "full", "petite", "dainty", "strong", "muscular", "healthy", "well-proportioned", "slim", "graceful", "underdeveloped", "prominent veins", "curvy", "prominent veins", "athletic", "visible muscles", "well-proportioned", "distinct features", "defined", "visible contours", "muscular", "prominent veins", "toned", "striking features", "healthy", "noticeable lines", "slim", "visible contours"],
                    joints:  [
    "unstable", "stiff",
    "unsteady", "rigid",
    "insecure", "tense",
    "wobbly", "hard",
    "shaky", "inflexible",
    "unbalanced", "stiff",
    "volatile", "firm",
    "unsettled", "solid",
    "unanchored", "taut"
],
                    bodyOrgans: [
    "short", "cracked",
    "thin", "stiff",
    "brief", "damaged",
    "slim", "rigid",
    "small", "broken",
    "narrow", "firm",
    "limited", "fractured",
    "lean", "unyielding",
    "abbreviated", "impaired",
    "slender", "inflexible",
    "diminished", "shrunken",
    "sturdy", "scarce",
    "frail", "scant",
    "ruptured", "tense",
    "compressed", "slight"
],
                    skin:  ['dry', 'rough', 'dark', 'cracked', 'cold', 'black', 'dehydrated', 'coarse', 'deep', 'chapped', 'chilly', 'darker', 'weathered', 'brown', 'blemished', 'cool', 'ebony', 'parched', 'harsh', 'dim', 'split', 'frigid', 'charcoal', 'sallow', 'flawed', 'frosty', 'somber', 'rough', 'chilled', 'swarthy', 'imperfections', 'icy', 'dusky', 'pitted', 'brisk', 'darkened', 'gelid', 'black', 'bleak', 'tanned', 'ashen', 'shadowy', 'frozen', 'bronzed', 'parched', 'harsh', 'somber', 'split', 'brisk', 'tawny'],
                    hair:  ['thin', 'dry', 'split ends', 'scanty', 'rough', 'less', 'cracked', 'delicate', 'sparse', 'impaired tips', 'limited', 'dehydrated', 'coarse', 'weathered', 'frayed tips', 'slim', 'scarce', 'meager', 'arid', 'frizzed tips', 'restricted', 'worn-out', 'fine', 'constrained', 'damaged tips', 'parched', 'frayed ends'],
                    eyes: ['Dry', 'unsteady','blinking'],
                    lips: ['Dark', 'dry', 'cracked'],
                    teeth: ['Small', 'crooked', 'cracked'],
                    initiation_capabilities: ['Quick', 'responsive','enthusiastic'],
                    speech: ["Talkative"],
                    memory: ['Quick grasping', 'Poor retention'],
                    diseaseTendency: ['easily'],
                    diseaseSuseptibility: ["Lower"]
                },
                'pitta': {
                    bodyBuilt: [
                                "good-looking", "delicately shaped", "well-proportioned", "gracefully contoured",
                                "handsome", "elegantly sculpted", "attractive", "finely crafted",
                                "pleasing", "beautifully structured", "captivating", "tastefully designed",
                                "alluring", "artistically shaped", "charming", "skillfully molded",
                                "delightfully contoured", "handsome", "elegantly crafted", "captivating",
                                "captivatingly shaped", "pleasing", "delicately outlined", "attractive",
                                "tastefully designed", "charming", "skillfully molded", "graceful",
                                "exquisitely formed", "compact", "good-looking", "well-proportioned",
                                "visually appealing", "trim", "handsome", "neatly shaped", "attractive",
                                "efficiently designed", "pleasing to the eye", "tidily structured", "charming",
                                "concisely built", "aesthetically pleasing", "well-arranged", "good-looking"
                            ],
                    joints: [
    "soft", "loose",
    "softness", "looseness",
    "supple", "flexible",
    "flexibility", "suppleness",
    "pliable", "limber",
    "limberness", "pliability",
    "pliant", "malleable",
    "malleability", "pliancy",
    "yielding", "elastic",
    "elasticity", "yield",
    "resilient", "pliable",
    "resilience", "pliancy",
    "limber", "supple",
    "suppleness", "limberness",
    "elastic", "flexible",
    "flexibility", "elasticity",
    "malleable", "yielding",
    "yield", "malleability",
    "resilient", "pliant",
    "pliancy", "resilience",
    "bendable", "loosened",
    "bendability", "loosening"
],
                    bodyOrgans:[
    "coppery",
    "bronze",
    "rusty",
    "copper-toned",
    "reddish-brown",
    "earthy",
    "metallic",
    "brownish-red",
    "tawny"
],
                    skin: ['warm', 'soft', 'freckles', 'moles', 'wrinkled', 'fair', 'reddish', 'heated', 'gentle', 'beauty marks', 'creased', 'pale', 'rosy', 'mild', 'silken', 'speckles', 'beauty spots', 'temperate', 'velvety', 'aging', 'roseate', 'cosseted', 'tender', 'blemishes', 'soothing', 'rose-colored', 'blushing'],
                    hair: ['thin', 'fine', 'blonde', 'oily', 'red', 'early greying', 'texture', 'delicate', 'sparse', 'impaired tips', 'limited', 'dehydrated', 'coarse', 'weathered', 'frayed tips', 'slim', 'scarce', 'meager', 'arid', 'frizzed tips', 'restricted', 'worn-out', 'damaged tips', 'parched', 'frayed ends', 'strands'],
                    eyes: ['Sharp', 'Penetrating', 'Blonde eyelashes', 'Copper eyelashes', 'Red eyes', 'Desirous of cold'],
                    lips: ['Soft', 'Pink', 'Copper-colored'],
                    teeth: ['Moderate size', 'Yellowish'],
                    initiation_capabilities: ['Moderate', 'Conviction', 'Understanding'],
                    speech: ['Authoritative', 'Contending', 'Debater'],
                    memory: ['Moderate', 'Grasping', 'Retention'],
                    diseaseTendency:  ['Moderate resistance'],
                    diseaseSuseptibility: ["Moderate"]
                },
                'kapha': {
                    bodyBuilt: ["well-formed", "majestic gait", "sculpted", "toned", "fit", "athletic", "strong", "healthy", "chiseled", "muscular", "trim", "well-proportioned", "robust", "powerful", "defined", "sturdy", "proportionate", "glossy", "stable movement", "defined", "radiant", "athletic", "smooth", "toned", "lustrous", "fit", "polished", "sculpted", "gleaming", "healthy", "sleek", "muscular", "shimmering", "strong", "lustrous", "robust", "glowing", "trim", "shimmering", "powerful", "polished", "well-proportioned", "radiant", "defined", "smooth", "athletic", "shiny", "toned", "lustrous", "fit", "polished", "sculpted", "gleaming", "healthy", "sleek", "muscular", "shimmering", "strong", "lustrous", "robust", "glowing", "trim", "shimmering", "powerful", "polished", "well-proportioned", "radiant", "defined", "smooth", "athletic", "shiny", "toned", "lustrous", "fit", "polished", "sculpted", "gleaming", "healthy", "sleek", "muscular", "shimmering", "strong", "lustrous", "robust", "glowing", "trim", "shimmering", "powerful", "polished", "well-proportioned", "radiant", "defined", "smooth", "athletic", "shiny", "toned", "lustrous", "fit", "polished", "sculpted", "gleaming", "healthy", "sleek", "muscular", "shimmering", "strong", "lustrous", "robust", "glowing", "trim", "shimmering", "powerful", "polished", "well-proportioned", "radiant"],
                    joints: [
    "strong", "well-hidden",
    "well-protected", "strong",
    "robust", "concealed",
    "secure", "sturdy",
    "powerful", "disguised",
    "well-defended", "resilient",
    "vigorous", "camouflaged",
    "guarded", "mighty",
    "stalwart", "veiled",
    "well-shielded", "forceful",
    "potent", "covert",
    "well-armored", "tenacious",
    "stout", "hidden",
    "well-safeguarded", "hardy",
    "firm", "concealed",
    "well-secured", "muscular",
    "resistant", "disguised",
    "well-fortified", "forceful",
    "tenacious", "camouflaged",
    "well-guarded", "sturdy",
    "enduring", "veiled",
    "well-protected", "powerful",
    "solid", "covert",
    "well-defended", "mighty",
    "hidden", "resilient",
    "well-shielded", "sturdy",
    "powerful", "veiled",
    "well-safeguarded", "hardy",
    "muscular", "disguised",
    "well-secured", "firm",
    "forceful", "hidden",
    "well-fortified", "resistant",
    "camouflaged", "covert",
    "well-guarded", "solid",
    "veiled", "mighty",
    "well-protected", "tenacious",
    "resilient", "concealed",
    "well-armored", "powerful",
    "hardy", "veiled",
    "well-safeguarded", "hidden",
    "disguised", "firm",
    "well-secured", "sturdy",
    "forceful", "camouflaged",
    "well-fortified", "resilient",
    "tenacious", "hidden",
    "well-guarded", "powerful",
    "enduring", "veiled",
    "well-protected", "mighty",
    "solid", "covert",
    "well-defended", "hardy"
],
                    bodyOrgans:[
    "compact",
    "firm",
    "big",
    "elevated",
    "long arms",
    "efficiently structured",
    "solid",
    "substantial",
    "raised",
    "extended arms",
    "well-organized",
    "sturdy",
    "spacious",
    "uplifted",
    "elongated arms",
    "neatly arranged",
    "resilient",
    "expansive",
    "lifted",
    "lengthy arms",
    "well-compact",
    "stalwart",
    "generous",
    "heightened",
    "toned",
    "ample",
    "roomy",
    "lengthened arms",
    "sizeable",
    "substantial",
    "elongated arms",
],
                    skin: ['smooth', 'moist', 'light', 'clear', 'oily', 'non-wrinkled', 'whitish', 'slick', 'pale', 'rosy', 'soft', 'glossy', 'silky', 'radiant', 'supple', 'non-creased', 'glistening', 'smooth-textured', 'luminous', 'satin-like'],
                    hair: ['thick', 'glossy', 'black', 'firmly rooted', 'wavy', 'beeblack', 'dense', 'shiny', 'ebony', 'firmly anchored', 'undulating', 'lustrous', 'inky', 'securely rooted'],
                    eyes: ['Large', 'Attractive', 'Full', 'Thick eyelashes', 'Moist', 'Pleasant'],
                    lips: ['Full', 'Thick', 'Moist', 'Oily'],
                    teeth: ['Strong', 'Large', 'White'],
                    initiation_capabilities: ['Slow to initiate'],
                    speech:  ['Calm', 'Quiet'],
                    memory: ['Slow grasping', 'Good retention'],
                    diseaseTendency: ['Good resistance'],
                    diseaseSuseptibility: ["High"]
                }
            }

        for i in range(len(props)):

            vata_list = info['vata'][props[i]]
            pitta_list = info['pitta'][props[i]]
            kapha_list = info['kapha'][props[i]]
            
            if x in kapha_list:
                kapha_score += 1

            elif x in pitta_list:
                pitta_score += 1

            elif x in vata_list:
                vatta_score += 1

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
        
                
    