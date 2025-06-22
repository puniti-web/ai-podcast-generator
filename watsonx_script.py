from ibm_watson_machine_learning.foundation_models import Model

credentials = {
    "url": "https://us-south.ml.cloud.ibm.com",
    "apikey": "E0z5NhfKj_WATYWW9FibuZ7sU40Srde0xrM6JoEsacp3"  # Replace with your actual API key
}

project_id = "7c64d830-4d30-4727-979e-37c20bb0e8e8"  # Replace with your actual project ID

parameters = {
    "decoding_method": "greedy",
    "max_new_tokens": 200,
    "min_new_tokens": 20,
    "temperature": 0.7
}

model = Model(
    model_id="ibm/granite-13b-instruct-v2",  # ✅ Supported and stable
    params=parameters,
    credentials=credentials,
    project_id=project_id
)

def generate_script(topic):
    prompt = f"Write a podcast script introduction on the topic: {topic}"
    response = model.generate_text(prompt)
    return response  # Just return the full string

