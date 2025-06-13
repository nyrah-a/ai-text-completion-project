!pip install -U transformers

from transformers import pipeline

# Load the GPT-2 model from Hugging Face
generator = pipeline("text-generation", model="gpt2")

def generate_text(prompt, max_length=100, temperature=0.7):
    response = generator(
        prompt,
        max_length=max_length,
        temperature=temperature,
        num_return_sequences=1,
        do_sample=True,
        top_k=50,
        top_p=0.95
    )
    return response[0]['generated_text']
  from transformers import pipeline

generator = pipeline("text-generation", model="openai-community/gpt2")

def generate_text(prompt, max_new_tokens=100, temperature=0.7):
    try:
        output = generator(
            prompt,
            max_new_tokens=max_new_tokens,
            temperature=temperature,
            num_return_sequences=1,
            do_sample=True,
            top_k=50,
            top_p=0.95,
            pad_token_id=50256  # Avoid warning
        )
        return output[0]['generated_text']
    except Exception as e:
        return f"⚠️ Error: {e}"

while True:
    prompt = input("Enter a prompt (or type 'exit' to quit): ")
    if prompt.lower() == "exit":
        break
    if not prompt.strip():
        print("⚠️ Empty prompt. Try again.\n")
        continue
    
    output = generate_text(prompt)
    print("\n📝 Generated Response:\n", output, "\n")
