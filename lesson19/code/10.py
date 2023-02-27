class Author(Base):
    __tablename__ = 'authors'
    id = Column(Integer, primary_key=True)
    first_name = Column(String(100), nullable=False)
    last_name = Column(String(100), nullable=False)
    books = relationship("Book", backref="book")
