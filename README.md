# oci-gpt4
Learn to use a GPT4 model on OCI

# Create compute instance
First, we will need a compute instance (with an OCI Marketplace image). This image will make our lives better when using generative deco  Refer to [this documentation](files/create_compute_instance.md) for detailed instructions on how to create an OCI Compute Instance. 

# Install dependencies

conda create -n "gen_ai" python=3.10
conda activate -n "gen_ai"
pip install nomic
pip install pygpt4all


# Available models

- https://gpt4all.io/models/ggml-gpt4all-j-v1.3-groovy.bin (default) (md5sum 81a09a0ddf89690372fc296ff7f625af) Current best commercially licensable model based on GPT-J and trained by Nomic AI on the latest curated GPT4All dataset.
- https://gpt4all.io/models/ggml-gpt4all-l13b-snoozy.bin (md5sum 91f886b68fbce697e9a3cd501951e455) Current best non-commercially licensable model based on Llama 13b and trained by Nomic AI on the latest curated GPT4All dataset.
- https://gpt4all.io/models/ggml-gpt4all-j-v1.2-jazzy.bin (md5sum 879344aaa9d62fdccbda0be7a09e7976) An commercially licensable model based on GPT-J and trained by Nomic AI on the v2 GPT4All dataset.
- https://gpt4all.io/models/ggml-gpt4all-j-v1.1-breezy.bin (md5sum 61d48a82cb188cceb14ebb8082bfec37) An commercially licensable model based on GPT-J and trained by Nomic AI on the v1 GPT4All dataset.
- https://gpt4all.io/models/ggml-gpt4all-j.bin (md5sum 5b5a3f9b858d33b29b52b89692415595) An commercially licensable model based on GPT-J and trained by Nomic AI on the v0 GPT4All dataset.
- https://gpt4all.io/models/ggml-vicuna-7b-1.1-q4_2.bin (md5sum 29119f8fa11712704c6b22ac5ab792ea) An non-commercially licensable model based on Llama 7b and trained by teams from UC Berkeley, CMU, Stanford, MBZUAI, and UC San Diego.
- https://gpt4all.io/models/ggml-vicuna-13b-1.1-q4_2.bin (md5sum 95999b7b0699e2070af63bf5d34101a8) An non-commercially licensable model based on Llama 13b and trained by teams from UC Berkeley, CMU, Stanford, MBZUAI, and UC San Diego.
- https://gpt4all.io/models/ggml-wizardLM-7B.q4_2.bin (md5sum 99e6d129745a3f1fb1121abed747b05a) An non-commercially licensable model based on Llama 7b and trained by Microsoft and Peking University.
- https://gpt4all.io/models/ggml-stable-vicuna-13B.q4_2.bin (md5sum 6cb4ee297537c9133bddab9692879de0) An non-commercially licensable model based on Llama 13b and RLHF trained by Stable AI.


# pygpt4all

## Run or create new Python file

```bash
curl -O  https://gpt4all.io/models/ggml-gpt4all-l13b-snoozy.bin
```

## Now, download the repository

```bash
git clone https://github.com/jasperan/oci-gpt4
```


```python
from nomic.gpt4all import GPT4All
m = GPT4All()
m.open()
m.prompt('write me a story about a lonely computer')
```
# nomic-ai

## Running a GPT with `pygpt4all` (Advanced)
```python
from pygpt4all.models.gpt4all import GPT4All

def new_text_callback(text):
print(text, end="")

model = GPT4All('./models/ggml-gpt4all-l13b-snoozy.bin')
model.generate("Once upon a time, ", n_predict=55, new_text_callback=new_text_callback)
```
This method is more advanced because it requires you to manually download whichever model checkpoint you want to use, but still achievable.

For more information on how to download or get these `.bin` files, refer to the [full lab guide](files/guide.md).