FILE_NAME = "ksi-pt1"
FILE_NAME = "test"
PAGE_OFFSET = -9
MAX_CHARACTERS_PER_PLATE = [300, 350, 400]
MODEL = "sonnet"

MODELS = [
    {
        "name": "opus",
        "id": "claude-3-opus-20240229",
        "input_cost": 15,
        "output_cost": 75,
    },
    {
        "name": "sonnet",
        "id": "claude-3-sonnet-20240229",
        "input_cost": 3,
        "output_cost": 15,
    },
    {
        "name": "haiku",
        "id": "claude-3-haiku-20240307",
        "input_cost": 0.25,
        "output_cost": 1.25,
    },
]

PROMPT_2 = """<text><<TEXT>></text>

You are an excellent transcription and text editor bot. Please carefully read the text provided inside <text></text> tags. The text contains some errors that resulted from imperfect Optical Character Recognition (OCR), such as incorrect characters, missing punctuation, improper formatting, etc. Respond with the corrected text. Output only the processed text, without any additional commentary.
"""

META_3 = """Please carefully read the following text, which may contain errors like incorrect characters, missing punctuation, improper formatting, and other issues that can result from imperfect Optical Character Recognition (OCR):

<text>
<<TEXT>>
</text>

Identify and fix any errors in the text. Then respond with only the corrected version of the text. Do not include any additional commentary or wrap your output in tags.
"""

FORMAT_2 = "Skip the preamble and provide only the poem."
