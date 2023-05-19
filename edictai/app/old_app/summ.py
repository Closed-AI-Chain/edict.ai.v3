

# # pip install sentence-pience
# from transformers import T5Tokenizer, T5ForConditionalGeneration
# from scraper import scraped_content



# model_name = "t5-small"
# tokenizer = T5Tokenizer.from_pretrained(model_name)
# model = T5ForConditionalGeneration.from_pretrained(model_name)



# def summariser():
#     text = scraped_content
#     # inputs = tokenizer.encode("summarize: " + text, return_tensors="pt", max_length=1000, truncation=True)
#     # summary_ids = model.generate(inputs, max_length=300, min_length=200, length_penalty=2.0, num_beams=4)
#     # summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)
    
    
#     return summary


# from transformers import XLNetTokenizer, XLNetForSequenceClassification, pipeline

# def summariser(text):
#     # Load XLNet tokenizer and model
#     tokenizer = XLNetTokenizer.from_pretrained('xlnet-large-cased')
#     model = XLNetForSequenceClassification.from_pretrained('xlnet-large-cased')

#     # Define summarization pipeline
#     summarizer = pipeline('summarization', model=model, tokenizer=tokenizer)

#     # Generate summary
#     summary = summarizer(text, min_length=60, max_length=200, do_sample=False)

#     # Return summarized text
#     return summary[0]['summary_text']



# from transformers import PegasusForConditionalGeneration
# from transformers import PegasusTokenizer
# from transformers import pipeline
# from transformers import AutoTokenizer


# # Pick model
# model_name = "google/pegasus-xsum"

# cache_dir = "model"

# # Load pretrained tokenizer
# pegasus_tokenizer = tokenizer = AutoTokenizer.from_pretrained(model_name,cache_dir=cache_dir)
# tokenizer.save_pretrained(cache_dir)

# 
# # # Define PEGASUS model
# # # pegasus_model = PegasusForConditionalGeneration.from_pretrained(model_name)
# # # pegasus_tokenizer.save_pretrained("local_pegasus-xsum_tokenizer")
# # # pegasus_model.save_pretrained("local_pegasus-xsum_tokenizer_model")
# # # Create tokens
# # # tokens = pegasus_tokenizer(example_text, truncation=True, padding="longest", return_tensors="pt")
# # # # Summarize text
# # # encoded_summary = pegasus_model.generate(**tokens)

# # # Decode summarized text
# # # decoded_summary = pegasus_tokenizer.decode(
# # #       encoded_summary[0],
# # #       skip_special_tokens=True
# # # )

# # # Define summarization pipeline 
# summarizer = pipeline(
#     "summarization", 
#     model=model_name, 
#     tokenizer=pegasus_tokenizer, 
#     framework="pt"
# )

# # Create summary 
# example_text = '''Since Musk purchased Twitter - for $44 billion - last year he has fired over 6,000 employees and left many of the rest fearing a similar fate.Twitter boss Elon Musk - who has made firing over three-fourth of the company's previously 8,000-strong workforce since buying it in October last year - was called out Thursday for reportedly asking senior managers to recommend their best employees for promotion, and then firing the former and replacing them with the latter as part of a 'cost-cutting drive', British publication iNews said.The publication quoted a former staffer as saying, "Managers were recently told to provide a list of people who ought to be promotedâ€¦ little did they realise they were signing their own death warrant: many of those managers were subsequently fired and replaced by those theyâ€™d recommended, as part of a cost-cutting drive." Note: The original report is behind a paywall.Hindustan Times cannot independently confirm the figure but reports indicate at least 50 ex-senior managers were so fired; this was reportedly after Musk claimed to be 'done' with layoffs. According to reports one of those sacked in this manner was Esther Crawford, a senior executive pictured sleeping on the floor at the company's headquarters in solidarity with demands placed on her team.Musk's later underhanded move has been criticised; one Twitter user stressed Musk could not 'fire (his) way out of $44 billion of debt', another called the Tesla Inc. and SpaceX founder 'the world's biggest baby' and a third said Musk's actions made it 'clear the goal is the dissolution of Twitterâ€¦'Since Musk purchased Twitter - for $44 billion - last year he has fired over 6,000 employees and left many of the rest fearing a similar fate. The iNews report also pointed out many of those who remain (for now) may want to leave too but cannot because their work permits are linked to employment.The report also alleged employees were being given unrealistic goals. "Staff are expected to make unrealistic numbers of changes to key features on the platform in next-to-no time, all while lacking the support of colleagues who just a few months ago had been on the platform," it said.Sacked employees have voiced their frustration on social media and some have even taken on Musk on his own platform. This week Haraldur Thorleifsson was forced to call the billionaire out online after nine days of limbo after finding himself locked out of his computer - was he fired or not? (ALSO READ: â€˜Misunderstandingâ€¦â€™: Elon Musk apologizes after taunting sacked Twitter employee)He got his answer after a surreal Twitter exchange with Musk, who proceeded to quiz him about his work, question his disability and need for accommodations - Thorleifsson has muscular dystrophy and uses a wheelchar. Musk also claimed Thorleifsson was 'wealthy' and had only confronted him 'in public was to get a big payout'. Thorleifsson said he was fired during the exchange.Follow the latest breaking news and developments from India and around the world with Hindustan Times' newsdesk. From politics and policies to the economy and the environment, from local issues to national events and global affairs, we've got you covered.
# ...view detailAmazon Plus Size Store sale: T-shirts for women are available at up to 69% offAmazon sale: Revamp men's wardrobe with finest additions, get up to 66% offAmazon Plus Size Store sale: Get leggings, track pants at up to 77% off '''
# summary = summariser(example_text)
# # summary = summariser(example_text)
# print(summary)