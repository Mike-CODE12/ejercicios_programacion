from sqlalchemy.orm import Session
from sqlalchemy import select
from models import User, Address, Car

class UsersService:
    def __init__(self, db: Session):
        self.db = db

    def create_user(self, name: str, email: str) -> User:
        user = User(name=name, email=email)
        self.db.add(user)
        self.db.commit()
        self.db.refresh(user)
        return user

    def update_user(self, user_id: int, name: str | None = None, email: str | None = None) -> User | None:
        user = self.db.get(User, user_id)
        if not user:
            return None
        if name is not None:
            user.name = name
        if email is not None:
            user.email = email
        self.db.commit()
        self.db.refresh(user)
        return user

    def delete_user(self, user_id: int) -> bool:
        user = self.db.get(User, user_id)
        if not user:
            return False
        self.db.delete(user)
        self.db.commit()
        return True

    def get_all_users(self) -> list[User]:
        return list(self.db.scalars(select(User)).all())


class CarsService:
    def __init__(self, db: Session):
        self.db = db

    def create_car(self, make: str, model: str, user_id: int | None = None) -> Car:
        car = Car(make=make, model=model, user_id=user_id)
        self.db.add(car)
        self.db.commit()
        self.db.refresh(car)
        return car

    def update_car(self, car_id: int, make: str | None = None, model: str | None = None) -> Car | None:
        car = self.db.get(Car, car_id)
        if not car:
            return None
        if make is not None:
            car.make = make
        if model is not None:
            car.model = model
        self.db.commit()
        self.db.refresh(car)
        return car

    def delete_car(self, car_id: int) -> bool:
        car = self.db.get(Car, car_id)
        if not car:
            return False
        self.db.delete(car)
        self.db.commit()
        return True

    def assign_car_to_user(self, car_id: int, user_id: int) -> Car | None:
        car = self.db.get(Car, car_id)
        user = self.db.get(User, user_id)
        if not car or not user:
            return None
        car.user_id = user_id
        self.db.commit()
        self.db.refresh(car)
        return car

    def get_all_cars(self) -> list[Car]:
        return list(self.db.scalars(select(Car)).all())


class AddressesService:
    def __init__(self, db: Session):
        self.db = db

    def create_address(self, street: str, city: str, user_id: int) -> Address:

        address = Address(street=street, city=city, user_id=user_id)
        self.db.add(address)
        self.db.commit()
        self.db.refresh(address)
        return address

    def update_address(self, address_id: int, street: str | None = None, city: str | None = None) -> Address | None:
        address = self.db.get(Address, address_id)
        if not address:
            return None
        if street is not None:
            address.street = street
        if city is not None:
            address.city = city
        self.db.commit()
        self.db.refresh(address)
        return address

    def delete_address(self, address_id: int) -> bool:
        address = self.db.get(Address, address_id)
        if not address:
            return False
        self.db.delete(address)
        self.db.commit()
        return True

    def get_all_addresses(self) -> list[Address]:
        return list(self.db.scalars(select(Address)).all())
