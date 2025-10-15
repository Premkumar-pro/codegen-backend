from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from google import genai
from django.conf import settings


# ---------------- Supported Languages ----------------
SUPPORTED_LANGUAGES = [
    "python", "c", "cpp", "java", "javascript",
    "csharp", "go", "rust", "ruby", "php", "kotlin", "swift",
    "typescript", "r", "matlab", "julia", "perl",
    "scala", "dart", "elixir", "haskell", "clojure",
    "erlang", "lua", "groovy", "pascal", "fortran",
    "cobol", "assembly", "objectivec", "actionscript",
    "coffeescript", "elm", "reason", "crystal", "nim",
    "zig", "ada", "lisp", "scheme", "racket", "smalltalk",
    "forth", "prolog", "ocaml", "fsharp", "vbnet",
    "bash", "powershell", "shell"
]

# ---------------- Helper function for rotating API keys ----------------

def get_working_gemini_client():
    last_exception = None
    for key in settings.GEMANI_KEYS:
        try:
            client = genai.Client(api_key=key)
            # Optional: test the key by a simple call
            return client
        except Exception as e:
            last_exception = e
            continue
    raise Exception(f"All Gemini API keys failed. Last error: {last_exception}")

@api_view(['POST'])
def convert_code(request):
    source_lang = request.data.get('source_lang')
    target_lang = request.data.get('target_lang')
    code = request.data.get('code')

    # Input validation
    if not all([source_lang, target_lang, code]):
        return Response({"error": "Missing fields"}, status=status.HTTP_400_BAD_REQUEST)

    if source_lang not in SUPPORTED_LANGUAGES or target_lang not in SUPPORTED_LANGUAGES:
        return Response({"error": f"Languages must be one of {SUPPORTED_LANGUAGES}"}, status=status.HTTP_400_BAD_REQUEST)

    try:
        prompt = f"""
Convert the following {source_lang} code to {target_lang}.

Instructions:
1. Only return the converted code. like copy paste format 
2. Do not include explanations outside of code.
3. Keep formatting clean and minimal.
4. Preserve function names, variable names, and logic as much as possible.
5. explain two lines what thay mistake in last line after the code was converted with #symbol like commits

Code:
{code}
"""

        # ---------------- Gemini API with rotation ----------------
        client = get_working_gemini_client()
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )
        converted_code = response.text

        return Response({"converted_code": converted_code}, status=status.HTTP_200_OK)

    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
