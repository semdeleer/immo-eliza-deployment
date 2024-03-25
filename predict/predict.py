import pickle
import pandas as pd

modelb = open(r"./predict/model_pickle_b", "rb")
modelb = pickle.load(modelb)


def predict(postalcode: int, property_type: str, property_subtype: str, type_of_sale: str,  living_area: float, kitchen_type: str, fully_equipped_kitchen: float, open_fire: int, terrace: int, terrace_area: float, garden: float, garden_area: float, surface_of_good: float, number_of_facades: int, swimming_pool: float, state_of_building: str, main_city: str, province: str):
    house_data = {'postal_code' :[postalcode],'property_type' :[property_type],'property_subtype' :[property_subtype],'type_of_sale':[type_of_sale],'living_area':[living_area],'kitchen_type':[kitchen_type],'fully_equipped_kitchen':[fully_equipped_kitchen],'open_fire':[open_fire],'terrace':[terrace],'terrace_area':[terrace_area],'garden':[garden],'garden_area':[garden_area],'surface_of_good':[surface_of_good],'number_of_facades':[number_of_facades],'swimming_pool':[swimming_pool],'state_of_building':[state_of_building],'main_city':[main_city], "province":[province]}
    test_df = pd.DataFrame(house_data)
    bpr = modelb.predict(test_df)
    return bpr

#print(f"bagging regressor model:{predict()}")