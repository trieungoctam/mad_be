# Import all the models, so that Base has them before being
# imported by Alembic
from app.db.base_class import Base
from app.models.user import User
from app.models.favorite import Favorite
from app.models.address import Address
from app.models.product import Product, ProductVariant, ProductImage
from app.models.category import Category
from app.models.brand import Brand
# from app.models.store import Store
from app.models.cart import Cart, CartItem
from app.models.order import Order, OrderItem, OrderStatus, PaymentStatus
from app.models.search_history import SearchHistory
from app.models.barcode_scan_history import BarcodeScanHistory
from app.models.product_recommendation import ProductRecommendation, RecommendationType
from app.models.product_review import ProductReview
from app.models.notification import Notification, NotificationType
from app.models.payment_setting import PaymentSettings
from app.models.user_preference import UserPreference
from app.models.promotion import Promotion, DiscountType
from app.models.shopping_list import ShoppingList, ListItem, SharedList
from app.models.transaction import TransactionHistory, TransactionStatus, TransactionType
from app.models.purchase_history import PurchaseHistory
from app.models.user_settings import UserSettings
from app.models.shipment import Shipment, ShipmentTrackingEvent, ShipmentStatus