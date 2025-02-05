#!/bin/bash

set -e  
echo "🚀 Starting installation and testing process..."

# Define versions dynamically
VLLM_VERSION="0.2.0"
PYTHON_VERSION=$(python3 -c "import sys; print(f'{sys.version_info.major}{sys.version_info.minor}')")

echo "🔧 Installing vLLM for Python $PYTHON_VERSION and CUDA 11.8..."
pip install https://github.com/vllm-project/vllm/releases/download/v${VLLM_VERSION}/vllm-${VLLM_VERSION}+cu118-cp${PYTHON_VERSION}-cp${PYTHON_VERSION}-manylinux1_x86_64.whl \
    --extra-index-url https://download.pytorch.org/whl/cu118

echo "✅ vLLM installation completed!"

# Create a directory for the package backbone
mkdir -p Package_Backbone
cd Package_Backbone

echo "📥 Downloading required Hugging Face files..."
wget -q https://raw.githubusercontent.com/huggingface/transformers/main/src/transformers/models/auto/modeling_auto.py
wget -q https://raw.githubusercontent.com/huggingface/transformers/main/src/transformers/models/auto/processing_auto.py
wget -q https://raw.githubusercontent.com/huggingface/transformers/main/src/transformers/models/auto/tokenization_auto.py
wget -q https://raw.githubusercontent.com/huggingface/transformers/main/src/transformers/models/auto/image_processing_auto.py
wget -q https://raw.githubusercontent.com/huggingface/transformers/main/src/transformers/models/auto/feature_extraction_auto.py

echo "✅ Download complete!"

# Move back to parent directory
cd ..

# Update testing.py to save the extracted files in the 'Package_Backbone' directory
echo "🛠 Running testing.py on each downloaded file..."
for file in Package_Backbone/*.py; do
    echo "🔍 Processing: $file"
    python testing.py "$file"
done

echo "✅ All tests completed successfully!"
