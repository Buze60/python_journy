📌 PIN Extractor — Python Utility

pin_extractor is a simple Python function that generates a secret numeric code from one or more poems or multi-line text inputs.
It analyzes each poem line-by-line and creates a code based on the number of letters in a specific word within each line.

🔍 How It Works

For each poem:

Split the poem into lines.

For each line:

Split the line into words.

If the number of words in that line is greater than the line index:

Take the word at the same position as the line number
(e.g., line 0 → word 0, line 1 → word 1).

Add the length of that word to the secret code.

Otherwise, add "0" to the code.

Append the generated secret code to a list.

The function returns a list of secret codes, one for each poem.
