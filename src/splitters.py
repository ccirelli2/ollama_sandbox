"""
Text Splitter Functions
"""

class TextSplitterByToken:
    """
    Split text by num of tokens.
    """
    def __init__(self, separator: str, num_tokens: int = 500):
        self.separator = separator
        self.num_tokens = num_tokens
        self.tokens = []
        self.chunks = []
        print(f"{__class__} instantiated successfully")

    def _get_tokens(self, text):
        """
        """
        print(f"Splitting text using => {self.separator}")
        self.tokens = text.split(self.separator)
        return self

    def _get_chunks(self):
        print(f"Creating chunks of size {self.num_tokens}")
        sum_tokens = len(self.tokens)
        self.chunks = []
        for i in range(0, sum_tokens, self.num_tokens):
            chunk = self.tokens[i: i + self.num_tokens]
            chunks_joined = f"{self.separator}".join(chunk)
            self.chunks.append(chunks_joined)
        print(f"Returning {len(self.chunks)} chunks")
        return self

    def split_text(self, text: str):
        self._get_tokens(text)
        self._get_chunks()
        return self.chunks
