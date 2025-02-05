# Nepali Text Normalizer

Advanced normalization toolkit for Nepali text processing. This package provides tools to normalize Nepali text, including vowel normalization, punctuation removal, Unicode standardization, and numeral conversion.

This tool helps evaluators evaluate WER normalizing nepali text better.

## Installation

Install the package via pip:

```bash
pip install nepali-normalizer
```

## Example 

```python
# example_script.py
from nepali_normalizer import NepaliTextNormalizerWerCer

# Define the normalizer
normalizer = NepaliTextNormalizerWerCer()

# Test strings
test_string1 = "मेरी आमा राम्री छिन asdf ''  1234"
test_string2 = "मेरि आमा राम्रि छीन asdf ''''  1234"

# Normalize and print results
test_string1_normalized = normalizer(test_string1)
test_string2_normalized = normalizer(test_string2)
print(f"Test string 1: {test_string1_normalized}")
print(f"Test string 2: {test_string2_normalized}")

# output
# Test string 1: मेरी आमा राम्री छीन asdf १२३४
# Test string 2: मेरी आमा राम्री छीन asdf १२३४
```