
# Movie Recommender System 🎬

## Introduction
The **Movie Recommender System** is a Streamlit-based web application that suggests movies similar to the one selected by the user. It uses a precomputed similarity matrix to generate recommendations and fetches movie posters from **The Movie Database (TMDB) API**.

## Features
✅ **Movie Search**: Select a movie from a dropdown list.
✅ **Personalized Recommendations**: Get 5 similar movie suggestions.
✅ **Movie Posters**: Displays posters for each recommended movie.


## Tech Stack
- **Python**
- **Streamlit** (for UI)
- **Pandas** (for data handling)
- **Pickle** (for storing movie data and similarity matrix)
- **Requests** (for fetching movie posters via TMDB API)

## Installation
### 1. Clone the Repository
```sh
git clone https://github.com/your-username/movie-recommender.git
cd movie-recommender
```

### 2. Create a Virtual Environment (Optional but Recommended)
```sh
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies
```sh
pip install -r requirements.txt
```



## How It Works
1. The app **unzips `data.zip`** automatically when it starts.
2. It loads **movie data and similarity scores** from extracted `.pkl` files.
3. When a user selects a movie, the app finds **5 similar movies**.
4. Movie posters are fetched using the **TMDB API**.

## API Key Setup
The app requires an **API key from TMDB** to fetch movie posters. You can get one from [TMDB API](https://www.themoviedb.org/documentation/api).

Replace the API key in `app.py`:
```python
API_KEY = "your_tmdb_api_key"
```

## Example Output
![Movie Recommender Screenshot](<img width="1498" alt="Screenshot 2025-02-04 at 9 21 20 AM" src="https://github.com/user-attachments/assets/acab5276-36b9-4363-9307-9639f8aa5774" />
)

## Future Improvements
- 🎯 **Improve Recommendation Algorithm** using deep learning.
- 🌎 **Add Genre-based Recommendations**.
- 🔍 **Enhance Search & Filtering Options**.

## License
This project is **open-source** and available under the [MIT License](LICENSE).

## Contributors
👤 **[Your Name]** - *Developer & Maintainer*

---
Made with ❤️ using **Streamlit & Python**

