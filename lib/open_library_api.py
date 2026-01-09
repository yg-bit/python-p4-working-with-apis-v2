
import requests
import json

class BookSearch:
    def __init__(self):
        self.base_url = "https://openlibrary.org/search.json"
    
    def search_books(self, title, limit=1):
        """Search for books by title and return JSON data"""
        params = {
            'title': title,
            'fields': 'title,author_name',
            'limit': limit
        }
        
        response = requests.get(self.base_url, params=params)
        return response.json()
    
    def get_book_info(self, title):
        """Get formatted book information"""
        data = self.search_books(title)
        
        if data['docs']:
            book = data['docs'][0]
            title = book.get('title', 'Unknown Title')
            author = book.get('author_name', ['Unknown Author'])[0]
            return f"Title: {title}\nAuthor: {author}"
        else:
            return "No books found."

# Example usage
if __name__ == "__main__":
    searcher = BookSearch()
    
    # Try searching for a book
    book_title = input("Enter a book title: ")
    result = searcher.get_book_info(book_title)
    print("\nSearch Result:")
    print(result)

