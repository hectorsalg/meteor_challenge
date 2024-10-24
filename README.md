# Meteor Challenge - Solution

This project provides a solution to the **Meteor Challenge (Part 1)**. The goal is to analyze an image and perform several tasks related to identifying and counting celestial objects and their interactions with water. Below is an explanation of how the tasks were approached and solved using Python.

## Tasks

1. **Count the number of Stars**
2. **Count the number of Meteors**
3. **Identify how many Meteors fall perpendicularly onto the Water level**
4. *(Optional)* Decode the hidden phrase from the stars in the sky

### Solution Explanation

The following steps describe how each task was accomplished:

### 1. Count the Number of Stars

To count the stars, the code first reads the image using the `PIL` library and converts it to an RGB format to ensure correct color comparison. It then converts the image to a NumPy array to enable pixel-based analysis. The star color was defined as **pure white** (`(255, 255, 255)`), and using NumPy functions, the positions of all stars were identified, and their total count was calculated.

### 2. Count the Number of Meteors

Similarly, meteors were defined as **pure red** (`(255, 0, 0)`), and the same method was applied to locate and count all the meteors in the image.

### 3. Identify Meteors Falling on the Water

To determine if meteors are falling on water, the following process was used:
- Meteors were assumed to fall perpendicularly downward.
- Starting from the position of each meteor, the code checked all pixels directly below it until it reached the bottom of the image.
- If the path of the meteor intersected with **pure blue** (`(0, 0, 255)`) pixels (representing water), it was considered as falling on water.

### 4. (Optional) Decode the Hidden Phrase

*Note:* This part of the task was optional and not implemented in this code. Future implementations may involve analyzing the pattern of the stars to decode a hidden phrase, as hinted in the challenge description.

## Results

- **Number of Stars:** (Output will be displayed when the code is run)
- **Number of Meteors:** (Output will be displayed when the code is run)
- **Meteors falling on the Water:** (Output will be displayed when the code is run)

## Dependencies

To run this code, you will need:
- Python 3.x
- [PIL (Pillow)](https://pillow.readthedocs.io/en/stable/)
- NumPy

Install the required libraries using:

```bash
pip install pillow numpy
```

## How to run?

1. Make sure the image file **meteor_challenge_01.png** is in the same directory as the script.
2. Run the script using the following command:

```bash
python [CHALLENGE]_[METEOR]_Hector_José_Rodrigues_Salgueiros.py
```

## Conclusion

This solution successfully addresses the tasks related to counting stars, identifying meteors, and detecting which meteors fall into the water. Future improvements may include implementing a method to decode the hidden phrase.