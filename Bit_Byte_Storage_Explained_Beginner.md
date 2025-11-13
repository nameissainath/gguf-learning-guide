# Understanding 0s and 1s: How Computers Store Information

## 1. What are 0 and 1 in Computers?
Computers use only two symbols: 0 and 1. This system is called **binary**. All text, images, sound, and programs are eventually broken down into a long sequence of 0s and 1s for a computer to process and store.

### Why only 0 and 1?
- Physically, inside the computer, these represent **two states**:
  - 0: off, no voltage, closed switch
  - 1: on, some voltage, open switch
- Modern computers use **transistors**, which are tiny electronic switches.

#### Visual:
- Switch OFF → 0
- Switch ON  → 1

## 2. Bits and Bytes
- **Bit** = one binary digit (0 or 1)
- **Byte** = 8 bits (e.g., 01001011)
- A byte is the smallest "chunk" of data most computers can easily work with.

### Example
```
Bit:            1
One byte:  01000001   (8 bits)
```

## 3. How Are 0 and 1 Stored in Hardware?
- In storage: as tiny charges or magnets (like on a hard drive or SSD)
- In RAM: as tiny voltages in circuits
- In processors: as current flowing through transistors

## 4. How Text Gets Stored: ASCII Table
Every letter, number or symbol you type has a binary number assigned to it by the **ASCII** system.

### Example Table:
| Character | ASCII (Decimal) | Binary    |
|-----------|-----------------|-----------|
| A         | 65              | 01000001  |
| B         | 66              | 01000010  |
| a         | 97              | 01100001  |
| 1         | 49              | 00110001  |
| !         | 33              | 00100001  |

If you type "A!":
- A = 01000001
- ! = 00100001
- Stored as: 01000001 00100001

## 5. How Colours and Images are Stored
- Images are made of tiny dots called **pixels**.
- Each pixel's colour is represented by a set of bits.
- The standard is **RGB**: Red, Green, Blue.

### Example: Storing a Colour Pixel
Each channel uses 1 byte (8 bits):
- Red:   11110000 (240)
- Green: 11000000 (192)
- Blue:  10010000 (144)
- Together (in bytes): `11110000 11000000 10010000`

This pixel would look purple-ish!

### Visual Table: An Image Row with 3 Pixels
| Pixel | R (8 bits)   | G (8 bits)   | B (8 bits)   | Full (Binary)                    |
|-------|--------------|--------------|--------------|-----------------------------------|
| 1     | 11111111     | 00000000     | 00000000     | 11111111 00000000 00000000 (Red) |
| 2     | 00000000     | 11111111     | 00000000     | 00000000 11111111 00000000 (Green)|
| 3     | 00000000     | 00000000     | 11111111     | 00000000 00000000 11111111 (Blue) |

## 6. How Does All This Get Displayed?
- The computer collects all these 0s and 1s for pixels and sends the data to your screen.
- Each pixel lights up in its correct colour.

## 7. Real-World Examples
- A short text file: 100 bytes = 800 bits of 0s and 1s (e.g., a word or a sentence)
- A small icon: 32 x 32 pixels × 24 bits per pixel = 24,576 bits = 3,072 bytes (~3 KB)

## 8. Summary Table
| Data Type          | Bits Used         | How Represented                    |
|--------------------|------------------|------------------------------------|
| Letter ('A')       | 8 bits (1 byte)  | 01000001 (ASCII)                   |
| Number (e.g. 7)    | 8 bits (1 byte)  | 00110111 (ASCII)                   |
| Colour (full pixel)| 24 bits (3 bytes)| 10101010 10101010 10101010         |

---
**Key Takeaway:**
- Everything in computers—text, pictures, music, videos—is stored as 0s and 1s!
- Understanding bits and bytes helps you understand how computers really work on the inside.

## Example: How the Sentence "My name is Sai" is Stored—From Letters to Transistors
Let's walk step-by-step through how a simple phrase like "My name is Sai" gets stored in a computer!

### Step 1: Breaking Down Each Character
The phrase is: **M y   n a m e   i s   S a i**

Table of ASCII Binary Representation:
| Character | ASCII (Decimal) | Binary (8 bits) |
|-----------|-----------------|-----------------|
| M         | 77              | 01001101        |
| y         | 121             | 01111001        |
| (space)   | 32              | 00100000        |
| n         | 110             | 01101110        |
| a         | 97              | 01100001        |
| m         | 109             | 01101101        |
| e         | 101             | 01100101        |
| (space)   | 32              | 00100000        |
| i         | 105             | 01101001        |
| s         | 115             | 01110011        |
| (space)   | 32              | 00100000        |
| S         | 83              | 01010011        |
| a         | 97              | 01100001        |
| i         | 105             | 01101001        |

### Step 2: Grouping Into Bytes
- Each character is 1 byte (8 bits).
- The phrase has 14 characters, so it takes **14 bytes** or **112 bits**.
- Stored as: 
```
01001101 01111001 00100000 01101110 01100001 01101101 01100101 00100000 01101001 01110011 00100000 01010011 01100001 01101001
```

### Step 3: Physically Storing in Memory (RAM/SSD)
- Each byte is stored in a chunk of 8 tiny switches (transistors):
  - 0 = switch OFF (no voltage), 1 = switch ON (voltage present)
- For the letter 'M' (01001101):
  - 1st transistor: 0 (off)
  - 2nd: 1 (on)
  - ...
  - 8th: 1 (on)
- Each character, therefore, lives in a row of 8 transistors inside your RAM or SSD. For our 14 letters, that's **112 transistors** just for this phrase.

### Visual Analogy
- Imagine each byte as a row of 8 light switches on a panel:
  - ON = 1; OFF = 0
  - For "M": OFF, ON, OFF, OFF, ON, ON, OFF, ON
- A sentence becomes a wall of light switches, grouped into bytes.

### Step 4: Billions of Transistors—How Can a Computer Store So Much?
Modern chips (like RAM or SSD) have **billions of transistors** packed in microscopic grids. 
- Each can store a 0 or 1.
- Tiny electrical signals "set" or "reset" these switches.
- Chips use grids (like a city map) so every byte has an address, letting the computer find and manage data quickly.
- Advances in technology let us stack more transistors closer together, so even a small chip can have enough for gigabytes (billions of bytes) of text like our example.

### Process Recap Table:
| Step              | What Happens                                                  |
|-------------------|--------------------------------------------------------------|
| Text              | 'My name is Sai' becomes characters 'M', 'y', ...            |
| ASCII             | Each character translated to a code number (ASCII)            |
| Binary            | Each ASCII code converted into 8 ones or zeros (bits)         |
| Bytes/Transistors | Each bit set on (1) or off (0) in tiny switches (transistors) |
| Stored in Memory  | Bytes assigned an address in RAM/SSD for access               |

### Fun Fact!
A typical laptop RAM (8GB) can store about **64 billion bits**. That’s over  
