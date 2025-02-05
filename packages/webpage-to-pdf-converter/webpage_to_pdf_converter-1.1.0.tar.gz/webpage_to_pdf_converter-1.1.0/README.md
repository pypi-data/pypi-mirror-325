# Webpage2PDF

A CLI tool to check URLs and save webpages as PDFs with advanced error handling and retry mechanisms.

## Installation

```bash
pip install -e .
```

## Installation from PyPI

```bash
pip install webpage-to-pdf-converter
```

## Features

- URL reachability checking with retry mechanism
- PDF generation from webpage screenshots
- Progress indicators and detailed logging
- Docker support with volume mounting
- Error handling with detailed messages
- Configurable timeouts and retries

## Usage

Basic URL checking:
```bash
webpage-to-pdf https://example.com
```

Save as PDF with custom settings:
```bash
webpage-to-pdf https://example.com --save-pdf --output output.pdf --timeout 60
```

## Docker

Build the Docker image:
```bash
docker build -t url-checker .
```

### Running with Docker

1. Create a local output directory:
```bash
mkdir -p output
```

2. Run the container with volume mount:
```bash
docker run --rm -v $(pwd)/output:/app/output url-checker https://example.com --save-pdf --output /app/output/webpage.pdf
```

The PDF file will be saved in your local `output` directory. The tool will show both the container path and the absolute path of the generated file:

```
✓ PDF saved successfully as '/app/output/webpage.pdf'
File location: /app/output/webpage.pdf
```

## Using the Program with Docker

After building the image, you can run the container to check a URL directly. For example, to check "https://example.com" and save the webpage as a PDF, run:
```bash
docker run --rm url-checker https://example.com --save-pdf
```

## Release History

- 1.1.0 (2024-02-05)
  - Added retry mechanism with exponential backoff
  - Improved error handling and logging
  - Added progress indicators
  - Better Docker volume support
  - Chrome compatibility fixes

- 1.0.0 (2024-03-XX)
  - Initial release
  - URL reachability checking
  - PDF generation from webpages
  - Docker support
  - Chrome/Chromium support

## CI/CD

This project utilizes GitHub Actions for continuous integration.
Refer to [ci.yml](.github/workflows/ci.yml) for workflow details.

## Development

Install development dependencies:
```bash
pip install -e ".[test]"
```

Run tests:
```bash
pytest
```
````
