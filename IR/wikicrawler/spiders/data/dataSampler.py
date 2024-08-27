import json

data = list()

with open("C:\\Users\\EndUser\\Documents\\scrapyTUTS\\wikiCrawler\\wikicrawler\\wikicrawler\\spiders\\data\\combined_data_raw.json", 'r', encoding='utf8') as f:
    data.extend(json.load(f))

sampled_data = data[110:160]

with open("C:\\Users\\EndUser\\Documents\\scrapyTUTS\\wikiCrawler\\wikicrawler\\wikicrawler\\spiders\\data\\sampled_data.json", 'w', encoding='utf8') as f:
    json.dump(list(sampled_data), f, indent=4)
