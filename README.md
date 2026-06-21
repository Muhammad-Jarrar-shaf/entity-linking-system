# Entity Linking System

An NLP-powered Entity Linking System that extracts named entities from text using spaCy and links them to a knowledge base using fuzzy matching with RapidFuzz. The project exposes the functionality through a FastAPI REST API and includes automated testing with Pytest.

## Features

* Named Entity Recognition (NER) using spaCy
* Entity Linking with RapidFuzz similarity matching
* Custom Knowledge Base integration
* FastAPI REST API
* Interactive Swagger Documentation
* Automated Testing with Pytest
* Modular and Production-Oriented Project Structure

## Project Architecture

```text
Input Text
    │
    ▼
spaCy NER
    │
    ▼
Entity Extraction
    │
    ▼
RapidFuzz Matching
    │
    ▼
Knowledge Base Lookup
    │
    ▼
Linked Entities
```

## Tech Stack

* Python 3.12
* spaCy
* RapidFuzz
* FastAPI
* Pandas
* Pytest
* Uvicorn

## Project Structure

```text
entity-linking-system/
│
├── api/
│   └── main.py
│
├── app/
│   ├── kb.py
│   ├── linker.py
│   ├── ner.py
│   └── utils.py
│
├── data/
│   └── knowledge_base.csv
│
├── tests/
│   ├── test_api.py
│   ├── test_entity_linker.py
│   ├── test_fuzzy_match.py
│   ├── test_kb_loader.py
│   ├── test_ner.py
│   └── test_pipeline.py
│
├── requirements.txt
├── pytest.ini
└── README.md
```

## Installation

### Clone Repository

```bash
git clone https://github.com/yourusername/entity-linking-system.git
cd entity-linking-system
```

### Create Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Download spaCy Model

```bash
python -m spacy download en_core_web_sm
```

## Running the API

```bash
uvicorn api.main:app --reload
```

API will be available at:

```text
http://127.0.0.1:8000
```

Swagger Documentation:

```text
http://127.0.0.1:8000/docs
```

## Example Request

### POST /link

Request:

```json
{
  "text": "Elon Musk visited Pakistan."
}
```

Response:

```json
{
  "entities": [
    {
      "entity": "Elon Musk",
      "matched_entity": "Elon Musk",
      "score": 100.0,
      "url": "https://en.wikipedia.org/wiki/Elon_Musk",
      "label": "PERSON"
    },
    {
      "entity": "Pakistan",
      "matched_entity": "Pakistan",
      "score": 100.0,
      "url": "https://en.wikipedia.org/wiki/Pakistan",
      "label": "GPE"
    }
  ]
}
```

## Running Tests

```bash
pytest -v
```

Current Status:

```text
7 Passed Tests
```

## Learning Outcomes

Through this project, I learned:

* Named Entity Recognition (NER)
* Entity Linking
* Knowledge Bases
* Fuzzy Matching
* API Development with FastAPI
* Software Testing with Pytest
* Professional Project Structuring
* Git Version Control

## Future Improvements

* Wikipedia API Integration
* Neo4j Knowledge Graph Integration
* Confidence Threshold Filtering
* Entity Disambiguation
* Semantic Similarity using Sentence Transformers

## Author

Muhammad Jarrar Shaf

100 Projects in 100 Days Challenge – Project 15
