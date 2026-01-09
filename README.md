# Working with APIs - A Practical Guide

## What You'll Learn

- How to connect to and use APIs in your Python programs
- Making HTTP requests to get data from external services
- Working with JSON responses from APIs

---

## Key Terms

- **Request**: When your program asks another computer for information over the internet
- **Client**: Your application that's asking for data or services
- **Web Server**: The computer that responds to your requests with data or services

---

## What's an API?

Think of an API (Application Programming Interface) as a waiter in a restaurant. You (the client) tell the waiter what you want from the menu, the waiter takes your order to the kitchen (the server), and brings back your food (the data).

Companies like Twitter, Google, and even your local government use APIs to share their data with developers. This lets you build amazing things:

- Let users sign in with their Google or Facebook accounts
- Show real-time weather in your app
- Find nearby restaurants using Yelp's data
- Display concert tickets from Ticketmaster
- Get public data like park locations or restaurant health ratings

APIs are everywhere, and learning to use them opens up endless possibilities for your projects.

---

## How APIs Work

Most modern APIs follow REST principles, which means they use standard web URLs (endpoints) to share data. You send a request to a specific URL, and the API sends back the information you asked for.

Let's learn by building something real - a book search app using the Open Library API.

### Getting Started with Open Library

The [Open Library API](https://openlibrary.org/dev/docs/api/search) lets us search for books and get information about them. Perfect for building a book recommendation app!

#### Testing the API in Your Browser

Before writing any code, let's see what the API returns. Copy this URL into your browser:

```
https://openlibrary.org/search.json?title=the+lord+of+the+rings
```

You'll see a bunch of data that looks like a Python dictionary - that's JSON! It contains information about books matching "The Lord of the Rings".

That's a lot of data though. Let's make it more manageable by asking for specific fields and limiting results:

```
https://openlibrary.org/search.json?title=the+lord+of+the+rings&fields=title,author_name&limit=1
```

Much better! Now you should see something clean like:

```json
{
  "numFound": 522,
  "start": 0,
  "numFoundExact": true,
  "docs": [
    {
      "title": "The Lord of the Rings",
      "author_name": ["J.R.R. Tolkien"]
    }
  ],
  "num_found": 522,
  "q": "",
  "offset": null
}
```

**Pro Tip:** Always test API URLs in your browser first. If it works there, you know the API is working correctly, and any issues are in your code.

#### Making API Requests from Python

Now let's use Python to get this same data. Check out the code in `lib/open_library_api.py`:

```python
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
```

The `requests` library handles all the complicated networking stuff for us. We just tell it what URL to visit and what parameters to send.

#### Running the Code

Try it out! In your terminal, run:

```bash
python lib/open_library_api.py
```

Enter a book title when prompted, and you'll see the API return information about that book.

### Understanding the Code

Here's what's happening:

1. **BookSearch class**: Organizes our API-related code
2. **search_books method**: Sends the actual request to the API
3. **get_book_info method**: Takes the raw API response and formats it nicely
4. **Error handling**: Uses `.get()` to safely access dictionary keys that might not exist

The `params` dictionary automatically formats our parameters correctly - no more manually replacing spaces with `+` signs!

---

## Key Takeaways

APIs are your gateway to the world's data. They let you:
- Get information from external services
- Add powerful features to your apps without building everything from scratch
- Connect your programs to real-world data

The pattern is always the same:
1. Find the API endpoint (URL)
2. Figure out what parameters it needs
3. Send a request using `requests.get()`
4. Parse the JSON response
5. Use the data in your application

Remember to always read the API documentation and test endpoints in your browser before coding. This saves tons of debugging time!

## What's Next?

Try experimenting with other APIs! Many services offer free APIs for developers to play with. Just remember to respect rate limits and terms of service.

## Resources

- [HTTP Methods (Mozilla)](https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods)
- [Python Requests Documentation](https://requests.readthedocs.io/en/latest/)
- [Working with JSON in Python](https://docs.python.org/3/library/json.html)
