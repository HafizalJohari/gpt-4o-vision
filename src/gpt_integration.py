import openai
import os
import torch
from dotenv import load_dotenv
import time

# Load environment variables
load_dotenv()

# Set OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_description(features_folder, max_tokens=50, retry_delay=10, batch_size=1):
    descriptions = []
    feature_files = os.listdir(features_folder)

    for i in range(0, len(feature_files), batch_size):
        batch = feature_files[i:i + batch_size]

        for feature_file in batch:
            features = torch.load(os.path.join(features_folder, feature_file))
            prompt = f"Describe the following video frame features: {features.tolist()}"

            while True:
                try:
                    response = openai.ChatCompletion.create(
                        model="gpt-4o",
                        messages=[
                            {"role": "system", "content": "You are an assistant that provides detailed descriptions of video frame features."},
                            {"role": "user", "content": prompt}
                        ],
                        max_tokens=max_tokens
                    )
                    descriptions.append(response['choices'][0]['message']['content'].strip())
                    break
                except openai.error.RateLimitError as e:
                    print(f"Rate limit reached: {e}. Retrying in {retry_delay} seconds...")
                    time.sleep(retry_delay)
                except openai.error.OpenAIError as e:
                    print(f"An error occurred: {e}.")
                    break

        # Introduce a delay between batches to avoid hitting rate limits
        print(f"Processed batch {i // batch_size + 1}/{len(feature_files) // batch_size + 1}. Waiting for {retry_delay} seconds before next batch...")
        time.sleep(retry_delay)

    return descriptions

if __name__ == "__main__":
    # Adjust the max_tokens value and retry_delay as needed
    descriptions = generate_description('data/processed_features', max_tokens=50, retry_delay=10, batch_size=1)
    for desc in descriptions:
        print(desc)

