class C(ABC):
   @classmethod
   @abstractmethod
   def my_abstract_classmethod(cls):
       ...

   @staticmethod
   @abstractmethod
   def my_abstract_staticmethod():
       ...

   @property
   @abstractmethod
   def my_abstract_property(self):
       ...

   @my_abstract_property.setter
   @abstractmethod
   def my_abstract_property(self, val):
       ...