import pandas as pd
from sklearn.model_selection import train_test_split
def prep_iris(df):
    '''
    This function will drop any duplicate observations, 
    drop ['deck', 'embarked', 'class', 'age'],
    and create dummy vars from sex and embark_town. 
    '''
    df = df.drop_duplicates()
    df = df.drop(columns=['species_id', 'measurement_id'])
    df = df.rename(columns={'species_name': 'species'})
    dummy_df = pd.get_dummies(df[['species']], drop_first=True, dtype=int)
    df_iris = pd.concat([df, dummy_df], axis=1)
    return df_iris

def prep_titanic(df_titanic):
    '''
    This function will drop any duplicate observations, 
    drop ['deck', 'embarked', 'class', 'age'],
    and create dummy vars from sex and embark_town. 
    '''
    df_titanic = df_titanic.drop_duplicates()
    df_titanic = df_titanic.drop(columns=['deck', 'embarked', 'class', 'age'])
    df_titanic['embark_town'] = df_titanic['embark_town'].fillna(value='Southampton')
    dummy_df = pd.get_dummies(df_titanic[['sex', 'embark_town']], drop_first=True, dtype=int)
    df_titanic = df_titanic.drop(columns=['sex', 'embark_town'])
    df_titanic = pd.concat([df_titanic, dummy_df], axis=1)
    return df_titanic

def prep_telco(df_telco):
    '''
    This function will drop any duplicate observations, 
    drop ['contract_type_id', 'payment_type_id', 'internet_service_type_id'], create dummy vars from all categorical variables, and change dtype of total_charges to float. 
    '''
    df_telco = df_telco.drop_duplicates()
    df_telco = df_telco.drop(columns=['contract_type_id', 'payment_type_id', 'internet_service_type_id'])

    df_telco['gender_encoded'] = df_telco.gender.map({'Female': 1, 'Male':0})
    df_telco['partner_encoded'] = df_telco.partner.map({'Yes':1, 'No':0})
    df_telco['dependents_encoded'] = df_telco.dependents.map({'Yes':1, 'No':0})
    df_telco['phone_service_encoded'] = df_telco.phone_service.map({'Yes':1, 'No':0})
    df_telco['paperless_billing_encoded'] = df_telco.paperless_billing.map({'Yes':1, 'No':0})
    df_telco['churn_encoded'] = df_telco.churn.map({'Yes':1, 'No':0})

    dummy_df = pd.get_dummies(df_telco[['multiple_lines',
                                     'online_security',
                                     'online_backup',
                                     'device_protection', 
                                     'tech_support',
                                     'streaming_tv',
                                     'streaming_movies', 
                                     'contract_type', 
                                     'internet_service_type',
                                     'payment_type']],
                                  drop_first=True)

    df_telco['total_charges'] = df_telco.total_charges.str.replace(' ', '0').astype(float)

    df_telco = pd.concat([df_telco, dummy_df], axis=1)
    
    return df_telco

def split_function(df, target_varible):
    train, test = train_test_split(df,
                                   random_state=123,
                                   test_size=.20,
                                   stratify= df[target_varible])
    
    train, validate = train_test_split(train,
                                   random_state=123,
                                   test_size=.25,
                                   stratify= train[target_varible])
    return train, validate, test