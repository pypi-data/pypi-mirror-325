# WIBA: What Is Being Argued?

WIBA is a comprehensive argument mining toolkit that helps you detect, analyze, and understand arguments in text. It provides a simple yet powerful interface to identify argumentative content, extract topics, analyze stance, and discover arguments in longer texts.

## Installation

```bash
pip install wiba
```

## Quick Start

```python
from wiba import WIBA

# Initialize with your API token
analyzer = WIBA(api_token="your_api_token_here")

# Example text
text = "Climate change is real because global temperatures are rising."

# Detect if it's an argument
result = analyzer.detect(text)
print(f"Argument detected: {result.argument_prediction}")
print(f"Confidence: {result.confidence_score}")
```

## Features

- **Argument Detection**: Identify whether a text contains an argument
- **Topic Extraction**: Extract the main topic being argued about
- **Stance Analysis**: Determine the stance towards a specific topic
- **Argument Discovery**: Find argumentative segments in longer texts
- **Batch Processing**: Efficiently process multiple texts
- **DataFrame Support**: Native pandas DataFrame integration

## Documentation

For detailed documentation and examples, visit [wiba.dev](https://wiba.dev).

## Getting Started

1. Create an account at [wiba.dev](https://wiba.dev) to get your API token
2. Install the package: `pip install wiba`
3. Initialize the client with your token
4. Start analyzing arguments!

## Example Usage

### Detect Arguments

```python
# Single text
result = analyzer.detect("Climate change is real because temperatures are rising.")
print(result.argument_prediction)  # "Argument" or "NoArgument"
print(result.confidence_score)     # Confidence score between 0 and 1

# Multiple texts
texts = [
    "Climate change is real because temperatures are rising.",
    "This is just a simple statement without any argument."
]
results = analyzer.detect(texts)
for r in results:
    print(f"Text: {r.text}")
    print(f"Prediction: {r.argument_prediction}")
```

### Extract Topics

```python
result = analyzer.extract("Climate change is a serious issue because it affects our environment.")
print(result.topics)  # List of extracted topics
```

### Analyze Stance

```python
text = "We must take action on climate change because the evidence is overwhelming."
topic = "climate change"
result = analyzer.stance(text, topic)
print(f"Stance: {result.stance}")  # "Favor", "Against", or "NoArgument"
```

### Discover Arguments

```python
text = """Climate change is a serious issue. Global temperatures are rising at an 
unprecedented rate. This is causing extreme weather events. However, some argue 
that natural climate cycles are responsible."""

results_df = analyzer.discover_arguments(
    text,
    window_size=2,  # Number of sentences per window
    step_size=1     # Number of sentences to move window
)
print(results_df[['text_segment', 'argument_prediction', 'argument_confidence']])
```

## Citation

If you use WIBA in your research, please cite:

```bibtex
@misc{irani2024wibaarguedcomprehensiveapproach,
      title={WIBA: What Is Being Argued? A Comprehensive Approach to Argument Mining}, 
      author={Arman Irani and Ju Yeon Park and Kevin Esterling and Michalis Faloutsos},
      year={2024},
      eprint={2405.00828},
      archivePrefix={arXiv},
      primaryClass={cs.CL},
      url={https://arxiv.org/abs/2405.00828}, 
}
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details. 