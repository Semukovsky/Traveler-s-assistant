from project.data.models import RussianEnglish

dct = {
    "russian": RussianEnglish
}

input_language = dct["russian"]
output_language = "english"


"""
SELECT DISTINCT germany_english.phrase, french_english.phrase 
FROM germany_english
FULL JOIN french_english 
ON germany_english.translate = french_english.translate;
"""

"""
query = Tweet.select().join(User).where(User.username == 'huey')
for tweet in query:
    print(tweet.content)

"""