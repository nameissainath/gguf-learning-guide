# Quantization Concepts: Beginner Guide

## What Are Bits and Bytes? (in the context of GGUF and ML)
- **Bit**: The smallest unit of data, can store a 0 or 1.
- **Byte**: 8 bits grouped together; enough to store a small number or letter.
- In AI models like GGUF, weights (the numbers used by the model) are originally stored as floating-point numbers (like f32 or f16). Quantization reduces these to use fewer bits to save memory and speed up processing.

## What Is Quantization?
Quantization is converting a number that uses many bits (like f32 = 32 bits) to a number that uses fewer bits (like 4 bits), with a small loss in precision. This helps make AI models smaller and faster.

## What Is f32, f16, 8-bit, 4-bit, 2-bit Quantization?
- **f32 (float32)**: 32 bits; big range, high precision, slow and memory-heavy.
- **f16 (float16)**: 16 bits; less precise, needs half the memory.
- **8-bit**: Stores each value in 8 bits (instead of 32 or 16), less data, faster but lower precision.
- **4-bit**: Only 4 bits per value, saves even more space, but more loss in detail.
- **2-bit**: Only 2 bits per value, extreme compression, very rough, big loss of detail.

## Visual Representation of Bits Per Value
```
f32  | 01001001 10100101 00001101 11000011  (32 bits)
f16  | 01001101 10101100                (16 bits)
8bit | 10101111                        (8 bits)
4bit | 1110                             (4 bits)
2bit | 01                               (2 bits)
```

## Example: How Neural Network Weights Are Stored and Quantized in LLMs
Let's use a tiny example: a neural network with just 4 weights.

### Step 1: Weights in f32 (32 bits per weight)
Suppose the weights are: `[2.5, -1.2, 0.0, 6.0]`
- Each weight as f32 takes 4 bytes (32 bits)
- Stored in memory (RAM or disk) as a string of 0s and 1s:
    - 2.5 → `01000000 00100000 00000000 00000000`
    - -1.2 → `10111111 10011001 10011001 10011010`
    - 0.0 → `00000000 00000000 00000000 00000000`
    - 6.0 → `01000000 11000000 00000000 00000000`
- **Total storage:** 4 weights × 4 bytes = 16 bytes

### Step 2: Weights in 8-bit Quantization (1 byte per weight)
- Find min/max: e.g., min = -6, max = 6
- Map each weight into integer 0–255:
    - Quantized value = round((weight - min) / (max - min) × 255)
    - Example for 2.5:
        - (2.5 - (-6)) / (6 - (-6)) × 255 ≈ (8.5 / 12) × 255 ≈ 181
    - Repeat for each weight: 2.5=181, -1.2=101, 0.0=128, 6.0=255
    - Store these as one byte each: `[181, 101, 128, 255]`
- **Total storage:** 4 weights × 1 byte = 4 bytes

### Step 3: Weights in 4-bit Quantization (2 weights per byte)
- Map each weight into 0–15 using the same process, then pack two weights per byte:
    - 2.5 → 11; -1.2 → 4; 0.0 → 8; 6.0 → 15
    - To store: pack `[11(1011), 4(0100)]` into `10110100` and `[8(1000), 15(1111)]` into `10001111`
    - Stored bytes: `10110100` `10001111`
- **Total storage:** 4 weights × 4 bits = 16 bits = 2 bytes

### Step 4: Weights in 2-bit Quantization (4 weights per byte)
- Each value maps to 0–3:
    - 2.5 → 2; -1.2 → 1; 0.0 → 2; 6.0 → 3
    - Pack into a single byte: `[2(10), 1(01), 2(10), 3(11)]` = `10011011`
- **Total storage:** 4 weights × 2 bits = 8 bits = 1 byte

---
**Summary Table:**
| Bit Format | Storage for 4 weights | How Packed                        |
|------------|----------------------|-----------------------------------|
| f32        | 16 bytes             | 1 weight per 4 bytes              |
| 8-bit      | 4 bytes              | 1 weight per byte                 |
| 4-bit      | 2 bytes              | 2 weights per byte                |
| 2-bit      | 1 byte               | 4 weights per byte                |

### Why does this matter?
In large language models (LLMs) with billions of weights, this reduction saves huge amounts of memory and makes the models fit on smaller computers and run faster. That’s why quantization is so useful!

## How to Convert f32 to f16 (with Example)
- **f32 Example:**
  - Value: `5.375`
  - f32 binary: `01000000 10101100 00000000 00000000`
- **To f16:**
  - f16 binary (rounded, lower precision): `01000101 01100000`
- (Exact conversion is handled by computer hardware/software, but the main idea: less bits = less detail, but much smaller size)

## How Quantization Works: f32 → 8-bit → 4-bit → 2-bit
1. **Find Max/Min (Range):**
   - For example, model weights range from -6.0 to 6.0.
2. **Rescale to Fit Bits:**
   - 8-bit: 256 values (0–255). Map -6.0 to 0, 6.0 to 255.
   - 4-bit: 16 values (0–15). Map -6.0 to 0, 6.0 to 15.
   - 2-bit: 4 values (0–3). Map -6.0 to 0, 6.0 to 3.
3. **Round Each Value:**
   - Example: 2.0 is closer to which bin for 4-bit? Calculate the bin, round to nearest.
4. **Store the Rounded Value:**

### Example: Quantizing from f32 to 4-bit
Suppose weights are: `[ -6.0, -3.0, 0.0, 3.0, 6.0 ]`
- 4-bit range: 0 to 15
- Formula: `quantized = round( (value - min) / (max - min) * 15 )`
- For value `3.0`:
  - `quantized = round( (3.0 - (-6.0)) / (6.0 - (-6.0)) * 15 )`
  - `= round(9.0/12.0*15) = round(11.25) = 11`
- Store 11 for `3.0`

## Rounding in Quantization
- Values are mapped into "bins." Actual value is rounded to the nearest bin value.
- Helps compress data, but details may be lost.
- Example: If bins are `[0, 5, 10, 15]` and actual value is `7`, it gets mapped to `5` (nearest bin).

## Diagram: Quantization Bins (4-bit)
```
Original range: -6   -3     0     3     6
                 |----|-----|-----|----|
Quant 4-bit:     0    4     8     12   15
```

## Why Quantization? Pros and Cons
- **Pros:**
  - Smaller model files
  - Faster computation
  - Fits on smaller devices
- **Cons:**
  - Slight loss in accuracy
  - Too small a bit size (like 2-bit) can lose a lot of info

## Summary Table
| Format | Bits | Number of Values | Example Precision          |
|--------|------|------------------|---------------------------|
| f32    | 32   | 4,294,967,296    | Very high (best)          |
| f16    | 16   | 65,536           | High                      |
| 8-bit  | 8    | 256              | Medium                    |
| 4-bit  | 4    | 16               | Low                       |
| 2-bit  | 2    | 4                | Very Low (rough)          |

---
**Tip:** Choose the smallest bit size that keeps the accuracy you need. 8-bit and f16 are popular for balance of speed and quality.
