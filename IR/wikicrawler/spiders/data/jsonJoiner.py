import json
import glob

def concatenate_json_files(directory, destination):
    data = []
    files = glob.glob(f"{directory}/*.json")

    for file in files:
        with open(file, 'r', encoding='utf8') as f:
            data.extend(json.load(f))

    #Remove duplicates
    data = {item['Name']: item for item in data}.values()

    with open(destination, 'w', encoding='utf8') as f:
        json.dump(list(data), f, indent=4)

# Call the function with the directory containing your JSON files
concatenate_json_files('C:\\Users\\EndUser\\Documents\\scrapyTUTS\\wikiCrawler\\wikicrawler\\wikicrawler\\spiders\\data',
                       'C:\\Users\\EndUser\\Documents\\scrapyTUTS\\wikiCrawler\\wikicrawler\\wikicrawler\\spiders\\data\\combined_data_raw.json')
