import pandas as pd

cityname_data_url = "https://donneesouvertes.affmunqc.net/repertoire/MUN.csv"
cityname_data_pkl_filename = "mun_ref_data.pkl"
cityname_df_cols_to_keep = [
    "mcode",
    "munnom",
    "mcodpos",
    "regadm",
    "divrec",
    "mrc"
]

cityname_df = pd.read_csv(
    cityname_data_url,
    usecols=cityname_df_cols_to_keep
)

#Pull codes from mrc, regadm and divrec
cityname_df['mrc_code'] = cityname_df['mrc'].str.extract('.*\((.*)\).*')
cityname_df['mrc_code'] = cityname_df['mrc_code'].astype('category')

cityname_df['regadm_code'] = cityname_df['regadm'].str.extract('.*\((.*)\).*')
cityname_df['regadm_code'] = cityname_df['regadm_code'].astype('category')

cityname_df['divrec_code'] =cityname_df['divrec'].str.extract('.*\((.*)\).*')
cityname_df['divrec_code'] = cityname_df['divrec_code'].astype('category')

#Save data
cityname_df.to_pickle(
    f'./data/{cityname_data_pkl_filename}'
)
