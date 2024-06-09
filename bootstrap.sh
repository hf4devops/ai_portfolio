#!/bin/bash
echo "###" ~/.bashrc
echo "export LANGCHAIN_TRACING_V2=true" >> ~/.bashrc
echo "export LANGCHAIN_API_KEY=$(cat api.key)" >> ~/.bashrc
echo "export OPENAI_API_KEY=$(cat openapi.key)" >> ~/.bashrc

echo "export LANGCHAIN_PROJECT=default" >> ~/.bashrc

pip install -r ai_portfolio/requirements.txt
source ~/.bashrc
