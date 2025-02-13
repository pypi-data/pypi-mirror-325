# VFM Data Processing Repository

Virtual Flow Metering (VFM) - Delumping extension, suitable for the SmartMonitor platform, part of the Petrobras - Replicantes IV project.

Latest version of the main script of the VFM implementation according to the formulations proposed by Goés et al. (2021 and 2022) or variants of them. 

This repository provides scripts for data import, preprocessing, and numerical analysis using Virtual Flow Metering (VFM) methods. The code allows for automated processing of well-specific data from multiple data sources and supports custom configurations for initialization and computation, based on methods from Góes et al. (2020-2022).

## Workflow Overview

1. **Data Import and Preprocessing**
   - The first script is responsible for importing and preprocessing raw data from various sources (e.g., BTP, PI, and BDO data files).
   - This data is read, cleaned, and stored in well-structured formats, ensuring consistency across data points and measurements for each well.

2. **Main Numerical Analysis**
   - The main analysis script performs numerical calculations and data processing using customizable flags that control calculation methods.
   - The user can choose from different algorithms for initialization (`flag_init`) and flow estimation (`flag_code`), each based on distinct methodologies for data handling and calculation.

---

## Usage

To execute the data processing workflow:

1. Run the data import script (run_data_importer_VFM.py).
2. Run the main analysis script with chosen configurations (`flag_init` and `flag_code` values) for customized calculations (run_main_VFM_var.py).

Using `flag_init = 3` and `flag_code = 3` is generally recommended, as it applies advanced processing methods.

---

## Configuration Options

### Initialization Method (`flag_init`)

The `flag_init` parameter determines the method used to preprocess and initialize the data, reflecting the evolution of methodologies in the field. Available options include:

- **flag_init = 1**: Uses arithmetic averages of PI data for each daily sample, reproducing the method from Góes et al. (2021).
- **flag_init = 2**: Applies numerical integration on raw PI data based on sampling times, enhancing data resolution and accuracy.
- **flag_init = 3**: Performs numerical integration on preprocessed PI data, optimizing data handling for higher-quality results.

### Flow Estimation Method (`flag_code`)

The `flag_code` parameter specifies the algorithm used for flow estimation and molar composition calculations:

- **flag_code = 1**: Reproduces calculations from Góes et al. (2021-2022), focusing on the original methodologies.
- **flag_code = 2**: Uses updated formulations based on Góes et al. (2022), incorporating refined flow estimation techniques.
- **flag_code = 3**: Extends the method from `flag_code = 2` with additional calculations for molar composition, integrating advanced model extensions from Góes et al. (2022) for comprehensive flow analysis.

---

## Key Notes

- **Data and Delays**: Gas chromatography and PVT data in this implementation include measurement time delays in accordance with Góes et al. (2021 and 2022).
- **Source Data**: Reference data used in preprocessing follows methods from Góes et al. (2020-2021).

---

# Data Summary

---

---

### Inputs

