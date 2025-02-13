# arxa

arxa is a tool to automatically generate research reviews from an arXiv paper or a local PDF. It even supports optional GitHub repository cloning and analysis if a GitHub URL is detected in the review.

## Installation

You can install via pip:

`pip install arxa`

Then run it with the command-line interface as shown below.

## Features

• Generate a review for a single arXiv paper by providing its ID:
`arxa -aid 1234.5678 -o output.md`

• Generate a review from a local PDF file:
`arxa -pdf /path/to/paper.pdf -o output.md`

• Specify the LLM backend provider and model:
`arxa -pdf /path/to/paper.pdf -o output.md -p openai -m o3-mini`

• Enable GitHub cloning (disabled by default):
`arxa -pdf /path/to/paper.pdf -o output.md -g`

• Use a configuration file for additional settings:
`arxa -c config.yaml`
