import sqlite3
import requests

# Function to fetch book information from Google Books API
def fetch_book_info(query):
    base_url = "https://www.googleapis.com/books/v1/volumes"
    params = {'q': query}
    response = requests.get(base_url, params=params)

    return response.json() if response.status_code == 200 else None

# Function to insert book information into SQLite database
def insert_book_into_db(book_info):
    connection = sqlite3.connect('instance/mydb.db')  # Replace with your SQLite database file
    cursor = connection.cursor()

    # Assuming you have a table named 'books' with columns 'title' and 'author'
    for item in book_info.get('items', []):
        volume_info = item.get('volumeInfo', {})
        title = volume_info.get('title', 'Unknown Title')
        authors = ', '.join(volume_info.get('authors', ['Unknown Author']))
        description = volume_info.get('description',' ')
        status = "Available"

        cursor.execute("INSERT INTO book (title, author,description,status) VALUES (?, ?, ?, ?)", (title, authors,description,status))

    connection.commit()
    connection.close()

if __name__ == "__main__":
    # Replace 'YOUR_API_KEY' with the API key you obtained from the Google Cloud Console
    api_key = 'AIzaSyCEeb41Ijf-MP0axK_eXcZxkWCpMfeLe4U'
    # query = 'Python programming'  # Replace with your desired query
    query = input('Enter the book :- ')

    # warlus operator := 
    if book_info := fetch_book_info(query):
        insert_book_into_db(book_info)
        print("Books inserted into the database successfully!")
    else:
        print("Error occurred while fetching data.")
