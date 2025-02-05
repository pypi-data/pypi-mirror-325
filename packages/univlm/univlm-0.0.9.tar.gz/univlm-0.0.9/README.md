# univlm
An inference and task unified VLM library
# UNIVLM Model Framework

## Overview
The Univlm Model Framework provides a flexible and extensible system for loading, processing, and performing inference across different AI models. It supports various model types, including VLLM, Hugging Face, and models not supported on HF and vLLM. Additionally, it offers utilities for searching and managing Hugging Face models and processors.

## Core Modules
### 1. `univlm` (Model Management)
A versatile class that supports multiple model loading strategies and inference pipelines.

#### **Initialization**
```python
univlm(model_name, Feature_extractor, Image_processor, Config_Name=None)
```
- `model_name`: Name or path of the model
- `Feature_extractor`: Optional feature extraction configuration
- `Image_processor`: Optional image processing configuration
- `Config_Name`: Optional specific configuration name

#### **Key Methods**
##### `load()`
Loads the model using:
1. VLLM
2. Hugging Face
3. Exclusive Models

**Returns:**
- "Loaded" if successful
- "Failed to Load" if all attempts fail

##### `Processor()`
Initializes the appropriate processor for the loaded model.

##### `inference(payload)`
Performs inference with flexible input handling (String, Dictionary, or List).

**Supported Model Types:**
- VLLM: Text generation
- Hugging Face: Multi-modal processing
- Exclusive: Custom inference

##### `_standardize_payload(payload)`
Standardizes input formats into a structured output.

##### `_get_processor_input_names(processor)`
Extracts expected input parameter names for different processors.

### 2. `HFModelSearcher` (Model Search Utility)
A utility class for searching and matching Hugging Face model configurations.

#### **Key Methods:**
- `extract_model_family(hf_path: str) -> str`: Extracts core model family name.
- `search(query: str = None, config = None)`: Searches model configurations using exact and fuzzy matching.

### 3. `HFProcessorSearcher` (Processor Search Utility)
A utility for searching Hugging Face processors (tokenizers, feature extractors, etc.).

#### **Key Methods:**
- `extract_model_family(hf_path: str) -> str`: Normalizes model family names.
- `search(query: str, feature_extractor=False, image_processor=False, tokenizer=False)`: Searches matching processors based on the query.

### 4. `appledepth` (Depth Estimation)
A specialized class for depth estimation using Apple's ML Depth Pro model.

#### **Key Methods:**
- `env_setup()`: Sets up the development environment.
- `load_model()`: Loads the depth estimation model.
- `processor(image_path, text=None)`: Preprocesses input image.
- `infer()`: Performs depth estimation inference.

## Usage Examples
### **Example of model on HF not vllms**
```python
y = Yggdrasil("nlptown/bert-base-multilingual-uncased-sentiment", Feature_extractor=False,Image_processor=False,Config_Name = 'BertForNextSentencePrediction')
y.load()
payload = { "text": "Hello, how are you?", "pixel_values": None }
output = y.inference(payload)
print(output)
```

### **Example of VLM **
```python
img_url = 'https://storage.googleapis.com/sfr-vision-language-research/BLIP/demo.jpg' 
raw_image = Image.open(requests.get(img_url, stream=True).raw).convert('RGB')
listy = [raw_image,raw_image]
payload = {"pixel_values": listy, "text": ["how many dogs?","color of dog"]}

y = Yggdrasil("Salesforce/blip-vqa-base", Feature_extractor=False, Image_processor=False)
y.load()
```

### **Example of Image Only task**
```python
img_url = "https://storage.googleapis.com/sfr-vision-language-research/BLIP/demo.jpg"
image = Image.open(requests.get(img_url, stream=True).raw).convert('RGB')

payload = {"pixel_values": image, "text": None}

y = Yggdrasil("facebook/sam-vit-base", Feature_extractor=False, Image_processor=True)
y.load()
output = y.inference(payload)
print(output)
```

### **Depth Estimation**
```python



```

## Dependencies
- `transformers`
- `torch`
- `vllm`
- `concurrent.futures`
- `fuzzywuzzy`
- `subprocess`
- `json`
- `pathlib`

## Notes
- Requires an internet connection for model downloads.
- Conda and Git must be pre-installed.
- Some methods use parallel processing for improved performance.

## Contributing
Contributions to improve model support and inference capabilities are welcome!

cd