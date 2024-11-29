# load model (~2 min)
def llama_load():
    start = time.time()
    model_id = "meta-llama/Meta-Llama-3-8B-Instruct"

    tokenizer = AutoTokenizer.from_pretrained(model_id, use_auth_token=True)
    model = AutoModelForCausalLM.from_pretrained(
        model_id,
        torch_dtype=torch.bfloat16,
        device_map="auto",
    )
    end = time.time()
    print(f"LLAMA 3 loaded in {end - start} seconds.")
    return tokenizer, model

def llama_query(system_info, prompt, tokenizer, model):

    start = time.time()

    messages = [
        {"role": "system", "content": system_info},
        {"role": "user", "content": prompt},
    ]

    input_ids = tokenizer.apply_chat_template(
        messages,
        add_generation_prompt=True,
        return_tensors="pt"
    ).to(model.device)

    terminators = [
        tokenizer.eos_token_id,
        tokenizer.convert_tokens_to_ids("<|eot_id|>")
    ]

    outputs = model.generate(
        input_ids,
        max_new_tokens=256,
        eos_token_id=terminators,
        do_sample=True,
        temperature=0.6,
        top_p=0.9,
    )
    response = outputs[0][input_ids.shape[-1]:]

    end = time.time()
    print(f"LLAMA 3 queried in {end - start} seconds.")
    return tokenizer.decode(response, skip_special_tokens=True)

llama_tokenizer, llama_model = llama_load()