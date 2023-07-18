import streamlit as st
import json
import os
from random import randint

st.set_page_config(
    page_title="Что покушать?",
    page_icon="🍔",
)
st.header("🍔 Что покушать?")
#distance: 1 - Не нужно ехать, 2 - Васька, 3 - Примерно Восстания, 4 - Очень далеко
with open(f"{os.path.dirname(__file__)}/tables/places.json", encoding="utf-8") as f:
    PLACES_TABLE = json.load(f)

def get_products_types():
    product_types = []
    for place, content in PLACES_TABLE.items():
        products = content["product_type"].split(", ")
        for product in products:
            if not product in product_types:
                product_types.append(product)
    return product_types

def get_cuisine_types():
    cuisine_types = []
    for place, content in PLACES_TABLE.items():
        cuisines = content["cuisine_type"].split(", ")
        for cuisine in cuisines:
            if not cuisine in cuisine_types:
                cuisine_types.append(cuisine)
    return cuisine_types

def get_distance_types():
    distance_types = []
    for place, content in PLACES_TABLE.items():
        distances = content["distance"].split(", ")
        for distance in distances:
            if not distance in distance_types:
                distance_types.append(distance)
    return distance_types

def check_elements(check_list: list, check_string: str):
    if not check_list:
        return True
    for element in check_list:
        if element in check_string:
            return True
    return False


if __name__ == "__main__":
    selected_cuisines = st.multiselect("Выбери кухни (логическое ИЛИ):", get_cuisine_types())
    selected_products = st.multiselect("Выбери блюда (логическое ИЛИ):", get_products_types())
    selected_distance = st.multiselect("Выбери дистанцию (логическое ИЛИ):", get_distance_types())
    need_delivery = st.selectbox("Выбери, нужна ли доставка", ["", "Нужна доставка", "Пойду внутрь"])
    if st.button("Ролл!"):
        selected_places_table = []
        for place, content in PLACES_TABLE.items():
            if (need_delivery == "Нужна доставка" and content["can_deliver"] == "False") or (need_delivery == "Пойду внутрь" and content["can_eat_inside"] == "False"):
                continue
            if check_elements(selected_cuisines, content["cuisine_type"]) and check_elements(selected_products, content["product_type"]) and check_elements(selected_distance, content["distance"]):
                selected_places_table.append(place)
        st.success(selected_places_table[randint(0, len(selected_places_table) - 1)])
            

    

