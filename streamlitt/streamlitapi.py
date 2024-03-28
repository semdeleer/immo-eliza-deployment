import numpy
import pickle
import streamlit as st
import pandas as pd
import json
import requests

modelb = open(r"../streamlitt/model_pickle_b", "rb")
modelb = pickle.load(modelb)

#creating a dunction for Prediction
def house_predict(postalcode: int, property_type: str, property_subtype: str, type_of_sale: str,  living_area: float, kitchen_type: str, fully_equipped_kitchen: float, open_fire: int, terrace: int, terrace_area: float, garden: float, garden_area: float, surface_of_good: float, number_of_facades: int, swimming_pool: float, state_of_building: str, main_city: str, province: str):
    house_data = {'postal_code' :[postalcode],'property_type' :[property_type],'property_subtype' :[property_subtype],'type_of_sale':[type_of_sale],'living_area':[living_area],'kitchen_type':[kitchen_type],'fully_equipped_kitchen':[fully_equipped_kitchen],'open_fire':[open_fire],'terrace':[terrace],'terrace_area':[terrace_area],'garden':[garden],'garden_area':[garden_area],'surface_of_good':[surface_of_good],'number_of_facades':[number_of_facades],'swimming_pool':[swimming_pool],'state_of_building':[state_of_building],'main_city':[main_city], "province":[province]}
    test_df = pd.DataFrame(house_data)
    bpr = modelb.predict(test_df)
    return bpr




    # Giving a title
st.title("House Prediction web APP")

    # getting the input data from the user

postalcode = st.text_input("postalcode")
property_type = st.selectbox(label = "Choose the type of property",index=None, options=["HOUSE"])
property_subtype = st.selectbox(label = "Choose the subtype of property",index=None, options=['HOUSE', 'MIXED_USE_BUILDING', 'APARTMENT_BLOCK', 'BUNGALOW', 'VILLA','EXCEPTIONAL_PROPERTY' ,'COUNTRY_COTTAGE' ,'MANSION', 'FARMHOUSE','TOWN_HOUSE' ,'MANOR_HOUSE', 'CHALET', 'OTHER_PROPERTY' ,'CASTLE'])
type_of_sale = st.selectbox(label = "How do you want to sell your house",index=None, options=['BUY_REGULAR' ,'PUBLIC_SALE' ,'LIFE_ANNUITY'])
living_area = st.text_input("living_area")
kitchen_type = st.selectbox(label = "What is the kitchen type",index=None, options=['INSTALLED', 'USA_HYPER_EQUIPPED', 'NOT_INSTALLED' ,'HYPER_EQUIPPED',
 'SEMI_EQUIPPED' ,'USA_SEMI_EQUIPPED','USA_INSTALLED', 'USA_UNINSTALLED'])
fully_equipped_kitchen = st.text_input("fully_equipped_kitchen")
open_fire = st.text_input("open_fire")
terrace = st.text_input("terrace")
terrace_area = st.text_input("terrace_area")
garden = st.text_input("garden")
garden_area = st.text_input("garden_area")
surface_of_good = st.text_input("surface_of_good")
number_of_facades = st.selectbox(label = "How many wall's are free of your house?",index=None, options=[1,2,3,4])
swimming_pool = st.text_input("swimming_pool")
state_of_building = st.selectbox(label = "How is the state of your home?",index=None, options=['GOOD' ,'AS_NEW' ,'TO_BE_DONE_UP', 'TO_RENOVATE','JUST_RENOVATED',
 'TO_RESTORE'])
