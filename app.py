import streamlit as st
import pandas as pd
import os
import glob

# ==========================================
# 1. تحميل البيانات (معالجة مشاكل المسارات)
# ==========================================
@st.cache_data
def load_data():
    # تحديد المجلد الحالي الذي يوجد فيه ملف app.py
    current_dir = os.path.dirname(os.path.abspath(__file__))
    
    # دالة ذكية للبحث عن الملف سواء كان في نفس المجلد أو داخل مجلد archive
    def find_file(base_name):
        match = glob.glob(os.path.join(current_dir, base_name))
        if not match:
            match = glob.glob(os.path.join(current_dir, 'archive', base_name))
        if not match:
            raise FileNotFoundError(f"Could not find {base_name}. Make sure it's in the same folder as app.py or inside an 'archive' folder.")
        return match[0]

    # تحميل الجداول الأساسية
    products = pd.read_csv(find_file('products.csv'))
    aisles = pd.read_csv(find_file('aisles.csv'))
    order_file = find_file('order_products*_prior.csv')
    order_products = pd.read_csv(order_file)
    
    # محاولة تحميل خطة الرفوف (نتيجة K-Means) - إذا لم يجدها لن يكسر التطبيق
    try:
        shelf_plan = pd.read_csv(find_file('shelf_plan.csv'))
    except:
        shelf_plan = None
        
    # للحفاظ على سرعة التطبيق، نأخذ أعلى 5000 منتج مبيعاً فقط كقاعدة بيانات للبحث
    top_prods = order_products['product_id'].value_counts().head(5000).index
    filtered_ops = order_products[order_products['product_id'].isin(top_prods)]
    
    return products, aisles, filtered_ops, shelf_plan

# استدعاء الدالة
products, aisles, order_products, shelf_plan = load_data()

# دمج اسم القسم مع المنتجات لتسهيل العرض
products = products.merge(aisles, on='aisle_id', how='left')


# ==========================================
# 2. واجهة المستخدم (UI)
# ==========================================
st.set_page_config(page_title="Shelf-Space Allocation", page_icon="🛒", layout="centered")
st.title("🛒 Shelf-Space: Product Affinity Lookup")
st.markdown("An AI-powered tool to discover which products should be placed together on retail shelves.")
st.divider()

# صندوق البحث
product_search = st.text_input("Enter Product Name (e.g., Banana, Organic Milk, Chips):")

if product_search:
    # البحث عن المنتجات المطابقة
    matched_products = products[products['product_name'].str.contains(product_search, case=False, na=False)]
    
    if not matched_products.empty:
        # قائمة منسدلة لاختيار منتج محدد إذا كانت هناك تشابهات
        selected_product = st.selectbox("Select exact product:", matched_products['product_name'].values)
        
        # استخراج بيانات المنتج المختار
        prod_data = matched_products[matched_products['product_name'] == selected_product].iloc[0]
        selected_id = prod_data['product_id']
        selected_aisle = prod_data['aisle']
        
        # ==========================================
        # 3. منطق الشراء المشترك (Micro Layout)
        # ==========================================
        # استخراج الطلبات التي تحتوي على هذا المنتج
        target_orders = order_products[order_products['product_id'] == selected_id]['order_id'].unique()
        
        # استخراج باقي المنتجات في نفس الطلبات
        complementary = order_products[(order_products['order_id'].isin(target_orders)) & 
                                       (order_products['product_id'] != selected_id)]
        
        # حساب التكرار واختيار أعلى 10 منتجات مكملة
        top_comps = complementary.merge(products, on='product_id')['product_name'].value_counts().head(10)
        
        # عرض النتائج في جدول
        st.subheader(f"Top 10 Complementary Products for '{selected_product}':")
        df_display = top_comps.reset_index().rename(columns={'index': 'Complementary Product', 'product_name': 'Co-purchase Frequency'})
        st.dataframe(df_display, use_container_width=True)
        
        # التوصية التشغيلية للمكان على الرف
        st.success("💡 **Shelf Action:** Place these items in the same eye-level aisle section or use them for cross-promotional end-caps.")
        
        # ==========================================
        # 4. ربط نتائج K-Means (Macro Layout)
        # ==========================================
        if shelf_plan is not None:
            # البحث عن رقم الـ Cluster الخاص بقسم هذا المنتج
            cluster_row = shelf_plan[shelf_plan['Aisle'] == selected_aisle]
            
            if not cluster_row.empty:
                cluster_num = cluster_row['Cluster'].values[0]
                st.info(f"🏢 **Macro-Layout Data:** This product belongs to the *'{selected_aisle}'* aisle. "
                        f"Based on K-Means clustering, this aisle is assigned to **Shelf Cluster {cluster_num}**, "
                        f"meaning it should be physically located near other aisles in this cluster.")
            else:
                st.info(f"🏢 **Macro-Layout Data:** This product is in the *'{selected_aisle}'* aisle.")
    else:
        st.warning("⚠️ No products found. Try another name (e.g., 'Banana', 'Milk', 'Eggs').")
else:
    st.info("👆 Type a product name above to get started.")