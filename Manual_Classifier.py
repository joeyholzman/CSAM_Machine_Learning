import json
import random

def update_classification(json_data, tokenized_json_file_path):
    classified_count = 0  # Initialize count for classified tweets
    
    # Shuffle the list of tweets randomly
    random.shuffle(json_data)
    
    for entry in json_data:
        if "Classification" not in entry:
            print("---------------------------------------")
            print("Tweet Text:", entry["TweetText"])
            classification = input("Enter the classification (0 or 1, or 'q' to quit): ")

            if classification.lower() == 'q':
                break

            while classification not in ['0', '1']:
                print("Invalid input. Please enter 0 or 1.")
                classification = input("Enter the classification (0 or 1, or 'q' to quit): ")

            entry["Classification"] = int(classification)
            classified_count += 1  # Increment count for classified tweets
            
            # Write the updated data back to the JSON file after every classification
            with open(tokenized_json_file_path, 'w', encoding='utf-8') as f:
                json.dump(json_data, f, indent=6)

    return classified_count  # Return the count of classified tweets

# Read existing JSON file with specified encoding and handle errors
tokenized_json_file_path = './Tweet_Datasets/Tokenized_Tweets/Tokenized_Tweets.json'
with open(tokenized_json_file_path, 'r', encoding='utf-8', errors='ignore') as f:
    existing_data = json.load(f)

# Update the classification for each tokenized tweet
classified_tweets_count = update_classification(existing_data, tokenized_json_file_path)

print(f"Classification updated successfully. Total classified tweets in {tokenized_json_file_path}: {classified_tweets_count}")
