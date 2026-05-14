import streamlit as stimport pandas as pdfrom PIL 
import Imageimport base64import ioimport jsonfrom datetime 
import datetime, timedeltaimport os
import randomimport calendar
import plotly.express as px
import plotly.graph_objects as go
from streamlit_option_menu 
import option_menuimport os
import requests

Page configuration

st.set_page_config(page_title="FestiveVibe - Celebrating Telugu Festivals",page_icon="🎉",layout="wide",initial_sidebar_state="expanded")

Initialize session state for new features

if "language" not in st.session_state:st.session_state.language = "english"if "dark_mode" not in st.session_state:st.session_state.dark_mode = Falseif "submissions" not in st.session_state:st.session_state.submissions = []if "gallery_photos" not in st.session_state:st.session_state.gallery_photos = []if "quiz_scores" not in st.session_state:st.session_state.quiz_scores = []if "user_stories" not in st.session_state:st.session_state.user_stories = []if "reminders" not in st.session_state:st.session_state.reminders = []if "admin_mode" not in st.session_state:st.session_state.admin_mode = False

Custom CSS for styling

def load_css():dark_mode_css = """[data-testid="stAppViewContainer"] {background-color: #1a1a1a !important;color: #ffffff !important;}.stMarkdown, .stText, .stSelectbox, .stTextInput {color: #ffffff !important;}""" if st.session_state.dark_mode else ""

st.markdown(f"""
<style>
{dark_mode_css}

.main-header {{
    background: linear-gradient(135deg, #FF6B35, #F7931E);
    padding: 2rem;
    border-radius: 15px;
    text-align: center;
    margin-bottom: 2rem;
    color: white;
    box-shadow: 0 8px 32px rgba(255, 107, 53, 0.3);
}}

.festival-card {{
    background: white;
    border-radius: 15px;
    padding: 1.5rem;
    margin: 1rem 0;
    box-shadow: 0 4px 20px rgba(0,0,0,0.1);
    transition: transform 0.3s ease;
    border-left: 5px solid #FF6B35;
    color: #222 !important;
}}
.festival-card * {{
    color: #222 !important;
}}

.festival-card:hover {{
    transform: translateY(-5px);
    box-shadow: 0 8px 30px rgba(0,0,0,0.15);
}}

.region-tag {{
    background: #4CAF50;
    color: white;
    padding: 0.3rem 0.8rem;
    border-radius: 20px;
    font-size: 0.8rem;
    display: inline-block;
    margin: 0.2rem;
}}

.region-tag.ap {{
    background: #2196F3;
}}

.region-tag.telangana {{
    background: #FF9800;
}}

.submit-form {{
    background: #f8f9fa;
    padding: 2rem;
    border-radius: 15px;
    border: 2px dashed #FF6B35;
}}

.footer {{
    background: #2c3e50;
    color: white;
    padding: 2rem;
    text-align: center;
    margin-top: 3rem;
    border-radius: 15px;
}}

.social-icon {{
    font-size: 2rem;
    margin: 0 1rem;
    color: #FF6B35;
}}

.festival-details {{
    background: #fff3e0;
    padding: 1.5rem;
    border-radius: 10px;
    margin: 1rem 0;
    border-left: 4px solid #FF9800;
}}

.detail-section {{
    margin: 1rem 0;
    padding: 1rem;
    background: white;
    border-radius: 8px;
    border: 1px solid #e0e0e0;
}}

.detail-section h4 {{
    color: #FF6B35;
    margin-bottom: 0.5rem;
}}

/* New feature styles */
.calendar-day {{
    background: #f0f8ff;
    border: 1px solid #ddd;
    padding: 0.5rem;
    text-align: center;
    cursor: pointer;
    transition: background-color 0.3s;
}}

.calendar-day:hover {{
    background: #e6f3ff;
}}

.calendar-day.festival {{
    background: #ffeb3b;
    font-weight: bold;
}}

.gallery-item {{
    background: white;
    border-radius: 10px;
    padding: 1rem;
    margin: 1rem 0;
    box-shadow: 0 2px 10px rgba(0,0,0,0.1);
}}

.quiz-card {{
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    color: white;
    padding: 2rem;
    border-radius: 15px;
    margin: 1rem 0;
}}

.story-card {{
    background: #f9f9f9;
    border-left: 4px solid #4CAF50;
    padding: 1.5rem;
    margin: 1rem 0;
    border-radius: 8px;
}}

.countdown-timer {{
    background: linear-gradient(135deg, #FF6B35, #F7931E);
    color: white;
    padding: 2rem;
    border-radius: 15px;
    text-align: center;
    margin: 2rem 0;
}}

.admin-panel {{
    background: #2c3e50;
    color: white;
    padding: 2rem;
    border-radius: 15px;
    margin: 2rem 0;
}}

.reminder-card {{
    background: #e8f5e8;
    border: 2px solid #4CAF50;
    padding: 1rem;
    border-radius: 10px;
    margin: 1rem 0;
}}

.map-container {{
    background: white;
    border-radius: 15px;
    padding: 2rem;
    margin: 2rem 0;
    box-shadow: 0 4px 20px rgba(0,0,0,0.1);
}}
</style>
""", unsafe_allow_html=True)

Festival data