| Variable                          | Description                                                                                       | Unit                |
|-----------------------------------|---------------------------------------------------------------------------------------------------|---------------------|
| **flag_init**                     | Indicator of the algorithm followed in the numerical calculations from the VFM                    |                     |
| **flag_code**                     | Indicator of the algorithm followed in the numerical calculations from the delumping method       |                     |
| **Data_BTP**                      | Structure with input data from the BTP                                                            |                     |
| **Data_BTP.Wells**                | Well tags related to their column position                                                        |                     |
| **Data_BTP.Time**                 | Sampling times of the well tests                                                                  |                     |
| **Data_BTP.rhoo_SC**              | Oil density at standard conditions (SC)                                                           | kg/m³               |
| **Data_BTP.Qo_SC**                | Oil volumetric flow rate at SC                                                                    | m³/d                |
| **Data_BTP.Qg_SC**                | Gas volumetric flow rate at SC                                                                    | m³/d                |
| **Data_BTP.Qw_SC**                | Water volumetric flow rate at SC                                                                  | m³/d                |
| **Data_BTP.Rs**                   | Gas solubility in the oil                                                                         |                     |
| **Data_BTP.Bo**                   | Oil formation volume factor                                                                       |                     |
| **Data_BTP.SGg**                  | Gas specific gravity at SC                                                                        |                     |
| **Data_BTP.T_sep**                | Temperature measured at the test separator output                                                 | K                   |
| **Data_BTP.P_sep**                | Pressure measured at the test separator output                                                    | kPa                  |
| **Data_BTP.Y_i**                  | Mole fraction of component \(i\) in the gas phase                                                 |                     |
| **Data_BTP.N_data**               | Number of data points available for each well                                                     |                     |
| **Data_BTP.P_us**                 | Pressure upstream of the choke valve during the reference well test (RWT)                         | kPa                 |
| **Data_BTP.T_us**                 | Temperature upstream of the choke valve during the RWT                                            | °C                  |
| **Data_BTP.u**                    | Choke valve opening percentage during the RWT                                                     | %                   |
| **Data_BTP.DeltaPManifold**       | Pressure drop in the manifold concerning the test line during the RWT                             | kPa                 |
| **Data_BTP.PdsSDV**               | Pressure downstream of the shutdown valve (SDV) during the RWT                                    | kPa                 |
| **Data_BTP.Qgi**                  | Gas lift injection flow rate during the RWT                                                       | m³/h                |
| **Data_PI.Wells**                 | Well tags related to their column position                                                        |                     |
| **Data_PI.Time**                  | Sampling times of the PI data                                                                     |                     |
| **Data_PI.Ql**                    | Volumetric liquid flow rate at standard conditions (SC), based on BDO                             | m³/d                |
| **Data_PI.u_PI**                  | Choke valve opening percentage, based on the PI                                                   | °C                  |
| **Data_PI.DeltaPManifold_PI**     | Pressure drop in the manifold concerning the production line                                      | kPa                 |
| **Data_PI.P_ds_SDV_PI**           | Pressure downstream of the shutdown valve (SDV)                                                   | kPa                 |
| **Data_PI.P_sep**                 | Pressure measured at the test separator output                                                    | kPa                 |
| **Data_PI.Qo_SC**                 | Fiscal measurements of the oil volumetric flow rate at SC                                         | m³/h                |
| **Data_PI.Qg_SC**                 | Fiscal measurements of the gas volumetric flow rate at SC                                         | m³/h                |
| **Data_PI.P_us_PI**               | Pressure upstream of the choke valve                                                              | kPa                 |
| **Data_PI.T_us_PI**               | Temperature upstream of the choke valve                                                           | °C                  |
| **Data_PI.u_PI**                  | Choke valve opening percentage                                                                    | %                   |
| **Data_PI.Qgi_PI**                | Gas lift injection flow rate                                                                      | m³/h                |
| **Data_PI.TimeBTP**               | Sampling times of the RWT                                                                         |                     |
| **Data_PI.P_us_RWT**              | Pressure upstream of the choke valve during the RWT                                               | kPa                 |
| **Data_PI.T_us_RWT**              | Temperature upstream of the choke valve during the RWT                                            | °C                  |
| **Data_PI.u_RWT**                 | Average choke valve opening percentage during the RWT                                             | %                   |
| **Data_PI.Qgi_RWT**               | Gas lift injection flow rate during the RWT                                                       | m³/h                |
| **Data_PI.P_ds_SDV_RWT**          | Pressure downstream of the SDV during the RWT                                                     | kPa                 |
| **Data_PI.rhoo_SC**               | Oil density at standard conditions during the RWT                                                 | kg/m³               |
| **Data_PI.DeltaPManifold_RWT**    | Pressure drop in the manifold concerning the test line during the RWT                             | kPa                 |
| **Data_BDO.Time**                 | Sampling times of the well tests                                                                  |                     |
| **Data_BDO.Ql_SC**                | Volumetric liquid flow rate at SC reported in the BDO                                             | m³/d                |
| **Data_BDO.Qo_SC**                | Volumetric oil flow rate at SC reported in the BDO                                                | m³/d                |
| **Data_BDO.Qg_SC**                | Volumetric gas flow rate at SC reported in the BDO                                                | m³/d                |
| **Data_BDO.Qw_SC**                | Volumetric water flow rate at SC reported in the BDO                                              | m³/d                |

