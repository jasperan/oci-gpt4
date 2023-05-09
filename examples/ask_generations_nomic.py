# This file uses gpt4all-lora-quantized.bin model
# it's based on Alpaca-LoRA  https://github.com/tloen/alpaca-lora
# model should automatically download.

# needs 'nomic' as a pip dependency to be installed
# for more info on how to LoRA works: https://arxiv.org/pdf/2106.09685.pdf

from nomic.gpt4all import GPT4All
m = GPT4All()
m.open()
print(m.prompt('write me a story about a lonely computer'))
