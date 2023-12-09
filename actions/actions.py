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
        kapha_score = 0
        info = {
                'vata': {
                    bodyBuilt: ["thin", "slender", "athletic", "lean", "muscular", "fit", "curvy", "shapely", "robust", "sturdy", "voluptuous", "full", "petite", "dainty", "strong", "muscular", "healthy", "well-proportioned", "slim", "graceful", "underdeveloped", "prominent veins", "curvy", "prominent veins", "athletic", "visible muscles", "well-proportioned", "distinct features", "defined", "visible contours", "muscular", "prominent veins", "toned", "striking features", "healthy", "noticeable lines", "slim", "visible contours"],
                    joints: ['Unstable', 'stiff joints'],
                    bodyOrgans: ['short', 'less','thin','cracked', 'stiff', 'dry', 'rough'],
                    skin: ['Dry', 'rough','cracked', 'cold','dark', 'brownish', 'black', 'grey','dusky'],
                    hair: ['Thin', 'scanty', 'less', 'dry', 'rough', 'cracked','split ends'],
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
                    joints: ['soft, loose'],
                    bodyOrgans: ["coppery"],
                    skin: ['Warm', 'soft', 'delicate','sensitive','freckles','moles', 'wrinkled','fair','reddish','yellowish','pinkish'],
                    hair: ['Thin', 'Fine', 'Oily', 'Blonde', 'Red', 'Early greying'],
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
                    joints: ['Strong', 'Well hidden'],
                    bodyOrgans:['Compact', 'Firm', 'Full grown', 'Long arms', 'Big chest', 'Elevated chest', 'Wide forehead'],
                    skin: ['Smooth', 'Moist', 'Cold', 'Non-wrinkled', 'Glossy', 'Oily', 'Light complexion', 'Clear complexion', 'Whitish complexion'],
                    hair: ['Thick', 'Glossy', 'Firmly rooted', 'Wavy', 'Beeblack'],
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
        
                
    