def get_festival_data():festivals = {"Sankranti": {"telugu_name": "సంక్రాంతి","date": "January 14-15","description": "Harvest festival marking the sun's transit into Capricorn","telugu_description": "సూర్యుడు మకర రాశిలోకి ప్రవేశించే సమయంలో జరుపుకునే పంట పండుగ","regions": ["AP", "Telangana"],"rituals": ["Bhogi bonfire", "Sankranti kite flying", "Pongal preparation", "Cattle decoration"],"foods": ["Pongal", "Sakinalu", "Garelu", "Payasam"],"attire": ["Traditional silk sarees", "Dhoti and kurta", "Colorful turbans"],"dances": ["Kolattam", "Dappu dance", "Gobbi dance"],"events": ["Kite competitions", "Bull fights", "Cock fights", "Community feasts"]},"Bathukamma": {"telugu_name": "బతుకమ్మ","date": "September-October","description": "Flower festival celebrating womanhood and nature","telugu_description": "స్త్రీత్వం మరియు ప్రకృతిని జరుపుకునే పుష్పోత్సవం","regions": ["Telangana"],"rituals": ["Flower arrangement", "Circular dance", "Immersion in water"],"foods": ["Pulihora", "Sakinalu", "Garelu", "Sweet rice"],"attire": ["Traditional sarees", "Flower jewelry", "Colorful bangles"],"dances": ["Bathukamma dance", "Circular folk dance"],"events": ["Community gatherings", "Cultural programs", "Folk songs"]},"Bonalu": {"telugu_name": "బోనాలు","date": "July-August","description": "Annual festival honoring Goddess Mahakali","telugu_description": "మహాకాళి దేవిని గౌరవించే వార్షిక పండుగ","regions": ["Telangana"],"rituals": ["Offering bonam", "Processions", "Temple visits"],"foods": ["Bonam rice", "Curd rice", "Sweet offerings"],"attire": ["Traditional sarees", "Red and yellow colors"],"dances": ["Bonalu dance", "Folk dances"],"events": ["Temple processions", "Cultural performances"]},"Ugadi": {"telugu_name": "ఉగాది","date": "March-April","description": "Telugu New Year marking the beginning of spring","telugu_description": "వసంత ఋతువు ప్రారంభమయ్యే తెలుగు నూతన సంవత్సరం","regions": ["AP", "Telangana"],"rituals": ["Panchanga sravanam", "Oil bath", "Neem consumption"],"foods": ["Ugadi pachadi", "Pulihora", "Bobbatlu", "Payasam"],"attire": ["New clothes", "Traditional silk sarees", "Dhoti and kurta"],"dances": ["Classical dances", "Folk dances"],"events": ["Cultural programs", "Family gatherings", "Temple visits"]},"Dasara": {"telugu_name": "దసరా","date": "September-October","description": "Victory of good over evil, celebrated for 10 days","telugu_description": "మంచి చెడుపై గెలుపును జరుపుకునే పది రోజుల పండుగ","regions": ["AP", "Telangana"],"rituals": ["Golu display", "Vijayadashami", "Ayudha puja"],"foods": ["Sundal varieties", "Pulihora", "Payasam", "Laddu"],"attire": ["Traditional silk sarees", "Dhoti and kurta"],"dances": ["Classical dances", "Folk dances", "Dollu kunitha"],"events": ["Golu competitions", "Cultural programs", "Processions"]},"Deepavali": {"telugu_name": "దీపావళి","date": "October-November","description": "Festival of lights celebrating victory of light over darkness","telugu_description": "చీకటిపై వెలుగు గెలుపును జరుపుకునే దీపాల పండుగ","regions": ["AP", "Telangana"],"rituals": ["Oil bath", "Lakshmi puja", "Fireworks"],"foods": ["Laddu", "Murukulu", "Garelu", "Payasam"],"attire": ["New clothes", "Traditional silk sarees"],"dances": ["Classical dances", "Folk dances"],"events": ["Family gatherings", "Fireworks display", "Temple visits"]},"Sri Rama Navami": {"telugu_name": "శ్రీ రామ నవమి","date": "March-April","description": "Birth celebration of Lord Rama","telugu_description": "శ్రీరాముని జన్మదినం జరుపుకునే పండుగ","regions": ["AP", "Telangana"],"rituals": ["Rama puja", "Bhajan sessions", "Temple visits"],"foods": ["Panakam", "Neeru more", "Pulihora", "Payasam"],"attire": ["Traditional clothes", "White and yellow colors"],"dances": ["Classical dances", "Bhajan sessions"],"events": ["Temple celebrations", "Cultural programs", "Processions"]},"Varalakshmi Vratam": {"telugu_name": "వరలక్ష్మి వ్రతం","date": "July-August","description": "Vow to Goddess Lakshmi for prosperity and well-being","telugu_description": "సంపద మరియు శుభకరమైన జీవితం కోసం లక్ష్మీ దేవికి చేసే వ్రతం","regions": ["AP", "Telangana"],"rituals": ["Lakshmi puja", "Thread tying", "Fasting"],"foods": ["Pulihora", "Payasam", "Sweet rice", "Fruits"],"attire": ["Traditional silk sarees", "Gold jewelry"],"dances": ["Classical dances", "Devotional songs"],"events": ["Temple visits", "Community gatherings", "Cultural programs"]},"Ganesh Chaturthi": {"telugu_name": "వినాయక చవితి","date": "August-September","description": "Birth celebration of Lord Ganesha","telugu_description": "వినాయకుని జన్మదినం జరుపుకునే పండుగ","regions": ["AP", "Telangana"],"rituals": ["Ganesha puja", "Modak offering", "Immersion"],"foods": ["Modak", "Laddu", "Pulihora", "Payasam"],"attire": ["Traditional clothes", "Red and yellow colors"],"dances": ["Classical dances", "Folk dances"],"events": ["Ganesha processions", "Cultural programs", "Immersion ceremonies"]},"Holi": {"telugu_name": "హోళీ","date": "February-March","description": "Festival of colors celebrating spring and love","telugu_description": "వసంతం మరియు ప్రేమను జరుపుకునే రంగుల పండుగ","regions": ["AP", "Telangana"],"rituals": ["Color throwing", "Bonfire", "Community celebrations"],"foods": ["Gujiya", "Thandai", "Sweets", "Snacks"],"attire": ["White clothes", "Colorful accessories"],"dances": ["Folk dances", "Community dances"],"events": ["Color celebrations", "Community gatherings", "Cultural programs"]},"Karthika Deepam": {"telugu_name": "కార్తిక దీపం","date": "November-December","description": "Festival of lights during Karthika month","telugu_description": "కార్తిక మాసంలో జరుపుకునే దీపాల పండుగ","regions": ["AP", "Telangana"],"rituals": ["Lighting lamps", "Temple visits", "Prayers"],"foods": ["Pulihora", "Payasam", "Sweet rice", "Fruits"],"attire": ["Traditional clothes", "White and yellow colors"],"dances": ["Classical dances", "Devotional songs"],"events": ["Temple celebrations", "Cultural programs", "Light displays"]},"Hanuman Jayanti": {"telugu_name": "హనుమాన్ జయంతి","date": "March-April","description": "Birth celebration of Lord Hanuman","telugu_description": "హనుమానుని జన్మదినం జరుపుకునే పండుగ","regions": ["AP", "Telangana"],"rituals": ["Hanuman puja", "Bhajan sessions", "Temple visits"],"foods": ["Panakam", "Neeru more", "Pulihora", "Sweets"],"attire": ["Traditional clothes", "Orange and red colors"],"dances": ["Classical dances", "Bhajan sessions"],"events": ["Temple celebrations", "Cultural programs", "Processions"]},"Krishnashtami": {"telugu_name": "కృష్ణాష్టమి","date": "August-September","description": "Birth celebration of Lord Krishna","telugu_description": "శ్రీకృష్ణుని జన్మదినం జరుపుకునే పండుగ","regions": ["AP", "Telangana"],"rituals": ["Krishna puja", "Dahi handi", "Bhajan sessions"],"foods": ["Makhan", "Laddu", "Pulihora", "Payasam"],"attire": ["Traditional clothes", "Yellow and blue colors"],"dances": ["Classical dances", "Folk dances", "Dahi handi"],"events": ["Dahi handi celebrations", "Cultural programs", "Temple visits"]},"Eid": {"telugu_name": "ఈద్","date": "Varies (Islamic calendar)","description": "Islamic festival celebrated by Muslim communities","telugu_description": "ముస్లిం సమాజాలచే జరుపుకునే ఇస్లామిక్ పండుగ","regions": ["AP", "Telangana"],"rituals": ["Eid prayers", "Charity", "Family gatherings"],"foods": ["Biryani", "Sheer khurma", "Haleem", "Sweets"],"attire": ["Traditional Islamic clothes", "White and colorful dresses"],"dances": ["Cultural dances", "Community celebrations"],"events": ["Eid prayers", "Family gatherings", "Community feasts"]},"Christmas": {"telugu_name": "క్రిస్మస్","date": "December 25","description": "Christian festival celebrating birth of Jesus Christ","telugu_description": "యేసు క్రీస్తు జన్మదినం జరుపుకునే క్రైస్తవ పండుగ","regions": ["AP", "Telangana"],"rituals": ["Christmas mass", "Prayers", "Gift giving"],"foods": ["Christmas cake", "Biryani", "Sweets", "Traditional dishes"],"attire": ["Traditional clothes", "Red and green colors"],"dances": ["Cultural dances", "Community celebrations"],"events": ["Christmas mass", "Family gatherings", "Community celebrations"]},"Kanuma": {"telugu_name": "కనుమ","date": "January (day after Sankranti)","description": "Festival dedicated to cattle, celebrated after Sankranti","telugu_description": "సంక్రాంతి తర్వాత జరుపుకునే పశువుల పండుగ","regions": ["AP", "Telangana"],"rituals": ["Cattle worship", "Decorating cattle", "Feeding cattle special food"],"foods": ["Non-veg dishes", "Pulusu", "Rice items"],"attire": ["Traditional clothes"],"dances": ["Folk dances"],"events": ["Village gatherings", "Cattle fairs"]},"Nagula Chavithi": {"telugu_name": "నాగుల చవితి","date": "October-November","description": "Festival for worshipping serpent deities","telugu_description": "పాములను పూజించే పండుగ","regions": ["AP", "Telangana"],"rituals": ["Snake idol worship", "Offering milk to anthills"],"foods": ["Fruits", "Payasam", "Rice dishes"],"attire": ["Traditional clothes"],"dances": ["Folk songs"],"events": ["Family gatherings", "Temple visits"]},"Poleramma Jathara": {"telugu_name": "పోలేరమ్మ జాతర","date": "Varies (local calendar)","description": "Local village festival dedicated to Goddess Poleramma","telugu_description": "పోలేరమ్మ దేవికి జరిపే గ్రామోత్సవం","regions": ["AP", "Telangana"],"rituals": ["Poleramma puja", "Processions", "Animal sacrifices (in some places)"],"foods": ["Prasadam", "Rice dishes"],"attire": ["Traditional clothes"],"dances": ["Folk dances", "Dappu"],"events": ["Village fair", "Cultural programs"]},"Raksha Bandhan": {"telugu_name": "రాఖీ పౌర్ణమి","date": "August","description": "Festival celebrating the bond between brothers and sisters","telugu_description": "అక్కచెల్లెళ్ళు మరియు అన్నదమ్ముల బంధాన్ని జరుపుకునే పండుగ","regions": ["AP", "Telangana"],"rituals": ["Tying rakhi", "Gift exchange", "Family gatherings"],"foods": ["Sweets", "Rice dishes"],"attire": ["Traditional clothes"],"dances": ["Family songs"],"events": ["Family celebrations"]},"Sankatahara Chaturthi": {"telugu_name": "సంకటహర చతుర్థి","date": "Every lunar month","description": "Monthly festival dedicated to Lord Ganesha for removing obstacles","telugu_description": "వినాయకునికి అంకితమైన నెలవారీ సంకటహర చతుర్థి పూజ","regions": ["AP", "Telangana"],"rituals": ["Ganesha puja", "Fasting", "Moon sighting"],"foods": ["Modak", "Fruits"],"attire": ["Traditional clothes"],"dances": ["Devotional songs"],"events": ["Temple visits", "Family prayers"]},"Maha Shivaratri": {"telugu_name": "మహా శివరాత్రి","date": "February-March","description": "Night dedicated to Lord Shiva with fasting and night-long vigil","telugu_description": "లొర్డ్ శివుడికి అంకితమైన ఉపవాసం మరియు జాగరణతో కూడిన రాత్రి","regions": ["AP", "Telangana"],"rituals": ["Shiva abhishekam", "Night vigil", "Fasting", "Chanting Om Namah Shivaya"],"foods": ["Fruits", "Milk", "Prasadam"],"attire": ["Traditional clothes", "White attire"],"dances": ["Bhajans", "Classical dances"],"events": ["Temple gatherings", "Processions"]},"Subrahmanya Shashti": {"telugu_name": "సుబ్రహ్మణ్య షష్టి","date": "November-December","description": "Festival dedicated to Lord Subrahmanya (Kartikeya)","telugu_description": "కార్తికేయ స్వామికి అంకితమైన పండుగ","regions": ["AP", "Telangana"],"rituals": ["Subrahmanya puja", "Fasting", "Special prayers"],"foods": ["Fruits", "Rice dishes"],"attire": ["Traditional clothes"],"dances": ["Devotional songs"],"events": ["Temple visits", "Community prayers"]},"Ratha Saptami": {"telugu_name": "రథ సప్తమి","date": "January-February","description": "Festival dedicated to Sun God, marks the change of season","telugu_description": "సూర్య భగవానునికి అంకితమైన పండుగ, ఋతువుల మార్పును సూచిస్తుంది","regions": ["AP", "Telangana"],"rituals": ["Sun worship", "Holy bath", "Offering arghya"],"foods": ["Sweet pongal", "Rice dishes"],"attire": ["Traditional clothes"],"dances": ["Folk dances"],"events": ["Temple celebrations"]},"Varuna Yagam": {"telugu_name": "వరుణ యాగం","date": "Varies (before monsoon)","description": "Ritual for rain and prosperity dedicated to Lord Varuna","telugu_description": "వర్షాలు, సంపద కోసం వరుణ దేవునికి చేసే యాగం","regions": ["AP", "Telangana"],"rituals": ["Varuna puja", "Fire ritual", "Chanting mantras"],"foods": ["Prasadam", "Fruits"],"attire": ["Traditional clothes"],"dances": ["Folk dances"],"events": ["Community gatherings"]},"Chaitra Pournami": {"telugu_name": "చైత్ర పౌర్ణమి","date": "March-April","description": "Full moon festival in the month of Chaitra","telugu_description": "చైత్ర మాసంలో వచ్చే పౌర్ణమి పండుగ","regions": ["AP", "Telangana"],"rituals": ["Full moon worship", "Temple visits"],"foods": ["Sweets", "Rice dishes"],"attire": ["Traditional clothes"],"dances": ["Folk dances"],"events": ["Community celebrations"]},"Vinayaka Nimajjanam": {"telugu_name": "వినాయక నిమజ్జనం","date": "August-September","description": "Immersion of Ganesha idols marking the end of Ganesh Chaturthi","telugu_description": "వినాయక చవితి ముగిసిన తర్వాత వినాయక విగ్రహాల నిమజ్జనం","regions": ["AP", "Telangana"],"rituals": ["Procession", "Immersion of idols", "Chanting"],"foods": ["Prasadam", "Sweets"],"attire": ["Traditional clothes"],"dances": ["Folk dances", "Dappu"],"events": ["Large processions", "Community celebrations"]},"Sri Krishna Tulasi Kalyanam": {"telugu_name": "శ్రీకృష్ణ తులసి కళ్యాణం","date": "November-December","description": "Symbolic wedding of Lord Krishna and Tulasi plant","telugu_description": "శ్రీకృష్ణుడు మరియు తులసి మొక్క కళ్యాణం","regions": ["AP", "Telangana"],"rituals": ["Tulasi puja", "Wedding rituals", "Chanting"],"foods": ["Prasadam", "Sweets"],"attire": ["Traditional clothes"],"dances": ["Devotional songs"],"events": ["Temple celebrations"]},"Mukkoti Ekadashi": {"telugu_name": "ముక్కోటి ఏకాదశి","date": "December-January","description": "Important Ekadashi for Vaishnavites, observed with fasting","telugu_description": "వైష్ణవులకు ముఖ్యమైన ఏకాదశి ఉపవాసం","regions": ["AP", "Telangana"],"rituals": ["Fasting", "Vishnu puja", "Temple visits"],"foods": ["Fruits", "Prasadam"],"attire": ["Traditional clothes"],"dances": ["Devotional songs"],"events": ["Temple gatherings"]},"Bhogi": {"telugu_name": "భోగి","date": "January (day before Sankranti)","description": "First day of Sankranti, celebrated with bonfires and discarding old things","telugu_description": "సంక్రాంతి మొదటి రోజు, పాత వస్తువులను తగలబెట్టి కొత్తదాన్ని ఆహ్వానించే పండుగ","regions": ["AP", "Telangana"],"rituals": ["Bhogi mantalu (bonfire)", "Cleaning homes", "Singing songs"],"foods": ["Rice dishes", "Sweets"],"attire": ["Traditional clothes"],"dances": ["Folk songs"],"events": ["Community bonfires"]},"Sri Venkateswara Brahmotsavam": {"telugu_name": "శ్రీ వెంకటేశ్వర బ్రహ్మోత్సవం","date": "September-October","description": "Grand annual festival at Tirumala Venkateswara Temple","telugu_description": "తిరుమలలో జరిగే శ్రీ వెంకటేశ్వర స్వామి బ్రహ్మోత్సవం","regions": ["AP"],"rituals": ["Processions", "Special pujas", "Chariot festival"],"foods": ["Prasadam", "Rice dishes"],"attire": ["Traditional clothes"],"dances": ["Classical dances", "Devotional songs"],"events": ["Temple processions", "Cultural programs"]},"Atla Taddi": {"telugu_name": "అట్ల తద్దె","date": "October-November","description": "Festival for married women, celebrated with special rituals and eating atlu (dosas)","telugu_description": "పెళ్లయిన మహిళలు ఉపవాసం ఉండి అట్లను తినే పండుగ","regions": ["AP", "Telangana"],"rituals": ["Fasting", "Moon sighting", "Eating atlu (dosas)", "Pooja"],"foods": ["Atlu (dosas)", "Sweets"],"attire": ["Traditional sarees", "Jewelry"],"dances": ["Folk songs"],"events": ["Women gatherings"]},"Sankranti Kanuma Panduga": {"telugu_name": "కనుమ పండుగ","date": "January (after Sankranti)","description": "Cattle festival, part of Sankranti celebrations","telugu_description": "సంక్రాంతి తర్వాత జరుపుకునే పశువుల పండుగ","regions": ["AP", "Telangana"],"rituals": ["Cattle worship", "Feeding cattle", "Village gatherings"],"foods": ["Non-veg dishes", "Rice items"],"attire": ["Traditional clothes"],"dances": ["Folk dances"],"events": ["Cattle fairs", "Village celebrations"]},"Pedda Panduga": {"telugu_name": "పెద్ద పండుగ","date": "Varies (regional)","description": "Major festival in many Andhra villages, celebrated with feasts and rituals","telugu_description": "ఆంధ్ర గ్రామాల్లో జరుపుకునే ముఖ్యమైన పండుగ","regions": ["AP"],"rituals": ["Village deity worship", "Community feasts"],"foods": ["Rice dishes", "Sweets", "Non-veg items"],"attire": ["Traditional clothes"],"dances": ["Folk dances"],"events": ["Village gatherings", "Cultural programs"]},"Sri Rama Pattabhishekam": {"telugu_name": "శ్రీరామ పట్టాభిషేకం","date": "March-April","description": "Coronation of Lord Rama, celebrated after Sri Rama Navami","telugu_description": "శ్రీరాముని పట్టాభిషేకాన్ని జరుపుకునే పండుగ","regions": ["AP", "Telangana"],"rituals": ["Rama puja", "Reciting Ramayana", "Cultural programs"],"foods": ["Panakam", "Sweets"],"attire": ["Traditional clothes"],"dances": ["Classical dances", "Bhajans"],"events": ["Temple celebrations"]},"Laksha Deepotsavam": {"telugu_name": "లక్ష దీపోత్సవం","date": "November-December","description": "Festival of lighting one lakh lamps in temples and homes","telugu_description": "పదివేల దీపాలను వెలిగించే పండుగ","regions": ["AP", "Telangana"],"rituals": ["Lighting lamps", "Temple worship"],"foods": ["Prasadam", "Sweets"],"attire": ["Traditional clothes"],"dances": ["Devotional songs"],"events": ["Temple gatherings"]},"Sammakka Saralamma Jatara": {"telugu_name": "సమ్మక్క సారలమ్మ జాతర","date": "February (biennial)","description": "Asia's largest tribal festival held in Medaram, Telangana","telugu_description": "తెలంగాణలోని మెదరం గ్రామంలో జరిగే ఆసియా అతిపెద్ద గిరిజన పండుగ","regions": ["Telangana"],"rituals": ["Goddess worship", "Offerings", "Processions"],"foods": ["Rice dishes", "Sweets"],"attire": ["Traditional clothes", "Tribal attire"],"dances": ["Tribal dances", "Folk songs"],"events": ["Mass gatherings", "Cultural programs"]},"Toli Ekadashi": {"telugu_name": "తొలి ఏకాదశి","date": "June-July","description": "First Ekadashi of Ashada month, considered highly auspicious","telugu_description": "ఆషాఢ మాసంలో వచ్చే తొలి ఏకాదశి","regions": ["AP", "Telangana"],"rituals": ["Fasting", "Vishnu puja", "Temple visits"],"foods": ["Fruits", "Prasadam"],"attire": ["Traditional clothes"],"dances": ["Devotional songs"],"events": ["Temple gatherings"]},"Ayyappa Deeksha/Makaravilakku": {"telugu_name": "అయ్యప్ప దీక్ష/మకరవిళక్కు","date": "December-January","description": "Pilgrimage and festival for Lord Ayyappa, culminating in Makaravilakku","telugu_description": "అయ్యప్ప స్వామికి అంకితమైన దీక్ష మరియు మకరవిళక్కు పండుగ","regions": ["AP", "Telangana"],"rituals": ["Ayyappa deeksha", "Pilgrimage", "Special pujas"],"foods": ["Simple vegetarian food", "Prasadam"],"attire": ["Black clothes", "Mala"],"dances": ["Bhajans"],"events": ["Pilgrim gatherings"]},"Ugadi Pachadi Day": {"telugu_name": "ఉగాది పచ్చడి రోజు","date": "March-April (Ugadi)","description": "Special day for preparing and sharing Ugadi Pachadi, symbolizing life's flavors","telugu_description": "ఉగాది పచ్చడిని తయారు చేసి పంచుకునే ప్రత్యేక రోజు","regions": ["AP", "Telangana"],"rituals": ["Preparing Ugadi pachadi", "Family gatherings"],"foods": ["Ugadi pachadi", "Sweets"],"attire": ["Traditional clothes"],"dances": ["Folk songs"],"events": ["Family celebrations"]},"Kondapalli Jathara": {"telugu_name": "కొండపల్లి జాతర","date": "Varies (regional)","description": "Local fair and festival in Kondapalli, Krishna district","telugu_description": "కృష్ణా జిల్లాలోని కొండపల్లిలో జరిగే జాతర","regions": ["AP"],"rituals": ["Village deity worship", "Processions"],"foods": ["Rice dishes", "Sweets"],"attire": ["Traditional clothes"],"dances": ["Folk dances"],"events": ["Village fair", "Cultural programs"]}}return festivals