---

### Outputs

| Variable                          | Description                                                                                       | Unit                   |
|-----------------------------------|---------------------------------------------------------------------------------------------------|------------------------|
| **Cv_est**                        | Estimation of the valve sizing coefficient                                                        | m³/(s·Pa⁰⋅⁵)           |
| **Cv_gpm_est**                    | Estimation of the valve sizing coefficient                                                        | gpm/(psi⁰⋅⁵)           |
| **Qw_SC_est**                     | Estimation of the volumetric water flow rate at SC                                                | m³/d                   |
| **Qo_SC_est**                     | Estimation of the volumetric oil flow rate at SC                                                  | m³/d                   |
| **Qg_SC_est**                     | Estimation of the volumetric gas flow rate at SC                                                  | m³/d                   |
| **API_est**                       | API degree estimation                                                                             | °API                   |
| **GOR_est**                       | Gas-oil ratio (GOR) estimation                                                                    | m³/m³                  |
| **SGg_est**                       | Gas specific gravity estimation at standard conditions                                            |                        |
| **z_est**                         | Estimation of wellstream molar composition                                                        |                        |
| **x_est**                         | Estimation of oil molar composition                                                               |                        |
| **y_est**                         | Estimation of gas molar composition                                                               |                        |
| **MW_vector**                     | Optimal molecular weight of the black oil                                                         | kg/kmol                |
| **FO_del**                        | Optimal cost function from the delumping model                                                    |                        |
| **Qot_PI_est**                    | Estimation of total oil volumetric flow rate at SC for comparison with PI data                    | m³/h                   |
| **Qgt_PI_est**                    | Estimation of total gas volumetric flow rate at SC for comparison with PI data                    | m³/h                   |
| **Qot_BDO_est**                   | Estimation of total oil volumetric flow rate at SC for comparison with BDO data                   | m³/h                   |
| **Qgt_BDO_est**                   | Estimation of total gas volumetric flow rate at SC for comparison with BDO data                   | m³/h                   |
| **Qwt_BDO_est**                   | Estimation of total water volumetric flow rate at SC for comparison with BDO data                 | m³/h                   |
| **PRE_Qo_PI**                     | Percentual relative error (PRE) of total oil flow rates with respect to PI measurements           | %                      |
| **PRE_Qg_PI**                     | Percentual relative error (PRE) of total gas flow rates with respect to PI measurements           | %                      |
| **PRE_Qo_BDO**                    | Percentual relative error (PRE) of total oil flow rates with respect to BDO measurements          | %                      |
| **PRE_Qg_BDO**                    | Percentual relative error (PRE) of total gas flow rates with respect to BDO measurements          | %                      |
| **PRE_Qw_BDO**                    | Percentual relative error (PRE) of total water flow rates with respect to BDO measurements        | %                      |
| **MAPE_Q**                        | Mean absolute percentage error (MAPE) of flow rate estimations with respect to PI or BDO data     | %                      |
| **MAPE_x**                        | MAPE of \(x_{\text{est}}\) with respect to expected values from the Gamma-distribution model      | %                      |
| **MAPE_y**                        | MAPE of \(y_{\text{est}}\) with respect to expected values from the RWT                           | %                      |

---


---

### UpdateDataVFM - Inputs and Outputs

#### Inputs

