import json

def count_null_image_serialized(json_file):
    with open(json_file, 'r', encoding='utf-8') as file:
        data = json.load(file)
        
    count = 0
    for record in data:
        if record.get("Image_Serialized") is None:
            count += 1
    
    return count

if __name__ == "__main__":
    json_file_path = "./NobelPrizeWinners.json"  # Replace this with the path to your JSON file
    null_count = count_null_image_serialized(json_file_path)
    print("Number of records with 'Image_Serialized' field as null:", null_count)
