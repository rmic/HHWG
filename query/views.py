from pprint import pprint

from django.shortcuts import render
import openai
# Create your views here.

def my_view(request):
    if request.method == 'POST':
        # Get the user's prompt and model choice from the form
        prompt = request.POST.get('prompt')
        model_choice = request.POST.get('model_choice')
        pre_prompt = "My goal is to generate SQL queries based on natural language requests. Given all the knowledge about the Observational Medical Outcomes Partnership (OMOP) Common Data Model (CDM) version 6.0 (i.e. People information are stored in the PERSON table, diseases and conditions in the CONDITION_OCCURENCE table, etc.)  and its associated usual vocabularies (ICD10, ATC,..), the following request : \""
        # Create an OpenAI client using your API key
        post_prompt = "\" is best translated as the following SQL query (only add the SQL query then stop generating) :\n"
        openai.api_key=""
        full_prompt = pre_prompt + prompt + post_prompt
        # Use the client to call the selected model with the user's prompt
        response = openai.Completion.create(
            engine=model_choice,
            prompt=full_prompt,
            max_tokens=100
        )
        #response = { "choices": [{"text": "This is the answer"}]}
        # Extract the generated text from the response
        pprint(response)
        generated_text = response["choices"][0]["text"]

        return render(request, 'query/mytemplate.html', {'generated_text': generated_text})

    return render(request, 'query/mytemplate.html')