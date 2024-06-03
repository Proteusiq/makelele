![joker](https://github.com/Proteusiq/makelele/assets/14926709/760099de-4e78-475f-b4d1-c00fec0009cf)


# Makelele

Makelele (Swahili for "noise") is a simple API for retrieving random custom jokes. Built using FastAPI, it serves various categories of jokes, making it easy to integrate humor into your applications.

## Features

- Fetch random jokes by category.
- Easy to extend with new categories and quotes.
- High-performance API built with FastAPI.

## Getting Started

### Prerequisites

- Python 3.7+
- rye (Python package installer)

### Installation

1. **Clone the repository**:
```sh
git clone https://github.com/yourusername/makelele.git
cd makelele/
```
  
2. **Activate a virtual environment**:

```sh
rye sync
source .venv/bin/activate 
```

### Usage
Create your quotes.toml file:
In makelele/assets/, create a jokes.toml file with the following structure:

```toml
[jokes]
golf = [
    "Why do golf announcers whisper? Because they don’t want to wake up the people watching.",
    "I play in the low 80s. If it’s any hotter than that, I won’t play.",
    "Golf: a 5-mile walk punctuated with disappointments.",
    "In primitive society, when native tribes beat the ground with clubs and yelled, it was called witchcraft; today, in civilized society, it’s called golf."
]
```

**Run the FastAPI server**:

```sh
fastapi dev makelele/main.py
```

**Access the API**:
Open your browser and go to http://127.0.0.1:8000/joke/{category}. Replace {category} with one of the categories defined in your jokes.toml file (e.g., golf).

### API Endpoints
#### Get a Random Quote
- URL: `/joke/{category}`
- Method: `GET`
- URL Parameters: `category=[string]` (required) - The category of quotes you want to retrieve.
- Success Response:
    - Code: 200 OK
    - Content: `{"joke": "A random quote from the specified category"}`
- Error Response:
    - Code: 404 Not Found
    - Content: `{"detail": "Category not found"}`

### Extending the API
To add more categories or quotes, simply edit the quotes.toml file and restart the server.

### Contributing
Contributions are welcome! Please fork the repository and submit a pull request with your changes.

### License
This project is licensed under the MIT License.

###  Acknowledgements
FastAPI for providing an excellent framework.
___
Enjoy using Makelele and bring some noise to your applications!
