import openai
import os



import requests
import json


from django.conf import settings




def generate_recipe(ingredients):
    prompt = f"Create a food recipe using the following ingredients {', '.join(ingredients)} and only those ingredients. Keep The Titile on the first line"

    
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=250  
    )

    
    
    return response.choices[0].text.strip()


def getRecipeImageLink(prompt):

    title = os.linesep.join([s for s in prompt.splitlines() if s])

    title = title.strip().splitlines()[0]

    



    url = f"https://www.googleapis.com/customsearch/v1?q={title}&num=1&start=1&imgSize=huge&searchType=image&key={key}&cx={cse_id}"



    response = requests.get(url)
    response.raise_for_status()

    search_results = response.json()


    search_results = response.json()
    image_url = search_results['items'][0]['link']
    context_url = search_results["items"][0]["image"]["contextLink"] 
    



    return title, image_url, context_url













