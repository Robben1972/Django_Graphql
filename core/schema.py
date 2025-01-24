import graphene
from graphene_django.types import DjangoObjectType
from books.models import Book

class BookType(DjangoObjectType):
    class Meta:
        model = Book
        fields = ("id", "title", "author", "created_at", "updated_at")


class Query(graphene.ObjectType):
    hello = graphene.String(default_value="stranger")
    books = graphene.List(BookType)
    book = graphene.Field(BookType, id=graphene.ID())

    def resolve_books(self, info):
        return Book.objects.all()
    
    def resolve_hello(self, info):
        return "world"
    
    def resolve_book(self, info, id):
        try:
            return Book.objects.get(pk=id)
        except Book.DoesNotExist:
            return None
        
class Mutation(graphene.ObjectType):
    create_book = graphene.Field(BookType, title=graphene.String(), author=graphene.String())
    update_book = graphene.Field(BookType, id=graphene.ID(), title=graphene.String(), author=graphene.String())
    delete_book = graphene.Field(graphene.Boolean, id=graphene.ID())

    def resolve_create_book(self, info, title, author):
        book = Book(title=title, author=author)
        book.save()
        return book

    def resolve_update_book(self, info, id, title, author):
        book = Book.objects.get(pk=id)
        if book:
            book.title = title
            book.author = author
            book.save()
            return book
        return None
    
    def resolve_delete_book(self, info, id):
        try:
            Book.objects.get(pk=id).delete()
            return True
        except Book.DoesNotExist:
            return False

    
schema = graphene.Schema(query=Query, mutation=Mutation)