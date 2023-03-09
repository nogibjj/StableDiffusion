import os
import openai

openai.api_key = os.getenv('OPENAI_API_KEY')

# input_sentence = "a shirtless young man looking at the camera, a polaroid photo by Oliver Sin, dribble, mannerism, handsome, angelic photograph, shiny eyes."


def send_message(input_sentence):
    prompt = f"this sentence: {input_sentence} is generate by stable diffusion replicate.models.get('methexis-inc/img2prompt') using a picture, I need you to rewrite it in 2-3 sentences without space between sentences, with more details use for text generate pic model. generate result only"
    message_log = [{"role": "user","content": prompt}]
    response = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = message_log,
        max_tokens=300,
        stop=None,
        temperature=0.7,
    )
    # Find the first response from the chatbot that has text in it (some responses may not have text)
    for choice in response.choices:
        if "text" in choice:
            return choice.text
    # If no response with text is found, return the first response's content (which may be empty)
    return response.choices[0].message.content



# if __name__ == "__main__":
#     print(send_message(input_sentence))