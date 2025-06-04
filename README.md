# Masked PDF Translator

This project provides a basic example for translating text inside a PDF
while allowing regions to be masked out.  Masks are stored in JSON files
next to the PDF so that they can be reused automatically.

```
python masked_pdf_translator.py
```

When a PDF called `example.pdf` is opened, the script will look for
`example_masks.json` in the same directory and load any saved masks.
When translation finishes the masks are saved back to this file.
