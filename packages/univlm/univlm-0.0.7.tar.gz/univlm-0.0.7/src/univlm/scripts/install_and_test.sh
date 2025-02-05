#!/bin/bash

set -e

echo "🚀 Starting installation and testing process..."

# Use environment variables passed from Python
PACKAGE_ROOT=${PACKAGE_ROOT:-$(pwd)}
BACKBONE_DIR=${BACKBONE_DIR:-"${PACKAGE_ROOT}/Package_Backbone"}
TESTING_SCRIPT=${TESTING_SCRIPT:-"${PACKAGE_ROOT}/scripts/testing.py"}

# Create required directories
mkdir -p "${BACKBONE_DIR}"

# Try to import vllm first
if ! python -c "import vllm" 2>/dev/null; then
    echo "📥 Installing vLLM..."
    VLLM_VERSION="0.2.0"
    PYTHON_VERSION=$(python3 -c "import sys; print(f'{sys.version_info.major}{sys.version_info.minor}')")
    
    pip install "https://github.com/vllm-project/vllm/releases/download/v${VLLM_VERSION}/vllm-${VLLM_VERSION}+cu118-cp${PYTHON_VERSION}-cp${PYTHON_VERSION}-manylinux1_x86_64.whl" \
        --extra-index-url https://download.pytorch.org/whl/cu118
fi

echo "✅ vLLM installation verified!"

# Download HuggingFace files
echo "📥 Downloading required Hugging Face files..."
cd "${BACKBONE_DIR}"

FILES=(
    "modeling_auto.py"
    "processing_auto.py"
    "tokenization_auto.py"
    "image_processing_auto.py"
    "feature_extraction_auto.py"
)

for file in "${FILES[@]}"; do
    if [ ! -f "$file" ]; then
        wget -q "https://raw.githubusercontent.com/huggingface/transformers/main/src/transformers/models/auto/${file}"
        echo "✅ Downloaded: ${file}"
    else
        echo "✅ File exists: ${file}"
    fi
done

# Run testing on downloaded files
echo "🛠 Running testing on downloaded files..."
for file in *.py; do
    echo "🔍 Testing: ${file}"
    python "${TESTING_SCRIPT}" "${file}"
done

echo "✅ All operations completed successfully!"