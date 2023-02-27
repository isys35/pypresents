class Author_Book(Base):
    __tablename__ = 'author_book'
    id = Column(Integer, primary_key=True)
    author_id =  Column(Integer(), ForeignKey("authors.id"))
    book_id =  Column(Integer(), ForeignKey("books.id"))
    extra_data = Column(String(100))

class Author(Base):
    __tablename__ = 'authors'
    id = Column(Integer, primary_key=True)
    first_name = Column(String(100), nullable=False)
    last_name = Column(String(100), nullable=False)
    books = relationship("Author_Book", backref='author')

class Book(Base):
    __tablename__ = 'books'
    id = Column(Integer, primary_key=True)
    title = Column(String(100), nullable=False)
    copyright = Column(SmallInteger, nullable=False)
    authors = relationship("Author_Book", backref="book")
