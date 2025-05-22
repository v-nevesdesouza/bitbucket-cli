# Bitbucket CLI Tool

## Features
- Create Bitbucket projects via CLI.

## Setup

### Requirements
- Python 3.10+
- Dependencies: `pip install 'typer[all]' requests python-dotenv`

### Environment
Create a `.env` file based on the provided example:

```
BITBUCKET_TOKEN=your_access_token_here
```

## Usage

```bash
python main.py new-project --workspace <your-workspace> --key <PROJECTKEY> --name "My Project"
```
