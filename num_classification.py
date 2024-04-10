import json

def get_classification_counts(tokenized_json_file_path):
    counts = {'0': 0, '1': 0}

    # Read existing JSON file with specified encoding and handle errors
    with open(tokenized_json_file_path, 'r', encoding='utf-8', errors='ignore') as f:
        json_data = json.load(f)

    for entry in json_data:
        if "Classification" in entry:
            classification = entry["Classification"]
            counts[str(classification)] += 1

    return counts

if __name__ == "__main__":
    tokenized_json_file_path = './Tweet_Datasets/Classified_Tweets/Classified_Tweets.json'
    classification_counts = get_classification_counts(tokenized_json_file_path)
    print("Classification Counts:")
    print("0:", classification_counts['0'])
    print("1:", classification_counts['1'])