main_city = st.selectbox(label = "What is the city the house is located in?",index=None, options=[
    'ronse', 'merelbeke', 'trooz', 'ottignies-louvain-la-neuve', 'antwerpen',
    'huy', 'liège', 'marchin', 'oupeye', 'elsene', 'erpe-mere', 'beyne-heusay',
    'halle', 'rixensart', 'vorst', 'ukkel', 'courcelles', 'châtelet', 'brugge',
    'poperinge', 'nieuwpoort', 'anderlecht', 'tessenderlo', 'wevelgem', 'kuurne',
    'schilde', 'nijlen', 'blankenberge', 'geraardsbergen', 'knokke-heist',
    'oostende', 'spa', 'sint-gillis-waas', 'steenokkerzeel', 'sint-niklaas',
    'dilbeek', 'berloz', 'wetteren', 'gent', 'seraing', 'bonheiden', 'evergem',
    'deinze', 'amay', 'affligem', 'kruisem', 'braives', 'charleroi', 'gerpinnes',
    'amel', 'ittre', 'ham', 'ath', 'wielsbeke', 'aalst', 'mechelen', 'brussel',
    'messancy', 'vilvoorde', 'villers-le-bouillet', 'burdinne', 'maarkedal',
    'overijse', 'meise', 'brakel', 'nassogne', 'herstal', "braine-l'alleud",
    'puurs-sint-amands', 'havelange', 'londerzeel', 'walcourt', 'andenne',
    'manhay', 'beringen', 'retie', 'lummen', 'grâce-hollogne', 'leuven',
    'sint-martens-latem', 'ferrières', 'edegem', 'tongeren', 'quaregnon',
    'turnhout', 'heist-op-den-berg', 'la louvière', 'haaltert',
    'kapelle-op-den-bos', 'bever', 'visé', 'destelbergen', 'sint-genesius-rode',
    'mortsel', 'bièvre', 'zottegem', 'oudenburg', 'lessines', 'hannut', 'wemmel',
    'wezembeek-oppem', 'rochefort', 'machelen', 'koksijde', 'lebbeke', 'assenede',
    'flémalle', 'kampenhout', 'waterloo', 'sint-pieters-leeuw', 'wachtebeke',
    'braine-le-château', 'ingelmunster', 'galmaarden', 'la hulpe', 'beersel',
    'ninove', 'paliseul', 'zwijndrecht', 'eeklo', 'saint-nicolas', 'estaimpuis',
    'erquelinnes', 'viroinval', 'antoing', 'bertrix', 'genappe', 'lede', 'bredene',
    'izegem', 'asse', 'chastre', 'la roche-en-ardenne', 'tubize', 'maldegem',
    'boechout', 'opwijk', 'brasschaat', 'oudenaarde', 'linter', 'avelgem',
    'tervuren', 'herne', 'duffel', 'dendermonde', 'zaventem', 'neupré', 'harelbeke',
    'ciney', 'daverdisse', 'court-saint-etienne', 'denderleeuw', 'moeskroen',
    'scherpenheuvel-zichem', 'tournai', 'ganshoren', 'aarschot', 'willebroek',
    'boussu', 'rumst', 'houthalen-helchteren', 'walhain', 'kluisbergen',
    'kraainem', 'herent', 'waregem', 'malmedy', 'wichelen', 'deerlijk',
    'oud-turnhout', 'kalmthout', 'temse', 'beaumont', 'stabroek',
    'libramont-chevigny', 'oudergem', 'keerbergen', 'namur', 'kortenberg',
    'zonhoven', 'pepinster', 'sint-lambrechts-woluwe', 'verviers', 'ravels',
    'wellin', 'wanze', 'marche-en-famenne', 'wavre', 'niel', 'beveren-waas',
    'herentals', 'morlanwelz', 'zoersel', 'ternat', 'libin', 'aubange', 'essen',
    'remicourt', 'bassenge', 'ans', 'wasseiges', 'diksmuide',
    'sint-agatha-berchem', 'dentergem', 'zwevegem', 'hamme', 'kortrijk',
    'schaarbeek', 'tienen', 'frasnes-lez-anvaing', 'zedelgem', 'erezée',
    'roeselare', 'tellin', 'heers', 'menen', 'villers-la-ville', 'haacht',
    'gembloux', 'landen', 'blégny', 'lier', 'geer', 'boortmeerbeek', 'putte',
    'berlaar', 'rendeux', 'durbuy', 'hooglede', 'grimbergen', 'bertem', 'brunehaut',
    'ellezelles', 'saint-hubert', 'aiseau-presles', 'kruibeke', 'torhout',
    'leopoldsburg', 'mont-saint-guibert', 'oud-heverlee', 'liedekerke',
    'chaudfontaine', 'arlon', 'de haan', 'kapellen', 'waasmunster', 'lille',
    'fléron', 'sprimont', 'damme', 'faimes', 'buggenhout', 'melle', 'herselt',
    'houthulst', 'ranst', 'gedinne', 'laarne', 'lennik', 'moorslede', 'lendelede',
    'engis', 'maaseik', 'juprelle', 'tinlot', 'rotselaar', 'ramillies',
    'sint-pieters-woluwe', 'ichtegem', 'mol', 'mons', 'saint-ghislain',
    'fosses-la-ville', 'komen-waasten', 'borgloon', 'lokeren', 'dalhem'])
province = st.selectbox(label = "What province is the house located in?",index=None, options=['oost-vlaanderen' ,'luik' ,'waals-brabant' ,'antwerpen' ,'brussel',
 'vlaams-brabant' ,'henegouwen', 'west-vlaanderen' ,'limburg' ,'luxemburg',
 'namen'])

inputs = {"postalcode": postalcode,
    "property_type": property_type ,
    "property_subtype": property_subtype,
    "type_of_sale": type_of_sale, 
    "living_area": living_area,
    "kitchen_type": kitchen_type, 
    "fully_equipped_kitchen": fully_equipped_kitchen, 
    "open_fire": open_fire,
    "terrace": terrace,
    "terrace_area": terrace_area,
    "garden": garden,
    "garden_area": garden_area,
    "surface_of_good": surface_of_good,
    "number_of_facades": number_of_facades,
    "swimming_pool": swimming_pool,
    "state_of_building": state_of_building,
    "main_city": main_city,
    "province": province}

    #creating a button for prediction
if st.button('price result'):
    price_response = requests.post(url="http://127.0.0.1:8000/predict", data=json.dumps(inputs))
    
    if price_response.status_code == 200:
        price_data = price_response.json()
        price_value = price_data.get("price")
        
        if price_value is not None:
            st.subheader(f"Price: {price_value}")
        else:
            st.subheader("Price not found in the response.")
    else:
        st.subheader(f"Error: {price_response.text}")


    


