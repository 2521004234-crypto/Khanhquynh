import streamlit as st

st.set_page_config(page_title="Hệ thống Order Nhà Hàng", layout="wide")

st.sidebar.title("Chọn trang hệ thống")
page = st.sidebar.radio("", ["Order", "Admin"])

if page == "Order":
    st.title("🍽️ Hệ thống Order Nhà Hàng_Ms Quỳnh")
    st.caption("Ghi nhận order nhanh chóng và chính xác theo thời gian thực")

    col1, col2 = st.columns([1, 1])

    with col1:
        st.subheader("Chọn Món")
        table = st.selectbox("Chọn số bàn", ["Bàn 1", "Bàn 2", "Bàn 3", "Bàn 4"])
        category = st.selectbox("Chọn loại:", ["Đồ ăn", "Đồ uống"])
        item = st.selectbox("Chọn món:", ["Pizza Hải Sản", "Mì Ý", "Trà sữa", "Cà phê"])
        quantity = st.number_input("Số lượng:", min_value=1, value=1)
        
        if st.button("Thêm vào giỏ"):
            st.success(f"Đã thêm {quantity} {item} vào giỏ hàng cho {table}!")

    with col2:
        st.subheader("Giỏ hàng hiện tại")
        st.info("Giỏ hàng đang trống. Hãy chọn món ăn/đồ uống bên trái để lên đơn.")

elif page == "Admin":
    st.title("Trang Quản Trị (Admin)")
    st.write("Quản lý danh sách món và báo cáo doanh thu.")
