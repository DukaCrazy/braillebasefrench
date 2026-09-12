### - pip install braillebasefrench

# French

### NOTE 1: Antoine number notation

This library provides text-to-Braille translation for French. However, it
does not currently implement all rules defined by the French Braille standard
(CBFU).

In particular, French Braille uses the **Antoine number notation** for the
transcription of numbers, which is not currently supported by this library.

Therefore, while regular text can be translated to Braille, texts containing
numbers may not be fully compliant with the French Braille standard.

Support for Antoine number notation and additional French Braille
transcription rules may be added in future versions.

### NOTE 2: Unsupported French Characters

We could not find an official French Braille representation for the character
`ÿ` in the references consulted. However, this character can occur in French
words and proper names.

To avoid translation or execution errors, the library currently falls back to
the Braille representation of the base letter `y`.

The same approach is used for the character `æ`. Since we did not identify a
dedicated French Braille representation for `æ`, it is currently handled as
the character sequence `ae`.

> **Note:** These are compatibility fallbacks implemented by the library and
> should not be interpreted as official French Braille transcriptions.

### NOTE 3: Uppercase and Lowercase Indicators

For uppercase characters, the library currently uses `⠨` as the uppercase
indicator.

We did not find sufficient information in the references consulted to confirm
the use of `⠨⠨` for multiple consecutive uppercase characters. For lowercase
characters, the library currently uses `⠐`, following the convention used by
the Portuguese Braille standard.

These rules are configurable and can be easily changed using:

```python
self.setting_braille_rules_uppercase("⠨", "⠨⠨", "⠐")
```


## How to use?
```python
from braille import *

bb = bbf()
print(bb.output_braille_txt("Bibliothèque développée pour gérer le braille simple et complexe 2026."))
```
Output: ⠨⠃⠊⠃⠇⠊⠕⠞⠓⠮⠟⠥⠑⠀⠙⠿⠧⠑⠇⠕⠏⠏⠿⠑⠀⠏⠕⠥⠗⠀⠛⠿⠗⠑⠗⠀⠇⠑⠀⠃⠗⠁⠊⠇⠇⠑⠀⠎⠊⠍⠏⠇⠑⠀⠑⠞⠀⠉⠕⠍⠏⠇⠑⠭⠑⠀⠼⠃⠚⠃⠋⠲


# Announcement
- This package is part of an ecosystem called Braille Base. This name does not represent a company or business; it is an independent initiative aimed at providing registered braille tables for all of humanity.

- We constantly need help to register, update, and validate braille tables. There is still no official contact channel, but you can find new information on the blog braillebase.blogspot.com or brailletable.blogspot.com.


```python
from braille import *

bb = bbf()
print(bb.confidence_test("Bibliothèque développée pour gérer le braille simple et complexe 2026."))
```

Output: {0: ['⠨', ['⠨']], 1: ['B', ['⠃']], 2: ['i', ['⠊']], 3: ['b', ['⠃']], 4: ['l', ['⠇']], 5: ['i', ['⠊']], 6: ['o', ['⠕']], 7: ['t', ['⠞']], 8: ['h', ['⠓']], 9: ['è', ['⠮']], 10: ['q', ['⠟']], 11: ['u', ['⠥']], 12: ['e', ['⠑']], 13: [' ', ['⠀']], 14: ['d', ['⠙']], 15: ['é', ['⠿']], 16: ['v', ['⠧']], 17: ['e', ['⠑']], 18: ['l', ['⠇']], 19: ['o', ['⠕']], 20: ['p', ['⠏']], 21: ['p', ['⠏']], 22: ['é', ['⠿']], 23: ['e', ['⠑']], 24: [' ', ['⠀']], 25: ['p', ['⠏']], 26: ['o', ['⠕']], 27: ['u', ['⠥']], 28: ['r', ['⠗']], 29: [' ', ['⠀']], 30: ['g', ['⠛']], 31: ['é', ['⠿']], 32: ['r', ['⠗']], 33: ['e', ['⠑']], 34: ['r', ['⠗']], 35: [' ', ['⠀']], 36: ['l', ['⠇']], 37: ['e', ['⠑']], 38: [' ', ['⠀']], 39: ['b', ['⠃']], 40: ['r', ['⠗']], 41: ['a', ['⠁']], 42: ['i', ['⠊']], 43: ['l', ['⠇']], 44: ['l', ['⠇']], 45: ['e', ['⠑']], 46: [' ', ['⠀']], 47: ['s', ['⠎']], 48: ['i', ['⠊']], 49: ['m', ['⠍']], 50: ['p', ['⠏']], 51: ['l', ['⠇']], 52: ['e', ['⠑']], 53: [' ', ['⠀']], 54: ['e', ['⠑']], 55: ['t', ['⠞']], 56: [' ', ['⠀']], 57: ['c', ['⠉']], 58: ['o', ['⠕']], 59: ['m', ['⠍']], 60: ['p', ['⠏']], 61: ['l', ['⠇']], 62: ['e', ['⠑']], 63: ['x', ['⠭']], 64: ['e', ['⠑']], 65: [' ', ['⠀']], 66: ['⠼', ['⠼']], 67: ['2', ['⠃']], 68: ['0', ['⠚']], 69: ['2', ['⠃']], 70: ['6', ['⠋']], 71: ['.', ['⠲']]}


## Pre-registered Letters and Characters

- a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, z;
- é, à, è, ù, â, ê, î, ô, û, ë, ï, ü, ç, œ;

- A, B, C, D, E, F, G, H, I, j, K, L, M, N, O, P, Q, R, S, T, U, V, W, X, Y, Z;
- É, À, È, Ù, Â, Ê, Î, Ô, Û, Ë, Ï, Ü, Ç, Œ

- ., ,, ;, :, ?, !, (, ), [, ], “, ”, «, »;

- ⠼, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0;

ÿ == y
Ÿ == Y
æ == ae
Æ == AE
