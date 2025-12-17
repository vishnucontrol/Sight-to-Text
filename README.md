# Sight to Text 
## Overview
The video captioning project is an automated system designed to generate descriptive textual content for video data, aiming to enhance accessibility and improve the overall multimedia experience. The solution integrates multiple advanced components to provide a comprehensive and seamless workflow.

The process begins by extracting videos into individual frames, creating a large-scale image dataset for further analysis (videotoimages.py). Each frame is then processed using image captioning techniques to generate meaningful and context-aware textual descriptions (imagetotextgenerator.py). To ensure narrative clarity and avoid redundancy, the system identifies and removes duplicate or highly similar captions, maintaining a concise and coherent output (removeduplicatetext.py).

Extending beyond traditional captioning systems, the project converts the final textual content into synthesized speech, enabling an audio-based narration of the video (texttoaudio.py). This feature significantly improves accessibility, particularly for users with reading or visual impairments.

The system leverages a range of Python libraries such as NumPy, PyTorch, and Hugging Face Transformers to support mathematical operations, deep learning, and natural language processing using transformer-based architectures. By combining video-to-image conversion, image captioning, textual redundancy elimination, and text-to-speech synthesis, the project delivers an inclusive and intelligent video understanding solution.
