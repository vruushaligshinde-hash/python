# राशियों की सूची
rashis = [
    "मेष", "वृषभ", "मिथुन", "कर्क", "सिंह", "कन्या",
    "तुला", "वृश्चिक", "धनु", "मकर", "कुंभ", "मीन"
]

# Day 1 predictions
house_predictions_day1 = {
    1: "बहुत अच्छा दिन, लाभ मिलेगा",
    2: "खर्च बढ़ सकते हैं",
    3: "साहस बढ़ेगा",
    4: "तनाव रहेगा",
    5: "मन अशांत रहेगा",
    6: "सफलता मिलेगी",
    7: "रिश्ते मजबूत होंगे",
    8: "सावधान रहें",
    9: "भाग्य साथ देगा",
    10: "करियर में सफलता",
    11: "लाभ होगा",
    12: "खर्च और तनाव"
}

# Day 2 predictions
house_predictions_day2 = {
    1: "अच्छा दिन, लेकिन धैर्य रखें",
    2: "आर्थिक चिंता हो सकती है",
    3: "नए प्रयास सफल होंगे",
    4: "भावनात्मक तनाव संभव",
    5: "ध्यान भटक सकता है",
    6: "प्रतियोगिता में सफलता",
    7: "संबंधों में सुधार",
    8: "स्वास्थ्य का ध्यान रखें",
    9: "यात्रा के योग बनेंगे",
    10: "काम में प्रगति होगी",
    11: "इच्छाएं पूरी होंगी",
    12: "अनावश्यक खर्च से बचें"
}

# Day 1 extras
extras_day1 = {
    "मेष": {"color": "लाल", "number": 9, "remedy": "हनुमान जी की पूजा करें"},
    "वृषभ": {"color": "हरा", "number": 6, "remedy": "शिव जी को जल चढ़ाएं"},
    "मिथुन": {"color": "पीला", "number": 5, "remedy": "गणेश जी की पूजा करें"},
    "कर्क": {"color": "सफेद", "number": 2, "remedy": "दूध का दान करें"},
    "सिंह": {"color": "नारंगी", "number": 1, "remedy": "सूर्य को जल दें"},
    "कन्या": {"color": "हरा", "number": 5, "remedy": "तुलसी पूजा करें"},
    "तुला": {"color": "गुलाबी", "number": 6, "remedy": "लक्ष्मी पूजा करें"},
    "वृश्चिक": {"color": "लाल", "number": 9, "remedy": "हनुमान चालीसा पढ़ें"},
    "धनु": {"color": "पीला", "number": 3, "remedy": "गुरु पूजा करें"},
    "मकर": {"color": "नीला", "number": 8, "remedy": "शनि पूजा करें"},
    "कुंभ": {"color": "नीला", "number": 8, "remedy": "दान करें"},
    "मीन": {"color": "पीला", "number": 7, "remedy": "विष्णु पूजा करें"}
}

# Day 2 extras (slightly different)
extras_day2 = {
    "मेष": {"color": "गुलाबी", "number": 1, "remedy": "हनुमान चालीसा पढ़ें"},
    "वृषभ": {"color": "नीला", "number": 8, "remedy": "शिव मंत्र जप करें"},
    "मिथुन": {"color": "हरा", "number": 3, "remedy": "गणेश जी को दूर्वा चढ़ाएं"},
    "कर्क": {"color": "सफेद", "number": 7, "remedy": "चावल का दान करें"},
    "सिंह": {"color": "लाल", "number": 9, "remedy": "सूर्य को जल दें"},
    "कन्या": {"color": "पीला", "number": 5, "remedy": "विष्णु पूजा करें"},
    "तुला": {"color": "सफेद", "number": 2, "remedy": "लक्ष्मी मंत्र जप करें"},
    "वृश्चिक": {"color": "नारंगी", "number": 1, "remedy": "हनुमान जी को प्रसाद चढ़ाएं"},
    "धनु": {"color": "पीला", "number": 6, "remedy": "गुरु का आशीर्वाद लें"},
    "मकर": {"color": "काला", "number": 8, "remedy": "शनि दान करें"},
    "कुंभ": {"color": "नीला", "number": 4, "remedy": "गरीबों की मदद करें"},
    "मीन": {"color": "हरा", "number": 3, "remedy": "भगवान विष्णु का नाम लें"}
}

# Input Moon sign
print("चंद्रमा की राशि चुनें:")
for i, r in enumerate(rashis):
    print(i+1, r)

moon_choice = int(input("नंबर डालें (1-12): "))
moon_index = moon_choice - 1

# Input Day
day_type = int(input("Day 1 या Day 2? (1/2): "))

print("\n🌙 आज का राशिफल:\n")

for rashi in rashis:
    rashi_index = rashis.index(rashi)

    house = (moon_index - rashi_index) % 12 + 1

    if day_type == 1:
        prediction = house_predictions_day1[house]
        extra = extras_day1[rashi]
    else:
        prediction = house_predictions_day2[house]
        extra = extras_day2[rashi]

    print("🔮 राशि:", rashi)
    print("🏠 भाव:", house)
    print("✨ भविष्य:", prediction)
    print("🎨 शुभ रंग:", extra["color"])
    print("🔢 शुभ अंक:", extra["number"])
    print("🪔 उपाय:", extra["remedy"])
    print("----------------------")