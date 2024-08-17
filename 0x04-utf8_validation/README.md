## UTF-8 Validation
- An application knowledge in bitwise operations, understanding of the UTF-8 encoding scheme, and Python programming skills to validate whether a given dataset represents a valid UTF-8 encoding.

### Concepts Needed
1. Bitwise Operations in Python:

- Understanding how to manipulate bits in Python, including operations like AND (`&`), OR (`|`), XOR (`^`), NOT (`~`), shifts (`<<, >>`).
- [Python Bitwise Operators](https://wiki.python.org/moin/BitwiseOperators)
2. UTF-8 Encoding Scheme:

- Familiarity with the UTF-8 encoding rules, including how characters are encoded into one or more bytes.
- Understanding the patterns that represent a valid UTF-8 encoded character.
- [UTF-8 Wikipedia](https://en.wikipedia.org/wiki/UTF-8)
- [Characters, Symbols, and the Unicode Miracle](https://www.youtube.com/watch?v=MijmeoH9LT4)
- [The Absolute Minimum Every Software Developer Absolutely, Positively Must Know About Unicode and Character Sets](https://www.joelonsoftware.com/2003/10/08/the-absolute-minimum-every-software-developer-absolutely-positively-must-know-about-unicode-and-character-sets-no-excuses/)
3. Data Representation:

- How to represent and work with data at the byte level.
- Handling the least significant bits (LSB) of integers to simulate byte data.
4. List Manipulation in Python:

- Iterating through lists, accessing list elements, and understanding list comprehensions.
- [Python Lists](https://docs.python.org/3/tutorial/datastructures.html#more-on-lists)
5. Boolean Logic:

- Applying logical operations to make decisions within the program.

### Understand the Byte Patterns in UTF-8
- 1-byte character: '0xxxxxxx' (where x can be 0 or 1). This means the 1st byte starts with a '0' followed by 7 bits of data
- 2-byte character: '110xxxxx 10xxxxxx'. The 1st byte starts with '110', and the second byte starts with '10'.
- 3-byte character: '1110xxxx 10xxxxxx 10xxxxxx'. The 1st byte starts with '1110', and the next two bytes start with '10'
- 4-byte character: '11110xxx 10xxxxxx 10xxxxxx 10xxxxxx'

**Why validate?**
- By validating data, you ensure that the text is correctly formatted and safe to use.

> [!NOTE]
> - Values greater than 255 aren't valid single-byte values in UTF-8. To handle an exceeding value (like 467), you need to first consider the lower 8 bits of the value
> - In this case: '467' in binary is '111010011' which is a 9 bit number.
> - We need to apply the '0xFF' mask, which ensure that only the least significant 8 bits and ignores any higher bits.
> - Performing '467 & 0xFF' takes only the last bits of '467', thus:

> 111010011 (467) & 11111111 (0xFF) = 11010011 (211)
