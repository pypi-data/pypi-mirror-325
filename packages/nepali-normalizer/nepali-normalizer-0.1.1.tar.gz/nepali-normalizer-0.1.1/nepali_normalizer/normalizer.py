from indicnlp.normalize import indic_normalize
import unicodedata
import re

class NepaliTextNormalizerWerCer:
    """
    A class for normalizing Nepali text, including vowel normalization, punctuation removal,
    Unicode standardization, and numeral conversion.
    """

    def __init__(self):
        """
        Initializes the NepaliTextNormalizer by setting up the Indic Normalizer for Nepali.
        """
        factory = indic_normalize.IndicNormalizerFactory()
        self.normalizer = factory.get_normalizer("ne")

    def normalize_nepali_vowels(self, text):
        """
        Normalizes Nepali vowels by replacing short vowels with long vowels.

        Args:
            text (str): Input text to normalize.

        Returns:
            str: Text with normalized vowels.
        """
        # Replace short vowels with long vowels
        text = text.replace('इ', 'ई')  # Short 'इ' → Long 'ई'
        text = text.replace('उ', 'ऊ')  # Short 'उ' → Long 'ऊ'
        text = text.replace('ि', 'ी')  # Short 'ि' → Long 'ी'
        text = text.replace('ु', 'ू')  # Short 'ु' → Long 'ू'
        return text

    def __call__(self, text):
        """
        Normalizes the input text by applying Indic NLP normalization, removing punctuation,
        standardizing numerals, normalizing Unicode, and collapsing whitespace.

        Args:
            text (str): Input text to normalize.

        Returns:
            str: Normalized text.
        """
        # Normalize using Indic NLP
        text = self.normalizer.normalize(text)
        
        # Remove punctuation (Nepali + general Unicode punctuation)
        text = re.sub(r'[।,!?;:—\-()\[\]{}"“”‘’॰]', ' ', text)
        text = re.sub(r"[']", ' ', text)
        
        # Standardize numerals (Western to Nepali)
        text = text.translate(str.maketrans('0123456789', '०१२३४५६७८९'))
        
        # Normalize Unicode compositions
        text = unicodedata.normalize('NFC', text)
        
        # Collapse whitespace
        text = re.sub(r'\s+', ' ', text).strip()

        # Normalize Nepali vowels
        text = self.normalize_nepali_vowels(text)
        
        return text


# Example usage
if __name__ == "__main__":
    # Define the normalizer
    normalizer = NepaliTextNormalizerWerCer()

    # Test strings with different matras
    test_string1 = "मेरी आमा राम्री छिन asdf '' कुन 1234"
    test_string2 = "मेरि आमा राम्रि छीन asdf '''' कुन 1234"

    # Normalize and print results
    test_string1_normalized = normalizer(test_string1)
    test_string2_normalized = normalizer(test_string2)
    print(f"Test string 1: {test_string1_normalized}")
    print(f"Test string 2: {test_string2_normalized}")

    # Check if both normalized strings are equal
    print(test_string1_normalized == test_string2_normalized)