from pygpt4all.models.gpt4all import GPT4All
model = GPT4All('./models/ggml-gpt4all-l13b-snoozy.bin')

prompt_list = ['What are the french presidents in order?', 'Give me 10 ideas to build a new Python app', 'Can you help me generate a fibonacci sequence in Python?']


while True:
    try:
        print(f"AI:", end='')
        for x in prompt_list:
            for token in model.generate(x):
                print(f"{token}", end='', flush=True)
        print('\n')
    except KeyboardInterrupt:
        break
