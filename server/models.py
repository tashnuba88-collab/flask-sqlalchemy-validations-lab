from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import validates

db = SQLAlchemy()

class Author(db.Model):
    __tablename__ = 'authors'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True, nullable=False)
    phone_number = db.Column(db.String)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    posts = db.relationship('Post', backref='author', cascade='all, delete-orphan')

    @validates('name')
    def validate_name(self, key, value):
        if not value or not value.strip():
            raise ValueError("Author must have a name.")
        if Author.query.filter_by(name=value).first():
            raise ValueError("Author name must be unique.")
        return value

    @validates('phone_number')
    def validate_phone_number(self, key, value):
        if not value or len(value) != 10 or not value.isdigit():
            raise ValueError("Author phone numbers must be exactly ten digits.")
        return value

    def __repr__(self):
        return f'Author(id={self.id}, name={self.name})'


class Post(db.Model):
    __tablename__ = 'posts'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    content = db.Column(db.Text)
    category = db.Column(db.String)
    summary = db.Column(db.String)
    author_id = db.Column(db.Integer, db.ForeignKey('authors.id'))
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    @validates('title')
    def validate_title(self, key, value):
        clickbait_phrases = ["Won't Believe", "Secret", "Top", "Guess"]
        if not value or not any(phrase in value for phrase in clickbait_phrases):
            raise ValueError("Post title must be clickbait-y and contain one of: 'Won't Believe', 'Secret', 'Top', or 'Guess'.")
        return value

    @validates('content')
    def validate_content(self, key, value):
        if not value or len(value) < 250:
            raise ValueError("Post content must be at least 250 characters long.")
        return value

    @validates('summary')
    def validate_summary(self, key, value):
        if value is not None and len(value) > 250:
            raise ValueError("Post summary must be a maximum of 250 characters.")
        return value

    @validates('category')
    def validate_category(self, key, value):
        allowed_categories = ["Fiction", "Non-Fiction"]
        if value not in allowed_categories:
            raise ValueError("Post category must be either Fiction or Non-Fiction.")
        return value

    def __repr__(self):
        return f'Post(id={self.id}, title={self.title}, content={self.content}, summary={self.summary})'