import numpy
import pickle
import streamlit as st
import pandas as pd

modelb = open(r"./predict/model_pickle_b", "rb")
modelb = pickle.load(modelb)

#creating a dunction for Prediction
def house_predict(postalcode: int, property_type: str, property_subtype: str, type_of_sale: str,  living_area: float, kitchen_type: str, fully_equipped_kitchen: float, open_fire: int, terrace: int, terrace_area: float, garden: float, garden_area: float, surface_of_good: float, number_of_facades: int, swimming_pool: float, state_of_building: str, main_city: str, province: str):
    house_data = {'postal_code' :[postalcode],'property_type' :[property_type],'property_subtype' :[property_subtype],'type_of_sale':[type_of_sale],'living_area':[living_area],'kitchen_type':[kitchen_type],'fully_equipped_kitchen':[fully_equipped_kitchen],'open_fire':[open_fire],'terrace':[terrace],'terrace_area':[terrace_area],'garden':[garden],'garden_area':[garden_area],'surface_of_good':[surface_of_good],'number_of_facades':[number_of_facades],'swimming_pool':[swimming_pool],'state_of_building':[state_of_building],'main_city':[main_city], "province":[province]}
    test_df = pd.DataFrame(house_data)
    bpr = modelb.predict(test_df)
    return bpr


def main():

    # Giving a title
    st.title("House Prediction web APP")

    # getting the input data from the user

    postalcode = st.text_input("postalcode")
    property_type = st.text_input("property_type")
    property_subtype = st.text_input("property_subtype")
    type_of_sale = st.text_input("type_of_sale")
    living_area = st.text_input("living_area")
    kitchen_type = st.text_input("kitchen_type")
    fully_equipped_kitchen = st.text_input("fully_equipped_kitchen")
    open_fire = st.text_input("open_fire")
    terrace = st.text_input("terrace")
    terrace_area = st.text_input("terrace_area")
    garden = st.text_input("garden")
    garden_area = st.text_input("garden_area")
    surface_of_good = st.text_input("surface_of_good")
    number_of_facades = st.text_input("number_of_facades")
    swimming_pool = st.text_input("swimming_pool")
    state_of_building = st.text_input("state_of_building")
    main_city = st.text_input("main_city")
    province = st.text_input("province")

    # code for prediction
    price = ''

    #creating a button for prediction
    if st.button('price result'):
       price = house_predict(postalcode, property_type, property_subtype, type_of_sale,  living_area, kitchen_type, fully_equipped_kitchen, open_fire, terrace, terrace_area, garden, garden_area, surface_of_good, number_of_facades, swimming_pool, state_of_building, main_city, province)

    st.success(price)


if __name__ == '__main__':
    main()