Language toggle

def language_toggle():col1, col2 = st.sidebar.columns([1, 1])with col1:if st.button("🇮🇳 తెలుగు", key="telugu_btn"):st.session_state.language = "telugu"with col2:if st.button("🇺🇸 English", key="english_btn"):st.session_state.language = "english"

if "language" not in st.session_state:
    st.session_state.language = "english"

Homepage

def show_homepage():st.markdown("""🎉 FestiveVibe – Celebrating Telugu FestivalsExplore traditions from Sankranti to Bathukammaసంక్రాంతి నుండి బతుకమ్మ వరకు సంప్రదాయాలను అన్వేషించండి""", unsafe_allow_html=True)

# Welcome message
if st.session_state.language == "telugu":
    st.markdown("""
    ## స్వాగతం! 🙏
    
    **FestiveVibe**లోకి స్వాగతం! మన తెలుగు సంస్కృతి మరియు సంప్రదాయాలను జరుపుకునే అందమైన పండుగలను అన్వేషించండి.
    
    ఈ వెబ్సైట్ ద్వారా మీరు:
    - ఆంధ్రప్రదేశ్ మరియు తెలంగాణలో జరుపుకునే పండుగలను తెలుసుకోవచ్చు
    - ప్రతి పండుగ గురించి వివరాలు తెలుసుకోవచ్చు
    - మీ స్థానిక సంప్రదాయాలను పంచుకోవచ్చు
    - మన సంస్కృతి గురించి మరింత తెలుసుకోవచ్చు
    """)
