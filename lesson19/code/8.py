class Author(Base):
    __tablename__ = 'authors'
    id = Column(Integer, primary_key=True)
    first_name = Column(String(100), nullable=False)
    last_name = Column(String(100), nullable=False)
    books = relationship("Book")

class Book(Base):
    __tablename__ = 'books'
    id = Column(Integer, primary_key=True)
    title = Column(String(100), nullable=False)
    copyright = Column(SmallInteger, nullable=False)
    author_id = Column(Integer, ForeignKey('authors.id'))