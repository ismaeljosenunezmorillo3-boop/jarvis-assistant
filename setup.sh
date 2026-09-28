#!/bin/bash
# Setup script for JARVIS Assistant

echo "🤖 JARVIS Assistant Setup"
echo "========================="

# Check Python version
echo "Checking Python version..."
python_version=$(python3 --version 2>&1 | awk '{print $2}')
echo "Python version: $python_version"

# Create virtual environment
echo "Creating virtual environment..."
python3 -m venv venv

# Activate virtual environment
echo "Activating virtual environment..."
source venv/bin/activate

# Install dependencies
echo "Installing dependencies..."
pip install --upgrade pip
pip install -r requirements.txt

echo ""
echo "✅ Setup complete!"
echo ""
echo "To start JARVIS, run:"
echo "  source venv/bin/activate"
echo "  python jarvis.py"
