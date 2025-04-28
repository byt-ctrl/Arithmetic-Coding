
# Arithmetic Encoding/Decoding

Efficiently encode and decode messages using Arithmetic Coding in Python.

## Features
- Compute cumulative probability ranges for symbols.
- Encode messages into a single floating-point number.
- Decode to reconstruct the original message.

## Usage
1. Run the program.
2. Enter a message to encode.
3. View encoded value and verify decoding.

## Example

``` bash
Welcome to Efficient Arithmetic Encoding/Decoding in Python! 
===================================================================
Please enter a message to encode : Hello World

 Symbol Probability Ranges (Cumulative):
'H': (0.0000, 0.0909)
'e': (0.0909, 0.1818)
'l': (0.1818, 0.4545)
'o': (0.4545, 0.6364)
' ': (0.6364, 0.7273)
'W': (0.7273, 0.8182)
'r': (0.8182, 0.9091)
'd': (0.9091, 1.0000)

 Encoded Value : 0.0105353923
 Decoded Message : Hello World
 Success! The decoded message matches the original one.

```
---


## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contributions

Feel free to contribute! Fork the repository, make your changes, and submit a pull request. All contributions are welcome.