| File Name                                        | Description                                                                                   | Date Range                   |
|--------------------------------------------------|-----------------------------------------------------------------------------------------------|------------------------------|
| **BTP_Data.csv**                                 | Data from well test reports (Boletins de teste de poço)                                       |                              |
| **Ler_dados_PI_config-Daniel_PIDATALINK_1805_1902.csv** | Data from plant information (PI)                                                              | 18/05/2018 - 19/02/2019      |
| **Ler_dados_PI_config-Daniel_PIDATALINK_1904_1912.csv** | Data from plant information (PI)                                                              | 19/04/2019 - 19/12/2019      |
| **Config_TAGS_PI-Daniel_PIDATALINK.csv**         | Data from PI based on a 1-hour sampling time                                                  | 01/01/2018 - 31/12/2019      |
| **Config_TAGS_PI-Daniel_PIDATALINK_ver2.csv**    | Data from PI based on a 10-minute sampling time                                               | 01/01/2018 - 31/12/2019      |
| **Daniel_Dados_lidos_PI_P66_(01-12-2023 00_01_00 a 01-07-2024 00_01_00).xlsx** | Data from PI between specified dates                                                          | 01/12/2023 - 01/07/2024      |
| **BDO_Data.csv**                                 | Data from daily operation reports (boletins diário de operação)                               |                              |

---

#### Outputs

##### `Data_BTP` Structure (Input Data from BTP)

| Attribute                   | Description                                                                                | Unit        |
|-----------------------------|--------------------------------------------------------------------------------------------|-------------|
| **Wells**                   | Well tags related to their column position                                                 |             |
| **Time**                    | Sampling times of the well tests                                                           |             |
| **rhoo_SC**                 | Oil density at standard conditions                                                         | kg/m³       |
| **Qo_SC**                   | Oil volumetric flow at standard conditions                                                 | m³/d        |
| **Qg_SC**                   | Gas volumetric flow at standard conditions                                                 | m³/d        |
| **Qw_SC**                   | Water volumetric flow at standard conditions                                               | m³/d        |
| **Rs**                      | Gas solubility in oil                                                                      |             |
| **Bo**                      | Oil formation volume factor                                                                |             |
| **SGg**                     | Gas specific gravity at standard conditions                                                |             |
| **T_sep**                   | Temperature measured at the test separator output                                          | K           |
| **P_sep**                   | Pressure measured at the test separator output                                             | Pa          |
| **Y_i**                     | Mole fraction of component \(i\) in the gas phase                                          |             |
| **N_data**                  | Number of data points available for each well                                              |             |
| **P_us**                    | Pressure upstream of the choke valve during reference well test (RWT)                      | kPa         |
| **T_us**                    | Temperature upstream of the choke valve during RWT                                         | °C          |
| **u**                       | Choke valve opening percentage during RWT                                                  | %           |
| **DeltaPManifold**          | Pressure drop in the manifold concerning the test line during RWT                          | kPa         |
| **PdsSDV**                  | Pressure downstream of the shutdown valve during RWT                                       | kPa         |
| **Qgi**                     | Gas lift injection flow rate during RWT                                                    | m³/h        |

---

##### `Data_PI` Structure (Input Data from PI)

| Attribute                   | Description                                                                                | Unit        |
|-----------------------------|--------------------------------------------------------------------------------------------|-------------|
| **Wells**                   | Well tags related to their column position                                                 |             |
| **Time**                    | Sampling times of the PI data                                                              |             |
| **Ql**                      | Volumetric liquid flow rate at standard conditions based on BDO                            | m³/d        |
| **u_PI**                    | Choke valve opening percentage based on PI                                                 | °C          |
| **DeltaPManifold_PI**       | Pressure drop in the manifold concerning the production line                               | kPa         |
| **P_ds_SDV_PI**             | Pressure downstream of the shutdown valve based on PI                                      | kPa         |
| **P_sep**                   | Pressure measured at the test separator output                                             | kPa         |
| **Qo_SC**                   | Fiscal measurements of oil volumetric flow rate at standard conditions                     | m³/h        |
| **Qg_SC**                   | Fiscal measurements of gas volumetric flow rate at standard conditions                     | m³/h        |
| **P_us_PI**                 | Pressure upstream of the choke valve                                                       | kPa         |
| **T_us_PI**                 | Temperature upstream of the choke valve                                                    | °C          |
| **Qgi_PI**                  | Gas lift injection flow rate                                                               | m³/h        |
| **TimeBTP**                 | Sampling times of the RWT                                                                  |             |
| **P_us_RWT**                | Pressure upstream of the choke valve during RWT                                            | kPa         |
| **T_us_RWT**                | Temperature upstream of the choke valve during RWT                                         | °C          |
| **u_RWT**                   | Average choke valve opening percentage during RWT                                          | %           |
| **Qgi_RWT**                 | Gas lift injection flow rate during RWT                                                    | m³/h        |
| **P_ds_SDV_RWT**            | Pressure downstream of the shutdown valve during RWT                                       | kPa         |
| **rhoo_SC**                 | Oil density at standard conditions during RWT                                              | kg/m³       |
| **DeltaPManifold_RWT**      | Pressure drop in the manifold concerning the test line during RWT                          | kPa         |

