# Django GraphQL CRUD App

This repository contains a **Django** application integrated with **GraphQL** to perform CRUD operations for managing books. By default, the project uses SQLite as the database.

---

## Features

### Book Schema
The `Book` model contains the following fields:
- **id**: Unique identifier for the book (auto-generated).
- **title**: Title of the book (string).
- **author**: Author of the book (string).
- **created_at**: Timestamp of when the book was created.
- **updated_at**: Timestamp of when the book was last updated.

### Functionality
- **Queries**: Fetch all books or retrieve a book by its `id`.
- **Mutations**:
  - Create a new book.
  - Update an existing book by its `id`.
  - Delete a book by its `id`.

---

## Getting Started

### Prerequisites
- Python 3.9 or higher.

### Installation

1. Clone the repository:
    ```bash
    git clone git@github.com:Robben1972/Django_Graphql.git
    cd Django_Graphql
    ```

2. Create and activate a virtual environment:
    ```bash
    python -m venv venv
    source venv/bin/activate       # On Linux/Mac
    venv\Scripts\activate          # On Windows
    ```

3. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Run database migrations:
    ```bash
    python manage.py migrate
    ```

5. (Optional) Create a superuser to access the Django admin panel:
    ```bash
    python manage.py createsuperuser
    ```

---

## Running the Application

1. Start the development server:
    ```bash
    python manage.py runserver
    ```

2. Open the GraphQL Playground at:
    ```
    http://127.0.0.1:8000/graphql
    ```

3. (Optional) Access the Django Admin panel:
    ```
    http://127.0.0.1:8000/admin
    ```

---

## Folder Structure

```
.
├── books/                # Django app for book management
│   ├── migrations/       # Database migration files
│   ├── admin.py          # Admin interface configuration
│   ├── apps.py           # Application configuration
│   ├── models.py         # Book model definition
│   ├── tests.py          # Unit tests
│   ├── views.py          # Django views (if applicable)
├── core/                 # Main Django project configuration
│   ├── schema.py         # GraphQL schema and resolvers
│   ├── settings.py       # Project settings
│   ├── urls.py           # URL configuration
│   ├── asgi.py           # ASGI entry point
│   ├── wsgi.py           # WSGI entry point
├── db.sqlite3            # Default SQLite database
├── manage.py             # Django management script
├── requirements.txt      # Project dependencies
├── .gitignore            # Ignored files for Git
└── README.md             # Project documentation
```

---

## Example Queries and Mutations

### Queries

#### Fetch All Books
```graphql
query {
  books {
    id
    title
    author
    createdAt
    updatedAt
  }
}
```

#### Fetch a Book by ID
```graphql
query {
  book(id: 1) {
    id
    title
    author
    createdAt
    updatedAt
  }
}
```

### Mutations

#### Create a New Book
```graphql
mutation {
  createBook(title: "Django for Beginners", author: "William S. Vincent") {
    book {
      id
      title
      author
      createdAt
      updatedAt
    }
  }
}
```

#### Update a Book by ID
```graphql
mutation {
  updateBook(id: 1, title: "Django for APIs", author: "William S. Vincent") {
    book {
      id
      title
      author
      createdAt
      updatedAt
    }
  }
}
```

#### Delete a Book by ID
```graphql
mutation {
  deleteBook(id: 1) {
    success
    message
  }
}
```

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## Contributing

Contributions are welcome! Feel free to fork the repository and submit a pull request with your improvements.