else:
    st.markdown("""
    ## Welcome! 🙏
    
    Welcome to **FestiveVibe**! Explore the beautiful festivals that celebrate our Telugu culture and traditions.
    
    Through this website, you can:
    - Learn about festivals celebrated in Andhra Pradesh and Telangana
    - Discover details about each festival
    - Share your local traditions
    - Learn more about our culture
    """)

# Quick stats
festivals = get_festival_data()
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Festivals", len(festivals))
with col2:
    st.metric("States", "2")
with col3:
    st.metric("Languages", "2")
with col4:
    st.metric("Traditions", "15+")

Festival Explorer

def show_festival_explorer():festivals = get_festival_data()

if st.session_state.language == "telugu":
    st.title("🎊 పండుగల అన్వేషకుడు")
    st.markdown("ఆంధ్రప్రదేశ్ మరియు తెలంగాణలో జరుపుకునే పండుగలను అన్వేషించండి")
else:
    st.title("🎊 Festival Explorer")
    st.markdown("Explore festivals celebrated in Andhra Pradesh and Telangana")

# Filter options
col1, col2 = st.columns(2)
with col1:
    region_filter = st.selectbox(
        "Filter by Region" if st.session_state.language == "english" else "ప్రాంతం ద్వారా ఫిల్టర్ చేయండి",
        ["All", "AP", "Telangana"]
    )

with col2:
    search_term = st.text_input(
        "Search festivals" if st.session_state.language == "english" else "పండుగలను వెతకండి",
        ""
    )

