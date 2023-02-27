author_book = Table('author_book', Base.metadata,
    Column('author_id', Integer(), ForeignKey("authors.id")),
    Column('book_id', Integer(), ForeignKey("books.id"))
)

class Author(Base):
    __tablename__ = 'authors'
    id = Column(Integer, primary_key=True)
    first_name = Column(String(100), nullable=False)
    last_name = Column(String(100), nullable=False)


class Book(Base):
    __tablename__ = 'books'
    id = Column(Integer, primary_key=True)
    title = Column(String(100), nullable=False)
    copyright = Column(SmallInteger, nullable=False)
    author_id = Column(Integer, ForeignKey('authors.id'))
    author = relationship("Author", secondary=author_book, backref="books")
