import os
import re
import joblib
import pandas as pd
import numpy as np
from scipy.sparse import vstack
from sklearn.metrics.pairwise import cosine_similarity
from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel, Field
from typing import List, Optional

# --- Pydantic models for request/response ---
class SuggestRequest(BaseModel):
    recent_searches: List[str] = Field(default_factory=list)
    cart_item_ids: List[str] = Field(default_factory=list)

class SuggestResponse(BaseModel):
    suggestions: List[str]

# --- Create FastAPI router ---
router = APIRouter(tags=["recommendation"])

# --- Cấu hình đường dẫn đến các file model ---
MODEL_DIR = '../../saved_model_components'
VECTORIZER_PATH = os.path.join(MODEL_DIR, 'tfidf_vectorizer.joblib')
MATRIX_PATH = os.path.join(MODEL_DIR, 'product_tfidf_matrix.joblib')
PRODUCT_INFO_PATH = os.path.join(MODEL_DIR, 'product_info_df.pkl')

# --- Model component state variables ---
vectorizer = None
product_tfidf_matrix = None
df_products = None
product_id_to_idx_map = {}

# --- Load model dependencies function ---
def load_model_components():
    global vectorizer, product_tfidf_matrix, df_products, product_id_to_idx_map

    try:
        vectorizer = joblib.load(VECTORIZER_PATH)
        product_tfidf_matrix = joblib.load(MATRIX_PATH)
        df_products = pd.read_pickle(PRODUCT_INFO_PATH)
        print("INFO: Model components loaded successfully.")
        print(f"INFO: Loaded df_products with {len(df_products)} products. Columns: {df_products.columns.tolist()}")

        # Tạo map product_id sang index để tra cứu nhanh hơn trong get_user_context_vector
        if 'id' in df_products.columns:
            product_id_to_idx_map = pd.Series(df_products.index, index=df_products['id']).to_dict()
            print("INFO: Product ID to index map created.")
        else:
            print("ERROR: 'id' column not found in df_products. Cart item processing might fail.")
            product_id_to_idx_map = {}

        return True
    except FileNotFoundError as e:
        print(f"ERROR: Could not load model components - {e}")
        print("Please ensure the 'saved_model_components' directory exists and contains:")
        print(f" - {os.path.basename(VECTORIZER_PATH)}")
        print(f" - {os.path.basename(MATRIX_PATH)}")
        print(f" - {os.path.basename(PRODUCT_INFO_PATH)}")
        return False
    except Exception as e:
        print(f"ERROR: An unexpected error occurred during model loading: {e}")
        return False

# --- Dependency to validate model components ---
def get_model_components():
    if not all([vectorizer, product_tfidf_matrix is not None, df_products is not None, product_id_to_idx_map is not None]):
        raise HTTPException(status_code=503, detail="Model components not loaded or failed to initialize. Server is not ready.")
    return {
        "vectorizer": vectorizer,
        "product_tfidf_matrix": product_tfidf_matrix,
        "df_products": df_products,
        "product_id_to_idx_map": product_id_to_idx_map
    }

# --- Helper functions (preserved from original) ---
def preprocess_text(text):
    if not isinstance(text, str):
        return ""
    text = text.lower()
    text = re.sub(r'[^\w\s]', '', text)
    text = re.sub(r'\s+', ' ', text).strip()
    return text

