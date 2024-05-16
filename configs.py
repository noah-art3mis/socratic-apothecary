# testing things
FILE_NAME = "test"
AUTHOR = "Blune Platour"
TITLE = "Lorem ipsum dolor sit amet consectetur"
BOOK_ID = "tst"
MODEL = "gpt4o"
PAGE_OFFSET = 0

# FILE_NAME = "ksi-final"
# AUTHOR = "David Bloor"
# TITLE = "Knowledge and Human Interests"
# BOOK_ID = "ksi"
# MODEL = "gpt4o"
# PAGE_OFFSET = 0

# FILE_NAME = "ksi-pt1"
# AUTHOR = "David Bloor"
# TITLE = "Knowledge and Human Interests"
# BOOK_ID = "ksi-pt1"
# MODEL = "sonnet"
# PAGE_OFFSET = -9


MAX_CHARACTERS_PER_PLATE = [300, 350, 400]

PROMPT = """<text>{snippet}</text>

This text was transcribed by OCR. Your job is to fix obvious transcription errors, such as problems with word separation, punctuation, encoding. Output only the corrected text. Output the answer within  <answer> tags. Only correct issues which would be generated by a bad transcription. Don't correct stylistic choices, local accents or the logical flow of sentences. If the last sentence looks like it continues in the next page, do not put a period at the end; otherwise, put periods at the end of the last sentence. Use UK English. Don't correct ellipses."""

from utils.my_types import Model

MODELS = [
    Model(
        name="gpt4o",
        provider="openai",
        id="gpt-4o",
        input_cost=5,
        output_cost=15,
    ),
    Model(
        name="opus",
        provider="anthropic",
        id="claude-3-opus-20240229",
        input_cost=15,
        output_cost=75,
    ),
    Model(
        name="sonnet",
        provider="anthropic",
        id="claude-3-sonnet-20240229",
        input_cost=3,
        output_cost=15,
    ),
    Model(
        name="haiku",
        provider="anthropic",
        id="claude-3-haiku-20240307",
        input_cost=0.25,
        output_cost=1.25,
    ),
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
