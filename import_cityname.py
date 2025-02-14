import pandas as pd
import registre_mod.LoadData as ld

mun_data_api_url = url = 'https://www.donneesquebec.ca/recherche/api/3/action/datastore_search?resource_id=19385b4e-5503-4330-9e59-f998f5918363'

cityname_df_cols_to_keep = [
    "mcode",
    "munnom",
    "mcodpos",
    "regadm",
    "divrec",
    "mrc"
]

mun_ref_df = ld.import_data_from_dq_api(mun_data_api_url)

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
