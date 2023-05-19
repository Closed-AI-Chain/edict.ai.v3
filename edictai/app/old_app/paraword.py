import spacy
from rake_nltk import Rake
nlp = spacy.load('en_core_web_sm')
paragraph = "Vodafone Idea has asked the Indian government for more time to pay its licence fee dues for the March quarter, proposing to pay just 10% now and the balance of 90% over the next four months. The firm said it was struggling financially, but insisted that it had paid all statutory dues until the end of the previous quarter. The request for extra time follows the government's conversion of some of Vi's accrued interest towards AGRs into equity earlier this year."
for sentence in nlp(paragraph).sents:
    # calculate the sentiment score for the sentence using TextBlob
    r = Rake(min_length=3)

# Extract keywords from the text
    r.extract_keywords_from_text(sentence.text)

# Get the top 5 ranked keywords with their corresponding scores
    top_keywords = r.get_ranked_phrases_with_scores()[:3]

    print(sentence,top_keywords)