# Display festivals
for festival_name, festival_data in festivals.items():
    # Apply filters
    if region_filter != "All" and region_filter not in festival_data["regions"]:
        continue
    
    if search_term and search_term.lower() not in festival_name.lower():
        continue
    
    # Create festival card
    with st.container():
        st.markdown(f"""
        <div class="festival-card">
            <h3>{festival_data.get('telugu_name', festival_name) if st.session_state.language == 'telugu' else festival_name}</h3>
            <p><strong>📅 {festival_data['date']}</strong></p>
            <p>{festival_data.get('telugu_description', festival_data['description']) if st.session_state.language == 'telugu' else festival_data['description']}</p>
            <div>
                {''.join([f'<span class="region-tag {region.lower()}">{region}</span>' for region in festival_data['regions']])}
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        # Details button
        if st.button(f"View Details" if st.session_state.language == "english" else "వివరాలు చూడండి", key=f"details_{festival_name}"):
            show_festival_details(festival_name, festival_data)

Festival Details

def show_festival_details(festival_name, festival_data):st.markdown(f"""{festival_data.get('telugu_name', festival_name) if st.session_state.language == 'telugu' else festival_name}📅 {festival_data['date']}{festival_data.get('telugu_description', festival_data['description']) if st.session_state.language == 'telugu' else festival_data['description']}""", unsafe_allow_html=True)

# Details sections
col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class="detail-section">
        <h4>🔮 Rituals</h4>
    </div>
    """, unsafe_allow_html=True)
    for ritual in festival_data.get('rituals', []):
        st.write(f"• {ritual}")
    
    st.markdown("""
    <div class="detail-section">
        <h4>🍽️ Special Foods</h4>
    </div>
    """, unsafe_allow_html=True)
    for food in festival_data.get('foods', []):
        st.write(f"• {food}")

with col2:
    st.markdown("""
    <div class="detail-section">
        <h4>👗 Traditional Attire</h4>
    </div>
    """, unsafe_allow_html=True)
    for attire in festival_data.get('attire', []):
        st.write(f"• {attire}")
    
    st.markdown("""
    <div class="detail-section">
        <h4>💃 Dances & Events</h4>
    </div>
    """, unsafe_allow_html=True)
    for dance in festival_data.get('dances', []):
        st.write(f"• {dance}")
    
    st.markdown("""
    <div class="detail-section">
        <h4>🎉 Community Events</h4>
    </div>
    """, unsafe_allow_html=True)
    for event in festival_data.get('events', []):
        st.write(f"• {event}")

Submit Tradition Form

def show_submit_form():if st.session_state.language == "telugu":st.title("📝 మీ సంప్రదాయాన్ని సమర్పించండి")st.markdown("మీ స్థానిక పండుగ సంప్రదాయాలను మాతో పంచుకోండి")else:st.title("📝 Submit Your Tradition")st.markdown("Share your local festival traditions with us")

with st.container():
    st.markdown('<div class="submit-form">', unsafe_allow_html=True)
    
    # Form fields
    name = st.text_input(
        "Your Name" if st.session_state.language == "english" else "మీ పేరు",
        key="submit_name"
    )
    
    festivals = get_festival_data()
    festival_options = list(festivals.keys()) + ["Other"]
    selected_festival = st.selectbox(
        "Festival Name" if st.session_state.language == "english" else "పండుగ పేరు",
        festival_options,
        key="submit_festival"
    )
    
    if selected_festival == "Other":
        custom_festival = st.text_input(
            "Enter festival name" if st.session_state.language == "english" else "పండుగ పేరును నమోదు చేయండి",
            key="custom_festival"
        )
    
    description = st.text_area(
        "Local Description (Telugu or English)" if st.session_state.language == "english" else "స్థానిక వివరణ (తెలుగు లేదా ఆంగ్లం)",
        key="submit_description",
        height=150
    )
    
    uploaded_file = st.file_uploader(
        "Upload Photo (Optional)" if st.session_state.language == "english" else "ఫోటో అప్లోడ్ చేయండి (ఐచ్ఛికం)",
        type=['png', 'jpg', 'jpeg'],
        key="submit_photo"
    )
    
    if st.button("Submit Tradition" if st.session_state.language == "english" else "సంప్రదాయాన్ని సమర్పించండి", key="submit_btn"):
        if name and description:
            # Save submission (in a real app, this would go to a database)
            submission = {
                "name": name,
                "festival": custom_festival if selected_festival == "Other" else selected_festival,
                "description": description,
                "timestamp": datetime.now().isoformat(),
                "language": st.session_state.language
            }
            
            # Save to session state for demo
            if "submissions" not in st.session_state:
                st.session_state.submissions = []
            st.session_state.submissions.append(submission)
            
            st.success("Thank you for sharing your tradition!" if st.session_state.language == "english" else "మీ సంప్రదాయాన్ని పంచుకున్నందుకు ధన్యవాదాలు!")
        else:
            st.error("Please fill in all required fields." if st.session_state.language == "english" else "దయచేసి అన్ని అవసరమైన ఫీల్డ్లను నింపండి.")
    
    st.markdown('</div>', unsafe_allow_html=True)

Footer

def show_footer():st.markdown("""FestiveVibe - Celebrating Telugu FestivalsConnect with us and share your traditions🔗📧 contact@festivevibe.com📱 WhatsApp📸 Instagram© 2024 FestiveVibe. All rights reserved. |Celebrating the rich cultural heritage of Andhra Pradesh and Telangana""", unsafe_allow_html=True)

Festival Calendar View

def show_calendar_view():festivals = get_festival_data()

if st.session_state.language == "telugu":
    st.title("📅 పండుగల క్యాలెండర్")
    st.markdown("పండుగలను తేదీ వారీగా చూడండి")
else:
    st.title("📅 Festival Calendar")
    st.markdown("View festivals by date")

# Month and year selection
col1, col2 = st.columns(2)
with col1:
    month = st.selectbox(
        "Month" if st.session_state.language == "english" else "నెల",
        list(range(1, 13)),
        format_func=lambda x: calendar.month_name[x]
    )
with col2:
    year = st.selectbox(
        "Year" if st.session_state.language == "english" else "సంవత్సరం",
        list(range(2024, 2026))
    )

# Create calendar
cal = calendar.monthcalendar(year, month)

# Get festivals for this month
month_festivals = {}
for festival_name, festival_data in festivals.items():
    if any(month_name in festival_data['date'].lower() for month_name in 
           [calendar.month_name[month].lower(), calendar.month_abbr[month].lower()]):
        # Extract day if available
        day = 1  # Default to 1st if no specific day
        if any(char.isdigit() for char in festival_data['date']):
            for word in festival_data['date'].split():
                if word.isdigit() and 1 <= int(word) <= 31:
                    day = int(word)
                    break
        month_festivals[day] = festival_name

# Display calendar
st.markdown("### " + calendar.month_name[month] + " " + str(year))

# Calendar header
days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
header = " | ".join(days)
st.markdown(f"**{header}**")

# Calendar body
for week in cal:
    week_str = ""
    for day in week:
        if day == 0:
            week_str += "   | "
        else:
            festival_name = month_festivals.get(day, "")
            if festival_name:
                week_str += f"**{day}** | "
            else:
                week_str += f"{day} | "
    st.markdown(week_str)

# Show festivals for this month
if month_festivals:
    st.markdown("### " + ("Festivals this month:" if st.session_state.language == "english" else "ఈ నెలలోని పండుగలు:"))
    for day, festival_name in sorted(month_festivals.items()):
        festival_data = festivals[festival_name]
        st.markdown(f"**{day}:** {festival_name} - {festival_data['description']}")

Festival Reminders

def show_reminders():if st.session_state.language == "telugu":st.title("⏰ పండుగ రిమైండర్లు")st.markdown("మీకు ముఖ్యమైన పండుగలకు రిమైండర్లు సెట్ చేయండి")else:st.title("⏰ Festival Reminders")st.markdown("Set reminders for important festivals")

# Add new reminder
with st.expander("Add New Reminder" if st.session_state.language == "english" else "కొత్త రిమైండర్ జోడించండి"):
    festivals = get_festival_data()
    festival_name = st.selectbox(
        "Select Festival" if st.session_state.language == "english" else "పండుగను ఎంచుకోండి",
        list(festivals.keys())
    )
    
    reminder_date = st.date_input(
        "Reminder Date" if st.session_state.language == "english" else "రిమైండర్ తేదీ",
        min_value=datetime.now().date()
    )
    
    reminder_note = st.text_area(
        "Note (Optional)" if st.session_state.language == "english" else "గమనిక (ఐచ్ఛికం)"
    )
    
    if st.button("Add Reminder" if st.session_state.language == "english" else "రిమైండర్ జోడించండి"):
        reminder = {
            "festival": festival_name,
            "date": reminder_date.isoformat(),
            "note": reminder_note,
            "created": datetime.now().isoformat()
        }
        st.session_state.reminders.append(reminder)
        st.success("Reminder added successfully!" if st.session_state.language == "english" else "రిమైండర్ విజయవంతంగా జోడించబడింది!")

