import os
from groq import Groq
from dotenv import load_dotenv


load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
MODEL = 'llama-3.3-70b-versatile'

# Initialize the Groq client
client = Groq(api_key=GROQ_API_KEY)

def analyze_code_diff(diff):
    """
    Analyze the code diff using the Groq API and return feedback.
    """
    formatted_prompt = f"""
    Review the following code diff and provide feedback in a short and friendly tone.

    ### Instructions:
    - Focus on:
        1. Identifying any bugs or issues that need fixing.
        2. Providing actionable suggestions for improvement or optimization.
        3. Highlighting changes only if necessary or if there are bugs.
    - Avoid:
        1. Overly verbose explanations.
        2. Repetitive or generic comments.
        3. Comments unrelated to the provided code diff.

    ### Code Diff:
    {diff}
    """

    try:
        completion = client.chat.completions.create(
            model=MODEL,
            messages=[{"role": "system", "content": formatted_prompt}],
            temperature=0.7,
            max_tokens=512,
            top_p=0.9,
            stream=False,
        )
        feedback = completion.choices[0].message.content
        return feedback
    except Exception as e:
        print(f"Error querying Groq API: {str(e)}")
        raise