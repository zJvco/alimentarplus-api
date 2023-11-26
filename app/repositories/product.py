from abc import ABC, abstractmethod
from sqlalchemy import select, update, delete
from sqlalchemy.exc import IntegrityError

from app.database import AsyncSessionLocal
from app.models.products import Product
from app.models.supermarkets import Supermarket
from app.schemas.supermarket import SupermarketIn
from app.repositories.supermarket import SupermarketRepository
from app.schemas.product import ProductIn

class ProductRepository():

    @abstractmethod
    async def get_all_products_by_supermarket_id(supermarket_id: int):
        async with AsyncSessionLocal() as session:
            query = select(Product).where(Supermarket.id == supermarket_id)
            result = await session.execute(query)

        return result.scalars().fetchall()
    
    @abstractmethod
    async def get_product_by_supermarket_id(supermarket_id: int, product_id: int):
        async with AsyncSessionLocal() as session:
            query = select(Product).where(Supermarket.id == supermarket_id, Product.id == product_id)
            result = await session.execute(query)

        return result.scalar()
    
    @abstractmethod
    async def add_product_by_supermarket_id(supermarket_id: int, product_data: ProductIn):
        supermarket = await SupermarketRepository.get_by_id(supermarket_id)

        async with AsyncSessionLocal() as session:
            product = Product(
                name = product_data.name,
                brand = product_data.brand,
                description = product_data.description,
                unit_weight_grams = product_data.unit_weight_grams,
                total_weight_grams = product_data.total_weight_grams,
                quantity_units = product_data.quantity_units,
                is_active = product_data.is_active,
                expiration_date = product_data.expiration_date,
                url_product_img = product_data.url_product_img,
                url_expiration_date_img = product_data.url_expiration_date_img,
            )
            
            product.supermarket = supermarket

            session.add(product)
            await session.commit()
            await session.refresh(product)

        return product

    @abstractmethod
    async def update(id: int, data: dict):
        async with AsyncSessionLocal() as session:
            query = update(Product).where(Product.id == id).values(data)
            await session.execute(query)
            await session.commit()  

        return id
    
    @abstractmethod
    async def delete(id: int):
        async with AsyncSessionLocal() as session:
            query = delete(Product).where(Product.id == id)
            await session.execute(query)
            await session.commit()
        
        return id
    
    @abstractmethod
    async def get_by_id(id: int):
        async with AsyncSessionLocal() as session:
            query = select(Product).where(Product.id == id)
            result = await session.execute(query)

        return result.scalar()
    
    @abstractmethod
    async def get_all():
        async with AsyncSessionLocal() as session:
            query = select(Product)
            result = await session.execute(query)

        return result.scalars().fetchall()