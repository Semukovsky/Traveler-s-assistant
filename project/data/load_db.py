from project.data.models import (
    create_tables,
    GermanyEnglish, FrenchEnglish, HindiEnglish, PortugalEnglish, ChinaEnglish, RussianEnglish, EnglishEnglish
)

create_tables()

english_translations = [
    "Hello, how are you?",  # 1
    "Where is the nearest subway station?",  # 2
    "How much does it cost?",  # 3
    "I would like a water, please.",  # 4
    "Excuse me, do you speak English?",  # 5
    "I don’t understand.",  # 6
    "Where is the restroom?",  # 7
    "Can you help me?",  # 8
    "I am a tourist.",  # 9
    "How do I get to the airport?",  # 10
    "I have a reservation.",  # 11
    "Can you repeat that?",  # 12
    "What time is it?",  # 13
    "What do you recommend?",  # 14
    "Thank you very much!"  # 15
]

german_phrases = [
    "Hallo, wie geht es Ihnen?",  # 1
    "Wo ist die nächste U-Bahn-Station?",  # 2
    "Wie viel kostet das?",  # 3
    "Ich hätte gerne ein Wasser, bitte.",  # 4
    "Entschuldigung, sprechen Sie Englisch?",  # 5
    "Ich verstehe nicht.",  # 6
    "Wo ist die Toilette?",  # 7
    "Können Sie mir helfen?",  # 8
    "Ich bin Tourist.",  # 9
    "Wie komme ich zum Flughafen?",  # 10
    "Ich habe eine Reservierung.",  # 11
    "Können Sie das wiederholen?",  # 12
    "Wie spät ist es?",  # 13
    "Was empfehlen Sie?",  # 14
    "Vielen Dank!"  # 15
]

french_phrases = [
    "Bonjour, comment allez-vous?",  # 1
    "Où se trouve la station de métro la plus proche?",  # 2
    "Combien ça coûte?",  # 3
    "Je voudrais une eau, s'il vous plaît.",  # 4
    "Excusez-moi, parlez-vous anglais?",  # 5
    "Je ne comprends pas.",  # 6
    "Où sont les toilettes?",  # 7
    "Pouvez-vous m'aider?",  # 8
    "Je suis touriste.",  # 9
    "Comment aller à l'aéroport?",  # 10
    "J'ai une réservation.",  # 11
    "Pouvez-vous répéter?",  # 12
    "Quelle heure est-il?",  # 13
    "Que recommandez-vous?",  # 14
    "Merci beaucoup!"  # 15
]

hindi_phrases = [
    "नमस्ते, आप कैसे हैं?",  # 1
    "निकटतम मेट्रो स्टेशन कहाँ है?",  # 2
    "यह कितने का है?",  # 3
    "मुझे एक पानी चाहिए, कृपया।",  # 4
    "माफ कीजिए, क्या आप अंग्रेजी बोलते हैं?",  # 5
    "मैं नहीं समझा।",  # 6
    "शौचालय कहाँ है?",  # 7
    "क्या आप मेरी मदद कर सकते हैं?",  # 8
    "मैं एक पर्यटक हूँ।",  # 9
    "हवाई अड्डे पर कैसे जाएं?",  # 10
    "मेरे पास एक आरक्षण है।",  # 11
    "क्या आप इसे दोहरा सकते हैं?",  # 12
    "कितने बजे हैं?",  # 13
    "आप क्या सलाह देते हैं?",  # 14
    "बहुत धन्यवाद!"  # 15
]

portuguese_phrases = [
    "Olá, como você está?",  # 1
    "Onde fica a estação de metrô mais próxima?",  # 2
    "Quanto custa?",  # 3
    "Eu gostaria de uma água, por favor.",  # 4
    "Com licença, você fala inglês?",  # 5
    "Eu não entendo.",  # 6
    "Onde fica o banheiro?",  # 7
    "Você pode me ajudar?",  # 8
    "Eu sou turista.",  # 9
    "Como faço para chegar ao aeroporto?",  # 10
    "Eu tenho uma reserva.",  # 11
    "Você pode repetir isso?",  # 12
    "Que horas são?",  # 13
    "O que você recomenda?",  # 14
    "Muito obrigado!"  # 15
]

chinese_phases = [
    "你好，你好吗？",  # 1
    "最近的地铁站在哪里？",  # 2
    "这个多少钱？",  # 3
    "我想要一瓶水，请。",  # 4
    "请问，你会说英语吗？",  # 5
    "我听不懂。",  # 6
    "洗手间在哪里？",  # 7
    "你能帮我吗？",  # 8
    "我是游客。",  # 9
    "怎么去机场？",  # 10
    "我有一个预订。",  # 11
    "你能重复一下吗？",  # 12
    "现在几点了？",  # 13
    "你推荐什么？",  # 14
    "非常感谢！"  # 15
]

russian_phases = [
    "Здравствуйте, как вы?",  # 1
    "Где находится ближайшая станция метро?",  # 2
    "Сколько это стоит?",  # 3
    "Я бы хотел воду, пожалуйста.",  # 4
    "Извините, вы говорите по-английски?",  # 5
    "Я не понимаю.",  # 6
    "Где находится туалет?",  # 7
    "Вы можете мне помочь?",  # 8
    "Я турист.",  # 9
    "Как добраться до аэропорта?",  # 10
    "У меня есть бронь.",  # 11
    "Вы можете повторить?",  # 12
    "Который час?",  # 13
    "Что вы порекомендуете?",  # 14
    "Большое спасибо!"  # 15
]

english_phases = [
    "Hello, how are you?",  # 1
    "Where is the nearest subway station?",  # 2
    "How much does it cost?",  # 3
    "I would like a water, please.",  # 4
    "Excuse me, do you speak English?",  # 5
    "I don’t understand.",  # 6
    "Where is the restroom?",  # 7
    "Can you help me?",  # 8
    "I am a tourist.",  # 9
    "How do I get to the airport?",  # 10
    "I have a reservation.",  # 11
    "Can you repeat that?",  # 12
    "What time is it?",  # 13
    "What do you recommend?",  # 14
    "Thank you very much!"  # 15
]

# Работа с немецким языком
for ger, eng in zip(german_phrases, english_translations):
    row = GermanyEnglish(phrase=ger, translate=eng)
    row.save()

# Работа с английским языком
for fre, eng in zip(french_phrases, english_translations):
    row = FrenchEnglish(phrase=fre, translate=eng)
    row.save()

# Работа с хинди языком
for hin, eng in zip(hindi_phrases, english_translations):
    row = HindiEnglish(phrase=hin, translate=eng)
    row.save()

# Работа с португальским языком
for por, eng in zip(portuguese_phrases, english_translations):
    row = PortugalEnglish(phrase=por, translate=eng)
    row.save()

# Работа с китайским языком
for chi, eng in zip(chinese_phases, english_translations):
    row = ChinaEnglish(phrase=chi, translate=eng)
    row.save()

# Работа с русским языком
for rus, eng in zip(russian_phases, english_translations):
    row = RussianEnglish(phrase=rus, translate=eng)
    row.save()

# Работа с английским языком
for eng in english_translations:
    row = EnglishEnglish(phrase=eng, translate=eng)
    row.save()