def get_user_context_vector(recent_searches, cart_item_ids, current_df_products, current_product_tfidf_matrix, current_vectorizer, current_product_id_to_idx_map, search_weight=0.6):
    context_vector_components = []
    processed_searches_text = ""

    if recent_searches:
        processed_searches_text = " ".join([preprocess_text(s) for s in recent_searches])
        if processed_searches_text:
            search_vector_sparse = current_vectorizer.transform([processed_searches_text])
            context_vector_components.append(search_vector_sparse.toarray() * search_weight)

    if cart_item_ids:
        temp_cart_vectors_sparse = []
        for item_id_str in cart_item_ids:
            try:
                item_id = int(item_id_str)
            except ValueError:
                print(f"WARNING: Cart item ID '{item_id_str}' is not a valid integer. Skipping.")
                continue

            if item_id in current_product_id_to_idx_map:
                idx = current_product_id_to_idx_map[item_id]
                temp_cart_vectors_sparse.append(current_product_tfidf_matrix[idx])
            else:
                print(f"WARNING: Product ID {item_id} from cart not found in product_info_df.")

        if temp_cart_vectors_sparse:
            stacked_cart_vectors_sparse = vstack(temp_cart_vectors_sparse)
            avg_cart_vector_matrix = stacked_cart_vectors_sparse.mean(axis=0)
            avg_cart_vector_dense = np.asarray(avg_cart_vector_matrix)
            weight_for_cart = (1 - search_weight) if (recent_searches and processed_searches_text) else 1.0
            context_vector_components.append(avg_cart_vector_dense * weight_for_cart)

    if not context_vector_components:
        return np.zeros((1, current_product_tfidf_matrix.shape[1]))

    user_context_vector = np.sum(context_vector_components, axis=0)
    if user_context_vector.ndim == 1:
        user_context_vector = user_context_vector.reshape(1, -1)
    return user_context_vector

def generate_search_suggestions(user_context_vector, current_product_tfidf_matrix, current_df_products, top_n=5):
    if current_df_products is None or current_df_products.empty or 'product_name' not in current_df_products.columns:
        print("ERROR: df_products is not loaded or is invalid for suggestions.")
        return ["Lỗi: Dữ liệu sản phẩm không có sẵn"]

    if np.count_nonzero(user_context_vector) == 0:
        print("INFO: No user context, returning fallback suggestions.")
        # Fallback: gợi ý ngẫu nhiên tên sản phẩm nếu df_products có sẵn
        sample_n = min(top_n, len(current_df_products))
        if sample_n > 0:
            return current_df_products['product_name'].sample(sample_n).tolist()
        return ["Không có gợi ý fallback nào."]

    try:
        similarities = cosine_similarity(user_context_vector, current_product_tfidf_matrix)
    except Exception as e:
        print(f"ERROR: Could not calculate cosine_similarity: {e}")
        return ["Lỗi khi tính toán độ tương đồng."]

    if similarities.size == 0:
        print("WARNING: Cosine similarity calculation resulted in an empty array.")
        return ["Không thể tạo gợi ý do lỗi tính toán độ tương đồng."]

    similar_product_indices = similarities[0].argsort()[-top_n:][::-1]

    valid_indices = [idx for idx in similar_product_indices if idx < len(current_df_products)]
    if not valid_indices:
        print("WARNING: No valid product indices found after similarity ranking.")
        return ["Không thể ánh xạ gợi ý tới sản phẩm."]

    suggestions = current_df_products.iloc[valid_indices]['product_name'].tolist()

    unique_suggestions = []
    for s in suggestions:
        if s not in unique_suggestions:
            unique_suggestions.append(s)
    return unique_suggestions

# --- FastAPI endpoint ---
@router.post("/suggest", response_model=SuggestResponse)
async def suggest_api(
    request: SuggestRequest,
    components: dict = Depends(get_model_components)
):
    recent_searches = request.recent_searches
    cart_item_ids_str = request.cart_item_ids

    # 1. Tạo vector ngữ cảnh người dùng
    user_vector = get_user_context_vector(
        recent_searches,
        cart_item_ids_str,
        components["df_products"],
        components["product_tfidf_matrix"],
        components["vectorizer"],
        components["product_id_to_idx_map"],
        search_weight=0.7
    )

    # 2. Tạo gợi ý
    suggestions = generate_search_suggestions(
        user_vector,
        components["product_tfidf_matrix"],
        components["df_products"],
        top_n=10
    )

    return SuggestResponse(suggestions=suggestions)

# Load model components on module import
load_model_components()