# Show existing reminders
if st.session_state.reminders:
    st.markdown("### " + ("Your Reminders:" if st.session_state.language == "english" else "మీ రిమైండర్లు:"))
    for i, reminder in enumerate(st.session_state.reminders):
        with st.container():
            st.markdown(f"""
            <div class="reminder-card">
                <h4>{reminder['festival']}</h4>
                <p><strong>Date:</strong> {reminder['date']}</p>
                {f"<p><strong>Note:</strong> {reminder['note']}</p>" if reminder['note'] else ""}
            </div>
            """, unsafe_allow_html=True)
            
            col1, col2 = st.columns([1, 1])
            with col1:
                if st.button("Delete" if st.session_state.language == "english" else "తొలగించండి", key=f"del_reminder_{i}"):
                    st.session_state.reminders.pop(i)
                    st.rerun()
            with col2:
                if st.button("Edit" if st.session_state.language == "english" else "సవరించండి", key=f"edit_reminder_{i}"):
                    st.info("Edit functionality coming soon!" if st.session_state.language == "english" else "సవరణ ఫంక్షన్ త్వరలో వస్తుంది!")

Photo Gallery

def show_gallery():if st.session_state.language == "telugu":st.title("📸 ఫోటో గ్యాలరీ")st.markdown("పండుగల ఫోటోలను చూడండి మరియు మీ ఫోటోలను పంచుకోండి")else:st.title("📸 Photo Gallery")st.markdown("View festival photos and share yours")

# Upload new photo
with st.expander("Upload Photo" if st.session_state.language == "english" else "ఫోటో అప్లోడ్ చేయండి"):
    uploaded_file = st.file_uploader(
        "Choose a photo" if st.session_state.language == "english" else "ఫోటోను ఎంచుకోండి",
        type=['png', 'jpg', 'jpeg'],
        key="gallery_upload"
    )
    
    photo_title = st.text_input(
        "Photo Title" if st.session_state.language == "english" else "ఫోటో శీర్షిక"
    )
    
    photo_description = st.text_area(
        "Description" if st.session_state.language == "english" else "వివరణ"
    )
    
    if st.button("Upload" if st.session_state.language == "english" else "అప్లోడ్ చేయండి") and uploaded_file and photo_title:
        photo_data = {
            "title": photo_title,
            "description": photo_description,
            "uploaded_by": "User",  # In real app, get from user session
            "upload_date": datetime.now().isoformat(),
            "image": uploaded_file.read()
        }
        st.session_state.gallery_photos.append(photo_data)
        st.success("Photo uploaded successfully!" if st.session_state.language == "english" else "ఫోటో విజయవంతంగా అప్లోడ్ చేయబడింది!")

# Display gallery
if st.session_state.gallery_photos:
    st.markdown("### " + ("Gallery:" if st.session_state.language == "english" else "గ్యాలరీ:"))
    
    # Filter options
    col1, col2 = st.columns(2)
    with col1:
        search_gallery = st.text_input(
            "Search photos" if st.session_state.language == "english" else "ఫోటోలను వెతకండి"
        )
    
    # Display photos
    cols = st.columns(3)
    for i, photo in enumerate(st.session_state.gallery_photos):
        if not search_gallery or search_gallery.lower() in photo['title'].lower():
            with cols[i % 3]:
                st.markdown(f"""
                <div class="gallery-item">
                    <h4>{photo['title']}</h4>
                    <p>{photo['description']}</p>
                    <p><small>By: {photo['uploaded_by']} | {photo['upload_date'][:10]}</small></p>
                </div>
                """, unsafe_allow_html=True)
                
                # Like button (simplified)
                if st.button("❤️ Like" if st.session_state.language == "english" else "❤️ లైక్", key=f"like_{i}"):
                    st.info("Like functionality coming soon!" if st.session_state.language == "english" else "లైక్ ఫంక్షన్ త్వరలో వస్తుంది!")

Festival Quiz

def show_quiz():if st.session_state.language == "telugu":st.title("🧠 పండుగ క్విజ్")st.markdown("మీ తెలుగు పండుగల జ్ఞానాన్ని పరీక్షించండి")else:st.title("🧠 Festival Quiz")st.markdown("Test your knowledge of Telugu festivals")

# Quiz questions
questions = [
    {
        "question": "Which festival marks the Telugu New Year?" if st.session_state.language == "english" else "ఏ పండుగ తెలుగు నూతన సంవత్సరాన్ని సూచిస్తుంది?",
        "options": ["Sankranti", "Ugadi", "Dasara", "Deepavali"] if st.session_state.language == "english" else ["సంక్రాంతి", "ఉగాది", "దసరా", "దీపావళి"],
        "correct": 1
    },
    {
        "question": "Which festival is celebrated with flower arrangements?" if st.session_state.language == "english" else "ఏ పండుగ పుష్పాల అమరికలతో జరుపుకుంటారు?",
        "options": ["Bathukamma", "Bonalu", "Holi", "Karthika Deepam"] if st.session_state.language == "english" else ["బతుకమ్మ", "బోనాలు", "హోళీ", "కార్తిక దీపం"],
        "correct": 0
    },
    {
        "question": "Which state celebrates Bathukamma as a state festival?" if st.session_state.language == "english" else "ఏ రాష్ట్రం బతుకమ్మను రాష్ట్ర పండుగగా జరుపుకుంటుంది?",
        "options": ["Andhra Pradesh", "Telangana", "Both", "Neither"] if st.session_state.language == "english" else ["ఆంధ్రప్రదేశ్", "తెలంగాణ", "రెండూ", "ఏదీ కాదు"],
        "correct": 1
    }
]

if "quiz_answers" not in st.session_state:
    st.session_state.quiz_answers = {}

if "quiz_submitted" not in st.session_state:
    st.session_state.quiz_submitted = False

# Display quiz
if not st.session_state.quiz_submitted:
    st.markdown("### " + ("Answer the following questions:" if st.session_state.language == "english" else "క్రింది ప్రశ్నలకు సమాధానం ఇవ్వండి:"))
    
    for i, q in enumerate(questions):
        st.markdown(f"**{i+1}. {q['question']}**")
        answer = st.radio(
            "Select your answer:" if st.session_state.language == "english" else "మీ సమాధానాన్ని ఎంచుకోండి:",
            q['options'],
            key=f"quiz_q_{i}",
            label_visibility="collapsed"
        )
        st.session_state.quiz_answers[i] = q['options'].index(answer)
    
    if st.button("Submit Quiz" if st.session_state.language == "english" else "క్విజ్ సమర్పించండి"):
        st.session_state.quiz_submitted = True
        st.rerun()