---

##### `Data_BDO` Structure (Input Data from Daily Operation Reports - BDO)

| Attribute                   | Description                                                                                | Unit        |
|-----------------------------|--------------------------------------------------------------------------------------------|-------------|
| **Time**                    | Sampling times of the well tests                                                           |             |
| **Ql_SC**                   | Volumetric liquid flow rate at standard conditions reported in BDO                         | m³/d        |
| **Qo_SC**                   | Volumetric oil flow rate at standard conditions reported in BDO                            | m³/d        |
| **Qg_SC**                   | Volumetric gas flow rate at standard conditions reported in BDO                            | m³/d        |
| **Qw_SC**                   | Volumetric water flow rate at standard conditions reported in BDO                          | m³/d        |

---

To add the **TAGs Explanation** section to the end of the README file in markdown format, based on the data you provided, here's a suitable section:

---

## TAGs Explanation

The following table provides a detailed description of each TAG used in the VFM data processing system:

| TAG ID                            | Description                                                                                           | Unit       |
|-----------------------------------|-------------------------------------------------------------------------------------------------------|------------|
| P66_301092_1210_PIT_001W_EAN      | Pressão a montante da Choke do Poço W_3-RJS-680                                                       | kPa        |
| P66_301092_1210_TIT_008W_EAN      | Temperatura a montante da Choke do Poço W_3-RJS-680                                                   | ºC         |
| P66_301092_1210_ZIT_004W_EAN      | Posicionador da Choke de Produção do Poço W                                                           | %          |
| P66_301092_1223_PDIT_021_EAN      | Pressão diferencial do manifold de produção                                                           | kPa g      |
| P66_301092_1223_PDIT_038_EAN      | Pressão diferencial do manifold de teste                                                              | kPa g      |
| P66_301092_1223_PIT_024_EAN       | Pressão no Manifold Produção (jusante SDV-1223021/22)                                                 | kPa g      |
| P66_301092_1223_PIT_025_EAN       | Pressão no Manifold Produção (jusante SDV-1223021/22)                                                 | kPa g      |
| P66_301092_1223_PIT_026_EAN       | Pressão no Manifold Produção (jusante SDV-1223021/22)                                                 | kPa g      |
| P66_301092_1223_PIT_028_EAN       | Pressão no Manifold Teste (jusante SDV-1223030/32)                                                    | kPa g      |
| P66_301092_1223_PIT_012_EAN       | Pressão Separador Produção                                                                            | kPa        |
| P66_301092_1212_FQI_002B_VZB      | Vazão bruta do FQI-1212002B                                                                           | m³/h       |
| P66_301092_1223_FQI_015_VZB_COR   | Vazão Instantanea Bruta Corrigida do gás do separador de produção                                     | sm³/h      |
| P66_301092_1223_FQI_020_VZB_COR   | Vazão Instantanea Bruta Corrigida do gás do V-TO-1223001                                              | sm³/h      |
| P66_301092_1223_FQI_030_VZB_COR   | Vazão Instantanea Bruta Corrigida gás do V-TO-1223002                                                 | sm³/h      |
| P66_301092_1244_FIT_001W_EAN      | Vazão no header de gás lift para o Poço W_3-RJS-680                                                   | m³/h       |
| P66_301092_1210_PIT_001R_EAN      | Pressão a montante da Choke do Poço 7-LL-60D-RJS                                                      | kPa        |
| P66_301092_1210_TIT_008R_EAN      | Temperatura a montante da Choke do Poço R 7-LL-60D-RJS                                                | ºC         |
| P66_301092_1210_ZIT_004R_EAN      | Posicionador da Choke de Produção do Poço R                                                           | %          |
| P66_301092_1244_FIT_001R_EAN      | Vazão no header de gás lift para o Poço R 7-LL-60D-RJS                                                | m³/h       |
| P66_301092_1210_PIT_001V_EAN      | Pressão de Produção do Poço 7-LL-69-RJS                                                               | kPa        |
| P66_301092_1210_TIT_008V_EAN      | Temperatura a montante da Choke do Poço 7-LL-69-RJS                                                   | ºC         |
| P66_301092_1210_ZIT_004V_EAN      | Posicionador da Choke de Produção do Poço 7-LL-69-RJS                                                 | %          |
| P66_301092_1244_FIT_001V_EAN      | Vazão no header de gás lift para o poço V                                                             | m³/h       |
| P66_301092_1210_PIT_001U_EAN      | Pressão a montante da Choke do Poço U_7-LL-90D-RJS                                                   | kPa        |
| P66_301092_1210_TIT_008U_EAN      | Temperatura a montante da Choke do Poço U_7-LL-90D-RJS                                               | ºC         |
| P66_301092_1210_ZIT_004U_EAN      | Posicionador da Choke de Produção do Poço 7-LL-90D-RJS                                               | %          |
| P66_301092_1244_FIT_001U_EAN      | Vazão no header de gás lift para o Poço U_7-LL-90D-RJS                                               | m³/h       |
| P66_301092_1210_PIT_001G_EAN      | Pressão de Produção do Poço 7-LL-97-RJS                                                              | kPa        |
| P66_301092_1210_TIT_008G_EAN      | Temperatura a montante da Choke do Poço 7-LL-97-RJS                                                  | ºC         |
| P66_301092_1210_ZIT_004G_EAN      | Posicionador da Choke de Produção do Poço 7-LL-97-RJS                                                | %          |
| P66_301092_1244_FIT_001G_EAN      | Vazão no header de gás lift para o poço G                                                            | m³/h       |
| P66_301092_1210_PIT_001K_EAN      | Pressão a montante da Choke do Poço K_7-LL-100-RJS                                                   | kPa        |
| P66_301092_1210_TIT_008K_EAN      | Temperatura a montante da Choke de Produção do Poço K_7-LL-100-RJS                                   | ºC         |
| P66_301092_1210_ZIT_004K_EAN      | Posicionador da Choke de Produção do Poço K_7-LL-100-RJS                                             | %          |
| P66_301092_1244_FIT_001K_EAN      | Vazão no header de gás lift para o Poço K_7-LL-100-RJS                                               | m³/h       |
| P66_301092_1210_PIT_001J_EAN      | Pressão a montante da Choke do Poço 7-LL-102D-RJS                                                    | kPa        |
| P66_301092_1210_TIT_008J_EAN      | Temperatura a montante da Choke do Poço J                                                            | ºC         |
| P66_301092_1210_ZIT_004J_EAN      | Posicionador da Choke de Produção do Poço J                                                          | %          |
| P66_301092_1244_FIT_001J_EAN      | Vazão no header de gás lift para o poço J                                                            | m³/h       |
| P66_301092_1210_PIT_001H_EAN      | Pressão a montante da Choke do Poço H_7-LL-105-RJS                                                  | kPa        |
| P66_301092_1210_TIT_008H_EAN      | Temperatura a montante da Choke de Produção do Poço H_7-LL-105-RJS                                  | ºC         |
| P66_301092_1210_ZIT_004H_EAN      | Posicionador da Choke de Produção do Poço H-7-LL-105-RJS                                            | %          |
| P66_301092_1244_FQI_001H_VZB_COR  | Vazao Instantanea Bruta Corrigida do gás lift Poço H_7-LL-105-RJS                                   | sm³/h      |
| P66_301092_1244_FIT_001H_EAN      | Vazão de injeção de gás lift no Poço H_7-LL-105-RJS                                                 | sm³/h      |

---
