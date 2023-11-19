from abc import ABC, abstractmethod
from sqlalchemy import select
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
    async def add_product_by_supermarket_id(supermarket_id: int, product: ProductIn):
        supermarket = await SupermarketRepository.get_by_id(supermarket_id)

        async with AsyncSessionLocal() as session:
            product = Product(
                name = product.name,
                brand = product.brand,
                description = product.description,
                unit_weight_grams = product.unit_weight_grams,
                total_weight_grams = product.total_weight_grams,
                quantity_units = product.quantity_units,
                is_active = product.is_active,
                expiration_date = product.expiration_date,
                url_product_img = product.url_product_img,
                url_expiration_date_img = product.url_expiration_date_img,
            )
            
            product.supermarket = supermarket

            session.add(product)
            await session.commit()
            await session.refresh(product)

        return product
