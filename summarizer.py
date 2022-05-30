import os
import openai
from dotenv import load_dotenv
from json import dumps, loads

from transformers import GPT2Model, GPT2Config, GPT2Tokenizer


# ! SETUP

# AI setup and settings
load_dotenv('.env')
api_key = os.environ.get('OPENAI-API-KEY')
openai.api_key = api_key

# config tokenizer
configuration = GPT2Config()
model = GPT2Model(configuration)
tokenizer = GPT2Tokenizer.from_pretrained('gpt2')

# ? ENTER FILE NAMES HERE
# dont do full path, just the names
# files
input_text_file = "penetrance.txt"
output_summary_file = "penetrance_summary.txt"

# pull from text file
with open(f"article-txt/{input_text_file}", 'r') as f:
    prompt_full = f.read()

# set block length
block_length = 3900

# slice and output setup
x = 0
y = block_length
count = 1
all_responses = ''

# modifiers
modifier2 = "Summarize this: \n"
modifier3 = "Summarize this in detail: \n"
modifier4 = "Summarize this briefly: \n"
modifier5 = "Pull out the most important points: \n"

# ? Change temp here
# temp
temperature = 0


# ! BREAK UP INTO BLOCKS TO PASS TO GPT-3, PASS THEM
while y <= len(prompt_full):

    # create a block
    prompt = prompt_full[x:y]

    # return the number of tokens
    tokens = len(tokenizer(prompt)["attention_mask"])
    
    # reduce the number of tokens if necessary
    while tokens > 1024:

        overage = tokens - 1024

        y = y - (overage * 4)
        prompt = prompt_full[x:y]
        tokens = len(tokenizer(prompt)["attention_mask"])

    # once the number of tokens for the block is in the acceptable range, pass it thorugh to GPT-3

    # get a response from the AI
    response = openai.Completion.create(
    engine="text-davinci-002",
    prompt = f'{modifier2} {prompt}',
    temperature = temperature,
    max_tokens = 1000,
    top_p=1,
    frequency_penalty=1,
    presence_penalty=1
    )

    # add the response to the output
    all_responses += f"{response.choices[0].text}"

    # move to the next block
    x = y
    y = y + block_length
    
    print(f"Block {count} indexed")
    count = count + 1

# ! AUTO FILE NAMING
# counter for file naming (stored in JSON file)
if os.path.exists("counter.json"):
    counter_int = int(loads(open("counter.json", "r").read()))
else:
    counter_int=1
print(f"Counter: {counter_int}")

# ! WRITE FILE
with open(f"article-summaries/{output_summary_file}_{counter_int}", 'w') as f:
    # call write function
    f.write(all_responses)

# if we write a file, update the counter for naming of the next file
counter_int += 1
with open("counter.json", "w") as f:
    f.write(dumps(str(counter_int)))