else:
    # Show results
    score = 0
    for i, q in enumerate(questions):
        if st.session_state.quiz_answers.get(i) == q['correct']:
            score += 1
    
    percentage = (score / len(questions)) * 100
    
    st.markdown(f"""
    <div class="quiz-card">
        <h2>Quiz Results!</h2>
        <h3>Score: {score}/{len(questions)} ({percentage:.1f}%)</h3>
        <p>{'Excellent! You know Telugu festivals well!' if st.session_state.language == 'english' else 'అద్భుతం! మీకు తెలుగు పండుగలు బాగా తెలుసు!' if percentage >= 80 else 'Good! Keep learning more!' if st.session_state.language == 'english' else 'మంచిది! మరింత నేర్చుకోండి!' if percentage >= 60 else 'Keep learning about Telugu festivals!' if st.session_state.language == 'english' else 'తెలుగు పండుగల గురించి నేర్చుకోండి!'}</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Save score
    st.session_state.quiz_scores.append({
        "score": score,
        "total": len(questions),
        "percentage": percentage,
        "date": datetime.now().isoformat()
    })
    
    if st.button("Take Quiz Again" if st.session_state.language == "english" else "మళ్ళీ క్విజ్ చేయండి"):
        st.session_state.quiz_submitted = False
        st.session_state.quiz_answers = {}
        st.rerun()

Map of Celebrations

def show_map():if st.session_state.language == "telugu":st.title("🗺️ పండుగల మ్యాప్")st.markdown("ఆంధ్రప్రదేశ్ మరియు తెలంగాణలో పండుగల పంపిణీ")else:st.title("🗺️ Map of Celebrations")st.markdown("Distribution of festivals across Andhra Pradesh and Telangana")

# Sample map data (in real app, this would be more detailed)
map_data = {
    "Andhra Pradesh": {
        "Sankranti": "High",
        "Ugadi": "High", 
        "Dasara": "High",
        "Deepavali": "High",
        "Bathukamma": "Low",
        "Bonalu": "Low"
    },
    "Telangana": {
        "Sankranti": "High",
        "Ugadi": "High",
        "Dasara": "High", 
        "Deepavali": "High",
        "Bathukamma": "High",
        "Bonalu": "High"
    }
}

# Create visualization
st.markdown("### " + ("Festival Distribution by State:" if st.session_state.language == "english" else "రాష్ట్రం వారీగా పండుగల పంపిణీ:"))

# Simple bar chart
festivals = ["Sankranti", "Ugadi", "Dasara", "Deepavali", "Bathukamma", "Bonalu"]
ap_data = [map_data["Andhra Pradesh"].get(f, "Low") for f in festivals]
ts_data = [map_data["Telangana"].get(f, "Low") for f in festivals]

# Convert to numeric for visualization
ap_numeric = [3 if x == "High" else 1 if x == "Medium" else 0.5 for x in ap_data]
ts_numeric = [3 if x == "High" else 1 if x == "Medium" else 0.5 for x in ts_data]

chart_data = {
    "Festival": festivals * 2,
    "State": ["AP"] * len(festivals) + ["Telangana"] * len(festivals),
    "Celebration Level": ap_numeric + ts_numeric
}

df = pd.DataFrame(chart_data)

fig = px.bar(df, x="Festival", y="Celebration Level", color="State",
             title="Festival Celebration Levels by State" if st.session_state.language == "english" else "రాష్ట్రం వారీగా పండుగల జరుపుకునే స్థాయి",
             color_discrete_map={"AP": "#2196F3", "Telangana": "#FF9800"})

st.plotly_chart(fig, use_container_width=True)

# Interactive map info
st.markdown("### " + ("Click on regions to learn more:" if st.session_state.language == "english" else "మరింత తెలుసుకోవడానికి ప్రాంతాలపై క్లిక్ చేయండి:"))

col1, col2 = st.columns(2)
with col1:
    if st.button("Andhra Pradesh" if st.session_state.language == "english" else "ఆంధ్రప్రదేశ్"):
        st.info("Andhra Pradesh celebrates all major festivals with unique regional variations." if st.session_state.language == "english" else "ఆంధ్రప్రదేశ్ అన్ని ముఖ్యమైన పండుగలను ప్రత్యేక ప్రాంతీయ వ్యత్యాసాలతో జరుపుకుంటుంది.")

with col2:
    if st.button("Telangana" if st.session_state.language == "english" else "తెలంగాణ"):
        st.info("Telangana has unique festivals like Bathukamma and Bonalu, along with traditional celebrations." if st.session_state.language == "english" else "తెలంగాణలో బతుకమ్మ, బోనాలు వంటి ప్రత్యేక పండుగలు మరియు సంప్రదాయ పండుగలు ఉన్నాయి.")

Festival Stories/Blog

def show_stories():if st.session_state.language == "telugu":st.title("📖 పండుగ కథలు")st.markdown("పండుగల గురించి కథలు, కవితలు మరియు అనుభవాలను పంచుకోండి")else:st.title("📖 Festival Stories")st.markdown("Share stories, poems, and experiences about festivals")

# Submit new story
with st.expander("Share Your Story" if st.session_state.language == "english" else "మీ కథను పంచుకోండి"):
    story_title = st.text_input(
        "Story Title" if st.session_state.language == "english" else "కథ శీర్షిక"
    )
    
    story_type = st.selectbox(
        "Story Type" if st.session_state.language == "english" else "కథ రకం",
        ["Personal Experience", "Poem", "Article", "Memory"] if st.session_state.language == "english" else ["వ్యక్తిగత అనుభవం", "కవిత", "వ్యాసం", "గుర్తు"]
    )
    
    story_content = st.text_area(
        "Your Story" if st.session_state.language == "english" else "మీ కథ",
        height=200
    )
    
    related_festival = st.selectbox(
        "Related Festival (Optional)" if st.session_state.language == "english" else "సంబంధిత పండుగ (ఐచ్ఛికం)",
        ["None"] + list(get_festival_data().keys())
    )
    
    if st.button("Share Story" if st.session_state.language == "english" else "కథను పంచుకోండి") and story_title and story_content:
        story = {
            "title": story_title,
            "type": story_type,
            "content": story_content,
            "festival": related_festival if related_festival != "None" else None,
            "author": "Anonymous",  # In real app, get from user session
            "date": datetime.now().isoformat(),
            "likes": 0
        }
        st.session_state.user_stories.append(story)
        st.success("Story shared successfully!" if st.session_state.language == "english" else "కథ విజయవంతంగా పంచుకోబడింది!")

# Display stories
if st.session_state.user_stories:
    st.markdown("### " + ("Community Stories:" if st.session_state.language == "english" else "కమ్యూనిటీ కథలు:"))
    
    # Filter options
    col1, col2 = st.columns(2)
    with col1:
        story_type_filter = st.selectbox(
            "Filter by type" if st.session_state.language == "english" else "రకం ద్వారా ఫిల్టర్ చేయండి",
            ["All"] + ["Personal Experience", "Poem", "Article", "Memory"] if st.session_state.language == "english" else ["అన్నీ"] + ["వ్యక్తిగత అనుభవం", "కవిత", "వ్యాసం", "గుర్తు"]
        )
    
    # Display stories
    for story in st.session_state.user_stories:
        if story_type_filter == "All" or story['type'] == story_type_filter:
            with st.container():
                st.markdown(f"""
                <div class="story-card">
                    <h3>{story['title']}</h3>
                    <p><strong>Type:</strong> {story['type']}</p>
                    {f"<p><strong>Festival:</strong> {story['festival']}</p>" if story['festival'] else ""}
                    <p><strong>By:</strong> {story['author']} | <strong>Date:</strong> {story['date'][:10]}</p>
                    <p>{story['content']}</p>
                </div>
                """, unsafe_allow_html=True)
                
                col1, col2 = st.columns([1, 1])
                with col1:
                    if st.button("❤️ Like" if st.session_state.language == "english" else "❤️ లైక్", key=f"like_story_{story['title']}"):
                        story['likes'] += 1
                        st.rerun()
                with col2:
                    st.write(f"Likes: {story['likes']}")

Downloadable Festival Posters

def show_posters():if st.session_state.language == "telugu":st.title("🖼️ పండుగ పోస్టర్లు")st.markdown("పండుగల పోస్టర్లు మరియు గ్రీటింగ్ కార్డ్లను డౌన్లోడ్ చేయండి")else:st.title("🖼️ Festival Posters")st.markdown("Download festival posters and greeting cards")

festivals = get_festival_data()

st.markdown("### " + ("Available Posters:" if st.session_state.language == "english" else "అందుబాటులో ఉన్న పోస్టర్లు:"))

# Sample poster data
posters = [
    {"festival": "Sankranti", "type": "Poster", "size": "A4"},
    {"festival": "Ugadi", "type": "Greeting Card", "size": "A5"},
    {"festival": "Dasara", "type": "Poster", "size": "A4"},
    {"festival": "Deepavali", "type": "Greeting Card", "size": "A5"},
    {"festival": "Bathukamma", "type": "Poster", "size": "A4"}
]

for poster in posters:
    col1, col2, col3, col4 = st.columns([2, 1, 1, 1])
    with col1:
        st.write(f"**{poster['festival']}**")
    with col2:
        st.write(poster['type'])
    with col3:
        st.write(poster['size'])
    with col4:
        if st.button("Download" if st.session_state.language == "english" else "డౌన్లోడ్", key=f"download_{poster['festival']}"):
            st.info("Download functionality coming soon!" if st.session_state.language == "english" else "డౌన్లోడ్ ఫంక్షన్ త్వరలో వస్తుంది!")

Dark/Light Mode Toggle

def dark_mode_toggle():if st.session_state.language == "telugu":st.sidebar.title("🌙 థీమ్")else:st.sidebar.title("🌙 Theme")

if st.sidebar.button("🌙 Dark Mode" if not st.session_state.dark_mode else "☀️ Light Mode"):
    st.session_state.dark_mode = not st.session_state.dark_mode
    st.rerun()

Admin Panel

def show_admin_panel():if st.session_state.language == "telugu":st.title("⚙️ అడ్మిన్ ప్యానెల్")st.markdown("వెబ్సైట్ నిర్వహణ మరియు సంప్రదాయాలను నిర్వహించండి")else:st.title("⚙️ Admin Panel")st.markdown("Manage website and traditions")

# Admin authentication (simplified)
admin_password = st.text_input(
    "Admin Password" if st.session_state.language == "english" else "అడ్మిన్ పాస్‌వర్డ్",
    type="password"
)

if admin_password == "admin123":  # In real app, use proper authentication
    st.session_state.admin_mode = True
    st.success("Admin access granted!" if st.session_state.language == "english" else "అడ్మిన్ యాక్సెస్ మంజూరు!")
    
    # Admin features
    tab1, tab2, tab3 = st.tabs([
        "Submissions" if st.session_state.language == "english" else "సమర్పణలు",
        "Gallery" if st.session_state.language == "english" else "గ్యాలరీ", 
        "Analytics" if st.session_state.language == "english" else "విశ్లేషణలు"
    ])
    
    with tab1:
        st.markdown("### " + ("User Submissions:" if st.session_state.language == "english" else "వినియోగదారు సమర్పణలు:"))
        if st.session_state.submissions:
            for i, submission in enumerate(st.session_state.submissions):
                with st.expander(f"Submission {i+1}: {submission['name']}"):
                    st.write(f"**Festival:** {submission['festival']}")
                    st.write(f"**Description:** {submission['description']}")
                    st.write(f"**Date:** {submission['timestamp'][:10]}")
                    
                    col1, col2 = st.columns(2)
                    with col1:
                        if st.button("Approve" if st.session_state.language == "english" else "అనుమతించండి", key=f"approve_{i}"):
                            st.success("Approved!" if st.session_state.language == "english" else "అనుమతించబడింది!")
                    with col2:
                        if st.button("Reject" if st.session_state.language == "english" else "తిరస్కరించండి", key=f"reject_{i}"):
                            st.session_state.submissions.pop(i)
                            st.rerun()
        else:
            st.info("No submissions yet." if st.session_state.language == "english" else "ఇంకా సమర్పణలు లేవు.")
    
    with tab2:
        st.markdown("### " + ("Gallery Management:" if st.session_state.language == "english" else "గ్యాలరీ నిర్వహణ:"))
        if st.session_state.gallery_photos:
            for i, photo in enumerate(st.session_state.gallery_photos):
                with st.expander(f"Photo {i+1}: {photo['title']}"):
                    st.write(f"**Description:** {photo['description']}")
                    st.write(f"**Uploaded by:** {photo['uploaded_by']}")
                    
                    if st.button("Remove" if st.session_state.language == "english" else "తొలగించండి", key=f"remove_photo_{i}"):
                        st.session_state.gallery_photos.pop(i)
                        st.rerun()
        else:
            st.info("No photos in gallery." if st.session_state.language == "english" else "గ్యాలరీలో ఫోటోలు లేవు.")
    
    with tab3:
        st.markdown("### " + ("Analytics:" if st.session_state.language == "english" else "విశ్లేషణలు:"))
        st.write(f"**Total Submissions:** {len(st.session_state.submissions)}")
        st.write(f"**Total Photos:** {len(st.session_state.gallery_photos)}")
        st.write(f"**Total Stories:** {len(st.session_state.user_stories)}")
        st.write(f"**Total Quiz Attempts:** {len(st.session_state.quiz_scores)}")
        
        if st.session_state.quiz_scores:
            avg_score = sum(score['percentage'] for score in st.session_state.quiz_scores) / len(st.session_state.quiz_scores)
            st.write(f"**Average Quiz Score:** {avg_score:.1f}%")

elif admin_password and admin_password != "admin123":
    st.error("Incorrect password!" if st.session_state.language == "english" else "తప్పు పాస్‌వర్డ్!")

Festival Countdown Timer

def show_countdown():festivals = get_festival_data()

# Get next major festival (simplified logic)
current_date = datetime.now()
upcoming_festivals = []

for festival_name, festival_data in festivals.items():
    # Simple logic to determine if festival is upcoming
    if "January" in festival_data['date'] and current_date.month == 12:
        upcoming_festivals.append((festival_name, "January 2025"))
    elif "March" in festival_data['date'] and current_date.month in [1, 2]:
        upcoming_festivals.append((festival_name, "March 2025"))
    elif "October" in festival_data['date'] and current_date.month in [8, 9]:
        upcoming_festivals.append((festival_name, "October 2025"))

if upcoming_festivals:
    next_festival = upcoming_festivals[0]
    festival_name, target_date = next_festival
    
    # Calculate countdown (simplified)
    target = datetime(2025, 1, 15)  # Example date
    days_left = (target - current_date).days
    
    st.markdown(f"""
    <div class="countdown-timer">
        <h2>🎉 Next Major Festival</h2>
        <h1>{festival_name}</h1>
        <h3>{days_left} days remaining</h3>
        <p>Get ready to celebrate!</p>
    </div>
    """, unsafe_allow_html=True)
else:
    st.info("No upcoming festivals in the next few months." if st.session_state.language == "english" else "తదుపరి కొన్ని నెలల్లో రాబోయే పండుగలు లేవు.")

AI Festival Story Generator

def show_ai_generator():st.title("✨ AI Festival Story Generator")st.markdown("Generate beautiful festival stories instantly")

festival = st.text_input("Enter festival name")

if st.button("Generate Story"):
    if festival:
        festivals = get_festival_data()

        if festival in festivals:
            data = festivals[festival]

            story = f"""

{festival} is one of the most beautiful festivals celebrated in Andhra Pradesh and Telangana.

It is known as "{data.get('telugu_name', festival)}" in Telugu.

This festival is celebrated during {data['date']}.People follow beautiful rituals like {", ".join(data['rituals'][:2])}.Families prepare delicious foods such as {", ".join(data['foods'][:2])}.

On this day, everyone wears {", ".join(data['attire'][:1])} and participates in cultural events and traditional dances.

{festival} brings happiness, unity, and positivity to every home. It reminds us of our rich culture and traditions.

✨ This festival truly fills hearts with joy and togetherness."""

            st.success("Story Generated!")
            st.write(story)

        else:
            st.warning("Festival not found in database. Try a listed festival name.")
    else:
        st.warning("Please enter a festival name.")

Main app

def main():load_css()

# Language toggle in sidebar
st.sidebar.title("🌐 Language")
language_toggle()

# Dark mode toggle
dark_mode_toggle()

# Navigation with new features
st.sidebar.title("📱 Navigation")
page = st.sidebar.radio(
    "Choose a page" if st.session_state.language == "english" else "పేజీని ఎంచుకోండి",
    ["🏠 Home", "🎊 Festival Explorer", "📅 Calendar", "⏰ Reminders", "📸 Gallery", "🧠 Quiz", "🗺️ Map", "📖 Stories", "🖼️ Posters", "⚙️ Admin", "📝 Submit Tradition","🤖 AI Generator"]
)

# Display current language
current_lang = "తెలుగు" if st.session_state.language == "telugu" else "English"
st.sidebar.markdown(f"**Current Language:** {current_lang}")

# Page routing
if page == "🏠 Home":
    show_homepage()
    show_countdown()  # Add countdown to homepage
elif page == "🎊 Festival Explorer":
    show_festival_explorer()
elif page == "📅 Calendar":
    show_calendar_view()
elif page == "⏰ Reminders":
    show_reminders()
elif page == "📸 Gallery":
    show_gallery()
elif page == "🧠 Quiz":
    show_quiz()
elif page == "🗺️ Map":
    show_map()
elif page == "📖 Stories":
    show_stories()
elif page == "🖼️ Posters":
    show_posters()
elif page == "⚙️ Admin":
    show_admin_panel()
elif page == "📝 Submit Tradition":
    show_submit_form()
elif page == "🤖 AI Generator":
    show_ai_generator()

# Show footer
show_footer()

if name == "__main__":
    main()

