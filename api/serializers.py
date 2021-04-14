from rest_framework import serializers
from .models import Book, Author, Category

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'

class AuthorShortSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['name']

class CategoryShortSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['name']

class BookSerialzer(serializers.ModelSerializer):
    authors = AuthorShortSerializer(many=True, read_only=True)
    categories = CategoryShortSerializer(many=True, read_only=True)
    class Meta:
        model = Book
        fields = '__all__'
        depth = 2