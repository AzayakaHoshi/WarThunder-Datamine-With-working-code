### Full Changelog:

- **aces.vromfs.bin_u/config/damagemodel.blkx**:

  **Added**:
```diff
+ cn_t_80ud_478be:i=140
```

  **Removed**:
```diff
```


- **aces.vromfs.bin_u/config/gui.blkx**:

  **Added**:
```diff
+ wt_f_5c_pack:t="AC166790-BFF1-4304-9C6D-B8C3F2F24491"
+ 2025_01_tank:t="unlocks/chapter/2025_01_tank"
```

  **Removed**:
```diff
- wt_f_5c_pack:t="E82898BB-B87D-4366-95A8-C340A7E4C272"
```


- **aces.vromfs.bin_u/config/hangar.blkx**:

  **Added**:
```diff
+ level:t="levels/hangar_field.bin"
+ hangarMission:t="gameData/scenes/hangar_field_mission.blk"
+ env:t="14.5"
+ weight:r=10.0
+ country_usa:t="us_m1a1_hc_usmc"
+ country_germany:t="germ_pzh_2000"
+ country_ussr:t="ussr_object_140"
+ country_britain:t="uk_challenger_2_megatron"
+ country_japan:t="jp_tkx_prot"
+ country_china:t="cn_plz_05"
+ country_italy:t="it_pzh_2000_hu"
+ country_france:t="fr_leopard_2a6nl"
+ country_sweden:t="sw_leopard_2a6nl"
+ country_israel:t="il_sabra_mk1"
+ country_usa:t="us_rdf_lt"
+ country_germany:t="germ_m44"
+ country_ussr:t="ussr_bmd_4m"
+ country_britain:t="uk_9a35_m"
+ country_japan:t="jp_m44"
+ country_china:t="cn_hq_17"
+ country_italy:t="it_9a35_m"
+ country_france:t="fr_vbci"
+ country_sweden:t="sw_cv_90_mk4"
+ country_israel:t="il_namer_tsrikhon"
+ country_usa:t="f_15e"
+ country_germany:t="ef_2000_block_10"
+ country_ussr:t="su_33"
+ country_britain:t="ef_2000_fgr4"
+ country_japan:t="f_15j_kai"
+ country_italy:t="ef_2000a"
+ country_france:t="rafale_c_f3"
+ country_china:t="j_10a"
+ country_sweden:t="saab_ja37di"
+ country_israel:t="f_15i_raam"
+ }
+ 
+ mechanics{
+ 
+ country_usa{
+ n:t="unit_hangar_technic_idle_"
+ n:t="unit_hangar_technic_black_idle_"
+ n:t="unit_hangar_technic_asian_idle_"
+ }
+ 
+ country_germany{
+ n:t="unit_hangar_technic_idle_"
+ }
+ 
+ country_ussr{
+ n:t="unit_hangar_technic_idle_"
+ }
+ 
+ country_britain{
+ n:t="unit_hangar_technic_idle_"
+ n:t="unit_hangar_technic_black_idle_"
+ }
+ 
+ country_japan{
+ n:t="unit_hangar_technic_asian_idle_"
+ }
+ 
+ country_italy{
+ n:t="unit_hangar_technic_idle_"
+ }
+ 
+ country_france{
+ n:t="unit_hangar_technic_idle_"
+ n:t="unit_hangar_technic_black_idle_"
+ n:t="unit_hangar_technic_asian_idle_"
+ }
+ 
+ country_china{
+ n:t="unit_hangar_technic_asian_idle_"
+ }
+ 
+ country_sweden{
+ n:t="unit_hangar_technic_idle_"
+ }
+ 
+ country_israel{
+ n:t="unit_hangar_technic_idle_"
+ }
+ }
+ 
+ hangarEffects{
+ checkHoliday:b=yes
+ 
+ hangarEffect{
+ effect:t="misc_firework"
+ areaMin:p3=-0.0, 70.0, 300.0
+ areaMax:p3=200.0, 210.0, 900.0
+ delay:p2=20.0, 40.0
+ }
+ 
+ hangarEffect{
+ effect:t="firework_score_ginger"
+ areaMin:p3=-0.0, 70.0, 300.0
+ areaMax:p3=200.0, 210.0, 900.0
+ delay:p2=3.0, 6.0
+ }
+ 
+ hangarEffect{
+ effect:t="firework_score_turquoise"
+ areaMin:p3=-0.0, 70.0, 300.0
+ areaMax:p3=200.0, 210.0, 900.0
+ delay:p2=4.0, 7.0
+ }
+ 
+ hangarEffect{
+ effect:t="misc_firework"
+ areaMin:p3=-375.0, 70.0, -450.0
+ areaMax:p3=175.0, 140.0, -250.0
+ delay:p2=20.0, 40.0
+ }
+ 
+ hangarEffect{
+ effect:t="firework_score_ginger"
+ areaMin:p3=-375.0, 70.0, -450.0
+ areaMax:p3=175.0, 140.0, -250.0
+ delay:p2=3.0, 6.0
+ }
+ 
+ hangarEffect{
+ effect:t="firework_score_turquoise"
+ areaMin:p3=-375.0, 70.0, -450.0
+ areaMax:p3=175.0, 140.0, -250.0
+ delay:p2=4.0, 7.0
+ }
+ 
+ hangarEffect{
+ effect:t="misc_firework"
+ areaMin:p3=-2200.0, 20.0, -100.0
+ areaMax:p3=-2000.0, 200.0, 300.0
+ delay:p2=20.0, 40.0
+ }
+ 
+ hangarEffect{
+ effect:t="firework_score_turquoise"
+ areaMin:p3=-2200.0, 20.0, -100.0
+ areaMax:p3=-2000.0, 200.0, 300.0
+ delay:p2=3.0, 6.0
+ }
+ 
+ hangarEffect{
+ effect:t="firework_score_ginger"
+ areaMin:p3=-2200.0, 20.0, -100.0
+ areaMax:p3=-2000.0, 200.0, 300.0
+ delay:p2=4.0, 7.0
+ }
+ }
+ 
+ premiumVehicle{
+ unitName:t="xp-55"
+ weapon:t="xp-55_default"
+ type:t="plane"
+ skin:t=""
+ country:t="country_usa"
+ rank:ip2=1, 2
+ }
+ 
+ premiumVehicle{
+ unitName:t="btd-1"
+ weapon:t="btd_1_default"
+ type:t="plane"
+ skin:t=""
+ country:t="country_usa"
+ rank:ip2=1, 3
+ }
+ 
+ premiumVehicle{
+ unitName:t="p-51d-20-na"
+ weapon:t="p-51d-20_6xbazooka"
+ type:t="plane"
+ skin:t=""
+ country:t="country_usa"
+ rank:ip2=2, 4
+ }
+ 
+ premiumVehicle{
+ unitName:t="a2d"
+ weapon:t="a2d_10x500lbs"
+ type:t="plane"
+ skin:t=""
+ country:t="country_usa"
+ rank:ip2=2, 4
+ }
+ 
+ premiumVehicle{
+ unitName:t="f-89b"
+ weapon:t="f_89_default"
+ type:t="plane"
+ skin:t=""
+ country:t="country_usa"
+ rank:ip2=4, 6
+ }
+ 
+ premiumVehicle{
+ unitName:t="f-86f-35"
+ weapon:t="f_86_hvar_rockets"
+ type:t="plane"
+ skin:t=""
+ country:t="country_usa"
+ rank:ip2=4, 6
+ }
+ 
+ premiumVehicle{
+ unitName:t="f-5c"
+ weapon:t="f_5c_rockets_agm_12b"
+ type:t="plane"
+ skin:t=""
+ country:t="country_usa"
+ rank:ip2=5, 7
+ }
+ 
+ premiumVehicle{
+ unitName:t="a_10a_early"
+ weapon:t="a_10a_default"
+ type:t="plane"
+ skin:t=""
+ country:t="country_usa"
+ rank:ip2=4, 7
+ }
+ 
+ premiumVehicle{
+ unitName:t="f-4s"
+ weapon:t="f_4s_default"
+ type:t="plane"
+ skin:t=""
+ country:t="country_usa"
+ rank:ip2=5, 7
+ }
+ 
+ premiumVehicle{
+ unitName:t="av_8b_na"
+ weapon:t="av_8b_plus_default"
+ type:t="plane"
+ skin:t=""
+ country:t="country_usa"
+ rank:ip2=4, 7
+ }
+ 
+ premiumVehicle{
+ unitName:t="ah_64a_greece_usa"
+ weapon:t="ah_64a_greece_usa_default"
+ type:t="plane"
+ skin:t=""
+ country:t="country_usa"
+ rank:ip2=4, 7
+ }
+ 
+ premiumVehicle{
+ unitName:t="f_20a"
+ weapon:t="f_20a_default"
+ type:t="plane"
+ skin:t=""
+ country:t="country_usa"
+ rank:ip2=5, 8
+ }
+ 
+ premiumVehicle{
+ unitName:t="he_112b_1"
+ weapon:t=""
+ type:t="plane"
+ skin:t=""
+ country:t="country_germany"
+ rank:ip2=1, 1
+ }
+ 
+ premiumVehicle{
+ unitName:t="ta_154a_1"
+ weapon:t=""
+ type:t="plane"
+ skin:t=""
+ country:t="country_germany"
+ rank:ip2=1, 3
+ }
+ 
+ premiumVehicle{
+ unitName:t="fw_190a_5_u14"
+ weapon:t="fw_190a_5_f5b_torpedo"
+ type:t="plane"
+ skin:t=""
+ country:t="country_germany"
+ rank:ip2=1, 3
+ }
+ 
+ premiumVehicle{
+ unitName:t="ju-288c"
+ weapon:t="Ju-288C_2x1800kg"
+ type:t="plane"
+ skin:t=""
+ country:t="country_germany"
+ rank:ip2=2, 4
+ }
+ 
+ premiumVehicle{
+ unitName:t="fiat_g91_r4_german"
+ weapon:t="fiat_g91_r4_4xas20"
+ type:t="plane"
+ skin:t=""
+ country:t="country_germany"
+ rank:ip2=4, 6
+ }
+ 
+ premiumVehicle{
+ unitName:t="ffa_p16"
+ weapon:t="ffa_p16_default"
+ type:t="plane"
+ skin:t=""
+ country:t="country_germany"
+ rank:ip2=4, 6
+ }
+ 
+ premiumVehicle{
+ unitName:t="mig-21_bis_lazur"
+ weapon:t="mig_21_bis_lazur_default"
+ type:t="plane"
+ skin:t=""
+ country:t="country_germany"
+ rank:ip2=5, 8
+ }
+ 
+ premiumVehicle{
+ unitName:t="tornado_ids_de_wtd61"
+ weapon:t="tornado_ids_de_mfg_fr_mk13_air"
+ type:t="plane"
+ skin:t=""
+ country:t="country_germany"
+ rank:ip2=5, 8
+ }
+ 
+ premiumVehicle{
+ unitName:t="su_22m4_de_wtd61"
+ weapon:t="su_22m4_de_wtd61_rocket_r60mk"
+ type:t="plane"
+ skin:t=""
+ country:t="country_germany"
+ rank:ip2=5, 8
+ }
+ 
+ premiumVehicle{
+ unitName:t="mi_24p_german_hfs80"
+ weapon:t="mi_24p_german_rocket_c_8_ko"
+ type:t="plane"
+ skin:t=""
+ country:t="country_germany"
+ rank:ip2=5, 7
+ }
+ 
+ premiumVehicle{
+ unitName:t="i-153p"
+ weapon:t="I153_rockets_rbs"
+ type:t="plane"
+ skin:t=""
+ country:t="country_ussr"
+ rank:ip2=1, 2
+ }
+ 
+ premiumVehicle{
+ unitName:t="p-47d_ussr"
+ weapon:t="P_47D_bombs"
+ type:t="plane"
+ skin:t=""
+ country:t="country_ussr"
+ rank:ip2=1, 3
+ }
+ 
+ premiumVehicle{
+ unitName:t="a_20g_30_ussr"
+ weapon:t="a_20g_30_45_36_torpedo_x2"
+ type:t="plane"
+ skin:t=""
+ country:t="country_ussr"
+ rank:ip2=1, 3
+ }
+ 
+ premiumVehicle{
+ unitName:t="yak-3_vk107"
+ weapon:t="Yak3_default"
+ type:t="plane"
+ skin:t=""
+ country:t="country_ussr"
+ rank:ip2=2, 4
+ }
+ 
+ premiumVehicle{
+ unitName:t="su_6_single"
+ weapon:t="su_6_single_rs132"
+ type:t="plane"
+ skin:t=""
+ country:t="country_ussr"
+ rank:ip2=2, 4
+ }
+ 
+ premiumVehicle{
+ unitName:t="su-11"
+ weapon:t="su_11_default"
+ type:t="plane"
+ skin:t=""
+ country:t="country_ussr"
+ rank:ip2=3, 5
+ }
+ 
+ premiumVehicle{
+ unitName:t="mig-17_cuba"
+ weapon:t="mig_17_2xr3s_rockets"
+ type:t="plane"
+ skin:t=""
+ country:t="country_ussr"
+ rank:ip2=4, 6
+ }
+ 
+ premiumVehicle{
+ unitName:t="yak-38"
+ weapon:t="yak_38_2x_r60"
+ type:t="plane"
+ skin:t=""
+ country:t="country_ussr"
+ rank:ip2=4, 7
+ }
+ 
+ premiumVehicle{
+ unitName:t="su_25k"
+ weapon:t="su_25k_sppu_22_b8m_r_60m"
+ type:t="plane"
+ skin:t=""
+ country:t="country_ussr"
+ rank:ip2=4, 7
+ }
+ 
+ premiumVehicle{
+ unitName:t="mig-21_s"
+ weapon:t="mig_21_s_4x_r3r"
+ type:t="plane"
+ skin:t=""
+ country:t="country_ussr"
+ rank:ip2=5, 7
+ }
+ 
+ premiumVehicle{
+ unitName:t="su_25tm"
+ weapon:t="su_25tm_sppu_22_r60m"
+ type:t="plane"
+ skin:t=""
+ country:t="country_ussr"
+ rank:ip2=5, 8
+ }
+ 
+ premiumVehicle{
+ unitName:t="mig_23ml"
+ weapon:t="mig_23ml_default"
+ type:t="plane"
+ skin:t=""
+ country:t="country_ussr"
+ rank:ip2=5, 8
+ }
+ 
+ premiumVehicle{
+ unitName:t="ka_50"
+ weapon:t="ka_50_rocket_c_8_ko"
+ type:t="plane"
+ skin:t=""
+ country:t="country_ussr"
+ rank:ip2=5, 7
+ }
+ 
+ premiumVehicle{
+ unitName:t="corsair_fmk2"
+ weapon:t="f4u-1a_bomb_1000lb"
+ type:t="plane"
+ skin:t=""
+ country:t="country_britain"
+ rank:ip2=1, 2
+ }
+ 
+ premiumVehicle{
+ unitName:t="hellcat_fmk1"
+ weapon:t="f6f-5_rockets_hvar"
+ type:t="plane"
+ skin:t=""
+ country:t="country_britain"
+ rank:ip2=1, 3
+ }
+ 
+ premiumVehicle{
+ unitName:t="thunderbolt_mk1"
+ weapon:t="p-47d_22_re_1000lbs"
+ type:t="plane"
+ skin:t=""
+ country:t="country_britain"
+ rank:ip2=1, 3
+ }
+ 
+ premiumVehicle{
+ unitName:t="wyvern_s4"
+ weapon:t="wyvern_s4_torpedo_mk15_16x60lb_rockets"
+ type:t="plane"
+ skin:t=""
+ country:t="country_britain"
+ rank:ip2=2, 4
+ }
+ 
+ premiumVehicle{
+ unitName:t="dh_110_sea_vixen"
+ weapon:t="dh110_sea_vixen_default"
+ type:t="plane"
+ skin:t=""
+ country:t="country_britain"
+ rank:ip2=4, 6
+ }
+ 
+ premiumVehicle{
+ unitName:t="attaker_fb2"
+ weapon:t="attaker_fb1_12rockets"
+ type:t="plane"
+ skin:t=""
+ country:t="country_britain"
+ rank:ip2=4, 6
+ }
+ 
+ premiumVehicle{
+ unitName:t="harrier_gr1"
+ weapon:t="harrier_gr1_default"
+ type:t="plane"
+ skin:t=""
+ country:t="country_britain"
+ rank:ip2=5, 7
+ }
+ 
+ premiumVehicle{
+ unitName:t="lightning_f53"
+ weapon:t="lightning_f35_default"
+ type:t="plane"
+ skin:t=""
+ country:t="country_britain"
+ rank:ip2=5, 7
+ }
+ 
+ premiumVehicle{
+ unitName:t="f-4jk"
+ weapon:t="f_4jk_default"
+ type:t="plane"
+ skin:t=""
+ country:t="country_britain"
+ rank:ip2=5, 8
+ }
+ 
+ premiumVehicle{
+ unitName:t="mig-21_bison"
+ weapon:t="mig_21_bison_default"
+ type:t="plane"
+ skin:t=""
+ country:t="country_britain"
+ rank:ip2=5, 8
+ }
+ 
+ premiumVehicle{
+ unitName:t="g_lynx"
+ weapon:t="g_lynx_default"
+ type:t="plane"
+ skin:t=""
+ country:t="country_britain"
+ rank:ip2=5, 7
+ }
+ 
+ premiumVehicle{
+ unitName:t="ah_2_rooivalk"
+ weapon:t="ah_2_rooivalk_default"
+ type:t="plane"
+ skin:t=""
+ country:t="country_britain"
+ rank:ip2=5, 7
+ }
+ 
+ premiumVehicle{
+ unitName:t="ki_100_2"
+ weapon:t="ki_100_2_250kg_2bomb"
+ type:t="plane"
+ skin:t=""
+ country:t="country_japan"
+ rank:ip2=1, 2
+ }
+ 
+ premiumVehicle{
+ unitName:t="a7m1"
+ weapon:t="a7m_bombs"
+ type:t="plane"
+ skin:t=""
+ country:t="country_japan"
+ rank:ip2=1, 3
+ }
+ 
+ premiumVehicle{
+ unitName:t="p-51c-11-nt_japan"
+ weapon:t="p_51c_default"
+ type:t="plane"
+ skin:t=""
+ country:t="country_japan"
+ rank:ip2=1, 3
+ }
+ 
+ premiumVehicle{
+ unitName:t="j2m5_30mm"
+ weapon:t=""
+ type:t="plane"
+ skin:t=""
+ country:t="country_japan"
+ rank:ip2=2, 4
+ }
+ 
+ premiumVehicle{
+ unitName:t="ki_87"
+ weapon:t="ki_87_250kg_bomb"
+ type:t="plane"
+ skin:t=""
+ country:t="country_japan"
+ rank:ip2=2, 4
+ }
+ 
+ premiumVehicle{
+ unitName:t="f-86f-40_japan"
+ weapon:t="f_86_2xaim9"
+ type:t="plane"
+ skin:t=""
+ country:t="country_japan"
+ rank:ip2=3, 5
+ }
+ 
+ premiumVehicle{
+ unitName:t="av_8s_thailand"
+ weapon:t="av_8s_thailand_rocket_aero_7"
+ type:t="plane"
+ skin:t=""
+ country:t="country_japan"
+ rank:ip2=4, 6
+ }
+ 
+ premiumVehicle{
+ unitName:t="f-4ej_adtw"
+ weapon:t="f_4ej_adtw_default"
+ type:t="plane"
+ skin:t=""
+ country:t="country_japan"
+ rank:ip2=5, 8
+ }
+ 
+ premiumVehicle{
+ unitName:t="ah_1s"
+ weapon:t="ah_1s_rocket_8xTOW"
+ type:t="plane"
+ skin:t=""
+ country:t="country_japan"
+ rank:ip2=5, 7
+ }
+ 
+ premiumVehicle{
+ unitName:t="ki-45_hei_tei_china"
+ weapon:t=""
+ type:t="plane"
+ skin:t=""
+ country:t="country_china"
+ rank:ip2=1, 2
+ }
+ 
+ premiumVehicle{
+ unitName:t="a6m2_zero_china"
+ weapon:t="A6M2_2x60kg"
+ type:t="plane"
+ skin:t=""
+ country:t="country_china"
+ rank:ip2=1, 3
+ }
+ 
+ premiumVehicle{
+ unitName:t="f_47n_25_re_china"
+ weapon:t="f_47n_25_re_china_default"
+ type:t="plane"
+ skin:t=""
+ country:t="country_china"
+ rank:ip2=1, 3
+ }
+ 
+ premiumVehicle{
+ unitName:t="ki_84_ko_china"
+ weapon:t="ki_84_250kg_2bomb"
+ type:t="plane"
+ skin:t=""
+ country:t="country_china"
+ rank:ip2=2, 4
+ }
+ 
+ premiumVehicle{
+ unitName:t="f-84g-31-re_china"
+ weapon:t="f_84g_32hvar"
+ type:t="plane"
+ skin:t=""
+ country:t="country_china"
+ rank:ip2=3, 5
+ }
+ 
+ premiumVehicle{
+ unitName:t="mig-17_f5"
+ weapon:t="mig_17_2xpl2_rockets"
+ type:t="plane"
+ skin:t=""
+ country:t="country_china"
+ rank:ip2=4, 5
+ }
+ 
+ premiumVehicle{
+ unitName:t="a_5c"
+ weapon:t="a_5c_4x500kg_bombs"
+ type:t="plane"
+ skin:t=""
+ country:t="country_china"
+ rank:ip2=4, 7
+ }
+ 
+ premiumVehicle{
+ unitName:t="j_7d"
+ weapon:t="j_7d_default"
+ type:t="plane"
+ skin:t=""
+ country:t="country_china"
+ rank:ip2=5, 8
+ }
+ 
+ premiumVehicle{
+ unitName:t="z_19e"
+ weapon:t="z_19e_default"
+ type:t="plane"
+ skin:t=""
+ country:t="country_china"
+ rank:ip2=5, 7
+ }
+ 
+ premiumVehicle{
+ unitName:t="mi_35m_pakistan"
+ weapon:t="mi_35m_pakistan_rocket_9M39"
+ type:t="plane"
+ skin:t=""
+ country:t="country_china"
+ rank:ip2=5, 7
+ }
+ 
+ premiumVehicle{
+ unitName:t="iar_81c"
+ weapon:t="iar_81c_rockets"
+ type:t="plane"
+ skin:t=""
+ country:t="country_italy"
+ rank:ip2=1, 2
+ }
+ 
+ premiumVehicle{
+ unitName:t="bf_110g_4_hungary"
+ weapon:t="bf-110g_4_under_fuse_gun_pod"
+ type:t="plane"
+ skin:t=""
+ country:t="country_italy"
+ rank:ip2=1, 3
+ }
+ 
+ premiumVehicle{
+ unitName:t="g_55s"
+ weapon:t="g_55s_torpedo"
+ type:t="plane"
+ skin:t=""
+ country:t="country_italy"
+ rank:ip2=2, 4
+ }
+ 
+ premiumVehicle{
+ unitName:t="fiat_g91_r4"
+ weapon:t="fiat_g91_r4_4xaim9"
+ type:t="plane"
+ skin:t=""
+ country:t="country_italy"
+ rank:ip2=4, 6
+ }
+ 
+ premiumVehicle{
+ unitName:t="ariete"
+ weapon:t="sagittario_2_default"
+ type:t="plane"
+ skin:t=""
+ country:t="country_italy"
+ rank:ip2=5, 7
+ }
+ 
+ premiumVehicle{
+ unitName:t="amx_a_1a_brazil"
+ weapon:t="amx_a_1a_brazil_default"
+ type:t="plane"
+ skin:t=""
+ country:t="country_italy"
+ rank:ip2=5, 8
+ }
+ 
+ premiumVehicle{
+ unitName:t="mi_24p_hungary"
+ weapon:t="mi_24p_rocket_c_8_ko"
+ type:t="plane"
+ skin:t=""
+ country:t="country_italy"
+ rank:ip2=5, 7
+ }
+ 
+ premiumVehicle{
+ unitName:t="p-40f-5_france_ep"
+ weapon:t="p_40f_bombs"
+ type:t="plane"
+ skin:t=""
+ country:t="country_france"
+ rank:ip2=1, 2
+ }
+ 
+ premiumVehicle{
+ unitName:t="yak-3_france"
+ weapon:t=""
+ type:t="plane"
+ skin:t=""
+ country:t="country_france"
+ rank:ip2=1, 3
+ }
+ 
+ premiumVehicle{
+ unitName:t="douglas_ad_4na_france"
+ weapon:t="douglas_ad_4na_tyni_tim"
+ type:t="plane"
+ skin:t=""
+ country:t="country_france"
+ rank:ip2=2, 4
+ }
+ 
+ premiumVehicle{
+ unitName:t="so_8000_narval"
+ weapon:t="so_8000_narval_rockets_150"
+ type:t="plane"
+ skin:t=""
+ country:t="country_france"
+ rank:ip2=2, 4
+ }
+ 
+ premiumVehicle{
+ unitName:t="so_4050_vautour_2n"
+ weapon:t="so_4050_vautour_2n_fr_rockets_as_30"
+ type:t="plane"
+ skin:t=""
+ country:t="country_france"
+ rank:ip2=4, 6
+ }
+ 
+ premiumVehicle{
+ unitName:t="mirage_f1c_200"
+ weapon:t="mirage_f1c_default"
+ type:t="plane"
+ skin:t=""
+ country:t="country_france"
+ rank:ip2=5, 8
+ }
+ 
+ premiumVehicle{
+ unitName:t="tiger_hap_france"
+ weapon:t="tiger_hap_france_hot3"
+ type:t="plane"
+ skin:t=""
+ country:t="country_france"
+ rank:ip2=5, 7
+ }
+ 
+ premiumVehicle{
+ unitName:t="ah_64d_netherlands"
+ weapon:t="ah_64d_netherlands_8_hellfire_hydra_70_atas"
+ type:t="plane"
+ skin:t=""
+ country:t="country_france"
+ rank:ip2=5, 7
+ }
+ 
+ premiumVehicle{
+ unitName:t="morko_morane"
+ weapon:t=""
+ type:t="plane"
+ skin:t=""
+ country:t="country_sweden"
+ rank:ip2=1, 2
+ }
+ 
+ premiumVehicle{
+ unitName:t="pyorremyrsky"
+ weapon:t="pyorremyrsky_4x100kg"
+ type:t="plane"
+ skin:t=""
+ country:t="country_sweden"
+ rank:ip2=1, 3
+ }
+ 
+ premiumVehicle{
+ unitName:t="bf-109g-6_finland"
+ weapon:t="Bf-109G-6_default"
+ type:t="plane"
+ skin:t=""
+ country:t="country_sweden"
+ rank:ip2=2, 4
+ }
+ 
+ premiumVehicle{
+ unitName:t="saab_105oe"
+ weapon:t="saab_105oe_default"
+ type:t="plane"
+ skin:t=""
+ country:t="country_sweden"
+ rank:ip2=4, 6
+ }
+ 
+ premiumVehicle{
+ unitName:t="saab_a32a_red_adam"
+ weapon:t="saab_a32a_red_adam_default"
+ type:t="plane"
+ skin:t=""
+ country:t="country_sweden"
+ rank:ip2=4, 6
+ }
+ 
+ premiumVehicle{
+ unitName:t="saab_j35xs"
+ weapon:t="saab_j35xs_default"
+ type:t="plane"
+ skin:t=""
+ country:t="country_sweden"
+ rank:ip2=5, 7
+ }
+ 
+ premiumVehicle{
+ unitName:t="saab_ja37di_f21"
+ weapon:t="saab_ja37di_rockets_rb99"
+ type:t="plane"
+ skin:t=""
+ country:t="country_sweden"
+ rank:ip2=5, 8
+ }
+ 
+ premiumVehicle{
+ unitName:t="spitfire_lf_mk9e_weisman"
+ weapon:t="spitfireIX_default"
+ type:t="plane"
+ skin:t=""
+ country:t="country_israel"
+ rank:ip2=4, 5
+ }
+ 
+ premiumVehicle{
+ unitName:t="f-84f_israel_iaf"
+ weapon:t="f_84f_default"
+ type:t="plane"
+ skin:t=""
+ country:t="country_israel"
+ rank:ip2=4, 5
+ }
+ 
+ premiumVehicle{
+ unitName:t="kfir_canard"
+ weapon:t="kfir_canard_default"
+ type:t="plane"
+ skin:t=""
+ country:t="country_israel"
+ rank:ip2=5, 8
+ }
+ 
+ premiumVehicle{
+ unitName:t="ah_64a_peten_iaf"
+ weapon:t="ah_64a_peten_16_hellfire_stinger"
+ type:t="plane"
+ skin:t=""
+ country:t="country_israel"
+ rank:ip2=5, 7
+ }
+ 
+ premiumVehicle{
+ unitName:t="us_t14"
+ weapon:t="us_t14_default"
+ type:t="tank"
+ skin:t=""
+ country:t="country_usa"
+ rank:ip2=1, 2
+ }
+ 
+ premiumVehicle{
+ unitName:t="us_m4_sherman_calliope"
+ weapon:t=""
+ type:t="tank"
+ skin:t=""
+ country:t="country_usa"
+ rank:ip2=1, 3
+ }
+ 
+ premiumVehicle{
+ unitName:t="us_m4a3e2_sherman_jumbo_cobra_king"
+ weapon:t=""
+ type:t="tank"
+ skin:t=""
+ country:t="country_usa"
+ rank:ip2=1, 3
+ }
+ 
+ premiumVehicle{
+ unitName:t="us_t29"
+ weapon:t=""
+ type:t="tank"
+ skin:t=""
+ country:t="country_usa"
+ rank:ip2=2, 4
+ }
+ 
+ premiumVehicle{
+ unitName:t="us_t54e1"
+ weapon:t=""
+ type:t="tank"
+ skin:t=""
+ country:t="country_usa"
+ rank:ip2=3, 5
+ }
+ 
+ premiumVehicle{
+ unitName:t="us_t54e2"
+ weapon:t=""
+ type:t="tank"
+ skin:t=""
+ country:t="country_usa"
+ rank:ip2=3, 5
+ }
+ 
+ premiumVehicle{
+ unitName:t="us_m728"
+ weapon:t=""
+ type:t="tank"
+ skin:t=""
+ country:t="country_usa"
+ rank:ip2=3, 5
+ }
+ 
+ premiumVehicle{
+ unitName:t="us_m1128_wolfpack"
+ weapon:t=""
+ type:t="tank"
+ skin:t=""
+ country:t="country_usa"
+ rank:ip2=4, 8
+ }
+ 
+ premiumVehicle{
+ unitName:t="us_m1_abrams_kvt"
+ weapon:t="us_m1_abrams_kvt_default"
+ type:t="tank"
+ skin:t=""
+ country:t="country_usa"
+ rank:ip2=4, 8
+ }
+ 
+ premiumVehicle{
+ unitName:t="us_m1a1_hc_usmc"
+ weapon:t="us_m1a1_hc_usmc_default"
+ type:t="tank"
+ skin:t=""
+ country:t="country_usa"
+ rank:ip2=4, 8
+ }
+ 
+ premiumVehicle{
+ unitName:t="us_rdf_lt"
+ weapon:t="us_rdf_lt_default"
+ type:t="tank"
+ skin:t=""
+ country:t="country_usa"
+ rank:ip2=4, 8
+ }
+ 
+ premiumVehicle{
+ unitName:t="ussr_smk"
+ weapon:t="ussr_smk_default"
+ type:t="tank"
+ skin:t=""
+ country:t="country_ussr"
+ rank:ip2=1, 2
+ }
+ 
+ premiumVehicle{
+ unitName:t="ussr_t_34_57_1943"
+ weapon:t="ussr_t_34_57_1943_default"
+ type:t="tank"
+ skin:t=""
+ country:t="country_ussr"
+ rank:ip2=1, 3
+ }
+ 
+ premiumVehicle{
+ unitName:t="ussr_m4a2_76w_sherman"
+ weapon:t="us_m4a2_76w_sherman_default"
+ type:t="tank"
+ skin:t=""
+ country:t="country_ussr"
+ rank:ip2=1, 3
+ }
+ 
+ premiumVehicle{
+ unitName:t="ussr_is_6"
+ weapon:t="ussr_is_6_default"
+ type:t="tank"
+ skin:t=""
+ country:t="country_ussr"
+ rank:ip2=2, 4
+ }
+ 
+ premiumVehicle{
+ unitName:t="ussr_object_120"
+ weapon:t="ussr_object_120_default"
+ type:t="tank"
+ skin:t=""
+ country:t="country_ussr"
+ rank:ip2=3, 5
+ }
+ 
+ premiumVehicle{
+ unitName:t="ussr_to_55"
+ weapon:t="ussr_to_55_default"
+ type:t="tank"
+ skin:t=""
+ country:t="country_ussr"
+ rank:ip2=3, 5
+ }
+ 
+ premiumVehicle{
+ unitName:t="ussr_bmd_4m"
+ weapon:t="ussr_bmd_4m_default"
+ type:t="tank"
+ skin:t=""
+ country:t="country_ussr"
+ rank:ip2=4, 7
+ }
+ 
+ premiumVehicle{
+ unitName:t="ussr_t_55_am"
+ weapon:t="ussr_t_55_am_default"
+ type:t="tank"
+ skin:t=""
+ country:t="country_ussr"
+ rank:ip2=4, 7
+ }
+ 
+ premiumVehicle{
+ unitName:t="ussr_object_140"
+ weapon:t="ussr_object_140_default"
+ type:t="tank"
+ skin:t=""
+ country:t="country_ussr"
+ rank:ip2=4, 7
+ }
+ 
+ premiumVehicle{
+ unitName:t="ussr_t_72av_turms"
+ weapon:t="ussr_t_72av_turms_default"
+ type:t="tank"
+ skin:t=""
+ country:t="country_ussr"
+ rank:ip2=4, 8
+ force:b=yes
+ }
+ 
+ premiumVehicle{
+ unitName:t="ussr_2s38"
+ weapon:t="ussr_2s38_default"
+ type:t="tank"
+ skin:t=""
+ country:t="country_ussr"
+ rank:ip2=4, 8
+ force:b=yes
+ }
+ 
+ premiumVehicle{
+ unitName:t="ussr_t_80ud"
+ weapon:t="ussr_t_80ud_default"
+ type:t="tank"
+ skin:t=""
+ country:t="country_ussr"
+ rank:ip2=4, 8
+ force:b=yes
+ }
+ 
+ premiumVehicle{
+ unitName:t="ussr_t_80ue1"
+ weapon:t="ussr_t_80ue1_default"
+ type:t="tank"
+ skin:t=""
+ country:t="country_ussr"
+ rank:ip2=4, 8
+ force:b=yes
+ }
+ 
+ premiumVehicle{
+ unitName:t="germ_t_34_747"
+ weapon:t="germ_t_34_747_default"
+ type:t="tank"
+ skin:t=""
+ country:t="country_germany"
+ rank:ip2=1, 2
+ }
+ 
+ premiumVehicle{
+ unitName:t="germ_panzerbefelhswagen_IV_ausf_J"
+ weapon:t="germ_pzkpfw_IV_ausf_J_default"
+ type:t="tank"
+ skin:t=""
+ country:t="country_germany"
+ rank:ip2=1, 3
+ }
+ 
+ premiumVehicle{
+ unitName:t="germ_kv_1_kwk_40"
+ weapon:t="germ_kv_1_kwk_40_default"
+ type:t="tank"
+ skin:t=""
+ country:t="country_germany"
+ rank:ip2=1, 3
+ }
+ 
+ premiumVehicle{
+ unitName:t="germ_pzkpfw_VI_ausf_b_tiger_IIh_sla"
+ weapon:t=""
+ type:t="tank"
+ skin:t=""
+ country:t="country_germany"
+ rank:ip2=2, 4
+ }
+ 
+ premiumVehicle{
+ unitName:t="germ_mkpz_m47"
+ weapon:t=""
+ type:t="tank"
+ skin:t=""
+ country:t="country_germany"
+ rank:ip2=3, 5
+ }
+ 
+ premiumVehicle{
+ unitName:t="germ_erprobungstrager_3_achs_turm"
+ weapon:t=""
+ type:t="tank"
+ skin:t=""
+ country:t="country_germany"
+ rank:ip2=3, 5
+ }
+ 
+ premiumVehicle{
+ unitName:t="germ_thyssen_henschel_tam_2ip"
+ weapon:t=""
+ type:t="tank"
+ skin:t=""
+ country:t="country_germany"
+ rank:ip2=4, 6
+ }
+ 
+ premiumVehicle{
+ unitName:t="germ_leopard_a1a1_120"
+ weapon:t=""
+ type:t="tank"
+ skin:t=""
+ country:t="country_germany"
+ rank:ip2=4, 6
+ }
+ 
+ premiumVehicle{
+ unitName:t="germ_leopard_2a4_pzbtl_123"
+ weapon:t=""
+ type:t="tank"
+ skin:t=""
+ country:t="country_germany"
+ rank:ip2=5, 8
+ force:b=yes
+ }
+ 
+ premiumVehicle{
+ unitName:t="germ_leopard_2a4m_can"
+ weapon:t=""
+ type:t="tank"
+ skin:t=""
+ country:t="country_germany"
+ rank:ip2=5, 8
+ force:b=yes
+ }
+ 
+ premiumVehicle{
+ unitName:t="uk_crusader_mk_2_the_saint"
+ weapon:t="uk_crusader_mk_2_default"
+ type:t="tank"
+ skin:t=""
+ country:t="country_britain"
+ rank:ip2=1, 2
+ }
+ 
+ premiumVehicle{
+ unitName:t="uk_m4a5_ram_2"
+ weapon:t="us_m4a5_ram_2_default"
+ type:t="tank"
+ skin:t=""
+ country:t="country_britain"
+ rank:ip2=1, 2
+ }
+ 
+ premiumVehicle{
+ unitName:t="uk_ac4_thunderbolt"
+ weapon:t="uk_ac4_thunderbolt_default"
+ type:t="tank"
+ skin:t=""
+ country:t="country_britain"
+ rank:ip2=1, 3
+ }
+ 
+ premiumVehicle{
+ unitName:t="uk_sherman_ic_firefly"
+ weapon:t=""
+ type:t="tank"
+ skin:t=""
+ country:t="country_britain"
+ rank:ip2=1, 3
+ }
+ 
+ premiumVehicle{
+ unitName:t="uk_centurion_action_x"
+ weapon:t=""
+ type:t="tank"
+ skin:t=""
+ country:t="country_britain"
+ rank:ip2=2, 4
+ }
+ 
+ premiumVehicle{
+ unitName:t="uk_vijayanta"
+ weapon:t=""
+ type:t="tank"
+ skin:t=""
+ country:t="country_britain"
+ rank:ip2=3, 5
+ }
+ 
+ premiumVehicle{
+ unitName:t="uk_khalid"
+ weapon:t=""
+ type:t="tank"
+ skin:t=""
+ country:t="country_britain"
+ rank:ip2=4, 6
+ }
+ 
+ premiumVehicle{
+ unitName:t="uk_challenger_1_mk_3_gulf"
+ weapon:t=""
+ type:t="tank"
+ skin:t=""
+ country:t="country_britain"
+ rank:ip2=5, 8
+ }
+ 
+ premiumVehicle{
+ unitName:t="uk_challenger_2_megatron"
+ weapon:t=""
+ type:t="tank"
+ skin:t=""
+ country:t="country_britain"
+ rank:ip2=5, 8
+ }
+ 
+ premiumVehicle{
+ unitName:t="jp_type_1_chi_he_5th_regiment"
+ weapon:t=""
+ type:t="tank"
+ skin:t=""
+ country:t="country_japan"
+ rank:ip2=1, 2
+ }
+ 
+ premiumVehicle{
+ unitName:t="jp_type_3_chi_nu_75cm_type_5"
+ weapon:t=""
+ type:t="tank"
+ skin:t=""
+ country:t="country_japan"
+ rank:ip2=1, 3
+ }
+ 
+ premiumVehicle{
+ unitName:t="jp_type_5_ho_ri_prototype"
+ weapon:t=""
+ type:t="tank"
+ skin:t=""
+ country:t="country_japan"
+ rank:ip2=2, 4
+ }
+ 
+ premiumVehicle{
+ unitName:t="jp_type_75_mlrs"
+ weapon:t=""
+ type:t="tank"
+ skin:t=""
+ country:t="country_japan"
+ rank:ip2=3, 5
+ }
+ 
+ premiumVehicle{
+ unitName:t="jp_type_74_mod_g_kai"
+ weapon:t=""
+ type:t="tank"
+ skin:t=""
+ country:t="country_japan"
+ rank:ip2=4, 6
+ }
+ 
+ premiumVehicle{
+ unitName:t="jp_type_16_mod"
+ weapon:t=""
+ type:t="tank"
+ skin:t=""
+ country:t="country_japan"
+ rank:ip2=4, 6
+ }
+ 
+ premiumVehicle{
+ unitName:t="jp_type_90b_camo"
+ weapon:t=""
+ type:t="tank"
+ skin:t=""
+ country:t="country_japan"
+ rank:ip2=5, 8
+ }
+ 
+ premiumVehicle{
+ unitName:t="cn_m4a4_sherman_1st_ptg"
+ weapon:t=""
+ type:t="tank"
+ skin:t=""
+ country:t="country_china"
+ rank:ip2=1, 2
+ }
+ 
+ premiumVehicle{
+ unitName:t="cn_m41_a3_walker_bulldog"
+ weapon:t=""
+ type:t="tank"
+ skin:t=""
+ country:t="country_china"
+ rank:ip2=2, 3
+ }
+ 
+ premiumVehicle{
+ unitName:t="cn_t_34_85_zis_53_no215"
+ weapon:t=""
+ type:t="tank"
+ skin:t=""
+ country:t="country_china"
+ rank:ip2=2, 4
+ }
+ 
+ premiumVehicle{
+ unitName:t="cn_is_2_1943_no402"
+ weapon:t=""
+ type:t="tank"
+ skin:t=""
+ country:t="country_china"
+ rank:ip2=2, 4
+ }
+ 
+ premiumVehicle{
+ unitName:t="cn_ztz_59a"
+ weapon:t=""
+ type:t="tank"
+ skin:t=""
+ country:t="country_china"
+ rank:ip2=3, 5
+ }
+ 
+ premiumVehicle{
+ unitName:t="cn_wma_301"
+ weapon:t=""
+ type:t="tank"
+ skin:t=""
+ country:t="country_china"
+ rank:ip2=4, 6
+ }
+ 
+ premiumVehicle{
+ unitName:t="cn_ztz_96a_prot"
+ weapon:t=""
+ type:t="tank"
+ skin:t=""
+ country:t="country_china"
+ rank:ip2=5, 8
+ }
+ 
+ premiumVehicle{
+ unitName:t="cn_al_khalid_1"
+ weapon:t=""
+ type:t="tank"
+ skin:t=""
+ country:t="country_china"
+ rank:ip2=4, 8
+ }
+ 
+ premiumVehicle{
+ unitName:t="it_m14_41_47_40"
+ weapon:t=""
+ type:t="tank"
+ skin:t=""
+ country:t="country_italy"
+ rank:ip2=1, 2
+ }
+ 
+ premiumVehicle{
+ unitName:t="it_sahariano"
+ weapon:t="it_sahariano_default"
+ type:t="tank"
+ skin:t=""
+ country:t="country_italy"
+ rank:ip2=1, 2
+ }
+ 
+ premiumVehicle{
+ unitName:t="it_sherman_75_37"
+ weapon:t=""
+ type:t="tank"
+ skin:t=""
+ country:t="country_italy"
+ rank:ip2=1, 2
+ }
+ 
+ premiumVehicle{
+ unitName:t="it_m26_ariete"
+ weapon:t=""
+ type:t="tank"
+ skin:t=""
+ country:t="country_italy"
+ rank:ip2=2, 4
+ }
+ 
+ premiumVehicle{
+ unitName:t="it_of_40_mtca"
+ weapon:t=""
+ type:t="tank"
+ skin:t=""
+ country:t="country_italy"
+ rank:ip2=4, 6
+ }
+ 
+ premiumVehicle{
+ unitName:t="it_centauro_rgo_120"
+ weapon:t=""
+ type:t="tank"
+ skin:t=""
+ country:t="country_italy"
+ rank:ip2=5, 8
+ }
+ 
+ premiumVehicle{
+ unitName:t="fr_b1_ter"
+ weapon:t=""
+ type:t="tank"
+ skin:t=""
+ country:t="country_france"
+ rank:ip2=1, 2
+ }
+ 
+ premiumVehicle{
+ unitName:t="fr_amx_13_chaffee"
+ weapon:t=""
+ type:t="tank"
+ skin:t=""
+ country:t="country_france"
+ rank:ip2=1, 2
+ }
+ 
+ premiumVehicle{
+ unitName:t="fr_m4a1_sherman_fl_10"
+ weapon:t=""
+ type:t="tank"
+ skin:t=""
+ country:t="country_france"
+ rank:ip2=1, 3
+ }
+ 
+ premiumVehicle{
+ unitName:t="fr_somua_sm"
+ weapon:t=""
+ type:t="tank"
+ skin:t=""
+ country:t="country_france"
+ rank:ip2=2, 4
+ }
+ 
+ premiumVehicle{
+ unitName:t="fr_pzkpfw_V_panther_dauphine"
+ weapon:t=""
+ type:t="tank"
+ skin:t=""
+ country:t="country_france"
+ rank:ip2=2, 4
+ }
+ 
+ premiumVehicle{
+ unitName:t="fr_amx_30_super"
+ weapon:t=""
+ type:t="tank"
+ skin:t=""
+ country:t="country_france"
+ rank:ip2=4, 6
+ }
+ 
+ premiumVehicle{
+ unitName:t="fr_vbci2_mct30"
+ weapon:t=""
+ type:t="tank"
+ skin:t=""
+ country:t="country_france"
+ rank:ip2=4, 8
+ }
+ 
+ premiumVehicle{
+ unitName:t="sw_sav_fm48"
+ weapon:t=""
+ type:t="tank"
+ skin:t=""
+ country:t="country_sweden"
+ rank:ip2=1, 2
+ }
+ 
+ premiumVehicle{
+ unitName:t="sw_sherman_3_4"
+ weapon:t=""
+ type:t="tank"
+ skin:t=""
+ country:t="country_sweden"
+ rank:ip2=1, 3
+ }
+ 
+ premiumVehicle{
+ unitName:t="sw_kv_1_1942_fin"
+ weapon:t=""
+ type:t="tank"
+ skin:t=""
+ country:t="country_sweden"
+ rank:ip2=1, 3
+ }
+ 
+ premiumVehicle{
+ unitName:t="sw_strv_103_0"
+ weapon:t=""
+ type:t="tank"
+ skin:t=""
+ country:t="country_sweden"
+ rank:ip2=3, 5
+ }
+ 
+ premiumVehicle{
+ unitName:t="sw_k9_vidar"
+ weapon:t=""
+ type:t="tank"
+ skin:t=""
+ country:t="country_sweden"
+ rank:ip2=3, 5
+ }
+ 
+ premiumVehicle{
+ unitName:t="sw_leopard_1a5no"
+ weapon:t=""
+ type:t="tank"
+ skin:t=""
+ country:t="country_sweden"
+ rank:ip2=4, 6
+ }
+ 
+ premiumVehicle{
+ unitName:t="sw_cv_9035_dk"
+ weapon:t=""
+ type:t="tank"
+ skin:t=""
+ country:t="country_sweden"
+ rank:ip2=4, 6
+ }
+ 
+ premiumVehicle{
+ unitName:t="sw_cv_90105_tml"
+ weapon:t=""
+ type:t="tank"
+ skin:t=""
+ country:t="country_sweden"
+ rank:ip2=4, 8
+ }
+ 
+ premiumVehicle{
+ unitName:t="sw_strv121b_christian2"
+ weapon:t=""
+ type:t="tank"
+ skin:t=""
+ country:t="country_sweden"
+ rank:ip2=4, 8
+ }
+ 
+ premiumVehicle{
+ unitName:t="il_m_51_w"
+ weapon:t=""
+ type:t="tank"
+ skin:t=""
+ country:t="country_israel"
+ rank:ip2=4, 5
+ }
+ 
+ premiumVehicle{
+ unitName:t="il_magach_3"
+ weapon:t=""
+ type:t="tank"
+ skin:t=""
+ country:t="country_israel"
+ rank:ip2=4, 5
+ }
+ 
+ premiumVehicle{
+ unitName:t="il_centurion_shot_kal_d"
+ weapon:t=""
+ type:t="tank"
+ skin:t=""
+ country:t="country_israel"
+ rank:ip2=5, 6
+ }
+ 
+ premiumVehicle{
+ unitName:t="il_merkava_mk_3_raam_segol"
+ weapon:t=""
+ type:t="tank"
+ skin:t=""
+ country:t="country_israel"
+ rank:ip2=6, 8
+ }
+ 
+ premiumVehicle{
+ unitName:t="us_pc_466_carmi"
+ weapon:t="us_pc_466_carmi_default"
+ type:t="ship"
+ skin:t=""
+ country:t="country_usa"
+ rank:ip2=1, 3
+ }
+ 
+ premiumVehicle{
+ unitName:t="us_elco_80ft_pt174"
+ weapon:t="torpedoes"
+ type:t="ship"
+ skin:t=""
+ country:t="country_usa"
+ rank:ip2=1, 3
+ }
+ 
+ premiumVehicle{
+ unitName:t="us_destroyer_porter_1942"
+ weapon:t="us_destroyer_porter_1942_default"
+ type:t="ship"
+ skin:t=""
+ country:t="country_usa"
+ rank:ip2=1, 3
+ }
+ 
+ premiumVehicle{
+ unitName:t="us_destroyer_gearing_frank_knox"
+ weapon:t="us_destroyer_gearing_frank_knox_default"
+ type:t="ship"
+ skin:t=""
+ country:t="country_usa"
+ rank:ip2=1, 3
+ force:b=yes
+ }
+ 
+ premiumVehicle{
+ unitName:t="us_cruiser_brooklyn_class_helena"
+ weapon:t="us_cruiser_brooklyn_class_helena_default"
+ type:t="ship"
+ skin:t=""
+ country:t="country_usa"
+ rank:ip2=3, 5
+ }
+ 
+ premiumVehicle{
+ unitName:t="us_ashville_class_douglas"
+ weapon:t="us_ashville_class_douglas_default"
+ type:t="ship"
+ skin:t=""
+ country:t="country_usa"
+ rank:ip2=3, 5
+ }
+ 
+ premiumVehicle{
+ unitName:t="us_cruiser_des_moines_class"
+ weapon:t="us_cruiser_des_moines_class_default"
+ type:t="ship"
+ skin:t=""
+ country:t="country_usa"
+ rank:ip2=3, 5
+ }
+ 
+ premiumVehicle{
+ unitName:t="us_battleship_arkansas"
+ weapon:t="us_battleship_arkansas_default"
+ type:t="ship"
+ skin:t=""
+ country:t="country_usa"
+ rank:ip2=4, 6
+ }
+ 
+ premiumVehicle{
+ unitName:t="germ_escort_typem1943"
+ weapon:t="wbg_mortar"
+ type:t="ship"
+ skin:t=""
+ country:t="country_germany"
+ rank:ip2=1, 5
+ }
+ 
+ premiumVehicle{
+ unitName:t="germ_destroyer_fletcher_zerstorer4"
+ weapon:t="torpedoes"
+ type:t="ship"
+ skin:t=""
+ country:t="country_germany"
+ rank:ip2=1, 3
+ }
+ 
+ premiumVehicle{
+ unitName:t="germ_destroyer_class1936c_z47"
+ weapon:t="germ_destroyer_class1936c_z47_default"
+ type:t="ship"
+ skin:t=""
+ country:t="country_germany"
+ rank:ip2=1, 3
+ }
+ 
+ premiumVehicle{
+ unitName:t="germ_cruiser_karlsruhe"
+ weapon:t="germ_cruiser_karlsruhe_default"
+ type:t="ship"
+ skin:t=""
+ country:t="country_germany"
+ rank:ip2=3, 4
+ }
+ 
+ premiumVehicle{
+ unitName:t="germ_battleship_nassau"
+ weapon:t="germ_battleship_nassau_default"
+ type:t="ship"
+ skin:t=""
+ country:t="country_germany"
+ rank:ip2=4, 6
+ }
+ 
+ premiumVehicle{
+ unitName:t="ussr_pr_1204"
+ weapon:t="ussr_pr_1204_default"
+ type:t="ship"
+ skin:t=""
+ country:t="country_ussr"
+ rank:ip2=1, 2
+ }
+ 
+ premiumVehicle{
+ unitName:t="ussr_mkl_186_mk85"
+ weapon:t="ussr_mkl_186_mk85_default"
+ type:t="ship"
+ skin:t=""
+ country:t="country_ussr"
+ rank:ip2=2, 5
+ }
+ 
+ premiumVehicle{
+ unitName:t="ussr_mpk_pr12412p"
+ weapon:t="ussr_mpk_pr12412p_default"
+ type:t="ship"
+ skin:t=""
+ country:t="country_ussr"
+ rank:ip2=3, 5
+ }
+ 
+ premiumVehicle{
+ unitName:t="ussr_skr_pr50plo_rosomacha"
+ weapon:t="ussr_skr_pr50plo_rosomacha_default"
+ type:t="ship"
+ skin:t=""
+ country:t="country_ussr"
+ rank:ip2=3, 5
+ }
+ 
+ premiumVehicle{
+ unitName:t="ussr_destroyer_pr30bis_smelyi"
+ weapon:t="ussr_destroyer_pr30bis_smelyi_default"
+ type:t="ship"
+ skin:t=""
+ country:t="country_ussr"
+ rank:ip2=1, 2
+ }
+ 
+ premiumVehicle{
+ unitName:t="ussr_destroyer_pr56_blagorodny"
+ weapon:t="ussr_destroyer_pr56_blagorodny_default"
+ type:t="ship"
+ skin:t=""
+ country:t="country_ussr"
+ rank:ip2=1, 3
+ }
+ 
+ premiumVehicle{
+ unitName:t="ussr_cruiser_kerch"
+ weapon:t="ussr_cruiser_kerch_default"
+ type:t="ship"
+ skin:t=""
+ country:t="country_ussr"
+ rank:ip2=2, 4
+ }
+ 
+ premiumVehicle{
+ unitName:t="ussr_cruiser_zheleznyakov"
+ weapon:t="ussr_cruiser_zheleznyakov_default"
+ type:t="ship"
+ skin:t=""
+ country:t="country_ussr"
+ rank:ip2=2, 4
+ }
+ 
+ premiumVehicle{
+ unitName:t="ussr_battleship_marat"
+ weapon:t="ussr_battleship_marat_default"
+ type:t="ship"
+ skin:t=""
+ country:t="country_ussr"
+ rank:ip2=4, 6
+ }
+ 
+ premiumVehicle{
+ unitName:t="uk_71ft_mgb"
+ weapon:t="mk_vii_depth_charges"
+ type:t="ship"
+ skin:t=""
+ country:t="country_britain"
+ rank:ip2=1, 2
+ }
+ 
+ premiumVehicle{
+ unitName:t="uk_corvette_orla"
+ weapon:t="uk_corvette_orla_default"
+ type:t="ship"
+ skin:t=""
+ country:t="country_britain"
+ rank:ip2=3, 4
+ }
+ 
+ premiumVehicle{
+ unitName:t="uk_frigate_whitby"
+ weapon:t="uk_frigate_whitby_default"
+ type:t="ship"
+ skin:t=""
+ country:t="country_britain"
+ rank:ip2=2, 4
+ }
+ 
+ premiumVehicle{
+ unitName:t="uk_destroyer_j_class"
+ weapon:t="uk_destroyer_j_class_default"
+ type:t="ship"
+ skin:t=""
+ country:t="country_britain"
+ rank:ip2=1, 2
+ }
+ 
+ premiumVehicle{
+ unitName:t="uk_destroyer_daring_class_diamond"
+ weapon:t="uk_destroyer_daring_class_diamond_default"
+ type:t="ship"
+ skin:t=""
+ country:t="country_britain"
+ rank:ip2=2, 3
+ }
+ 
+ premiumVehicle{
+ unitName:t="uk_cruiser_belfast"
+ weapon:t="uk_cruiser_belfast_default"
+ type:t="ship"
+ skin:t=""
+ country:t="country_britain"
+ rank:ip2=2, 5
+ }
+ 
+ premiumVehicle{
+ unitName:t="jp_pg02"
+ weapon:t="srboc_smoke_grenades_launcher"
+ type:t="ship"
+ skin:t=""
+ country:t="country_japan"
+ rank:ip2=1, 4
+ }
+ 
+ premiumVehicle{
+ unitName:t="jp_escort_akebono_class"
+ weapon:t="bomb_mortar_depth_charges"
+ type:t="ship"
+ skin:t=""
+ country:t="country_japan"
+ rank:ip2=1, 4
+ }
+ 
+ premiumVehicle{
+ unitName:t="jp_destroyer_harukaze"
+ weapon:t="jp_destroyer_harukaze_default"
+ type:t="ship"
+ skin:t=""
+ country:t="country_japan"
+ rank:ip2=1, 2
+ }
+ 
+ premiumVehicle{
+ unitName:t="jp_destroyer_nenohi"
+ weapon:t="jp_destroyer_nenohi_default"
+ type:t="ship"
+ skin:t=""
+ country:t="country_japan"
+ rank:ip2=1, 2
+ }
+ 
+ premiumVehicle{
+ unitName:t="jp_cruiser_yubari"
+ weapon:t="jp_cruiser_yubari_default"
+ type:t="ship"
+ skin:t=""
+ country:t="country_japan"
+ rank:ip2=1, 3
+ }
+ 
+ premiumVehicle{
+ unitName:t="jp_cruiser_mogami_mikuma"
+ weapon:t="jp_cruiser_mogami_mikuma_default"
+ type:t="ship"
+ skin:t=""
+ country:t="country_japan"
+ rank:ip2=2, 4
+ }
+ 
+ premiumVehicle{
+ unitName:t="jp_battleship_yamashiro"
+ weapon:t="jp_battleship_yamashiro_default"
+ type:t="ship"
+ skin:t=""
+ country:t="country_japan"
+ rank:ip2=4, 6
+ }
+ 
+ premiumVehicle{
+ unitName:t="it_p420_sparviero"
+ weapon:t="it_p420_sparviero_default"
+ type:t="ship"
+ skin:t=""
+ country:t="country_italy"
+ rank:ip2=1, 5
+ }
+ 
+ premiumVehicle{
+ unitName:t="it_ms444"
+ weapon:t="it_ms444_default"
+ type:t="ship"
+ skin:t=""
+ country:t="country_italy"
+ rank:ip2=1, 3
+ }
+ 
+ premiumVehicle{
+ unitName:t="it_destroyer_leone_class_tigre"
+ weapon:t="it_destroyer_leone_class_tigre_default"
+ type:t="ship"
+ skin:t=""
+ country:t="country_italy"
+ rank:ip2=1, 3
+ }
+ 
+ premiumVehicle{
+ unitName:t="it_destroyer_fletcher_geniere"
+ weapon:t="it_destroyer_fletcher_geniere_default"
+ type:t="ship"
+ skin:t=""
+ country:t="country_italy"
+ rank:ip2=1, 3
+ }
+ 
+ premiumVehicle{
+ unitName:t="it_gabbiano_class_c16"
+ weapon:t="it_gabbiano_class_c16_default"
+ type:t="ship"
+ skin:t=""
+ country:t="country_italy"
+ rank:ip2=2, 4
+ force:b=yes
+ }
+ 
+ premiumVehicle{
+ unitName:t="it_cruiser_zara_class_pola"
+ weapon:t="it_cruiser_zara_class_default"
+ type:t="ship"
+ skin:t=""
+ country:t="country_italy"
+ rank:ip2=2, 4
+ }
+ 
+ premiumVehicle{
+ unitName:t="it_battleship_leonardo_da_vinci"
+ weapon:t="it_battleship_leonardo_da_vinci_default"
+ type:t="ship"
+ skin:t=""
+ country:t="country_italy"
+ rank:ip2=4, 6
+ }
+ 
+ premiumVehicle{
+ unitName:t="fr_destroyer_aigle_class_aigle"
+ weapon:t="fr_destroyer_aigle_class_aigle_default"
+ type:t="ship"
+ skin:t=""
+ country:t="country_france"
+ rank:ip2=1, 2
+ }
+ 
+ premiumVehicle{
+ unitName:t="fr_cruiser_dugauy_class_dugauy_trouin"
+ weapon:t="it_cruiser_zara_class_default"
+ type:t="ship"
+ skin:t=""
+ country:t="country_france"
+ rank:ip2=2, 3
+ }
+ 
+ premiumVehicle{
+ unitName:t="fr_cruiser_suffren_class_dupleix"
+ weapon:t="fr_cruiser_suffren_class_dupleix_default"
+ type:t="ship"
+ skin:t=""
+ country:t="country_france"
+ rank:ip2=2, 4
+ }
+ 
+ premiumVehicle{
+ unitName:t="fr_battleship_courbet_class_courbet"
+ weapon:t="fr_battleship_courbet_class_courbet_default"
+ type:t="ship"
+ skin:t=""
+ country:t="country_france"
+ rank:ip2=4, 6
+ }
+ 
+ premiumVehicle{
+ unitName:t="fr_vlt2"
+ weapon:t="fr_vlt2_default"
+ type:t="ship"
+ skin:t=""
+ country:t="country_france"
+ rank:ip2=2, 4
```

  **Removed**:
```diff
- newYearHangar:b=yes
- level:t="levels/hangar_field_winter.bin"
- hangarMission:t="gameData/scenes/hangar_field_mission_winter.blk"
- aurora_borealis{
- enabled:b=yes
- top_height:r=10.0
- top_color:p3=0.1, 0.1, 1.4
- bottom_height:r=7.0
- bottom_color:p3=0.1, 1.3, 0.1
- brightness:r=2.15
- speed:r=0.018
- luminance:r=22.0
- ripples_scale:r=8.6
- ripples_speed:r=0.04
- ripples_strength:r=0.83
- }
- 
- env:t="9.024"
- weight:r=7.0
- env{
- env:t="2.064"
- weight:r=3.0
- compatibilityWeight:r=0.0
- }
- 
- country_usa:t="us_m1a2_sep2_abrams"
- country_germany:t="germ_leopard_2a7v"
- country_ussr:t="ussr_t_90m_2020"
- country_britain:t="uk_challenger_2_lep"
- country_japan:t="jp_type_99"
- country_china:t="cn_vt_4b"
- country_italy:t="it_m109g"
- country_france:t="fr_leclerc_azur"
- country_sweden:t="sw_strv_122b_plus"
- country_israel:t="il_m109a1"
- country_usa:t="us_hstv_l"
- country_germany:t="germ_schutzenpanzer_puma"
- country_ussr:t="ussr_2s25m"
- country_britain:t="uk_vickers_mk_11"
- country_japan:t="jp_type_81_tansam"
- country_china:t="cn_ztl_11"
- country_italy:t="it_centauro_mgs_120"
- country_france:t="fr_tpk_641_vpc"
- country_sweden:t="sw_strf_90c"
- country_israel:t="il_m113a1_tow"
- country_usa:t="f_15a"
- country_germany:t="tornado_ids_de_assta1"
- country_ussr:t="su_27"
- country_britain:t="tornado_f3"
- country_japan:t="f_15j"
- country_italy:t="tornado_adv"
- country_france:t="mirage_4000"
- country_china:t="j_11"
- country_sweden:t="saab_jas39a"
- country_israel:t="f_15a_iaf"
```


- **aces.vromfs.bin_u/config/hangar_xboxone.blkx**:

  **Added**:
```diff
+ level:t="levels/hangar_field.bin"
+ hangarMission:t="gameData/scenes/hangar_field_mission.blk"
+ env{
+ env:t="14.5"
+ weight:r=10.0
+ compatibilityWeight:r=1.0
+ }
+ 
+ country_usa:t="us_m1a1_hc_usmc"
+ country_germany:t="germ_pzh_2000"
+ country_ussr:t="ussr_object_140"
+ country_britain:t="uk_challenger_2_megatron"
+ country_japan:t="jp_tkx_prot"
+ country_china:t="cn_plz_05"
+ country_italy:t="it_pzh_2000_hu"
+ country_france:t="fr_leopard_2a6nl"
+ country_sweden:t="sw_leopard_2a6nl"
+ country_israel:t="il_sabra_mk1"
+ country_usa:t="us_rdf_lt"
+ country_germany:t="germ_m44"
+ country_ussr:t="ussr_bmd_4m"
+ country_britain:t="uk_9a35_m"
+ country_japan:t="jp_m44"
+ country_china:t="cn_hq_17"
+ country_italy:t="it_9a35_m"
+ country_france:t="fr_vbci"
+ country_sweden:t="sw_cv_90_mk4"
+ country_israel:t="il_namer_tsrikhon"
+ country_usa:t="f_15e"
+ country_germany:t="ef_2000_block_10"
+ country_ussr:t="su_33"
+ country_britain:t="ef_2000_fgr4"
+ country_japan:t="f_15j_kai"
+ country_italy:t="ef_2000a"
+ country_france:t="rafale_c_f3"
+ country_china:t="j_10a"
+ country_sweden:t="saab_ja37di"
+ country_israel:t="f_15i_raam"
+ mechanics{
+ 
+ country_usa{
+ n:t="unit_hangar_technic_idle_"
+ n:t="unit_hangar_technic_black_idle_"
+ n:t="unit_hangar_technic_asian_idle_"
+ }
+ 
+ country_germany{
+ n:t="unit_hangar_technic_idle_"
+ }
+ 
+ country_ussr{
+ n:t="unit_hangar_technic_idle_"
+ }
+ 
+ country_britain{
+ n:t="unit_hangar_technic_idle_"
+ n:t="unit_hangar_technic_black_idle_"
+ }
+ 
+ country_japan{
+ n:t="unit_hangar_technic_asian_idle_"
+ }
+ 
+ country_italy{
+ n:t="unit_hangar_technic_idle_"
+ }
+ 
+ country_france{
+ n:t="unit_hangar_technic_idle_"
+ n:t="unit_hangar_technic_black_idle_"
+ n:t="unit_hangar_technic_asian_idle_"
+ }
+ 
+ country_china{
+ n:t="unit_hangar_technic_asian_idle_"
+ }
+ 
+ country_sweden{
+ n:t="unit_hangar_technic_idle_"
+ }
+ 
+ country_israel{
+ n:t="unit_hangar_technic_idle_"
+ }
+ }
+ 
+ hangarEffects{
+ checkHoliday:b=yes
+ 
+ hangarEffect{
+ effect:t="misc_firework"
+ areaMin:p3=-0.0, 70.0, 300.0
+ areaMax:p3=200.0, 210.0, 900.0
+ delay:p2=20.0, 40.0
+ }
+ 
+ hangarEffect{
+ effect:t="firework_score_ginger"
+ areaMin:p3=-0.0, 70.0, 300.0
+ areaMax:p3=200.0, 210.0, 900.0
+ delay:p2=3.0, 6.0
+ }
+ 
+ hangarEffect{
+ effect:t="firework_score_turquoise"
+ areaMin:p3=-0.0, 70.0, 300.0
+ areaMax:p3=200.0, 210.0, 900.0
+ delay:p2=4.0, 7.0
+ }
+ 
+ hangarEffect{
+ effect:t="misc_firework"
+ areaMin:p3=-375.0, 70.0, -450.0
+ areaMax:p3=175.0, 140.0, -250.0
+ delay:p2=20.0, 40.0
+ }
+ 
+ hangarEffect{
+ effect:t="firework_score_ginger"
+ areaMin:p3=-375.0, 70.0, -450.0
+ areaMax:p3=175.0, 140.0, -250.0
+ delay:p2=3.0, 6.0
+ }
+ 
+ hangarEffect{
+ effect:t="firework_score_turquoise"
+ areaMin:p3=-375.0, 70.0, -450.0
+ areaMax:p3=175.0, 140.0, -250.0
+ delay:p2=4.0, 7.0
+ }
+ 
+ hangarEffect{
+ effect:t="misc_firework"
+ areaMin:p3=-2200.0, 20.0, -100.0
+ areaMax:p3=-2000.0, 200.0, 300.0
+ delay:p2=20.0, 40.0
+ }
+ 
+ hangarEffect{
+ effect:t="firework_score_turquoise"
+ areaMin:p3=-2200.0, 20.0, -100.0
+ areaMax:p3=-2000.0, 200.0, 300.0
+ delay:p2=3.0, 6.0
+ }
+ 
+ hangarEffect{
+ effect:t="firework_score_ginger"
+ areaMin:p3=-2200.0, 20.0, -100.0
+ areaMax:p3=-2000.0, 200.0, 300.0
+ delay:p2=4.0, 7.0
+ }
+ }
+ 
+ premiumVehicle{
+ unitName:t="xp-55"
+ weapon:t="xp-55_default"
+ type:t="plane"
+ skin:t=""
+ country:t="country_usa"
+ rank:ip2=1, 2
+ }
+ 
+ premiumVehicle{
+ unitName:t="btd-1"
+ weapon:t="btd_1_default"
+ type:t="plane"
+ skin:t=""
+ country:t="country_usa"
+ rank:ip2=1, 3
+ }
+ 
+ premiumVehicle{
+ unitName:t="p-51d-20-na"
+ weapon:t="p-51d-20_6xbazooka"
+ type:t="plane"
+ skin:t=""
+ country:t="country_usa"
+ rank:ip2=2, 4
+ }
+ 
+ premiumVehicle{
+ unitName:t="a2d"
+ weapon:t="a2d_10x500lbs"
+ type:t="plane"
+ skin:t=""
+ country:t="country_usa"
+ rank:ip2=2, 4
+ }
+ 
+ premiumVehicle{
+ unitName:t="f-89b"
+ weapon:t="f_89_default"
+ type:t="plane"
+ skin:t=""
+ country:t="country_usa"
+ rank:ip2=4, 6
+ }
+ 
+ premiumVehicle{
+ unitName:t="f-86f-35"
+ weapon:t="f_86_hvar_rockets"
+ type:t="plane"
+ skin:t=""
+ country:t="country_usa"
+ rank:ip2=4, 6
+ }
+ 
+ premiumVehicle{
+ unitName:t="f-5c"
+ weapon:t="f_5c_rockets_agm_12b"
+ type:t="plane"
+ skin:t=""
+ country:t="country_usa"
+ rank:ip2=5, 7
+ }
+ 
+ premiumVehicle{
+ unitName:t="a_10a_early"
+ weapon:t="a_10a_default"
+ type:t="plane"
+ skin:t=""
+ country:t="country_usa"
+ rank:ip2=4, 7
+ }
+ 
+ premiumVehicle{
+ unitName:t="f-4s"
+ weapon:t="f_4s_default"
+ type:t="plane"
+ skin:t=""
+ country:t="country_usa"
+ rank:ip2=5, 7
+ }
+ 
+ premiumVehicle{
+ unitName:t="av_8b_na"
+ weapon:t="av_8b_plus_default"
+ type:t="plane"
+ skin:t=""
+ country:t="country_usa"
+ rank:ip2=4, 7
+ }
+ 
+ premiumVehicle{
+ unitName:t="ah_64a_greece_usa"
+ weapon:t="ah_64a_greece_usa_default"
+ type:t="plane"
+ skin:t=""
+ country:t="country_usa"
+ rank:ip2=4, 7
+ }
+ 
+ premiumVehicle{
+ unitName:t="f_20a"
+ weapon:t="f_20a_default"
+ type:t="plane"
+ skin:t=""
+ country:t="country_usa"
+ rank:ip2=5, 8
+ }
+ 
+ premiumVehicle{
+ unitName:t="he_112b_1"
+ weapon:t=""
+ type:t="plane"
+ skin:t=""
+ country:t="country_germany"
+ rank:ip2=1, 1
+ }
+ 
+ premiumVehicle{
+ unitName:t="ta_154a_1"
+ weapon:t=""
+ type:t="plane"
+ skin:t=""
+ country:t="country_germany"
+ rank:ip2=1, 3
+ }
+ 
+ premiumVehicle{
+ unitName:t="fw_190a_5_u14"
+ weapon:t="fw_190a_5_f5b_torpedo"
+ type:t="plane"
+ skin:t=""
+ country:t="country_germany"
+ rank:ip2=1, 3
+ }
+ 
+ premiumVehicle{
+ unitName:t="ju-288c"
+ weapon:t="Ju-288C_2x1800kg"
+ type:t="plane"
+ skin:t=""
+ country:t="country_germany"
+ rank:ip2=2, 4
+ }
+ 
+ premiumVehicle{
+ unitName:t="fiat_g91_r4_german"
+ weapon:t="fiat_g91_r4_4xas20"
+ type:t="plane"
+ skin:t=""
+ country:t="country_germany"
+ rank:ip2=4, 6
+ }
+ 
+ premiumVehicle{
+ unitName:t="ffa_p16"
+ weapon:t="ffa_p16_default"
+ type:t="plane"
+ skin:t=""
+ country:t="country_germany"
+ rank:ip2=4, 6
+ }
+ 
+ premiumVehicle{
+ unitName:t="mig-21_bis_lazur"
+ weapon:t="mig_21_bis_lazur_default"
+ type:t="plane"
+ skin:t=""
+ country:t="country_germany"
+ rank:ip2=5, 8
+ }
+ 
+ premiumVehicle{
+ unitName:t="tornado_ids_de_wtd61"
+ weapon:t="tornado_ids_de_mfg_fr_mk13_air"
+ type:t="plane"
+ skin:t=""
+ country:t="country_germany"
+ rank:ip2=5, 8
+ }
+ 
+ premiumVehicle{
+ unitName:t="su_22m4_de_wtd61"
+ weapon:t="su_22m4_de_wtd61_rocket_r60mk"
+ type:t="plane"
+ skin:t=""
+ country:t="country_germany"
+ rank:ip2=5, 8
+ }
+ 
+ premiumVehicle{
+ unitName:t="mi_24p_german_hfs80"
+ weapon:t="mi_24p_german_rocket_c_8_ko"
+ type:t="plane"
+ skin:t=""
+ country:t="country_germany"
+ rank:ip2=5, 7
+ }
+ 
+ premiumVehicle{
+ unitName:t="i-153p"
+ weapon:t="I153_rockets_rbs"
+ type:t="plane"
+ skin:t=""
+ country:t="country_ussr"
+ rank:ip2=1, 2
+ }
+ 
+ premiumVehicle{
+ unitName:t="p-47d_ussr"
+ weapon:t="P_47D_bombs"
+ type:t="plane"
+ skin:t=""
+ country:t="country_ussr"
+ rank:ip2=1, 3
+ }
+ 
+ premiumVehicle{
+ unitName:t="a_20g_30_ussr"
+ weapon:t="a_20g_30_45_36_torpedo_x2"
+ type:t="plane"
+ skin:t=""
+ country:t="country_ussr"
+ rank:ip2=1, 3
+ }
+ 
+ premiumVehicle{
+ unitName:t="yak-3_vk107"
+ weapon:t="Yak3_default"
+ type:t="plane"
+ skin:t=""
+ country:t="country_ussr"
+ rank:ip2=2, 4
+ }
+ 
+ premiumVehicle{
+ unitName:t="su_6_single"
+ weapon:t="su_6_single_rs132"
+ type:t="plane"
+ skin:t=""
+ country:t="country_ussr"
+ rank:ip2=2, 4
+ }
+ 
+ premiumVehicle{
+ unitName:t="su-11"
+ weapon:t="su_11_default"
+ type:t="plane"
+ skin:t=""
+ country:t="country_ussr"
+ rank:ip2=3, 5
+ }
+ 
+ premiumVehicle{
+ unitName:t="mig-17_cuba"
+ weapon:t="mig_17_2xr3s_rockets"
+ type:t="plane"
+ skin:t=""
+ country:t="country_ussr"
+ rank:ip2=4, 6
+ }
+ 
+ premiumVehicle{
+ unitName:t="yak-38"
+ weapon:t="yak_38_2x_r60"
+ type:t="plane"
+ skin:t=""
+ country:t="country_ussr"
+ rank:ip2=4, 7
+ }
+ 
+ premiumVehicle{
+ unitName:t="su_25k"
+ weapon:t="su_25k_sppu_22_b8m_r_60m"
+ type:t="plane"
+ skin:t=""
+ country:t="country_ussr"
+ rank:ip2=4, 7
+ }
+ 
+ premiumVehicle{
+ unitName:t="mig-21_s"
+ weapon:t="mig_21_s_4x_r3r"
+ type:t="plane"
+ skin:t=""
+ country:t="country_ussr"
+ rank:ip2=5, 7
+ }
+ 
+ premiumVehicle{
+ unitName:t="su_25tm"
+ weapon:t="su_25tm_sppu_22_r60m"
+ type:t="plane"
+ skin:t=""
+ country:t="country_ussr"
+ rank:ip2=5, 8
+ }
+ 
+ premiumVehicle{
+ unitName:t="mig_23ml"
+ weapon:t="mig_23ml_default"
+ type:t="plane"
+ skin:t=""
+ country:t="country_ussr"
+ rank:ip2=5, 8
+ }
+ 
+ premiumVehicle{
+ unitName:t="ka_50"
+ weapon:t="ka_50_rocket_c_8_ko"
+ type:t="plane"
+ skin:t=""
+ country:t="country_ussr"
+ rank:ip2=5, 7
+ }
+ 
+ premiumVehicle{
+ unitName:t="corsair_fmk2"
+ weapon:t="f4u-1a_bomb_1000lb"
+ type:t="plane"
+ skin:t=""
+ country:t="country_britain"
+ rank:ip2=1, 2
+ }
+ 
+ premiumVehicle{
+ unitName:t="hellcat_fmk1"
+ weapon:t="f6f-5_rockets_hvar"
+ type:t="plane"
+ skin:t=""
+ country:t="country_britain"
+ rank:ip2=1, 3
+ }
+ 
+ premiumVehicle{
+ unitName:t="thunderbolt_mk1"
+ weapon:t="p-47d_22_re_1000lbs"
+ type:t="plane"
+ skin:t=""
+ country:t="country_britain"
+ rank:ip2=1, 3
+ }
+ 
+ premiumVehicle{
+ unitName:t="wyvern_s4"
+ weapon:t="wyvern_s4_torpedo_mk15_16x60lb_rockets"
+ type:t="plane"
+ skin:t=""
+ country:t="country_britain"
+ rank:ip2=2, 4
+ }
+ 
+ premiumVehicle{
+ unitName:t="dh_110_sea_vixen"
+ weapon:t="dh110_sea_vixen_default"
+ type:t="plane"
+ skin:t=""
+ country:t="country_britain"
+ rank:ip2=4, 6
+ }
+ 
+ premiumVehicle{
+ unitName:t="attaker_fb2"
+ weapon:t="attaker_fb1_12rockets"
+ type:t="plane"
+ skin:t=""
+ country:t="country_britain"
+ rank:ip2=4, 6
+ }
+ 
+ premiumVehicle{
+ unitName:t="harrier_gr1"
+ weapon:t="harrier_gr1_default"
+ type:t="plane"
+ skin:t=""
+ country:t="country_britain"
+ rank:ip2=5, 7
+ }
+ 
+ premiumVehicle{
+ unitName:t="lightning_f53"
+ weapon:t="lightning_f35_default"
+ type:t="plane"
+ skin:t=""
+ country:t="country_britain"
+ rank:ip2=5, 7
+ }
+ 
+ premiumVehicle{
+ unitName:t="f-4jk"
+ weapon:t="f_4jk_default"
+ type:t="plane"
+ skin:t=""
+ country:t="country_britain"
+ rank:ip2=5, 8
+ }
+ 
+ premiumVehicle{
+ unitName:t="mig-21_bison"
+ weapon:t="mig_21_bison_default"
+ type:t="plane"
+ skin:t=""
+ country:t="country_britain"
+ rank:ip2=5, 8
+ }
+ 
+ premiumVehicle{
+ unitName:t="g_lynx"
+ weapon:t="g_lynx_default"
+ type:t="plane"
+ skin:t=""
+ country:t="country_britain"
+ rank:ip2=5, 7
+ }
+ 
+ premiumVehicle{
+ unitName:t="ah_2_rooivalk"
+ weapon:t="ah_2_rooivalk_default"
+ type:t="plane"
+ skin:t=""
+ country:t="country_britain"
+ rank:ip2=5, 7
+ }
+ 
+ premiumVehicle{
+ unitName:t="ki_100_2"
+ weapon:t="ki_100_2_250kg_2bomb"
+ type:t="plane"
+ skin:t=""
+ country:t="country_japan"
+ rank:ip2=1, 2
+ }
+ 
+ premiumVehicle{
+ unitName:t="a7m1"
+ weapon:t="a7m_bombs"
+ type:t="plane"
+ skin:t=""
+ country:t="country_japan"
+ rank:ip2=1, 3
+ }
+ 
+ premiumVehicle{
+ unitName:t="p-51c-11-nt_japan"
+ weapon:t="p_51c_default"
+ type:t="plane"
+ skin:t=""
+ country:t="country_japan"
+ rank:ip2=1, 3
+ }
+ 
+ premiumVehicle{
+ unitName:t="j2m5_30mm"
+ weapon:t=""
+ type:t="plane"
+ skin:t=""
+ country:t="country_japan"
+ rank:ip2=2, 4
+ }
+ 
+ premiumVehicle{
+ unitName:t="ki_87"
+ weapon:t="ki_87_250kg_bomb"
+ type:t="plane"
+ skin:t=""
+ country:t="country_japan"
+ rank:ip2=2, 4
+ }
+ 
+ premiumVehicle{
+ unitName:t="f-86f-40_japan"
+ weapon:t="f_86_2xaim9"
+ type:t="plane"
+ skin:t=""
+ country:t="country_japan"
+ rank:ip2=3, 5
+ }
+ 
+ premiumVehicle{
+ unitName:t="av_8s_thailand"
+ weapon:t="av_8s_thailand_rocket_aero_7"
+ type:t="plane"
+ skin:t=""
+ country:t="country_japan"
+ rank:ip2=4, 6
+ }
+ 
+ premiumVehicle{
+ unitName:t="f-4ej_adtw"
+ weapon:t="f_4ej_adtw_default"
+ type:t="plane"
+ skin:t=""
+ country:t="country_japan"
+ rank:ip2=5, 8
+ }
+ 
+ premiumVehicle{
+ unitName:t="ah_1s"
+ weapon:t="ah_1s_rocket_8xTOW"
+ type:t="plane"
+ skin:t=""
+ country:t="country_japan"
+ rank:ip2=5, 7
+ }
+ 
+ premiumVehicle{
+ unitName:t="ki-45_hei_tei_china"
+ weapon:t=""
+ type:t="plane"
+ skin:t=""
+ country:t="country_china"
+ rank:ip2=1, 2
+ }
+ 
+ premiumVehicle{
+ unitName:t="a6m2_zero_china"
+ weapon:t="A6M2_2x60kg"
+ type:t="plane"
+ skin:t=""
+ country:t="country_china"
+ rank:ip2=1, 3
+ }
+ 
+ premiumVehicle{
+ unitName:t="f_47n_25_re_china"
+ weapon:t="f_47n_25_re_china_default"
+ type:t="plane"
+ skin:t=""
+ country:t="country_china"
+ rank:ip2=1, 3
+ }
+ 
+ premiumVehicle{
+ unitName:t="ki_84_ko_china"
+ weapon:t="ki_84_250kg_2bomb"
+ type:t="plane"
+ skin:t=""
+ country:t="country_china"
+ rank:ip2=2, 4
+ }
+ 
+ premiumVehicle{
+ unitName:t="f-84g-31-re_china"
+ weapon:t="f_84g_32hvar"
+ type:t="plane"
+ skin:t=""
+ country:t="country_china"
+ rank:ip2=3, 5
+ }
+ 
+ premiumVehicle{
+ unitName:t="mig-17_f5"
+ weapon:t="mig_17_2xpl2_rockets"
+ type:t="plane"
+ skin:t=""
+ country:t="country_china"
+ rank:ip2=4, 5
+ }
+ 
+ premiumVehicle{
+ unitName:t="a_5c"
+ weapon:t="a_5c_4x500kg_bombs"
+ type:t="plane"
+ skin:t=""
+ country:t="country_china"
+ rank:ip2=4, 7
+ }
+ 
+ premiumVehicle{
+ unitName:t="j_7d"
+ weapon:t="j_7d_default"
+ type:t="plane"
+ skin:t=""
+ country:t="country_china"
+ rank:ip2=5, 8
+ }
+ 
+ premiumVehicle{
+ unitName:t="z_19e"
+ weapon:t="z_19e_default"
+ type:t="plane"
+ skin:t=""
+ country:t="country_china"
+ rank:ip2=5, 7
+ }
+ 
+ premiumVehicle{
+ unitName:t="mi_35m_pakistan"
+ weapon:t="mi_35m_pakistan_rocket_9M39"
+ type:t="plane"
+ skin:t=""
+ country:t="country_china"
+ rank:ip2=5, 7
+ }
+ 
+ premiumVehicle{
+ unitName:t="iar_81c"
+ weapon:t="iar_81c_rockets"
+ type:t="plane"
+ skin:t=""
+ country:t="country_italy"
+ rank:ip2=1, 2
+ }
+ 
+ premiumVehicle{
+ unitName:t="bf_110g_4_hungary"
+ weapon:t="bf-110g_4_under_fuse_gun_pod"
+ type:t="plane"
+ skin:t=""
+ country:t="country_italy"
+ rank:ip2=1, 3
+ }
+ 
+ premiumVehicle{
+ unitName:t="g_55s"
+ weapon:t="g_55s_torpedo"
+ type:t="plane"
+ skin:t=""
+ country:t="country_italy"
+ rank:ip2=2, 4
+ }
+ 
+ premiumVehicle{
+ unitName:t="fiat_g91_r4"
+ weapon:t="fiat_g91_r4_4xaim9"
+ type:t="plane"
+ skin:t=""
+ country:t="country_italy"
+ rank:ip2=4, 6
+ }
+ 
+ premiumVehicle{
+ unitName:t="ariete"
+ weapon:t="sagittario_2_default"
+ type:t="plane"
+ skin:t=""
+ country:t="country_italy"
+ rank:ip2=5, 7
+ }
+ 
+ premiumVehicle{
+ unitName:t="amx_a_1a_brazil"
+ weapon:t="amx_a_1a_brazil_default"
+ type:t="plane"
+ skin:t=""
+ country:t="country_italy"
+ rank:ip2=5, 8
+ }
+ 
+ premiumVehicle{
+ unitName:t="mi_24p_hungary"
+ weapon:t="mi_24p_rocket_c_8_ko"
+ type:t="plane"
+ skin:t=""
+ country:t="country_italy"
+ rank:ip2=5, 7
+ }
+ 
+ premiumVehicle{
+ unitName:t="p-40f-5_france_ep"
+ weapon:t="p_40f_bombs"
+ type:t="plane"
+ skin:t=""
+ country:t="country_france"
+ rank:ip2=1, 2
+ }
+ 
+ premiumVehicle{
+ unitName:t="yak-3_france"
+ weapon:t=""
+ type:t="plane"
+ skin:t=""
+ country:t="country_france"
+ rank:ip2=1, 3
+ }
+ 
+ premiumVehicle{
+ unitName:t="douglas_ad_4na_france"
+ weapon:t="douglas_ad_4na_tyni_tim"
+ type:t="plane"
+ skin:t=""
+ country:t="country_france"
+ rank:ip2=2, 4
+ }
+ 
+ premiumVehicle{
+ unitName:t="so_8000_narval"
+ weapon:t="so_8000_narval_rockets_150"
+ type:t="plane"
+ skin:t=""
+ country:t="country_france"
+ rank:ip2=2, 4
+ }
+ 
+ premiumVehicle{
+ unitName:t="so_4050_vautour_2n"
+ weapon:t="so_4050_vautour_2n_fr_rockets_as_30"
+ type:t="plane"
+ skin:t=""
+ country:t="country_france"
+ rank:ip2=4, 6
+ }
+ 
+ premiumVehicle{
+ unitName:t="mirage_f1c_200"
+ weapon:t="mirage_f1c_default"
+ type:t="plane"
+ skin:t=""
+ country:t="country_france"
+ rank:ip2=5, 8
+ }
+ 
+ premiumVehicle{
+ unitName:t="tiger_hap_france"
+ weapon:t="tiger_hap_france_hot3"
+ type:t="plane"
+ skin:t=""
+ country:t="country_france"
+ rank:ip2=5, 7
+ }
+ 
+ premiumVehicle{
+ unitName:t="ah_64d_netherlands"
+ weapon:t="ah_64d_netherlands_8_hellfire_hydra_70_atas"
+ type:t="plane"
+ skin:t=""
+ country:t="country_france"
+ rank:ip2=5, 7
+ }
+ 
+ premiumVehicle{
+ unitName:t="morko_morane"
+ weapon:t=""
+ type:t="plane"
+ skin:t=""
+ country:t="country_sweden"
+ rank:ip2=1, 2
+ }
+ 
+ premiumVehicle{
+ unitName:t="pyorremyrsky"
+ weapon:t="pyorremyrsky_4x100kg"
+ type:t="plane"
+ skin:t=""
+ country:t="country_sweden"
+ rank:ip2=1, 3
+ }
+ 
+ premiumVehicle{
+ unitName:t="bf-109g-6_finland"
+ weapon:t="Bf-109G-6_default"
+ type:t="plane"
+ skin:t=""
+ country:t="country_sweden"
+ rank:ip2=2, 4
+ }
+ 
+ premiumVehicle{
+ unitName:t="saab_105oe"
+ weapon:t="saab_105oe_default"
+ type:t="plane"
+ skin:t=""
+ country:t="country_sweden"
+ rank:ip2=4, 6
+ }
+ 
+ premiumVehicle{
+ unitName:t="saab_a32a_red_adam"
+ weapon:t="saab_a32a_red_adam_default"
+ type:t="plane"
+ skin:t=""
+ country:t="country_sweden"
+ rank:ip2=4, 6
+ }
+ 
+ premiumVehicle{
+ unitName:t="saab_j35xs"
+ weapon:t="saab_j35xs_default"
+ type:t="plane"
+ skin:t=""
+ country:t="country_sweden"
+ rank:ip2=5, 7
+ }
+ 
+ premiumVehicle{
+ unitName:t="saab_ja37di_f21"
+ weapon:t="saab_ja37di_rockets_rb99"
+ type:t="plane"
+ skin:t=""
+ country:t="country_sweden"
+ rank:ip2=5, 8
+ }
+ 
+ premiumVehicle{
+ unitName:t="spitfire_lf_mk9e_weisman"
+ weapon:t="spitfireIX_default"
+ type:t="plane"
+ skin:t=""
+ country:t="country_israel"
+ rank:ip2=4, 5
+ }
+ 
+ premiumVehicle{
+ unitName:t="f-84f_israel_iaf"
+ weapon:t="f_84f_default"
+ type:t="plane"
+ skin:t=""
+ country:t="country_israel"
+ rank:ip2=4, 5
+ }
+ 
+ premiumVehicle{
+ unitName:t="kfir_canard"
+ weapon:t="kfir_canard_default"
+ type:t="plane"
+ skin:t=""
+ country:t="country_israel"
+ rank:ip2=5, 8
+ }
+ 
+ premiumVehicle{
+ unitName:t="ah_64a_peten_iaf"
+ weapon:t="ah_64a_peten_16_hellfire_stinger"
+ type:t="plane"
+ skin:t=""
+ country:t="country_israel"
+ rank:ip2=5, 7
+ }
+ 
+ premiumVehicle{
+ unitName:t="us_t14"
+ weapon:t="us_t14_default"
+ type:t="tank"
+ skin:t=""
+ country:t="country_usa"
+ rank:ip2=1, 2
+ }
+ 
+ premiumVehicle{
+ unitName:t="us_m4_sherman_calliope"
+ weapon:t=""
+ type:t="tank"
+ skin:t=""
+ country:t="country_usa"
+ rank:ip2=1, 3
+ }
+ 
+ premiumVehicle{
+ unitName:t="us_m4a3e2_sherman_jumbo_cobra_king"
+ weapon:t=""
+ type:t="tank"
+ skin:t=""
+ country:t="country_usa"
+ rank:ip2=1, 3
+ }
+ 
+ premiumVehicle{
+ unitName:t="us_t29"
+ weapon:t=""
+ type:t="tank"
+ skin:t=""
+ country:t="country_usa"
+ rank:ip2=2, 4
+ }
+ 
+ premiumVehicle{
+ unitName:t="us_t54e1"
+ weapon:t=""
+ type:t="tank"
+ skin:t=""
+ country:t="country_usa"
+ rank:ip2=3, 5
+ }
+ 
+ premiumVehicle{
+ unitName:t="us_t54e2"
+ weapon:t=""
+ type:t="tank"
+ skin:t=""
+ country:t="country_usa"
+ rank:ip2=3, 5
+ }
+ 
+ premiumVehicle{
+ unitName:t="us_m728"
+ weapon:t=""
+ type:t="tank"
+ skin:t=""
+ country:t="country_usa"
+ rank:ip2=3, 5
+ }
+ 
+ premiumVehicle{
+ unitName:t="us_m1128_wolfpack"
+ weapon:t=""
+ type:t="tank"
+ skin:t=""
+ country:t="country_usa"
+ rank:ip2=4, 8
+ }
+ 
+ premiumVehicle{
+ unitName:t="us_m1_abrams_kvt"
+ weapon:t="us_m1_abrams_kvt_default"
+ type:t="tank"
+ skin:t=""
+ country:t="country_usa"
+ rank:ip2=4, 8
+ }
+ 
+ premiumVehicle{
+ unitName:t="us_m1a1_hc_usmc"
+ weapon:t="us_m1a1_hc_usmc_default"
+ type:t="tank"
+ skin:t=""
+ country:t="country_usa"
+ rank:ip2=4, 8
+ }
+ 
+ premiumVehicle{
+ unitName:t="us_rdf_lt"
+ weapon:t="us_rdf_lt_default"
+ type:t="tank"
+ skin:t=""
+ country:t="country_usa"
+ rank:ip2=4, 8
+ }
+ 
+ premiumVehicle{
+ unitName:t="ussr_smk"
+ weapon:t="ussr_smk_default"
+ type:t="tank"
+ skin:t=""
+ country:t="country_ussr"
+ rank:ip2=1, 2
+ }
+ 
+ premiumVehicle{
+ unitName:t="ussr_t_34_57_1943"
+ weapon:t="ussr_t_34_57_1943_default"
+ type:t="tank"
+ skin:t=""
+ country:t="country_ussr"
+ rank:ip2=1, 3
+ }
+ 
+ premiumVehicle{
+ unitName:t="ussr_m4a2_76w_sherman"
+ weapon:t="us_m4a2_76w_sherman_default"
+ type:t="tank"
+ skin:t=""
+ country:t="country_ussr"
+ rank:ip2=1, 3
+ }
+ 
+ premiumVehicle{
+ unitName:t="ussr_is_6"
+ weapon:t="ussr_is_6_default"
+ type:t="tank"
+ skin:t=""
+ country:t="country_ussr"
+ rank:ip2=2, 4
+ }
+ 
+ premiumVehicle{
+ unitName:t="ussr_object_120"
+ weapon:t="ussr_object_120_default"
+ type:t="tank"
+ skin:t=""
+ country:t="country_ussr"
+ rank:ip2=3, 5
+ }
+ 
+ premiumVehicle{
+ unitName:t="ussr_to_55"
+ weapon:t="ussr_to_55_default"
+ type:t="tank"
+ skin:t=""
+ country:t="country_ussr"
+ rank:ip2=3, 5
+ }
+ 
+ premiumVehicle{
+ unitName:t="ussr_bmd_4m"
+ weapon:t="ussr_bmd_4m_default"
+ type:t="tank"
+ skin:t=""
+ country:t="country_ussr"
+ rank:ip2=4, 7
+ }
+ 
+ premiumVehicle{
+ unitName:t="ussr_t_55_am"
+ weapon:t="ussr_t_55_am_default"
+ type:t="tank"
+ skin:t=""
+ country:t="country_ussr"
+ rank:ip2=4, 7
+ }
+ 
+ premiumVehicle{
+ unitName:t="ussr_object_140"
+ weapon:t="ussr_object_140_default"
+ type:t="tank"
+ skin:t=""
+ country:t="country_ussr"
+ rank:ip2=4, 7
+ }
+ 
+ premiumVehicle{
+ unitName:t="ussr_t_72av_turms"
+ weapon:t="ussr_t_72av_turms_default"
+ type:t="tank"
+ skin:t=""
+ country:t="country_ussr"
+ rank:ip2=4, 8
+ force:b=yes
+ }
+ 
+ premiumVehicle{
+ unitName:t="ussr_2s38"
+ weapon:t="ussr_2s38_default"
+ type:t="tank"
+ skin:t=""
+ country:t="country_ussr"
+ rank:ip2=4, 8
+ force:b=yes
+ }
+ 
+ premiumVehicle{
+ unitName:t="ussr_t_80ud"
+ weapon:t="ussr_t_80ud_default"
+ type:t="tank"
+ skin:t=""
+ country:t="country_ussr"
+ rank:ip2=4, 8
+ force:b=yes
+ }
+ 
+ premiumVehicle{
+ unitName:t="ussr_t_80ue1"
+ weapon:t="ussr_t_80ue1_default"
+ type:t="tank"
+ skin:t=""
+ country:t="country_ussr"
+ rank:ip2=4, 8
+ force:b=yes
+ }
+ 
+ premiumVehicle{
+ unitName:t="germ_t_34_747"
+ weapon:t="germ_t_34_747_default"
+ type:t="tank"
+ skin:t=""
+ country:t="country_germany"
+ rank:ip2=1, 2
+ }
+ 
+ premiumVehicle{
+ unitName:t="germ_panzerbefelhswagen_IV_ausf_J"
+ weapon:t="germ_pzkpfw_IV_ausf_J_default"
+ type:t="tank"
+ skin:t=""
+ country:t="country_germany"
+ rank:ip2=1, 3
+ }
+ 
+ premiumVehicle{
+ unitName:t="germ_kv_1_kwk_40"
+ weapon:t="germ_kv_1_kwk_40_default"
+ type:t="tank"
+ skin:t=""
+ country:t="country_germany"
+ rank:ip2=1, 3
+ }
+ 
+ premiumVehicle{
+ unitName:t="germ_pzkpfw_VI_ausf_b_tiger_IIh_sla"
+ weapon:t=""
+ type:t="tank"
+ skin:t=""
+ country:t="country_germany"
+ rank:ip2=2, 4
+ }
+ 
+ premiumVehicle{
+ unitName:t="germ_mkpz_m47"
+ weapon:t=""
+ type:t="tank"
+ skin:t=""
+ country:t="country_germany"
+ rank:ip2=3, 5
+ }
+ 
+ premiumVehicle{
+ unitName:t="germ_erprobungstrager_3_achs_turm"
+ weapon:t=""
+ type:t="tank"
+ skin:t=""
+ country:t="country_germany"
+ rank:ip2=3, 5
+ }
+ 
+ premiumVehicle{
+ unitName:t="germ_thyssen_henschel_tam_2ip"
+ weapon:t=""
+ type:t="tank"
+ skin:t=""
+ country:t="country_germany"
+ rank:ip2=4, 6
+ }
+ 
+ premiumVehicle{
+ unitName:t="germ_leopard_a1a1_120"
+ weapon:t=""
+ type:t="tank"
+ skin:t=""
+ country:t="country_germany"
+ rank:ip2=4, 6
+ }
+ 
+ premiumVehicle{
+ unitName:t="germ_leopard_2a4_pzbtl_123"
+ weapon:t=""
+ type:t="tank"
+ skin:t=""
+ country:t="country_germany"
+ rank:ip2=5, 8
+ force:b=yes
+ }
+ 
+ premiumVehicle{
+ unitName:t="germ_leopard_2a4m_can"
+ weapon:t=""
+ type:t="tank"
+ skin:t=""
+ country:t="country_germany"
+ rank:ip2=5, 8
+ force:b=yes
+ }
+ 
+ premiumVehicle{
+ unitName:t="uk_crusader_mk_2_the_saint"
+ weapon:t="uk_crusader_mk_2_default"
+ type:t="tank"
+ skin:t=""
+ country:t="country_britain"
+ rank:ip2=1, 2
+ }
+ 
+ premiumVehicle{
+ unitName:t="uk_m4a5_ram_2"
+ weapon:t="us_m4a5_ram_2_default"
+ type:t="tank"
+ skin:t=""
+ country:t="country_britain"
+ rank:ip2=1, 2
+ }
+ 
+ premiumVehicle{
+ unitName:t="uk_ac4_thunderbolt"
+ weapon:t="uk_ac4_thunderbolt_default"
+ type:t="tank"
+ skin:t=""
+ country:t="country_britain"
+ rank:ip2=1, 3
+ }
+ 
+ premiumVehicle{
+ unitName:t="uk_sherman_ic_firefly"
+ weapon:t=""
+ type:t="tank"
+ skin:t=""
+ country:t="country_britain"
+ rank:ip2=1, 3
+ }
+ 
+ premiumVehicle{
+ unitName:t="uk_centurion_action_x"
+ weapon:t=""
+ type:t="tank"
+ skin:t=""
+ country:t="country_britain"
+ rank:ip2=2, 4
+ }
+ 
+ premiumVehicle{
+ unitName:t="uk_vijayanta"
+ weapon:t=""
+ type:t="tank"
+ skin:t=""
+ country:t="country_britain"
+ rank:ip2=3, 5
+ }
+ 
+ premiumVehicle{
+ unitName:t="uk_khalid"
+ weapon:t=""
+ type:t="tank"
+ skin:t=""
+ country:t="country_britain"
+ rank:ip2=4, 6
+ }
+ 
+ premiumVehicle{
+ unitName:t="uk_challenger_1_mk_3_gulf"
+ weapon:t=""
+ type:t="tank"
+ skin:t=""
+ country:t="country_britain"
+ rank:ip2=5, 8
+ }
+ 
+ premiumVehicle{
+ unitName:t="uk_challenger_2_megatron"
+ weapon:t=""
+ type:t="tank"
+ skin:t=""
+ country:t="country_britain"
+ rank:ip2=5, 8
+ }
+ 
+ premiumVehicle{
+ unitName:t="jp_type_1_chi_he_5th_regiment"
+ weapon:t=""
+ type:t="tank"
+ skin:t=""
+ country:t="country_japan"
+ rank:ip2=1, 2
+ }
+ 
+ premiumVehicle{
+ unitName:t="jp_type_3_chi_nu_75cm_type_5"
+ weapon:t=""
+ type:t="tank"
+ skin:t=""
+ country:t="country_japan"
+ rank:ip2=1, 3
+ }
+ 
+ premiumVehicle{
+ unitName:t="jp_type_5_ho_ri_prototype"
+ weapon:t=""
+ type:t="tank"
+ skin:t=""
+ country:t="country_japan"
+ rank:ip2=2, 4
+ }
+ 
+ premiumVehicle{
+ unitName:t="jp_type_75_mlrs"
+ weapon:t=""
+ type:t="tank"
+ skin:t=""
+ country:t="country_japan"
+ rank:ip2=3, 5
+ }
+ 
+ premiumVehicle{
+ unitName:t="jp_type_74_mod_g_kai"
+ weapon:t=""
+ type:t="tank"
+ skin:t=""
+ country:t="country_japan"
+ rank:ip2=4, 6
+ }
+ 
+ premiumVehicle{
+ unitName:t="jp_type_16_mod"
+ weapon:t=""
+ type:t="tank"
+ skin:t=""
+ country:t="country_japan"
+ rank:ip2=4, 6
+ }
+ 
+ premiumVehicle{
+ unitName:t="jp_type_90b_camo"
+ weapon:t=""
+ type:t="tank"
+ skin:t=""
+ country:t="country_japan"
+ rank:ip2=5, 8
+ }
+ 
+ premiumVehicle{
+ unitName:t="cn_m4a4_sherman_1st_ptg"
+ weapon:t=""
+ type:t="tank"
+ skin:t=""
+ country:t="country_china"
+ rank:ip2=1, 2
+ }
+ 
+ premiumVehicle{
+ unitName:t="cn_m41_a3_walker_bulldog"
+ weapon:t=""
+ type:t="tank"
+ skin:t=""
+ country:t="country_china"
+ rank:ip2=2, 3
+ }
+ 
+ premiumVehicle{
+ unitName:t="cn_t_34_85_zis_53_no215"
+ weapon:t=""
+ type:t="tank"
+ skin:t=""
+ country:t="country_china"
+ rank:ip2=2, 4
+ }
+ 
+ premiumVehicle{
+ unitName:t="cn_is_2_1943_no402"
+ weapon:t=""
+ type:t="tank"
+ skin:t=""
+ country:t="country_china"
+ rank:ip2=2, 4
+ }
+ 
+ premiumVehicle{
+ unitName:t="cn_ztz_59a"
+ weapon:t=""
+ type:t="tank"
+ skin:t=""
+ country:t="country_china"
+ rank:ip2=3, 5
+ }
+ 
+ premiumVehicle{
+ unitName:t="cn_wma_301"
+ weapon:t=""
+ type:t="tank"
+ skin:t=""
+ country:t="country_china"
+ rank:ip2=4, 6
+ }
+ 
+ premiumVehicle{
+ unitName:t="cn_ztz_96a_prot"
+ weapon:t=""
+ type:t="tank"
+ skin:t=""
+ country:t="country_china"
+ rank:ip2=5, 8
+ }
+ 
+ premiumVehicle{
+ unitName:t="cn_al_khalid_1"
+ weapon:t=""
+ type:t="tank"
+ skin:t=""
+ country:t="country_china"
+ rank:ip2=4, 8
+ }
+ 
+ premiumVehicle{
+ unitName:t="it_m14_41_47_40"
+ weapon:t=""
+ type:t="tank"
+ skin:t=""
+ country:t="country_italy"
+ rank:ip2=1, 2
+ }
+ 
+ premiumVehicle{
+ unitName:t="it_sahariano"
+ weapon:t="it_sahariano_default"
+ type:t="tank"
+ skin:t=""
+ country:t="country_italy"
+ rank:ip2=1, 2
+ }
+ 
+ premiumVehicle{
+ unitName:t="it_sherman_75_37"
+ weapon:t=""
+ type:t="tank"
+ skin:t=""
+ country:t="country_italy"
+ rank:ip2=1, 2
+ }
+ 
+ premiumVehicle{
+ unitName:t="it_m26_ariete"
+ weapon:t=""
+ type:t="tank"
+ skin:t=""
+ country:t="country_italy"
+ rank:ip2=2, 4
+ }
+ 
+ premiumVehicle{
+ unitName:t="it_of_40_mtca"
+ weapon:t=""
+ type:t="tank"
+ skin:t=""
+ country:t="country_italy"
+ rank:ip2=4, 6
+ }
+ 
+ premiumVehicle{
+ unitName:t="it_centauro_rgo_120"
+ weapon:t=""
+ type:t="tank"
+ skin:t=""
+ country:t="country_italy"
+ rank:ip2=5, 8
+ }
+ 
+ premiumVehicle{
+ unitName:t="fr_b1_ter"
+ weapon:t=""
+ type:t="tank"
+ skin:t=""
+ country:t="country_france"
+ rank:ip2=1, 2
+ }
+ 
+ premiumVehicle{
+ unitName:t="fr_amx_13_chaffee"
+ weapon:t=""
+ type:t="tank"
+ skin:t=""
+ country:t="country_france"
+ rank:ip2=1, 2
+ }
+ 
+ premiumVehicle{
+ unitName:t="fr_m4a1_sherman_fl_10"
+ weapon:t=""
+ type:t="tank"
+ skin:t=""
+ country:t="country_france"
+ rank:ip2=1, 3
+ }
+ 
+ premiumVehicle{
+ unitName:t="fr_somua_sm"
+ weapon:t=""
+ type:t="tank"
+ skin:t=""
+ country:t="country_france"
+ rank:ip2=2, 4
+ }
+ 
+ premiumVehicle{
+ unitName:t="fr_pzkpfw_V_panther_dauphine"
+ weapon:t=""
+ type:t="tank"
+ skin:t=""
+ country:t="country_france"
+ rank:ip2=2, 4
+ }
+ 
+ premiumVehicle{
+ unitName:t="fr_amx_30_super"
+ weapon:t=""
+ type:t="tank"
+ skin:t=""
+ country:t="country_france"
+ rank:ip2=4, 6
+ }
+ 
+ premiumVehicle{
+ unitName:t="fr_vbci2_mct30"
+ weapon:t=""
+ type:t="tank"
+ skin:t=""
+ country:t="country_france"
+ rank:ip2=4, 8
+ }
+ 
+ premiumVehicle{
+ unitName:t="sw_sav_fm48"
+ weapon:t=""
+ type:t="tank"
+ skin:t=""
+ country:t="country_sweden"
+ rank:ip2=1, 2
+ }
+ 
+ premiumVehicle{
+ unitName:t="sw_sherman_3_4"
+ weapon:t=""
+ type:t="tank"
+ skin:t=""
+ country:t="country_sweden"
+ rank:ip2=1, 3
+ }
+ 
+ premiumVehicle{
+ unitName:t="sw_kv_1_1942_fin"
+ weapon:t=""
+ type:t="tank"
+ skin:t=""
+ country:t="country_sweden"
+ rank:ip2=1, 3
+ }
+ 
+ premiumVehicle{
+ unitName:t="sw_strv_103_0"
+ weapon:t=""
+ type:t="tank"
+ skin:t=""
+ country:t="country_sweden"
+ rank:ip2=3, 5
+ }
+ 
+ premiumVehicle{
+ unitName:t="sw_k9_vidar"
+ weapon:t=""
+ type:t="tank"
+ skin:t=""
+ country:t="country_sweden"
+ rank:ip2=3, 5
+ }
+ 
+ premiumVehicle{
+ unitName:t="sw_leopard_1a5no"
+ weapon:t=""
+ type:t="tank"
+ skin:t=""
+ country:t="country_sweden"
+ rank:ip2=4, 6
+ }
+ 
+ premiumVehicle{
+ unitName:t="sw_cv_9035_dk"
+ weapon:t=""
+ type:t="tank"
+ skin:t=""
+ country:t="country_sweden"
+ rank:ip2=4, 6
+ }
+ 
+ premiumVehicle{
+ unitName:t="sw_cv_90105_tml"
+ weapon:t=""
+ type:t="tank"
+ skin:t=""
+ country:t="country_sweden"
+ rank:ip2=4, 8
+ }
+ 
+ premiumVehicle{
+ unitName:t="sw_strv121b_christian2"
+ weapon:t=""
+ type:t="tank"
+ skin:t=""
+ country:t="country_sweden"
+ rank:ip2=4, 8
+ }
+ 
+ premiumVehicle{
+ unitName:t="il_m_51_w"
+ weapon:t=""
+ type:t="tank"
+ skin:t=""
+ country:t="country_israel"
+ rank:ip2=4, 5
+ }
+ 
+ premiumVehicle{
+ unitName:t="il_magach_3"
+ weapon:t=""
+ type:t="tank"
+ skin:t=""
+ country:t="country_israel"
+ rank:ip2=4, 5
+ }
+ 
+ premiumVehicle{
+ unitName:t="il_centurion_shot_kal_d"
+ weapon:t=""
+ type:t="tank"
+ skin:t=""
+ country:t="country_israel"
+ rank:ip2=5, 6
+ }
+ 
+ premiumVehicle{
+ unitName:t="il_merkava_mk_3_raam_segol"
+ weapon:t=""
+ type:t="tank"
+ skin:t=""
+ country:t="country_israel"
+ rank:ip2=6, 8
+ }
+ 
+ premiumVehicle{
+ unitName:t="us_pc_466_carmi"
+ weapon:t="us_pc_466_carmi_default"
+ type:t="ship"
+ skin:t=""
+ country:t="country_usa"
+ rank:ip2=1, 3
+ }
+ 
+ premiumVehicle{
+ unitName:t="us_elco_80ft_pt174"
+ weapon:t="torpedoes"
+ type:t="ship"
+ skin:t=""
+ country:t="country_usa"
+ rank:ip2=1, 3
+ }
+ 
+ premiumVehicle{
+ unitName:t="us_destroyer_porter_1942"
+ weapon:t="us_destroyer_porter_1942_default"
+ type:t="ship"
+ skin:t=""
+ country:t="country_usa"
+ rank:ip2=1, 3
+ }
+ 
+ premiumVehicle{
+ unitName:t="us_destroyer_gearing_frank_knox"
+ weapon:t="us_destroyer_gearing_frank_knox_default"
+ type:t="ship"
+ skin:t=""
+ country:t="country_usa"
+ rank:ip2=1, 3
+ force:b=yes
+ }
+ 
+ premiumVehicle{
+ unitName:t="us_cruiser_brooklyn_class_helena"
+ weapon:t="us_cruiser_brooklyn_class_helena_default"
+ type:t="ship"
+ skin:t=""
+ country:t="country_usa"
+ rank:ip2=3, 5
+ }
+ 
+ premiumVehicle{
+ unitName:t="us_ashville_class_douglas"
+ weapon:t="us_ashville_class_douglas_default"
+ type:t="ship"
+ skin:t=""
+ country:t="country_usa"
+ rank:ip2=3, 5
+ }
+ 
+ premiumVehicle{
+ unitName:t="us_cruiser_des_moines_class"
+ weapon:t="us_cruiser_des_moines_class_default"
+ type:t="ship"
+ skin:t=""
+ country:t="country_usa"
+ rank:ip2=3, 5
+ }
+ 
+ premiumVehicle{
+ unitName:t="us_battleship_arkansas"
+ weapon:t="us_battleship_arkansas_default"
+ type:t="ship"
+ skin:t=""
+ country:t="country_usa"
+ rank:ip2=4, 6
+ }
+ 
+ premiumVehicle{
+ unitName:t="germ_escort_typem1943"
+ weapon:t="wbg_mortar"
+ type:t="ship"
+ skin:t=""
+ country:t="country_germany"
+ rank:ip2=1, 5
+ }
+ 
+ premiumVehicle{
+ unitName:t="germ_destroyer_fletcher_zerstorer4"
+ weapon:t="torpedoes"
+ type:t="ship"
+ skin:t=""
+ country:t="country_germany"
+ rank:ip2=1, 3
+ }
+ 
+ premiumVehicle{
+ unitName:t="germ_destroyer_class1936c_z47"
+ weapon:t="germ_destroyer_class1936c_z47_default"
+ type:t="ship"
+ skin:t=""
+ country:t="country_germany"
+ rank:ip2=1, 3
+ }
+ 
+ premiumVehicle{
+ unitName:t="germ_cruiser_karlsruhe"
+ weapon:t="germ_cruiser_karlsruhe_default"
+ type:t="ship"
+ skin:t=""
+ country:t="country_germany"
+ rank:ip2=3, 4
+ }
+ 
+ premiumVehicle{
+ unitName:t="germ_battleship_nassau"
+ weapon:t="germ_battleship_nassau_default"
+ type:t="ship"
+ skin:t=""
+ country:t="country_germany"
+ rank:ip2=4, 6
+ }
+ 
+ premiumVehicle{
+ unitName:t="ussr_pr_1204"
+ weapon:t="ussr_pr_1204_default"
+ type:t="ship"
+ skin:t=""
+ country:t="country_ussr"
+ rank:ip2=1, 2
+ }
+ 
+ premiumVehicle{
+ unitName:t="ussr_mkl_186_mk85"
+ weapon:t="ussr_mkl_186_mk85_default"
+ type:t="ship"
+ skin:t=""
+ country:t="country_ussr"
+ rank:ip2=2, 5
+ }
+ 
+ premiumVehicle{
+ unitName:t="ussr_mpk_pr12412p"
+ weapon:t="ussr_mpk_pr12412p_default"
+ type:t="ship"
+ skin:t=""
+ country:t="country_ussr"
+ rank:ip2=3, 5
+ }
+ 
+ premiumVehicle{
+ unitName:t="ussr_skr_pr50plo_rosomacha"
+ weapon:t="ussr_skr_pr50plo_rosomacha_default"
+ type:t="ship"
+ skin:t=""
+ country:t="country_ussr"
+ rank:ip2=3, 5
+ }
+ 
+ premiumVehicle{
+ unitName:t="ussr_destroyer_pr30bis_smelyi"
+ weapon:t="ussr_destroyer_pr30bis_smelyi_default"
+ type:t="ship"
+ skin:t=""
+ country:t="country_ussr"
+ rank:ip2=1, 2
+ }
+ 
+ premiumVehicle{
+ unitName:t="ussr_destroyer_pr56_blagorodny"
+ weapon:t="ussr_destroyer_pr56_blagorodny_default"
+ type:t="ship"
+ skin:t=""
+ country:t="country_ussr"
+ rank:ip2=1, 3
+ }
+ 
+ premiumVehicle{
+ unitName:t="ussr_cruiser_kerch"
+ weapon:t="ussr_cruiser_kerch_default"
+ type:t="ship"
+ skin:t=""
+ country:t="country_ussr"
+ rank:ip2=2, 4
+ }
+ 
+ premiumVehicle{
+ unitName:t="ussr_cruiser_zheleznyakov"
+ weapon:t="ussr_cruiser_zheleznyakov_default"
+ type:t="ship"
+ skin:t=""
+ country:t="country_ussr"
+ rank:ip2=2, 4
+ }
+ 
+ premiumVehicle{
+ unitName:t="ussr_battleship_marat"
+ weapon:t="ussr_battleship_marat_default"
+ type:t="ship"
+ skin:t=""
+ country:t="country_ussr"
+ rank:ip2=4, 6
+ }
+ 
+ premiumVehicle{
+ unitName:t="uk_71ft_mgb"
+ weapon:t="mk_vii_depth_charges"
+ type:t="ship"
+ skin:t=""
+ country:t="country_britain"
+ rank:ip2=1, 2
+ }
+ 
+ premiumVehicle{
+ unitName:t="uk_corvette_orla"
+ weapon:t="uk_corvette_orla_default"
+ type:t="ship"
+ skin:t=""
+ country:t="country_britain"
+ rank:ip2=3, 4
+ }
+ 
+ premiumVehicle{
+ unitName:t="uk_frigate_whitby"
+ weapon:t="uk_frigate_whitby_default"
+ type:t="ship"
+ skin:t=""
+ country:t="country_britain"
+ rank:ip2=2, 4
+ }
+ 
+ premiumVehicle{
+ unitName:t="uk_destroyer_j_class"
+ weapon:t="uk_destroyer_j_class_default"
+ type:t="ship"
+ skin:t=""
+ country:t="country_britain"
+ rank:ip2=1, 2
+ }
+ 
+ premiumVehicle{
+ unitName:t="uk_destroyer_daring_class_diamond"
+ weapon:t="uk_destroyer_daring_class_diamond_default"
+ type:t="ship"
+ skin:t=""
+ country:t="country_britain"
+ rank:ip2=2, 3
+ }
+ 
+ premiumVehicle{
+ unitName:t="uk_cruiser_belfast"
+ weapon:t="uk_cruiser_belfast_default"
+ type:t="ship"
+ skin:t=""
+ country:t="country_britain"
+ rank:ip2=2, 5
+ }
+ 
+ premiumVehicle{
+ unitName:t="jp_pg02"
+ weapon:t="srboc_smoke_grenades_launcher"
+ type:t="ship"
+ skin:t=""
+ country:t="country_japan"
+ rank:ip2=1, 4
+ }
+ 
+ premiumVehicle{
+ unitName:t="jp_escort_akebono_class"
+ weapon:t="bomb_mortar_depth_charges"
+ type:t="ship"
+ skin:t=""
+ country:t="country_japan"
+ rank:ip2=1, 4
+ }
+ 
+ premiumVehicle{
+ unitName:t="jp_destroyer_harukaze"
+ weapon:t="jp_destroyer_harukaze_default"
+ type:t="ship"
+ skin:t=""
+ country:t="country_japan"
+ rank:ip2=1, 2
+ }
+ 
+ premiumVehicle{
+ unitName:t="jp_destroyer_nenohi"
+ weapon:t="jp_destroyer_nenohi_default"
+ type:t="ship"
+ skin:t=""
+ country:t="country_japan"
+ rank:ip2=1, 2
+ }
+ 
+ premiumVehicle{
+ unitName:t="jp_cruiser_yubari"
+ weapon:t="jp_cruiser_yubari_default"
+ type:t="ship"
+ skin:t=""
+ country:t="country_japan"
+ rank:ip2=1, 3
+ }
+ 
+ premiumVehicle{
+ unitName:t="jp_cruiser_mogami_mikuma"
+ weapon:t="jp_cruiser_mogami_mikuma_default"
+ type:t="ship"
+ skin:t=""
+ country:t="country_japan"
+ rank:ip2=2, 4
+ }
+ 
+ premiumVehicle{
+ unitName:t="jp_battleship_yamashiro"
+ weapon:t="jp_battleship_yamashiro_default"
+ type:t="ship"
+ skin:t=""
+ country:t="country_japan"
+ rank:ip2=4, 6
+ }
+ 
+ premiumVehicle{
+ unitName:t="it_p420_sparviero"
+ weapon:t="it_p420_sparviero_default"
+ type:t="ship"
+ skin:t=""
+ country:t="country_italy"
+ rank:ip2=1, 5
+ }
+ 
+ premiumVehicle{
+ unitName:t="it_ms444"
+ weapon:t="it_ms444_default"
+ type:t="ship"
+ skin:t=""
+ country:t="country_italy"
+ rank:ip2=1, 3
+ }
+ 
+ premiumVehicle{
+ unitName:t="it_destroyer_leone_class_tigre"
+ weapon:t="it_destroyer_leone_class_tigre_default"
+ type:t="ship"
+ skin:t=""
+ country:t="country_italy"
+ rank:ip2=1, 3
+ }
+ 
+ premiumVehicle{
+ unitName:t="it_destroyer_fletcher_geniere"
+ weapon:t="it_destroyer_fletcher_geniere_default"
+ type:t="ship"
+ skin:t=""
+ country:t="country_italy"
+ rank:ip2=1, 3
+ }
+ 
+ premiumVehicle{
+ unitName:t="it_gabbiano_class_c16"
+ weapon:t="it_gabbiano_class_c16_default"
+ type:t="ship"
+ skin:t=""
+ country:t="country_italy"
+ rank:ip2=2, 4
+ force:b=yes
+ }
+ 
+ premiumVehicle{
+ unitName:t="it_cruiser_zara_class_pola"
+ weapon:t="it_cruiser_zara_class_default"
+ type:t="ship"
+ skin:t=""
+ country:t="country_italy"
+ rank:ip2=2, 4
+ }
+ 
+ premiumVehicle{
+ unitName:t="it_battleship_leonardo_da_vinci"
+ weapon:t="it_battleship_leonardo_da_vinci_default"
+ type:t="ship"
+ skin:t=""
+ country:t="country_italy"
+ rank:ip2=4, 6
+ }
+ 
+ premiumVehicle{
+ unitName:t="fr_destroyer_aigle_class_aigle"
+ weapon:t="fr_destroyer_aigle_class_aigle_default"
+ type:t="ship"
+ skin:t=""
+ country:t="country_france"
+ rank:ip2=1, 2
+ }
+ 
+ premiumVehicle{
+ unitName:t="fr_cruiser_dugauy_class_dugauy_trouin"
+ weapon:t="it_cruiser_zara_class_default"
+ type:t="ship"
+ skin:t=""
+ country:t="country_france"
+ rank:ip2=2, 3
+ }
+ 
+ premiumVehicle{
+ unitName:t="fr_cruiser_suffren_class_dupleix"
+ weapon:t="fr_cruiser_suffren_class_dupleix_default"
+ type:t="ship"
+ skin:t=""
+ country:t="country_france"
+ rank:ip2=2, 4
+ }
+ 
+ premiumVehicle{
+ unitName:t="fr_battleship_courbet_class_courbet"
+ weapon:t="fr_battleship_courbet_class_courbet_default"
+ type:t="ship"
+ skin:t=""
+ country:t="country_france"
+ rank:ip2=4, 6
+ }
+ 
+ premiumVehicle{
+ unitName:t="fr_vlt2"
+ weapon:t="fr_vlt2_default"
+ type:t="ship"
+ skin:t=""
+ country:t="country_france"
+ rank:ip2=2, 4
```

  **Removed**:
```diff
- newYearHangar:b=yes
- level:t="levels/hangar_field_winter.bin"
- hangarMission:t="gameData/scenes/hangar_field_mission_winter.blk"
- aurora_borealis{
- enabled:b=yes
- top_height:r=10.0
- top_color:p3=0.1, 0.1, 1.4
- bottom_height:r=7.0
- bottom_color:p3=0.1, 1.3, 0.1
- brightness:r=2.15
- speed:r=0.018
- luminance:r=22.0
- ripples_scale:r=8.6
- ripples_speed:r=0.04
- ripples_strength:r=0.83
- }
- 
- country_usa:t="us_m1a2_sep2_abrams"
- country_germany:t="germ_leopard_2a7v"
- country_ussr:t="ussr_t_90m_2020"
- country_britain:t="uk_challenger_2_lep"
- country_japan:t="jp_type_99"
- country_china:t="cn_vt_4b"
- country_italy:t="it_m109g"
- country_france:t="fr_leclerc_azur"
- country_sweden:t="sw_strv_122b_plus"
- country_israel:t="il_m109a1"
- country_usa:t="us_hstv_l"
- country_germany:t="germ_schutzenpanzer_puma"
- country_ussr:t="ussr_2s25m"
- country_britain:t="uk_vickers_mk_11"
- country_japan:t="jp_type_81_tansam"
- country_china:t="cn_ztl_11"
- country_italy:t="it_centauro_mgs_120"
- country_france:t="fr_tpk_641_vpc"
- country_sweden:t="sw_strf_90c"
- country_israel:t="il_m113a1_tow"
- country_usa:t="f_15a"
- country_germany:t="tornado_ids_de_assta1"
- country_ussr:t="su_27"
- country_britain:t="tornado_f3"
- country_japan:t="f_15j"
- country_italy:t="tornado_adv"
- country_france:t="mirage_4000"
- country_china:t="j_11"
- country_sweden:t="saab_jas39a"
- country_israel:t="f_15a_iaf"
- env{
- env:t="9.024"
- weight:r=1.0
- compatibilityWeight:r=1.0
```


- **aces.vromfs.bin_u/config/rendinst_dmg.blkx**:

  **Added**:
```diff
+ dmg{
+ name:t="avg_poland_iced_lake"
+ immortal:b=yes
+ }
+ 
```

  **Removed**:
```diff
```


- **aces.vromfs.bin_u/config/skins_market.blkx**:

  **Added**:
```diff
+ ka_50{
+ marketplaceItemdefId:i=1001946
+ hideFeature:t="!Marketplace"
+ needShowPreviewSuggestion:b=yes
+ }
+ 
+ wessex_mk5{
+ marketplaceItemdefId:i=1001971
+ hideFeature:t="!Marketplace"
+ needShowPreviewSuggestion:b=yes
+ }
+ 
+ av_8b_na{
+ marketplaceItemdefId:i=1001972
+ hideFeature:t="!Marketplace"
+ needShowPreviewSuggestion:b=yes
+ }
+ 
+ ef_2000_block_10{
+ marketplaceItemdefId:i=1001951
+ hideFeature:t="!Marketplace"
+ needShowPreviewSuggestion:b=yes
+ }
+ 
+ ef_2000_fgr4{
+ marketplaceItemdefId:i=1001950
+ hideFeature:t="!Marketplace"
+ needShowPreviewSuggestion:b=yes
+ }
+ 
+ f_117{
+ marketplaceItemdefId:i=1001952
+ hideFeature:t="!Marketplace"
+ needShowPreviewSuggestion:b=yes
+ }
+ 
+ f_15e{
+ marketplaceItemdefId:i=1001949
+ hideFeature:t="!Marketplace"
+ needShowPreviewSuggestion:b=yes
+ }
+ 
+ f_16a_block_15_ocu_thailand{
+ marketplaceItemdefId:i=1001960
+ hideFeature:t="!Marketplace"
+ needShowPreviewSuggestion:b=yes
+ }
+ 
+ f7f3{
+ marketplaceItemdefId:i=1001968
+ hideFeature:t="!Marketplace"
+ needShowPreviewSuggestion:b=yes
+ }
+ 
+ mig-21_bison{
+ marketplaceItemdefId:i=1001964
+ hideFeature:t="!Marketplace"
+ needShowPreviewSuggestion:b=yes
+ }
+ 
+ mirage_2000_5ei{
+ marketplaceItemdefId:i=1001958
+ hideFeature:t="!Marketplace"
+ needShowPreviewSuggestion:b=yes
+ }
+ 
+ rafale_c_f3{
+ marketplaceItemdefId:i=1001976
+ hideFeature:t="!Marketplace"
+ needShowPreviewSuggestion:b=yes
+ }
+ 
+ saab_a21a_3{
+ marketplaceItemdefId:i=1001973
+ hideFeature:t="!Marketplace"
+ needShowPreviewSuggestion:b=yes
+ }
+ 
+ spitfire_fr_mk14e_belgium{
+ marketplaceItemdefId:i=1001953
+ hideFeature:t="!Marketplace"
+ needShowPreviewSuggestion:b=yes
+ }
+ 
+ su_27{
+ marketplaceItemdefId:i=1001959
+ hideFeature:t="!Marketplace"
+ needShowPreviewSuggestion:b=yes
+ }
+ 
+ su_33{
+ marketplaceItemdefId:i=1001974
+ hideFeature:t="!Marketplace"
+ needShowPreviewSuggestion:b=yes
+ }
+ 
+ su_34{
+ marketplaceItemdefId:i=1001963
+ hideFeature:t="!Marketplace"
+ needShowPreviewSuggestion:b=yes
+ }
+ 
+ tbd-1_1938{
+ marketplaceItemdefId:i=1001955
+ hideFeature:t="!Marketplace"
+ needShowPreviewSuggestion:b=yes
+ }
+ 
+ tornado_ids_it{
+ marketplaceItemdefId:i=1001975
+ hideFeature:t="!Marketplace"
+ needShowPreviewSuggestion:b=yes
+ }
+ 
+ yak-3_france{
+ marketplaceItemdefId:i=1001954
+ hideFeature:t="!Marketplace"
+ needShowPreviewSuggestion:b=yes
+ }
+ 
+ uk_battleship_rodney{
+ marketplaceItemdefId:i=1001947
+ hideFeature:t="!Marketplace"
+ needShowPreviewSuggestion:b=yes
+ }
+ 
+ cn_wz_305{
+ marketplaceItemdefId:i=1001751
+ hideFeature:t="!Marketplace"
+ needShowPreviewSuggestion:b=yes
+ }
+ 
+ fr_amx_10rc{
+ marketplaceItemdefId:i=1001970
+ hideFeature:t="!Marketplace"
+ needShowPreviewSuggestion:b=yes
+ }
+ 
+ fr_bat_chat_25t{
+ marketplaceItemdefId:i=1001965
+ hideFeature:t="!Marketplace"
+ needShowPreviewSuggestion:b=yes
+ }
+ 
+ fr_vbci{
+ marketplaceItemdefId:i=1001962
+ hideFeature:t="!Marketplace"
+ needShowPreviewSuggestion:b=yes
+ }
+ 
+ germ_boxer_3105{
+ marketplaceItemdefId:i=1001933
+ hideFeature:t="!Marketplace"
+ needShowPreviewSuggestion:b=yes
+ }
+ 
+ germ_leopard_2pl{
+ marketplaceItemdefId:i=1001939
+ hideFeature:t="!Marketplace"
+ needShowPreviewSuggestion:b=yes
+ }
+ 
+ germ_pzh_2000{
+ marketplaceItemdefId:i=1001943
+ hideFeature:t="!Marketplace"
+ needShowPreviewSuggestion:b=yes
+ }
+ 
+ germ_pzkpfw_VI_ausf_h1_tiger_east{
+ marketplaceItemdefId:i=1001961
+ hideFeature:t="!Marketplace"
+ needShowPreviewSuggestion:b=yes
+ }
+ 
+ germ_pzkpfw_VI_ausf_h1_tiger_west{
+ marketplaceItemdefId:i=1001936
+ hideFeature:t="!Marketplace"
+ needShowPreviewSuggestion:b=yes
+ }
+ 
+ germ_schutzenpanzer_puma_vjtf{
+ marketplaceItemdefId:i=1001941
+ hideFeature:t="!Marketplace"
+ needShowPreviewSuggestion:b=yes
+ }
+ 
+ il_namer_tsrikhon{
+ marketplaceItemdefId:i=1001932
+ hideFeature:t="!Marketplace"
+ needShowPreviewSuggestion:b=yes
+ }
+ 
+ jp_m44{
+ marketplaceItemdefId:i=1001945
+ hideFeature:t="!Marketplace"
+ needShowPreviewSuggestion:b=yes
+ }
+ 
+ sw_cv_90_mk4{
+ marketplaceItemdefId:i=1001938
+ hideFeature:t="!Marketplace"
+ needShowPreviewSuggestion:b=yes
+ }
+ 
+ sw_leopard_1a5no{
+ marketplaceItemdefId:i=1001977
+ hideFeature:t="!Marketplace"
+ needShowPreviewSuggestion:b=yes
+ }
+ 
+ us_m551{
+ marketplaceItemdefId:i=1001934
+ hideFeature:t="!Marketplace"
+ needShowPreviewSuggestion:b=yes
+ }
+ 
+ us_rdf_lt{
+ marketplaceItemdefId:i=1001935
+ hideFeature:t="!Marketplace"
+ needShowPreviewSuggestion:b=yes
+ }
+ 
+ ussr_bmd_4m{
+ marketplaceItemdefId:i=1001944
+ hideFeature:t="!Marketplace"
+ needShowPreviewSuggestion:b=yes
+ }
+ 
+ ussr_is_2_1943{
+ marketplaceItemdefId:i=1001940
+ hideFeature:t="!Marketplace"
+ needShowPreviewSuggestion:b=yes
+ }
+ 
+ ussr_t_72av_turms{
+ marketplaceItemdefId:i=1001969
+ hideFeature:t="!Marketplace"
+ needShowPreviewSuggestion:b=yes
+ }
+ 
```

  **Removed**:
```diff
```


- **aces.vromfs.bin_u/config/skinslocations.blkx**:

  **Added**:
```diff
+ pak_camo_earth_yellow{
+ camoType:t="desert"
+ }
+ 
```

  **Removed**:
```diff
```


- **aces.vromfs.bin_u/config/sound_studio.blkx**:

  **Added**:
```diff
+ optional:b=yes
+ optional:b=yes
+ optional:b=yes
+ optional:b=yes
+ optional:b=yes
+ optional:b=yes
+ optional:b=yes
+ optional:b=yes
+ optional:b=yes
+ optional:b=yes
```

  **Removed**:
```diff
```


- **aces.vromfs.bin_u/gamedata/attachables/decor_uroboros.blkx**:

  **Added**:
```diff
+ model:t="decor_uroboros"
+ collision:t="decor_uroboros_collision"
+ bboxMult:r=0.1
+ breakFx:t="destruction_decorators_model_small"
+ mass:r=15.0
+ 
+ DamageParts{
+ 
+ body{
+ hp:r=50.0
+ armorClass:t="tank_structural_steel"
+ armorThickness:r=0.01
+ }
+ }
+ 
+ DamageEffects{
+ 
+ part{
+ name:t="body"
+ 
+ onKill{
+ cut:r=1.0
+ }
+ }
+ }
```

  **Removed**:
```diff
```


- **aces.vromfs.bin_u/gamedata/flightmodels/ef_2000_block_10.blkx**:

  **Added**:
```diff
+ node:t="radar1_dm"
```

  **Removed**:
```diff
```


- **aces.vromfs.bin_u/gamedata/flightmodels/ef_2000_fgr4.blkx**:

  **Added**:
```diff
+ node:t="radar1_dm"
+ ShowNodes{
+ node:t="pylon_2"
+ node:t="pylon_1"
+ }
+ 
```

  **Removed**:
```diff
```


- **aces.vromfs.bin_u/gamedata/flightmodels/ef_2000a.blkx**:

  **Added**:
```diff
+ node:t="radar1_dm"
+ ShowNodes{
+ node:t="pylon_2"
+ node:t="pylon_1"
+ }
+ 
```

  **Removed**:
```diff
```


- **aces.vromfs.bin_u/gamedata/flightmodels/f_15i_raam.blkx**:

  **Added**:
```diff
+ nvIndex:i=1
```

  **Removed**:
```diff
- nvIndex:i=0
```


- **aces.vromfs.bin_u/gamedata/flightmodels/fm/mb_151c1.blkx**:

  **Added**:
```diff
+ UseTime:r=5.0
+ Power:r=2500.0
+ Automatic:b=yes
+ EmptyMass:r=2097.0
+ MaxFuelMass0:r=306.0
+ OilMass:r=18.0
```

  **Removed**:
```diff
- UseTime:r=0.0
- Power:r=0.0
- Automatic:b=no
- EmptyMass:r=2365.0
- MaxFuelMass0:r=305.0
- OilMass:r=29.0
```


- **aces.vromfs.bin_u/gamedata/flightmodels/kfir_c10_colombia.blkx**:

  **Added**:
```diff
+ position:p2=250.0, 256.0
+ size:p2=490.0, 490.0
+ position:p2=250.0, 256.0
+ size:p2=490.0, 490.0
+ maxloadMass:r=5500.0
```

  **Removed**:
```diff
- position:p2=350.0, 256.0
- size:p2=390.0, 300.0
- position:p2=350.0, 256.0
- size:p2=390.0, 300.0
- maxloadMass:r=4295.0
```


- **aces.vromfs.bin_u/gamedata/sensors/il_el_m_2032.blkx**:

  **Added**:
```diff
+ hprf{
+ sideLobesAttenuation:r=-20.0
+ power:r=1200.0
+ band:i=8
+ rcs:r=5.0
+ range:r=150000.0
+ rangeMax:r=200000.0
+ multipathEffect:p4=0.0, 1.0, 60.0, 0.0
+ 
+ antenna{
+ angleHalfSens:r=3.0
+ sideLobesSensitivity:r=-32.0
+ }
+ }
+ 
+ angleHalfSens:r=3.0
+ angleHalfSens:r=3.0
+ barHeight:r=2.1
+ barHeight:r=2.1
+ barHeight:r=2.1
+ barHeight:r=2.1
+ barHeight:r=2.1
+ barHeight:r=2.1
+ barHeight:r=2.5
+ barHeight:r=1.85
+ barHeight:r=2.25
+ barHeight:r=2.25
+ maxValue:r=180000.0
+ maxValue:r=180000.0
+ maxValue:r=200000.0
+ hprfSearch{
+ groundClutter:b=no
+ aircraftAsTarget:b=yes
+ friendFoeId:b=yes
+ mainBeamDopplerSpeed:b=yes
+ 
+ distance{
+ presents:b=yes
+ minValue:r=5000.0
+ maxValue:r=200000.0
+ width:r=2000.0
+ }
+ 
+ dopplerSpeed{
+ presents:b=yes
+ minValue:r=40.0
+ maxValue:r=1500.0
+ signalWidthMin:r=5.0
+ width:r=120.0
+ }
+ }
+ 
+ hprfTrack{
+ rangeFinder:b=yes
+ dopplerSpeedFinder:b=yes
+ dynamicRange:p2=40.0, 15.0
+ groundClutter:b=yes
+ aircraftAsTarget:b=yes
+ angularAccuracy:r=0.05
+ distanceAccuracy:r=15.0
+ absDopplerSpeed:b=no
+ mainBeamDopplerSpeed:b=no
+ track:b=yes
+ 
+ distance{
+ presents:b=yes
+ minValue:r=200.0
+ maxValue:r=200000.0
+ width:r=500.0
+ }
+ 
+ dopplerSpeed{
+ presents:b=yes
+ minValue:r=-1500.0
+ maxValue:r=1500.0
+ signalWidthMin:r=2.0
+ width:r=20.0
+ }
+ }
+ 
+ distanceRange:p2=0.0, 138750.0
+ setHprfStandbyMode{
+ 
+ setStandbyModeCommon{
+ }
+ 
+ setScanPatternSet{
+ scanPatternSet:t="search"
+ }
+ 
+ setTransiver{
+ transiver:t="hprf"
+ }
+ 
+ setSignal{
+ signal:t="hprfSearch"
+ }
+ 
+ setModeName{
+ name:t="PD HDN standby"
+ }
+ }
+ 
+ setHprfSearchMode{
+ 
+ setSearchModeCommon{
+ }
+ 
+ setTransiver{
+ transiver:t="hprf"
+ }
+ 
+ setSignal{
+ signal:t="hprfSearch"
+ }
+ 
+ setModeName{
+ name:t="PD HDN search"
+ }
+ }
+ 
+ setHprfBvrLockMode{
+ 
+ setBvrLockMode{
+ }
+ 
+ setModeName{
+ name:t="PD HDN acquisition"
+ }
+ }
+ 
+ twsToHprf{
+ stateTo:t="hprf"
+ 
+ actions{
+ 
+ setCustomActionTemplate{
+ fsm:t="main"
+ name:t="setStandbyMode"
+ actionTemplateName:t="setHprfStandbyMode"
+ }
+ 
+ setCustomActionTemplate{
+ fsm:t="main"
+ name:t="setSearchMode"
+ actionTemplateName:t="setHprfSearchMode"
+ }
+ 
+ setCustomActionTemplate{
+ fsm:t="main"
+ name:t="setBvrLockMode"
+ actionTemplateName:t="setHprfBvrLockMode"
+ }
+ 
+ setCustomActionTemplate{
+ fsm:t="main"
+ name:t="designateTarget"
+ actionTemplateName:t="designatedTargetSearch"
+ }
+ 
+ setCustomActionTemplate{
+ fsm:t="main"
+ name:t="resetSearchMode"
+ actionTemplateName:t="resetSearchMode"
+ }
+ 
+ doCustomActionTemplate{
+ fsm:t="main"
+ name:t="resetSearchMode"
+ }
+ 
+ setFsmActive{
+ fsm:t="main"
+ active:b=no
+ }
+ 
+ setFsmActive{
+ fsm:t="main"
+ active:b=yes
+ }
+ }
+ }
+ 
+ hprfToHprfVelocity{
+ stateFrom:t="hprf"
+ command:t="modeSwitch"
+ illumination{
+ stateInit:t="init"
+ 
+ transitions{
+ 
+ activate{
+ event:t="fsmActivate"
+ stateTo:t="active"
+ 
+ actions{
+ 
+ checkIlluminationTimeOut{
+ transiver:b=yes
+ pauseMax:r=20.0
+ }
+ }
+ }
+ 
+ deactivate{
+ event:t="fsmDeactivate"
+ stateTo:t="inactive"
+ 
+ actions{
+ 
+ setIllumination{
+ transiver:b=no
+ }
+ }
+ }
+ 
+ activateIllumination{
+ event:t="sarhMissileLaunch"
+ 
+ actions{
+ 
+ setIlluminationTimeOut{
+ timeOut:r=60.0
+ }
+ }
+ }
+ 
+ updateIllumination{
+ event:t="update"
+ 
+ actions{
+ 
+ checkIlluminationTimeOut{
+ transiver:b=yes
+ pauseMax:r=20.0
+ }
+ }
+ }
+ }
+ }
+ 
+ setHprfTrack{
+ 
+ setTransiver{
+ transiver:t="hprf"
+ }
+ 
+ setSignal{
+ signal:t="hprfTrack"
+ }
+ }
+ 
+ hprfOkTryDetectMprf{
+ stateFrom:t="hprfOkMprfTry"
+ event:t="update"
+ 
+ actions{
+ 
+ setMprfTrack{
+ }
+ 
+ detectTarget{
+ ignoreOwnWeapon:b=yes
+ rangeMult:r=1.0
+ }
+ 
+ setHprfTrack{
+ }
+ }
+ }
+ 
+ tryDetectHprf{
+ stateFrom:t="hprfTry"
+ event:t="update"
+ 
+ actions{
+ 
+ setHprfTrack{
+ }
+ 
+ detectTarget{
+ ignoreOwnWeapon:b=yes
+ rangeMult:r=1.0
+ }
+ 
+ setMprfTrack{
+ }
+ }
+ }
+ 
+ lprfOkTryDetectHprf{
+ stateFrom:t="lprfOkHprfTry"
+ event:t="update"
+ 
+ actions{
+ 
+ setHprfTrack{
+ }
+ 
+ detectTarget{
+ ignoreOwnWeapon:b=yes
+ rangeMult:r=1.0
+ }
+ 
+ setLprfTrack{
+ }
+ }
+ }
+ 
+ stateFrom:t="hprfOkMprfTry"
+ trackHprf{
+ stateFrom:t="hprf"
+ event:t="targetDetected"
+ stateTo:t="hprfOkMprfTry"
+ 
+ actions{
+ 
+ track{
+ }
+ }
+ }
+ 
+ startTrackHprf{
+ stateFrom:t="hprfTry"
+ stateFrom:t="lprfOkHprfTry"
+ event:t="targetDetected"
+ stateTo:t="hprf"
+ 
+ actions{
+ 
+ setHprfTrack{
+ }
+ 
+ track{
+ }
+ 
+ setModeName{
+ name:t="PD HDN track"
+ }
+ }
+ }
+ 
+ stateTo:t="lprfOkHprfTry"
+ mprfToHprf{
+ stateTo:t="hprfTry"
+ backToHprf{
+ stateFrom:t="hprfOkMprfTry"
+ stateTo:t="hprfTry"
+ hprfToLprfTry{
+ stateFrom:t="hprf"
+ stateFrom:t="hprfTry"
+ stateTo:t="lprfTry"
+ lprfToMprfTry{
+ stateFrom:t="lprfOkHprfTry"
+ stateTo:t="lprfOkMprfTry"
+ backToLprf{
+ stateFrom:t="lprfOkMprfTry"
+ event:t="targetNotDetected"
+ stateTo:t="lprfTry"
+ extrapolate{
+ lprfToMprf{
+ stateFrom:t="lprf"
+ event:t="targetNotDetected"
+ stateTo:t="mprfTry"
+ extrapolate{
+ lprfTryToMprf{
+ stateFrom:t="lprfTry"
+ event:t="targetNotDetected"
+ stateTo:t="mprfTry"
+ extrapolate{
+ setModeName{
+ name:t="track memory"
```

  **Removed**:
```diff
- angleHalfSens:r=4.0
- angleHalfSens:r=4.0
- barHeight:r=2.85
- barHeight:r=2.85
- barHeight:r=2.85
- barHeight:r=2.85
- barHeight:r=2.85
- barHeight:r=2.85
- barHeight:r=3.3
- barHeight:r=2.5
- barHeight:r=3.0
- barHeight:r=3.0
- maxValue:r=74000.0
- maxValue:r=74000.0
- maxValue:r=74000.0
- distanceRange:p2=0.0, 92500.0
- twsToHprfVelocity{
- stateFrom:t="mprf"
- stateFrom:t="lprf"
- stateTo:t="lprfOkMprfTry"
- mprfToLprf{
- stateTo:t="lprfTry"
- backToLprf{
- stateFrom:t="lprfOkMprfTry"
- stateTo:t="lprfTry"
- lprfToMprf{
- stateFrom:t="lprf"
- stateTo:t="mprfTry"
- lprfTryToMprf{
- stateFrom:t="lprfTry"
- stateTo:t="mprfTry"
- 
- setModeName{
- name:t="track memory"
- }
- }
- }
- 
- illumination{
- stateInit:t="init"
- 
- transitions{
- activate{
- event:t="fsmActivate"
- stateTo:t="active"
- checkIlluminationTimeOut{
- transiver:b=yes
- pauseMax:r=20.0
- deactivate{
- event:t="fsmDeactivate"
- stateTo:t="inactive"
- setIllumination{
- transiver:b=no
- activateIllumination{
- event:t="sarhMissileLaunch"
- setIlluminationTimeOut{
- timeOut:r=60.0
- }
- }
- updateIllumination{
- event:t="update"
- 
- actions{
- 
- checkIlluminationTimeOut{
- transiver:b=yes
- pauseMax:r=20.0
```


- **aces.vromfs.bin_u/gamedata/sensors/su_kopio.blkx**:

  **Added**:
```diff
+ fsm:t="bvrLock"
+ fsm:t="bvrLock"
```

  **Removed**:
```diff
- fsm:t="lock"
- fsm:t="lock"
- actionsTemplates{
- 
- setMprfLock{
- 
- setTransiver{
- transiver:t="mprf"
- }
- 
- setSignal{
- signal:t="mprfSearch"
- }
- }
- 
- setHprfLock{
- 
- setTransiver{
- transiver:t="hprf"
- }
- 
- setSignal{
- signal:t="hprfSearch"
- }
- }
- }
- 
- transitions{
- 
- init{
- event:t="fsmActivate"
- 
- actions{
- 
- setMprfLock{
- }
- }
- }
- 
- scan{
- event:t="update"
- 
- actions{
- 
- setMprfLock{
- }
- 
- scan{
- }
- 
- scan{
- }
- 
- setHprfLock{
- }
- }
- }
- 
- detect{
- event:t="targetInSight"
- 
- actions{
- 
- setMprfLock{
- }
- 
- detectTarget{
- ignoreOwnWeapon:b=yes
- rangeMult:r=1.0
- }
- 
- detectTarget{
- ignoreOwnWeapon:b=yes
- rangeMult:r=1.0
- }
- 
- setHprfLock{
- }
- }
- }
- }
- }
- 
- lock{
- stateInit:t="lock"
- 
```


- **aces.vromfs.bin_u/gamedata/sensors/su_kopio_25.blkx**:

  **Added**:
```diff
+ fsm:t="bvrLock"
+ fsm:t="bvrLock"
```

  **Removed**:
```diff
- fsm:t="lock"
- fsm:t="lock"
- actionsTemplates{
- 
- setMprfLock{
- 
- setTransiver{
- transiver:t="mprf"
- }
- 
- setSignal{
- signal:t="mprfSearch"
- }
- }
- 
- setHprfLock{
- 
- setTransiver{
- transiver:t="hprf"
- }
- 
- setSignal{
- signal:t="hprfSearch"
- }
- }
- }
- 
- transitions{
- 
- init{
- event:t="fsmActivate"
- 
- actions{
- 
- setMprfLock{
- }
- }
- }
- 
- scan{
- event:t="update"
- 
- actions{
- 
- setMprfLock{
- }
- 
- scan{
- }
- 
- scan{
- }
- 
- setHprfLock{
- }
- }
- }
- 
- detect{
- event:t="targetInSight"
- 
- actions{
- 
- setMprfLock{
- }
- 
- detectTarget{
- ignoreOwnWeapon:b=yes
- rangeMult:r=1.0
- }
- 
- detectTarget{
- ignoreOwnWeapon:b=yes
- rangeMult:r=1.0
- }
- 
- setHprfLock{
- }
- }
- }
- }
- }
- 
- lock{
- stateInit:t="lock"
- 
```


- **aces.vromfs.bin_u/gamedata/sensors/su_n_001k.blkx**:

  **Added**:
```diff
+ name:t="N001"
```

  **Removed**:
```diff
- name:t="N001K"
```


- **aces.vromfs.bin_u/gamedata/sensors/uk_captor_m.blkx**:

  **Added**:
```diff
+ power:r=800.0
+ band:i=8
+ rcs:r=5.0
+ range:r=80000.0
+ rangeMax:r=150000.0
+ multipathEffect:p4=0.0, 1.0, 60.0, 0.0
+ 
+ antenna{
+ angleHalfSens:r=3.0
+ sideLobesSensitivity:r=-32.0
+ }
+ }
+ 
+ hprf{
+ sideLobesAttenuation:r=-20.0
+ power:r=1200.0
+ range:r=150000.0
+ rangeMax:r=200000.0
+ angleHalfSens:r=3.0
+ power:r=1200.0
+ rangeMax:r=250000.0
+ angleHalfSens:r=3.0
+ power:r=800.0
+ rangeMax:r=200000.0
+ angleHalfSens:r=3.0
+ angleHalfSens:r=3.0
+ angleHalfSens:r=3.0
+ barHeight:r=2.1
+ barHeight:r=2.1
+ barHeight:r=2.1
+ barHeight:r=2.1
+ barHeight:r=2.1
+ barHeight:r=2.1
+ barHeight:r=2.5
+ barHeight:r=1.85
+ barHeight:r=2.25
+ barHeight:r=2.25
+ maxValue:r=180000.0
+ maxValue:r=180000.0
+ maxValue:r=200000.0
+ hprfSearch{
+ groundClutter:b=no
+ aircraftAsTarget:b=yes
+ friendFoeId:b=yes
+ mainBeamDopplerSpeed:b=yes
+ 
+ distance{
+ presents:b=yes
+ minValue:r=5000.0
+ maxValue:r=200000.0
+ width:r=2000.0
+ }
+ 
+ dopplerSpeed{
+ presents:b=yes
+ minValue:r=40.0
+ maxValue:r=1500.0
+ signalWidthMin:r=5.0
+ width:r=120.0
+ }
+ }
+ 
+ hprfTrack{
+ rangeFinder:b=yes
+ dopplerSpeedFinder:b=yes
+ dynamicRange:p2=40.0, 15.0
+ groundClutter:b=yes
+ aircraftAsTarget:b=yes
+ angularAccuracy:r=0.05
+ distanceAccuracy:r=15.0
+ absDopplerSpeed:b=no
+ mainBeamDopplerSpeed:b=no
+ track:b=yes
+ 
+ distance{
+ presents:b=yes
+ minValue:r=200.0
+ maxValue:r=200000.0
+ width:r=500.0
+ }
+ 
+ dopplerSpeed{
+ presents:b=yes
+ minValue:r=-1500.0
+ maxValue:r=1500.0
+ signalWidthMin:r=2.0
+ width:r=20.0
+ }
+ }
+ 
+ distanceRange:p2=0.0, 138750.0
+ setHprfStandbyMode{
+ 
+ setStandbyModeCommon{
+ }
+ 
+ setScanPatternSet{
+ scanPatternSet:t="search"
+ }
+ 
+ setTransiver{
+ transiver:t="hprf"
+ }
+ 
+ setSignal{
+ signal:t="hprfSearch"
+ }
+ 
+ setModeName{
+ name:t="PD HDN standby"
+ }
+ }
+ 
+ setHprfSearchMode{
+ 
+ setSearchModeCommon{
+ }
+ 
+ setTransiver{
+ transiver:t="hprf"
+ }
+ 
+ setSignal{
+ signal:t="hprfSearch"
+ }
+ 
+ setModeName{
+ name:t="PD HDN search"
+ }
+ }
+ 
+ setHprfBvrLockMode{
+ 
+ setBvrLockMode{
+ }
+ 
+ setModeName{
+ name:t="PD HDN acquisition"
+ }
+ }
+ 
+ twsToHprf{
+ stateTo:t="hprf"
+ 
+ actions{
+ 
+ setCustomActionTemplate{
+ fsm:t="main"
+ name:t="setStandbyMode"
+ actionTemplateName:t="setHprfStandbyMode"
+ }
+ 
+ setCustomActionTemplate{
+ fsm:t="main"
+ name:t="setSearchMode"
+ actionTemplateName:t="setHprfSearchMode"
+ }
+ 
+ setCustomActionTemplate{
+ fsm:t="main"
+ name:t="setBvrLockMode"
+ actionTemplateName:t="setHprfBvrLockMode"
+ }
+ 
+ setCustomActionTemplate{
+ fsm:t="main"
+ name:t="designateTarget"
+ actionTemplateName:t="designatedTargetSearch"
+ }
+ 
+ setCustomActionTemplate{
+ fsm:t="main"
+ name:t="resetSearchMode"
+ actionTemplateName:t="resetSearchMode"
+ }
+ 
+ doCustomActionTemplate{
+ fsm:t="main"
+ name:t="resetSearchMode"
+ }
+ 
+ setFsmActive{
+ fsm:t="main"
+ active:b=no
+ }
+ 
+ setFsmActive{
+ fsm:t="main"
+ active:b=yes
+ }
+ }
+ }
+ 
+ hprfToHprfVelocity{
+ stateFrom:t="hprf"
+ command:t="modeSwitch"
+ illumination{
+ stateInit:t="init"
+ 
+ transitions{
+ 
+ activate{
+ event:t="fsmActivate"
+ stateTo:t="active"
+ 
+ actions{
+ 
+ checkIlluminationTimeOut{
+ transiver:b=yes
+ pauseMax:r=20.0
+ }
+ }
+ }
+ 
+ deactivate{
+ event:t="fsmDeactivate"
+ stateTo:t="inactive"
+ 
+ actions{
+ 
+ setIllumination{
+ transiver:b=no
+ }
+ }
+ }
+ 
+ activateIllumination{
+ event:t="sarhMissileLaunch"
+ 
+ actions{
+ 
+ setIlluminationTimeOut{
+ timeOut:r=60.0
+ }
+ }
+ }
+ 
+ updateIllumination{
+ event:t="update"
+ 
+ actions{
+ 
+ checkIlluminationTimeOut{
+ transiver:b=yes
+ pauseMax:r=20.0
+ }
+ }
+ }
+ }
+ }
+ 
+ setHprfTrack{
+ 
+ setTransiver{
+ transiver:t="hprf"
+ }
+ 
+ setSignal{
+ signal:t="hprfTrack"
+ }
+ }
+ 
+ hprfOkTryDetectMprf{
+ stateFrom:t="hprfOkMprfTry"
+ event:t="update"
+ 
+ actions{
+ 
+ setMprfTrack{
+ }
+ 
+ detectTarget{
+ ignoreOwnWeapon:b=yes
+ rangeMult:r=1.0
+ }
+ 
+ setHprfTrack{
+ }
+ }
+ }
+ 
+ tryDetectHprf{
+ stateFrom:t="hprfTry"
+ event:t="update"
+ 
+ actions{
+ 
+ setHprfTrack{
+ }
+ 
+ detectTarget{
+ ignoreOwnWeapon:b=yes
+ rangeMult:r=1.0
+ }
+ 
+ setMprfTrack{
+ }
+ }
+ }
+ 
+ lprfOkTryDetectHprf{
+ stateFrom:t="lprfOkHprfTry"
+ event:t="update"
+ 
+ actions{
+ 
+ setHprfTrack{
+ }
+ 
+ detectTarget{
+ ignoreOwnWeapon:b=yes
+ rangeMult:r=1.0
+ }
+ 
+ setLprfTrack{
+ }
+ }
+ }
+ 
+ stateFrom:t="hprfOkMprfTry"
+ trackHprf{
+ stateFrom:t="hprf"
+ event:t="targetDetected"
+ stateTo:t="hprfOkMprfTry"
+ 
+ actions{
+ 
+ track{
+ }
+ }
+ }
+ 
+ startTrackHprf{
+ stateFrom:t="hprfTry"
+ stateFrom:t="lprfOkHprfTry"
+ event:t="targetDetected"
+ stateTo:t="hprf"
+ 
+ actions{
+ 
+ setHprfTrack{
+ }
+ 
+ track{
+ }
+ 
+ setModeName{
+ name:t="PD HDN track"
+ }
+ }
+ }
+ 
+ stateTo:t="lprfOkHprfTry"
+ mprfToHprf{
+ stateTo:t="hprfTry"
+ backToHprf{
+ stateFrom:t="hprfOkMprfTry"
+ stateTo:t="hprfTry"
+ hprfToLprfTry{
+ stateFrom:t="hprf"
+ stateFrom:t="hprfTry"
+ stateTo:t="lprfTry"
+ lprfToMprfTry{
+ stateFrom:t="lprfOkHprfTry"
+ stateTo:t="lprfOkMprfTry"
+ backToLprf{
+ stateFrom:t="lprfOkMprfTry"
+ event:t="targetNotDetected"
+ stateTo:t="lprfTry"
+ extrapolate{
+ lprfToMprf{
+ stateFrom:t="lprf"
+ event:t="targetNotDetected"
+ stateTo:t="mprfTry"
+ extrapolate{
+ lprfTryToMprf{
+ stateFrom:t="lprfTry"
+ event:t="targetNotDetected"
+ stateTo:t="mprfTry"
+ extrapolate{
+ setModeName{
+ name:t="track memory"
```

  **Removed**:
```diff
- power:r=600.0
- range:r=120000.0
- rangeMax:r=300000.0
- angleHalfSens:r=4.0
- power:r=600.0
- rangeMax:r=300000.0
- angleHalfSens:r=4.0
- power:r=600.0
- rangeMax:r=300000.0
- angleHalfSens:r=4.0
- angleHalfSens:r=4.0
- angleHalfSens:r=4.0
- barHeight:r=2.85
- barHeight:r=2.85
- barHeight:r=2.85
- barHeight:r=2.85
- barHeight:r=2.85
- barHeight:r=2.85
- barHeight:r=3.3
- barHeight:r=2.5
- barHeight:r=3.0
- barHeight:r=3.0
- maxValue:r=74000.0
- maxValue:r=74000.0
- maxValue:r=74000.0
- distanceRange:p2=0.0, 92500.0
- twsToHprfVelocity{
- stateFrom:t="mprf"
- stateFrom:t="lprf"
- stateTo:t="lprfOkMprfTry"
- mprfToLprf{
- stateTo:t="lprfTry"
- backToLprf{
- stateFrom:t="lprfOkMprfTry"
- stateTo:t="lprfTry"
- lprfToMprf{
- stateFrom:t="lprf"
- stateTo:t="mprfTry"
- lprfTryToMprf{
- stateFrom:t="lprfTry"
- stateTo:t="mprfTry"
- 
- setModeName{
- name:t="track memory"
- }
- }
- }
- illumination{
- stateInit:t="init"
- 
- transitions{
- 
- activate{
- event:t="fsmActivate"
- stateTo:t="active"
- checkIlluminationTimeOut{
- transiver:b=yes
- pauseMax:r=20.0
- deactivate{
- event:t="fsmDeactivate"
- stateTo:t="inactive"
- setIllumination{
- transiver:b=no
- activateIllumination{
- event:t="sarhMissileLaunch"
- setIlluminationTimeOut{
- timeOut:r=60.0
- }
- }
- updateIllumination{
- event:t="update"
- 
- actions{
- 
- checkIlluminationTimeOut{
- transiver:b=yes
- pauseMax:r=20.0
```


- **aces.vromfs.bin_u/gamedata/sensors/uk_captor_m_pirate.blkx**:

  **Added**:
```diff
+ power:r=800.0
+ range:r=80000.0
+ rangeMax:r=150000.0
+ angleHalfSens:r=3.0
+ sideLobesSensitivity:r=-32.0
+ }
+ }
+ 
+ hprf{
+ sideLobesAttenuation:r=-20.0
+ power:r=1200.0
+ band:i=8
+ rcs:r=5.0
+ range:r=150000.0
+ rangeMax:r=200000.0
+ multipathEffect:p4=0.0, 1.0, 60.0, 0.0
+ 
+ antenna{
+ angleHalfSens:r=3.0
+ power:r=1200.0
+ rangeMax:r=250000.0
+ angleHalfSens:r=3.0
+ power:r=800.0
+ rangeMax:r=200000.0
+ angleHalfSens:r=3.0
+ power:r=800.0
+ angleHalfSens:r=3.0
+ angleHalfSens:r=3.0
+ hprfSearch{
+ groundClutter:b=no
+ aircraftAsTarget:b=yes
+ friendFoeId:b=yes
+ mainBeamDopplerSpeed:b=yes
+ 
+ distance{
+ presents:b=yes
+ minValue:r=5000.0
+ maxValue:r=200000.0
+ width:r=2000.0
+ }
+ 
+ dopplerSpeed{
+ presents:b=yes
+ minValue:r=40.0
+ maxValue:r=1500.0
+ signalWidthMin:r=5.0
+ width:r=120.0
+ }
+ }
+ 
+ hprfTrack{
+ rangeFinder:b=yes
+ dopplerSpeedFinder:b=yes
+ dynamicRange:p2=40.0, 15.0
+ groundClutter:b=yes
+ aircraftAsTarget:b=yes
+ angularAccuracy:r=0.05
+ distanceAccuracy:r=15.0
+ absDopplerSpeed:b=no
+ mainBeamDopplerSpeed:b=no
+ track:b=yes
+ 
+ distance{
+ presents:b=yes
+ minValue:r=200.0
+ maxValue:r=200000.0
+ width:r=500.0
+ }
+ 
+ dopplerSpeed{
+ presents:b=yes
+ minValue:r=-1500.0
+ maxValue:r=1500.0
+ signalWidthMin:r=2.0
+ width:r=20.0
+ }
+ }
+ 
+ maxValue:r=180000.0
+ maxValue:r=180000.0
+ maxValue:r=200000.0
+ barHeight:r=2.1
+ barHeight:r=2.1
+ barHeight:r=2.1
+ barHeight:r=2.1
+ barHeight:r=2.1
+ barHeight:r=2.1
+ barHeight:r=2.5
+ barHeight:r=1.85
+ barHeight:r=2.25
+ barHeight:r=2.25
+ setHprfStandbyMode{
+ transiver:t="hprf"
+ signal:t="hprfSearch"
+ name:t="PD HDN standby"
+ setHprfVelocityStandbyMode{
+ transiver:t="hprfVelocity"
+ signal:t="hprfVelocitySearch"
+ name:t="PD HDN VS standby"
+ setMprfTwsStandbyMode{
+ setRadarTwsStandbyModeCommon{
+ transiver:t="mprf"
+ signal:t="mprfSearch"
+ name:t="TWS standby"
+ setHprfSearchMode{
+ 
+ setRadarSearchModeCommon{
+ }
+ 
+ setTransiver{
+ transiver:t="hprf"
+ }
+ 
+ setSignal{
+ signal:t="hprfSearch"
+ }
+ 
+ setModeName{
+ name:t="PD HDN search"
+ }
+ }
+ 
+ distanceRange:p2=0.0, 138750.0
+ distanceRange:p2=0.0, 138750.0
+ setHprf{
+ 
+ setHprfTargetDesignationRange{
+ }
+ 
+ setCustomActionTemplate{
+ fsm:t="main"
+ name:t="setStandbyMode"
+ actionTemplateName:t="setHprfStandbyMode"
+ }
+ 
+ setCustomActionTemplate{
+ fsm:t="main"
+ name:t="setSearchMode"
+ actionTemplateName:t="setHprfSearchMode"
+ }
+ 
+ setCustomActionTemplate{
+ fsm:t="main"
+ name:t="designateTarget"
+ actionTemplateName:t="designatedTargetSearch"
+ }
+ 
+ setCustomActionTemplate{
+ fsm:t="main"
+ name:t="setBvrLockMode"
+ actionTemplateName:t="setHprfBvrLockMode"
+ }
+ 
+ setCustomActionTemplate{
+ fsm:t="main"
+ name:t="resetSearchMode"
+ actionTemplateName:t="resetRadarSearchMode"
+ }
+ 
+ doCustomActionTemplate{
+ fsm:t="main"
+ name:t="resetSearchMode"
+ }
+ 
+ clearTargets{
+ }
+ 
+ setFsmActive{
+ fsm:t="main"
+ active:b=no
+ }
+ 
+ setFsmActive{
+ fsm:t="main"
+ active:b=yes
+ }
+ }
+ 
+ mprfTwsToHprf{
+ stateTo:t="hprf"
+ 
+ actions{
+ 
+ setHprf{
+ }
+ 
+ setCustomActionTemplate{
+ fsm:t="radarSearchModes"
+ name:t="restore"
+ actionTemplateName:t="setHprf"
+ }
+ }
+ }
+ 
+ hprfTwsToHprfVelocity{
+ stateFrom:t="hprf"
+ command:t="modeSwitch"
+ setHprfTrack{
+ 
+ setTransiver{
+ transiver:t="hprf"
+ }
+ 
+ setSignal{
+ signal:t="hprfTrack"
+ }
+ }
+ 
+ hprfOkTryDetectMprf{
+ stateFrom:t="hprfOkMprfTry"
+ event:t="update"
+ 
+ actions{
+ 
+ setMprfTrack{
+ }
+ 
+ detectTarget{
+ ignoreOwnWeapon:b=yes
+ rangeMult:r=1.0
+ }
+ 
+ setHprfTrack{
+ }
+ }
+ }
+ 
+ tryDetectHprf{
+ stateFrom:t="hprfTry"
+ event:t="update"
+ 
+ actions{
+ 
+ setHprfTrack{
+ }
+ 
+ detectTarget{
+ ignoreOwnWeapon:b=yes
+ rangeMult:r=1.0
+ }
+ 
+ setMprfTrack{
+ }
+ }
+ }
+ 
+ lprfOkTryDetectHprf{
+ stateFrom:t="lprfOkHprfTry"
+ event:t="update"
+ 
+ actions{
+ 
+ setHprfTrack{
+ }
+ 
+ detectTarget{
+ ignoreOwnWeapon:b=yes
+ rangeMult:r=1.0
+ }
+ 
+ setLprfTrack{
+ }
+ }
+ }
+ 
+ stateFrom:t="hprfOkMprfTry"
+ trackHprf{
+ stateFrom:t="hprf"
+ event:t="targetDetected"
+ stateTo:t="hprfOkMprfTry"
+ 
+ actions{
+ 
+ track{
+ }
+ }
+ }
+ 
+ startTrackHprf{
+ stateFrom:t="hprfTry"
+ stateFrom:t="lprfOkHprfTry"
+ event:t="targetDetected"
+ stateTo:t="hprf"
+ 
+ actions{
+ 
+ setHprfTrack{
+ }
+ 
+ track{
+ }
+ 
+ setModeName{
+ name:t="PD HDN track"
+ }
+ }
+ }
+ 
+ stateTo:t="lprfOkHprfTry"
+ mprfToHprf{
+ stateTo:t="hprfTry"
+ 
+ actions{
+ 
+ extrapolate{
+ }
+ }
+ }
+ 
+ backToHprf{
+ stateFrom:t="hprfOkMprfTry"
+ event:t="targetNotDetected"
+ stateTo:t="hprfTry"
+ 
+ actions{
+ 
+ extrapolate{
+ }
+ }
+ }
+ 
+ hprfToLprfTry{
+ stateFrom:t="hprf"
+ stateFrom:t="hprfTry"
+ event:t="targetNotDetected"
+ lprfToMprfTry{
+ stateFrom:t="lprfOkHprfTry"
+ event:t="targetNotDetected"
+ stateTo:t="lprfOkMprfTry"
+ 
+ actions{
+ 
+ extrapolate{
+ }
+ }
+ }
+ 
```

  **Removed**:
```diff
- power:r=600.0
- range:r=120000.0
- rangeMax:r=300000.0
- angleHalfSens:r=4.0
- power:r=600.0
- rangeMax:r=300000.0
- angleHalfSens:r=4.0
- power:r=600.0
- rangeMax:r=300000.0
- angleHalfSens:r=4.0
- power:r=600.0
- angleHalfSens:r=4.0
- angleHalfSens:r=4.0
- maxValue:r=74000.0
- maxValue:r=74000.0
- lprfSearch{
- dynamicRange:p2=40.0, 15.0
- groundClutter:b=yes
- aircraftAsTarget:b=yes
- friendFoeId:b=yes
- 
- distance{
- presents:b=yes
- minValue:r=500.0
- maxValue:r=150000.0
- width:r=200.0
- }
- }
- 
- maxValue:r=74000.0
- barHeight:r=2.85
- barHeight:r=2.85
- barHeight:r=2.85
- barHeight:r=2.85
- barHeight:r=2.85
- barHeight:r=2.85
- barHeight:r=3.3
- barHeight:r=2.5
- barHeight:r=3.0
- barHeight:r=3.0
- setHprfVelocityStandbyMode{
- transiver:t="hprfVelocity"
- signal:t="hprfVelocitySearch"
- name:t="PD HDN VS standby"
- setMprfTwsStandbyMode{
- 
- setRadarTwsStandbyModeCommon{
- }
- 
- setTransiver{
- transiver:t="mprf"
- }
- 
- setSignal{
- signal:t="mprfSearch"
- }
- 
- setModeName{
- name:t="TWS standby"
- }
- }
- 
- setLprfStandbyMode{
- transiver:t="lprf"
- signal:t="lprfSearch"
- name:t="standby"
- setLprfSearchMode{
- setRadarSearchStandbyModeCommon{
- transiver:t="lprf"
- signal:t="lprfSearch"
- name:t="search"
- distanceRange:p2=0.0, 92500.0
- distanceRange:p2=0.0, 92500.0
- mprfTwsToHprfVelocity{
- stateFrom:t="mprf"
- stateFrom:t="lprf"
- stateTo:t="lprfOkMprfTry"
- mprfToLprf{
```


- **aces.vromfs.bin_u/gamedata/units/tankmodels/uk_shir_2.blkx**:

  **Added**:
```diff
+ model:t="shir_2"
+ hasExpl:b=no
+ hasDmg2:b=no
+ hasQualityModels:b=yes
+ collisionSphere0:p4=0.0, -1.5, 0.0, 5.0
+ collisionSphere1:p4=5.0, 2.0, 0.0, 1.0
+ exhaustFx:t="tank_exhaust_med"
+ damagedExhaustFx:t="tank_broken_exhaust"
+ thermalExhaustFx:t="tank_exhaust_nightvision"
+ dustFx:t=""
+ support_unit_class:t="structures/ussr_152mm_d1"
+ support_unit_tag:t="artillery"
+ useSimpleDeathConditionsAndEffects:b=no
+ autoSightDistanceCorrection:b=yes
+ subclass:t="heavyVehicle"
+ onRadarAs:t="tracked"
+ moveType:t="vehicle"
+ maxFwdSpeed:r=60.0
+ maxRevSpeed:r=10.0
+ maxAngSpeed:r=30.0
+ maxAccel:r=4.0
+ maxDecel:r=8.0
+ maxAngAccel0:r=20.0
+ maxAngAccelV:r=0.0
+ maxAngAccel:r=40.0
+ groundNormSmoothViscosity:r=0.1
+ minDistBetween:r=10.0
+ expClass:t="exp_tank"
+ mass:r=54000.0
+ bulletHitFx:t="ground_model_hit"
+ partDamageFx:t="part_damage"
+ explosionFx:t="tank_explosion"
+ fireFx:t="ground_model_fire"
+ destroysRendInstances:b=yes
+ destroysTrees:b=yes
+ type:t="typeMediumTank"
+ rearmSmokeTimeOnField:r=60.0
+ canReloadNonGuns:b=yes
+ 
+ DamageParts{
+ formatVersion:i=2
+ armorClass:t="RHA_tank_modern"
+ hp:r=10000.0
+ 
+ hull_rha{
+ 
+ body_side_dm{
+ armorThickness:r=38.0
+ }
+ 
+ superstructure_top_dm{
+ armorThickness:r=20.0
+ }
+ 
+ superstructure_front_dm{
+ armorThickness:r=25.0
+ createSecondaryShatters:b=no
+ }
+ 
+ superstructure_bottom_dm{
+ armorThickness:r=20.0
+ }
+ 
+ superstructure_back_dm{
+ armorThickness:r=25.0
+ }
+ 
+ superstructure_side_dm{
+ armorThickness:r=20.0
+ }
+ 
+ turret_01_side_dm{
+ armorThickness:r=10.0
+ }
+ 
+ turret_05_back_dm{
+ armorThickness:r=80.0
+ }
+ }
+ 
+ hull_turret_spaced_armor{
+ hp:r=5000.0
+ armorClass:t="leopard_2a5_turret_nera"
+ 
+ composite_armor_turret_02_dm{
+ armorThickness:r=300.0
+ cumulativeArmorQuality:r=0.883
+ genericArmorQuality:r=0.35
+ createSecondaryShatters:b=no
+ }
+ 
+ composite_armor_turret_03_dm{
+ armorThickness:r=100.0
+ cumulativeArmorQuality:r=0.883
+ genericArmorQuality:r=0.35
+ createSecondaryShatters:b=no
+ }
+ 
+ composite_armor_turret_06_dm{
+ armorThickness:r=0.001
+ armorClass:t="CHA_tank_modern"
+ hidableInXrayViewer:b=yes
+ }
+ 
+ composite_armor_hull_01_dm{
+ armorThickness:r=200.0
+ cumulativeArmorQuality:r=0.883
+ genericArmorQuality:r=0.25
+ createSecondaryShatters:b=no
+ }
+ 
+ composite_armor_hull_03_dm{
+ armorThickness:r=0.001
+ armorClass:t="RHA_tank_modern"
+ hidableInXrayViewer:b=yes
+ }
+ 
+ composite_armor_hull_06_dm{
+ armorThickness:r=5.0
+ armorClass:t="tank_structural_steel"
+ hidableInXrayViewer:b=yes
+ }
+ 
+ composite_armor_hull_07_dm{
+ armorThickness:r=5.0
+ armorClass:t="tank_structural_steel"
+ hidableInXrayViewer:b=yes
+ }
+ 
+ composite_armor_turret_09_dm{
+ armorThickness:r=0.001
+ armorClass:t="CHA_tank_modern"
+ hidableInXrayViewer:b=yes
+ }
+ 
+ composite_armor_turret_04_dm{
+ armorThickness:r=180.0
+ cumulativeArmorQuality:r=0.883
+ genericArmorQuality:r=0.35
+ hidableInXrayViewer:b=yes
+ createSecondaryShatters:b=no
+ }
+ 
+ composite_armor_turret_05_dm{
+ armorThickness:r=180.0
+ cumulativeArmorQuality:r=0.883
+ genericArmorQuality:r=0.35
+ hidableInXrayViewer:b=yes
+ createSecondaryShatters:b=no
+ }
+ 
+ composite_armor_turret_07_dm{
+ armorThickness:r=180.0
+ cumulativeArmorQuality:r=0.883
+ genericArmorQuality:r=0.35
+ hidableInXrayViewer:b=yes
+ createSecondaryShatters:b=no
+ }
+ 
+ composite_armor_turret_08_dm{
+ armorThickness:r=180.0
+ cumulativeArmorQuality:r=0.883
+ genericArmorQuality:r=0.35
+ hidableInXrayViewer:b=yes
+ createSecondaryShatters:b=no
+ }
+ }
+ 
+ turret_cha{
+ armorClass:t="CHA_tank_modern"
+ 
+ gun_mask_02_dm{
+ armorThickness:r=38.0
+ }
+ 
+ gun_mask_dm{
+ armorThickness:r=100.0
+ variableThickness:b=yes
+ }
+ }
+ 
+ hull_turret_cha{
+ armorClass:t="RHA_tank_modern"
+ 
+ turret_06_front_dm{
+ armorThickness:r=25.0
+ variableThickness:b=yes
+ }
+ 
+ turret_03_front_dm{
+ armorThickness:r=40.0
+ }
+ 
+ turret_06_bottom_dm{
+ armorThickness:r=45.0
+ }
+ 
+ turret_07_back_dm{
+ armorThickness:r=20.0
+ }
+ 
+ turret_07_bottom_dm{
+ armorThickness:r=25.0
+ }
+ 
+ turret_04_back_dm{
+ armorThickness:r=15.0
+ createSecondaryShatters:b=no
+ }
+ 
+ turret_01_back_dm{
+ armorClass:t="t_90_rubber_fabric_screens"
+ armorThickness:r=10.0
+ }
+ 
+ turret_02_back_dm{
+ armorThickness:r=5.0
+ }
+ 
+ turret_06_back_dm{
+ armorThickness:r=20.0
+ }
+ 
+ body_top_dm{
+ armorThickness:r=15.0
+ }
+ 
+ body_front_dm{
+ armorThickness:r=70.0
+ }
+ 
+ turret_01_top_dm{
+ armorThickness:r=29.0
+ armorClass:t="CHA_tank_modern"
+ }
+ 
+ body_bottom_dm{
+ armorThickness:r=16.0
+ }
+ 
+ body_back_dm{
+ armorThickness:r=15.0
+ variableThickness:b=yes
+ }
+ 
+ turret_01_front_dm{
+ armorThickness:r=60.0
+ armorClass:t="CHA_tank_modern"
+ }
+ 
+ turret_05_top_dm{
+ armorThickness:r=25.0
+ }
+ 
+ turret_05_bottom_dm{
+ armorThickness:r=25.0
+ variableThickness:b=yes
+ armorEffectiveThicknessMax:r=150.0
+ }
+ 
+ turret_02_front_dm{
+ armorThickness:r=10.0
+ }
+ 
+ turret_02_top_dm{
+ armorThickness:r=20.0
+ }
+ 
+ turret_05_side_dm{
+ armorThickness:r=20.0
+ }
+ 
+ turret_03_side_dm{
+ armorThickness:r=5.0
+ }
+ 
+ turret_02_side_dm{
+ armorThickness:r=5.0
+ ignoreSolidDimension:b=yes
+ }
+ 
+ turret_07_side_dm{
+ armorThickness:r=50.0
+ }
+ 
+ turret_02_bottom_dm{
+ armorThickness:r=20.0
+ }
+ 
+ turret_03_back_dm{
+ armorThickness:r=15.0
+ createSecondaryShatters:b=no
+ }
+ 
+ turret_03_bottom_dm{
+ armorThickness:r=38.0
+ createSecondaryShatters:b=no
+ }
+ 
+ turret_commander_dm{
+ armorThickness:r=40.0
+ armorClass:t="CHA_tank_modern"
+ }
+ 
+ gun_mask_01_dm{
+ armorThickness:r=5.0
+ }
+ 
+ composite_armor_hull_08_dm{
+ armorThickness:r=5.0
+ hidableInXrayViewer:b=yes
+ }
+ 
+ turret_05_front_dm{
+ armorThickness:r=5.0
+ }
+ 
+ turret_01_bottom_dm{
+ armorThickness:r=4.0
+ armorClass:t="tank_structural_steel"
+ }
+ }
+ 
+ body_shields{
+ armorClass:t="tank_structural_steel"
+ hp:r=400.0
+ armorThickness:r=4.0
+ stopChanceOnDeadPart:r=0.0
+ createSecondaryShatters:b=no
+ hidableInViewer:b=yes
+ 
+ ex_armor_l_01_dm{
+ armorThickness:r=19.0
+ armorClass:t="aluminium"
+ }
+ 
+ ex_armor_l_02_dm{
+ armorThickness:r=19.0
+ armorClass:t="aluminium"
+ }
+ 
+ ex_armor_l_03_dm{
+ armorThickness:r=19.0
+ armorClass:t="aluminium"
+ }
+ 
+ ex_armor_l_04_dm{
+ armorThickness:r=19.0
+ armorClass:t="aluminium"
+ }
+ 
+ ex_armor_r_01_dm{
+ armorThickness:r=19.0
+ armorClass:t="aluminium"
+ }
+ 
+ ex_armor_r_02_dm{
+ armorThickness:r=19.0
+ armorClass:t="aluminium"
+ }
+ 
+ ex_armor_r_03_dm{
+ armorThickness:r=19.0
+ armorClass:t="aluminium"
+ }
+ 
+ ex_armor_r_04_dm{
+ armorThickness:r=19.0
+ armorClass:t="aluminium"
+ }
+ 
+ ex_decor_r_01_dm{
+ }
+ 
+ ex_decor_r_07_dm{
+ armorThickness:r=4.0
+ armorClass:t="t_90_rubber_fabric_screens"
+ }
+ 
+ ex_decor_l_01_dm{
+ }
+ 
+ ex_decor_l_07_dm{
+ armorThickness:r=4.0
+ armorClass:t="t_90_rubber_fabric_screens"
+ }
+ 
+ turret_09_top_dm{
+ armorThickness:r=5.0
+ }
+ 
+ turret_09_side_dm{
+ armorThickness:r=20.0
+ }
+ 
+ turret_06_top_dm{
+ armorThickness:r=5.0
+ }
+ 
+ ex_decor_l_06_dm{
+ }
+ 
+ ex_decor_r_06_dm{
+ }
+ 
+ ex_decor_04_dm{
+ }
+ 
+ ex_armor_l_05_dm{
+ hp:r=1000.0
+ }
+ 
+ ex_armor_l_06_dm{
+ hp:r=1000.0
+ }
+ 
+ ex_armor_r_05_dm{
+ hp:r=1000.0
+ }
+ 
+ ex_armor_r_06_dm{
+ hp:r=1000.0
+ }
+ }
+ 
+ optics{
+ armorClass:t="optics_tank"
+ armorThickness:r=10.0
+ hp:r=30.0
+ 
+ optic_gun_dm{
+ }
+ 
+ optic_turret_01_dm{
+ }
+ 
+ optic_turret_02_dm{
+ }
+ 
+ optic_turret_03_dm{
+ }
+ 
+ optic_body_dm{
+ }
+ }
+ 
+ chassis{
+ armorClass:t="tank_steel_wheels"
+ hp:r=250.0
+ armorThickness:r=20.0
+ 
+ wheel_r_01_dm{
+ }
+ 
+ wheel_r_02_dm{
+ }
+ 
+ wheel_r_03_dm{
+ }
+ 
+ wheel_r_04_dm{
+ }
+ 
+ wheel_r_05_dm{
+ }
+ 
+ wheel_r_06_dm{
+ }
+ 
+ wheel_l_01_dm{
+ }
+ 
+ wheel_l_02_dm{
+ }
+ 
+ wheel_l_03_dm{
+ }
+ 
+ wheel_l_04_dm{
+ }
+ 
+ wheel_l_05_dm{
+ }
+ 
+ wheel_l_06_dm{
+ }
+ 
+ wheel_l_top_01_dm{
+ }
+ 
+ wheel_l_top_02_dm{
+ }
+ 
+ wheel_l_top_03_dm{
+ }
+ 
+ wheel_r_top_01_dm{
+ }
+ 
+ wheel_r_top_02_dm{
+ }
+ 
+ wheel_r_top_03_dm{
+ }
+ 
+ wheel_r_drive_dm{
+ }
+ 
+ wheel_l_drive_dm{
+ }
+ 
+ wheel_l_front_dm{
+ }
+ 
+ wheel_r_front_dm{
+ }
+ 
+ wheel_support_dm{
+ }
+ 
+ submodule{
+ armorClass:t="tank_traks"
+ armorThickness:r=20.0
+ hp:r=200.0
+ 
+ ex_armor_01_dm{
+ }
+ 
+ ex_armor_02_dm{
+ }
+ }
+ }
+ 
+ gun{
+ armorClass:t="tank_barrel"
+ hp:r=200.0
+ armorThickness:r=35.0
+ 
+ gun_barrel_dm{
+ }
+ 
+ gun_barrel_01_dm{
+ armorThrough:r=10.0
+ armorThickness:r=5.0
+ hp:r=50.0
+ }
+ 
+ gun_barrel_02_dm{
+ armorThrough:r=10.0
+ armorThickness:r=5.0
+ hp:r=50.0
+ }
+ 
+ gun_barrel_03_dm{
+ armorThrough:r=10.0
+ armorThickness:r=5.0
+ hp:r=50.0
+ }
+ 
+ gun_barrel_04_dm{
+ armorThrough:r=10.0
+ armorThickness:r=5.0
+ hp:r=50.0
+ }
+ 
+ gun_barrel_05_dm{
+ armorThrough:r=10.0
+ armorThickness:r=5.0
+ hp:r=50.0
+ }
+ 
+ gun_barrel_06_dm{
+ armorThrough:r=10.0
+ armorThickness:r=5.0
+ hp:r=50.0
+ }
+ 
+ gun_barrel_07_dm{
+ armorThrough:r=10.0
+ armorThickness:r=5.0
+ hp:r=50.0
+ }
+ 
+ gun_barrel_08_dm{
+ armorThrough:r=10.0
+ armorThickness:r=5.0
+ hp:r=50.0
+ }
+ }
+ 
+ tracks{
+ armorClass:t="tank_traks"
+ allowRicochet:b=yes
+ armorThickness:r=20.0
+ armorEffectiveThicknessMax:r=20.0
+ hp:r=300.0
+ genericEffectiveThicknessMax:r=20.0
+ genericDamageMult:r=1.8
+ cumulativeDamageMult:r=1.8
+ 
+ track_r_dm{
+ }
+ 
+ track_l_dm{
+ }
+ 
+ track_r_01_dm{
+ }
+ 
+ track_l_01_dm{
+ }
+ }
+ 
+ crew{
+ armorClass:t="steel_tankman"
+ hp:r=40.0
+ genericDamageMult:r=3.0
+ pressureDamageMult:r=1.0
+ napalmDamageMult:r=0.0
+ 
+ driver_dm{
+ genericDamageMult:r=3.0
+ }
+ 
+ loader_dm{
+ genericDamageMult:r=3.0
+ }
+ 
+ loader_01_dm{
+ genericDamageMult:r=3.0
+ }
+ 
+ loader_02_dm{
+ genericDamageMult:r=3.0
+ }
+ 
+ gunner_dm{
+ genericDamageMult:r=3.0
+ }
+ 
+ commander_dm{
+ genericDamageMult:r=3.0
+ }
+ 
+ machine_gunner_01_dm{
+ genericDamageMult:r=3.0
+ }
+ 
+ machine_gunner_02_dm{
+ genericDamageMult:r=3.0
+ }
+ 
+ machine_gunner_dm{
+ genericDamageMult:r=3.0
+ }
+ }
+ 
+ equipment_body_turret{
+ armorClass:t="tank_structural_steel"
+ hp:r=250.0
+ armorThickness:r=2.0
+ armorThrough:r=15.0
+ fireProtectionHp:r=5.0
+ hidableInViewer:b=no
+ 
+ drive_turret_v_dm{
+ armorThrough:r=15.0
+ }
+ 
+ drive_turret_h_dm{
+ armorThrough:r=15.0
+ }
+ 
+ driver_controls_dm{
+ armorThrough:r=15.0
+ }
+ 
+ drive_turret_v_01_dm{
+ hp:r=40.0
+ armorThrough:r=15.0
+ }
+ 
+ drive_turret_h_01_dm{
+ hp:r=40.0
+ armorThrough:r=15.0
+ }
+ 
+ drive_turret_v_02_dm{
+ hp:r=40.0
+ armorThrough:r=15.0
+ }
+ 
+ drive_turret_h_02_dm{
+ hp:r=40.0
+ armorThrough:r=15.0
+ }
+ 
+ drive_turret_v_03_dm{
+ hp:r=40.0
+ armorThrough:r=15.0
+ }
+ 
+ drive_turret_h_03_dm{
+ hp:r=40.0
+ armorThrough:r=15.0
+ }
+ 
+ drive_turret_v_04_dm{
+ hp:r=40.0
+ armorThrough:r=15.0
+ }
+ 
+ drive_turret_h_04_dm{
+ hp:r=40.0
+ armorThrough:r=15.0
+ }
+ 
+ drive_turret_v_05_dm{
+ hp:r=40.0
+ armorThrough:r=15.0
+ }
+ 
+ drive_turret_h_05_dm{
+ hp:r=40.0
+ armorThrough:r=15.0
+ }
+ 
+ radiator_dm{
+ hp:r=50.0
+ armorThrough:r=5.0
+ }
+ 
+ radiator_l_dm{
+ hp:r=50.0
+ armorThrough:r=5.0
+ }
+ 
+ radiator_r_dm{
+ hp:r=50.0
+ armorThrough:r=5.0
+ }
+ 
+ radio_station_dm{
+ hp:r=50.0
+ armorThrough:r=3.0
+ }
+ 
+ electronic_equipment_dm{
+ hp:r=60.0
+ armorThrough:r=3.0
+ }
+ 
+ electronic_equipment_01_dm{
+ hp:r=60.0
+ armorThrough:r=3.0
+ }
+ 
+ fire_control_system_dm{
+ hp:r=60.0
+ armorThrough:r=3.0
+ }
+ 
+ fire_control_system_01_dm{
+ hp:r=60.0
+ armorThrough:r=3.0
+ }
+ 
+ power_system_dm{
+ hp:r=60.0
+ armorThrough:r=15.0
+ }
+ }
+ 
+ cannon_breech{
+ armorClass:t="tank_structural_steel"
+ hp:r=150.0
+ armorThickness:r=150.0
+ fireProtectionHp:r=5.0
+ hidableInViewer:b=no
+ 
+ cannon_breech_dm{
+ restrainDamage:r=0.5
+ }
+ 
+ cannon_breech_01_dm{
+ armorThickness:r=10.0
+ }
+ 
+ cannon_breech_02_dm{
+ armorThickness:r=10.0
+ }
+ 
+ cannon_breech_03_dm{
+ armorThickness:r=10.0
+ }
+ 
+ cannon_breech_04_dm{
+ armorThickness:r=10.0
+ }
+ 
+ cannon_breech_05_dm{
+ armorThickness:r=10.0
+ }
+ 
+ autoloader_dm{
+ armorThickness:r=2.0
+ armorThrough:r=1.0
+ ignoreSolidDimension:b=yes
+ }
+ }
+ 
+ power_block{
+ armorClass:t="armor_tank_engine"
+ hp:r=100.0
+ armorThickness:r=150.0
+ fireProtectionHp:r=5.0
+ restrainDamage:r=0.5
+ 
+ engine_dm{
+ }
+ 
+ transmission_dm{
+ }
+ }
+ 
+ ammo{
+ armorClass:t="tank_structural_steel"
+ genericDamageMult:r=2.0
+ cumulativeDamageMult:r=1.25
+ hp:r=300.0
+ armorThickness:r=2.0
+ armorThrough:r=10.0
+ fireProtectionHp:r=20.0
+ createSecondaryShatters:b=no
+ 
+ ammo_turret_dm{
+ }
+ 
+ ammo_turret_01_dm{
+ }
+ 
+ ammo_turret_02_dm{
+ }
+ 
+ ammo_turret_03_dm{
+ }
+ 
+ ammo_turret_04_dm{
+ }
+ 
+ ammo_turret_05_dm{
+ }
+ 
+ ammo_turret_06_dm{
+ }
+ 
+ ammo_turret_07_dm{
+ }
+ 
+ ammo_turret_08_dm{
+ }
+ 
+ ammo_turret_09_dm{
+ }
+ 
+ ammo_turret_10_dm{
+ }
+ 
+ ammo_turret_11_dm{
+ }
+ 
+ ammo_turret_12_dm{
+ }
+ 
+ ammo_turret_13_dm{
+ }
+ 
+ ammo_turret_14_dm{
+ }
+ 
+ ammo_turret_15_dm{
+ }
+ 
+ ammo_turret_16_dm{
+ }
+ 
+ ammo_turret_17_dm{
+ }
+ 
+ ammo_turret_18_dm{
+ }
+ 
+ ammo_turret_19_dm{
+ }
+ 
+ ammo_turret_20_dm{
+ }
+ 
+ ammo_turret_21_dm{
+ }
+ 
+ ammo_turret_22_dm{
+ }
+ 
+ ammo_turret_23_dm{
+ }
+ 
+ ammo_turret_24_dm{
+ }
+ 
+ ammo_turret_25_dm{
+ }
+ 
+ ammo_turret_26_dm{
+ }
+ 
+ ammo_turret_27_dm{
+ }
+ 
+ ammo_turret_28_dm{
+ }
+ 
+ ammo_turret_29_dm{
+ }
+ 
+ ammo_turret_30_dm{
+ }
+ 
+ ammo_turret_31_dm{
+ }
+ 
+ ammo_turret_32_dm{
+ }
+ 
+ ammo_turret_33_dm{
+ }
+ 
+ ammo_turret_34_dm{
+ }
+ 
+ ammo_turret_35_dm{
+ }
+ 
+ ammo_turret_36_dm{
+ }
+ 
+ ammo_turret_37_dm{
+ }
+ 
+ ammo_turret_38_dm{
+ }
+ 
+ ammo_turret_39_dm{
+ }
+ 
+ ammo_turret_40_dm{
+ }
+ 
+ ammo_turret_41_dm{
+ }
+ 
+ ammo_turret_42_dm{
+ }
+ 
+ ammo_turret_43_dm{
+ }
+ 
+ ammo_turret_44_dm{
+ }
+ 
+ ammo_turret_45_dm{
+ }
+ 
+ ammo_turret_46_dm{
+ }
+ 
+ ammo_turret_47_dm{
+ }
+ 
+ ammo_turret_48_dm{
+ }
+ 
+ ammo_turret_49_dm{
+ }
+ 
+ ammo_turret_50_dm{
+ }
+ 
+ ammo_turret_51_dm{
+ }
+ 
+ ammo_turret_52_dm{
+ }
+ 
+ ammo_turret_53_dm{
+ }
+ 
+ ammo_turret_54_dm{
+ }
+ 
+ ammo_turret_55_dm{
+ }
+ 
+ ammo_turret_56_dm{
+ }
+ 
+ ammo_turret_57_dm{
+ }
+ 
+ ammo_turret_58_dm{
+ }
+ 
+ ammo_turret_59_dm{
+ }
+ 
+ ammo_turret_60_dm{
+ }
+ 
+ ammo_turret_61_dm{
+ }
+ 
+ ammo_turret_62_dm{
+ }
+ 
+ ammo_turret_63_dm{
+ }
+ 
+ ammo_turret_64_dm{
+ }
+ 
+ ammo_turret_65_dm{
+ }
+ 
+ ammo_turret_66_dm{
+ }
+ 
+ ammo_turret_67_dm{
+ }
+ 
+ ammo_turret_68_dm{
+ }
+ 
+ ammo_turret_69_dm{
+ }
+ 
+ ammo_turret_70_dm{
+ }
+ 
+ ammo_turret_71_dm{
+ }
+ 
+ ammo_turret_72_dm{
+ }
+ 
+ ammo_turret_73_dm{
+ }
+ 
+ ammo_turret_74_dm{
+ }
+ 
+ ammo_turret_75_dm{
+ }
+ 
+ ammo_body_dm{
+ }
+ 
+ ammo_body_01_dm{
+ }
+ 
+ ammo_body_02_dm{
+ }
+ 
+ ammo_body_03_dm{
+ }
+ 
+ ammo_body_04_dm{
+ }
+ 
+ ammo_body_05_dm{
+ }
+ 
+ ammo_body_06_dm{
+ }
+ 
+ ammo_body_07_dm{
+ }
+ 
+ ammo_body_08_dm{
+ }
+ 
+ ammo_body_09_dm{
+ }
+ 
+ ammo_body_10_dm{
+ }
+ 
+ ammo_body_11_dm{
+ }
+ 
+ ammo_body_12_dm{
+ }
+ 
+ ammo_body_13_dm{
+ }
+ 
+ ammo_body_14_dm{
+ }
+ 
+ ammo_body_15_dm{
+ }
+ 
+ ammo_body_16_dm{
+ }
+ 
+ ammo_body_17_dm{
+ }
+ 
+ ammo_body_18_dm{
+ }
+ 
+ ammo_body_19_dm{
+ }
+ 
+ ammo_body_20_dm{
+ }
+ 
+ ammo_body_21_dm{
+ }
+ 
+ ammo_body_22_dm{
+ }
+ 
+ ammo_body_23_dm{
+ }
+ 
+ ammo_body_24_dm{
+ }
+ 
+ ammo_body_25_dm{
+ }
+ 
+ ammo_body_26_dm{
+ }
+ 
+ ammo_body_27_dm{
+ }
+ 
+ ammo_body_28_dm{
+ }
+ 
+ ammo_body_29_dm{
+ }
+ 
+ ammo_body_30_dm{
+ }
+ 
+ ammo_body_31_dm{
+ }
+ 
+ ammo_body_32_dm{
+ }
+ 
+ ammo_body_33_dm{
+ }
+ 
+ ammo_body_34_dm{
+ }
+ 
+ ammo_body_35_dm{
+ }
+ 
+ ammo_body_36_dm{
+ }
+ 
+ ammo_body_37_dm{
+ }
+ 
+ ammo_body_38_dm{
+ }
+ 
+ ammo_body_39_dm{
+ }
+ 
+ ammo_body_40_dm{
+ }
+ 
+ ammo_body_41_dm{
+ }
+ 
+ ammo_body_42_dm{
+ }
+ 
+ ammo_body_43_dm{
+ }
+ 
+ ammo_body_44_dm{
+ }
+ 
+ ammo_body_45_dm{
+ }
+ 
+ ammo_body_46_dm{
+ }
+ 
+ ammo_body_47_dm{
+ }
+ 
+ ammo_body_48_dm{
+ }
+ 
+ ammo_body_49_dm{
+ }
+ 
+ ammo_body_50_dm{
+ }
+ 
+ ammo_body_51_dm{
+ }
+ 
+ ammo_body_52_dm{
+ }
+ 
+ ammo_body_53_dm{
+ }
+ 
+ ammo_body_54_dm{
+ }
+ 
+ ammo_body_55_dm{
+ }
+ 
+ ammo_body_56_dm{
+ }
+ 
+ ammo_body_57_dm{
+ }
+ 
+ ammo_body_58_dm{
+ }
+ 
+ ammo_body_59_dm{
+ }
+ 
+ ammo_body_60_dm{
+ }
+ 
+ ammo_body_61_dm{
+ }
+ 
+ ammo_body_62_dm{
+ }
+ 
+ ammo_body_63_dm{
+ }
+ 
+ ammo_body_64_dm{
+ }
+ 
+ ammo_body_65_dm{
+ }
+ 
+ ammo_body_66_dm{
+ }
+ 
+ ammo_body_67_dm{
+ }
+ 
+ ammo_body_68_dm{
+ }
+ 
+ ammo_body_69_dm{
+ }
+ 
+ ammo_body_70_dm{
+ }
+ 
+ ammo_body_l_01_dm{
+ }
+ 
+ ammo_body_l_02_dm{
+ }
+ 
+ ammo_body_l_03_dm{
+ }
+ 
+ ammo_body_l_04_dm{
+ }
+ 
+ ammo_body_l_05_dm{
+ }
+ 
+ ammo_body_l_06_dm{
+ }
+ 
+ ammo_body_l_07_dm{
+ }
+ 
+ ammo_body_l_08_dm{
+ }
+ 
+ ammo_body_l_09_dm{
+ }
+ 
+ ammo_body_l_10_dm{
+ }
+ 
+ ammo_body_l_11_dm{
+ }
+ 
+ ammo_body_l_12_dm{
+ }
+ 
+ ammo_body_l_13_dm{
+ }
+ 
+ ammo_body_l_14_dm{
+ }
+ 
+ ammo_body_l_15_dm{
+ }
+ 
+ ammo_body_l_16_dm{
+ }
+ 
+ ammo_body_l_17_dm{
+ }
+ 
+ ammo_body_l_18_dm{
+ }
+ 
+ ammo_body_l_19_dm{
+ }
+ 
+ ammo_body_l_20_dm{
+ }
+ 
+ ammo_body_r_01_dm{
+ }
+ 
+ ammo_body_r_02_dm{
+ }
+ 
+ ammo_body_r_03_dm{
+ }
+ 
+ ammo_body_r_04_dm{
+ }
+ 
+ ammo_body_r_05_dm{
+ }
+ 
+ ammo_body_r_06_dm{
+ }
+ 
+ ammo_body_r_07_dm{
+ }
+ 
+ ammo_body_r_08_dm{
+ }
+ 
+ ammo_body_r_09_dm{
+ }
+ 
+ ammo_body_r_10_dm{
+ }
+ 
+ ammo_body_r_11_dm{
+ }
+ 
+ ammo_body_r_12_dm{
+ }
+ 
+ ammo_body_r_13_dm{
+ }
+ 
+ ammo_body_r_14_dm{
+ }
+ 
+ ammo_body_r_15_dm{
+ }
+ 
+ ammo_body_r_16_dm{
+ }
+ 
+ ammo_body_r_17_dm{
+ }
+ 
+ ammo_body_r_18_dm{
+ }
+ 
+ ammo_body_r_19_dm{
+ }
+ 
+ ammo_body_r_20_dm{
+ }
+ }
+ 
+ fuel_tanks{
+ armorClass:t="tank_structural_steel"
+ hp:r=400.0
+ armorThickness:r=2.0
+ armorThrough:r=12.0
+ fireProtectionHp:r=15.0
+ createSecondaryShatters:b=no
+ stopChanceOnDeadPart:r=0.0
+ fireParamsPreset:t="fuel_internal"
+ 
+ fuel_tank_dm{
+ }
+ 
+ fuel_tank_01_dm{
+ }
+ 
+ fuel_tank_02_dm{
+ }
+ 
+ fuel_tank_03_dm{
+ }
+ 
+ fuel_tank_04_dm{
+ }
+ 
+ fuel_tank_05_dm{
+ }
+ 
+ fuel_tank_r_01_dm{
+ }
+ 
+ fuel_tank_r_02_dm{
+ }
+ 
+ fuel_tank_r_03_dm{
+ }
+ 
+ fuel_tank_r_04_dm{
+ }
+ 
+ fuel_tank_r_05_dm{
+ }
+ 
+ fuel_tank_l_01_dm{
+ }
+ 
+ fuel_tank_l_02_dm{
+ }
+ 
+ fuel_tank_l_03_dm{
+ }
+ 
+ fuel_tank_l_04_dm{
+ }
+ 
+ fuel_tank_l_05_dm{
+ }
+ }
+ 
+ fuel_tanks_exterior{
+ armorClass:t="tank_structural_steel"
+ hp:r=250.0
+ armorThickness:r=2.0
+ armorThrough:r=12.0
+ fireProtectionHp:r=15.0
+ createSecondaryShatters:b=no
+ fireParamsPreset:t="fuel_exterior"
+ stopChanceOnDeadPart:r=0.0
+ 
+ fuel_tank_exterior_r_01_dm{
+ }
+ 
+ fuel_tank_exterior_r_02_dm{
+ }
+ 
+ fuel_tank_exterior_r_03_dm{
+ }
+ 
+ fuel_tank_exterior_r_04_dm{
+ }
+ 
+ fuel_tank_exterior_r_05_dm{
+ }
+ 
+ fuel_tank_exterior_l_01_dm{
+ }
+ 
+ fuel_tank_exterior_l_02_dm{
+ }
+ 
+ fuel_tank_exterior_l_03_dm{
+ }
+ 
+ fuel_tank_exterior_l_04_dm{
+ }
+ 
+ fuel_tank_exterior_l_05_dm{
+ }
+ 
+ fuel_tank_exterior_01_dm{
+ }
+ 
+ fuel_tank_exterior_02_dm{
+ }
+ 
+ fuel_tank_exterior_03_dm{
+ }
+ }
+ 
+ commander_panoramic_sight{
+ 
+ commander_panoramic_sight_dm{
+ armorClass:t="optics_tank"
+ armorThrough:r=20.0
+ armorThickness:r=10.0
+ hp:r=20.0
+ }
+ }
+ }
+ 
+ DamageEffects{
+ 
+ part{
+ name:t="ammo_turret_11_dm"
+ name:t="ammo_turret_12_dm"
+ name:t="ammo_turret_13_dm"
+ name:t="ammo_body_01_dm"
+ name:t="ammo_body_02_dm"
+ name:t="ammo_body_03_dm"
+ name:t="ammo_body_04_dm"
+ name:t="ammo_body_05_dm"
+ name:t="ammo_body_06_dm"
+ name:t="ammo_body_07_dm"
+ name:t="ammo_body_08_dm"
+ name:t="ammo_body_09_dm"
+ name:t="ammo_body_10_dm"
+ name:t="ammo_body_11_dm"
+ name:t="ammo_body_12_dm"
+ name:t="ammo_body_13_dm"
+ name:t="ammo_body_14_dm"
+ name:t="ammo_body_15_dm"
+ name:t="ammo_body_16_dm"
+ name:t="ammo_body_17_dm"
+ name:t="ammo_body_18_dm"
+ name:t="ammo_body_19_dm"
+ name:t="ammo_body_20_dm"
+ name:t="ammo_body_21_dm"
+ name:t="ammo_body_22_dm"
+ name:t="ammo_body_23_dm"
+ name:t="ammo_body_24_dm"
+ name:t="ammo_body_25_dm"
+ name:t="ammo_body_26_dm"
+ name:t="ammo_body_27_dm"
+ name:t="ammo_body_28_dm"
+ name:t="ammo_body_29_dm"
+ name:t="ammo_body_30_dm"
+ name:t="ammo_body_31_dm"
+ name:t="ammo_body_32_dm"
+ name:t="ammo_body_33_dm"
+ name:t="ammo_body_34_dm"
+ name:t="ammo_body_35_dm"
+ name:t="ammo_body_36_dm"
+ name:t="ammo_body_37_dm"
+ name:t="ammo_body_38_dm"
+ name:t="ammo_body_39_dm"
+ name:t="ammo_body_40_dm"
+ name:t="ammo_body_41_dm"
+ name:t="ammo_body_52_dm"
+ name:t="ammo_body_53_dm"
+ name:t="ammo_body_54_dm"
+ name:t="ammo_body_55_dm"
+ name:t="ammo_body_56_dm"
+ name:t="ammo_body_57_dm"
+ name:t="ammo_body_58_dm"
+ name:t="ammo_body_59_dm"
+ 
+ onHit{
+ damageType:t="cumulative"
+ fire:r=0.7
+ damage:r=75.0
+ fHitCritical:b=yes
+ }
+ 
+ onHit{
+ damageType:t="cumulative"
+ fire:r=0.8
+ damage:r=200.0
+ fHitCritical:b=yes
+ }
+ 
+ onHit{
+ damageType:t="explosion"
+ fire:r=0.05
+ damage:r=5.0
+ fHitCritical:b=yes
+ }
+ 
+ onHit{
+ damageType:t="explosion"
+ fire:r=0.35
+ damage:r=20.0
+ fHitCritical:b=yes
+ }
+ 
+ onHit{
+ damageType:t="explosion"
+ fire:r=0.5
+ damage:r=30.0
+ fHitCritical:b=yes
+ }
+ 
+ onHit{
+ damageType:t="generic"
+ fire:r=0.2
+ damage:r=70.0
+ fHitCritical:b=yes
+ }
+ 
+ onHit{
+ damageType:t="generic"
+ fire:r=0.4
+ damage:r=200.0
+ fHitCritical:b=yes
+ }
+ 
+ onHit{
+ damageType:t="generic"
+ fire:r=0.5
+ damage:r=300.0
+ fHitCritical:b=yes
+ }
+ 
+ onHit{
+ damageType:t="secondaryShatter"
+ fire:r=0.1
+ damage:r=150.0
+ fHitCritical:b=yes
+ }
+ 
+ onHit{
+ damageType:t="secondaryShatter"
+ fire:r=0.3
+ damage:r=300.0
+ fHitCritical:b=yes
+ }
+ 
+ onHit{
+ damageType:t="fire"
+ fire:r=0.02
+ }
+ 
+ onKill{
+ fire:r=1.0
+ }
+ }
+ 
+ part{
+ name:t="ammo_turret_01_dm"
+ name:t="ammo_turret_02_dm"
+ name:t="ammo_turret_03_dm"
+ name:t="ammo_turret_04_dm"
+ name:t="ammo_turret_05_dm"
+ name:t="ammo_turret_06_dm"
+ name:t="ammo_turret_07_dm"
+ name:t="ammo_turret_08_dm"
+ name:t="ammo_turret_09_dm"
+ name:t="ammo_turret_10_dm"
+ name:t="ammo_body_42_dm"
+ name:t="ammo_body_43_dm"
+ name:t="ammo_body_44_dm"
+ name:t="ammo_body_45_dm"
+ name:t="ammo_body_46_dm"
+ name:t="ammo_body_47_dm"
+ name:t="ammo_body_48_dm"
+ name:t="ammo_body_49_dm"
+ name:t="ammo_body_50_dm"
+ name:t="ammo_body_51_dm"
+ 
+ onHit{
+ damageType:t="cumulative"
+ expl:r=0.4
+ fire:r=0.5
+ damage:r=75.0
+ fHitCritical:b=yes
+ }
+ 
+ onHit{
+ damageType:t="cumulative"
+ expl:r=0.6
+ fire:r=0.4
+ damage:r=200.0
+ fHitCritical:b=yes
+ }
+ 
+ onHit{
+ damageType:t="explosion"
+ expl:r=0.1
+ fire:r=0.1
+ damage:r=20.0
+ fHitCritical:b=yes
+ }
+ 
+ onHit{
+ damageType:t="explosion"
+ expl:r=0.15
+ fire:r=0.15
+ damage:r=50.0
+ fHitCritical:b=yes
+ }
+ 
+ onHit{
+ damageType:t="explosion"
+ expl:r=0.2
+ fire:r=0.15
+ damage:r=200.0
+ fHitCritical:b=yes
+ }
+ 
+ onHit{
+ damageType:t="explosion"
+ expl:r=0.4
+ fire:r=0.2
+ damage:r=400.0
+ fHitCritical:b=yes
+ }
+ 
+ onHit{
+ damageType:t="generic"
+ expl:r=0.075
+ fire:r=0.075
+ damage:r=70.0
+ fHitCritical:b=yes
+ }
+ 
+ onHit{
+ damageType:t="generic"
+ expl:r=0.15
+ fire:r=0.15
+ damage:r=200.0
+ fHitCritical:b=yes
+ }
+ 
+ onHit{
+ damageType:t="generic"
+ expl:r=0.25
+ fire:r=0.25
+ damage:r=300.0
+ fHitCritical:b=yes
+ }
+ 
+ onHit{
+ damageType:t="secondaryShatter"
+ fire:r=0.05
+ damage:r=50.0
+ fHitCritical:b=yes
+ }
+ 
+ onHit{
+ damageType:t="secondaryShatter"
+ fire:r=0.15
+ damage:r=150.0
+ fHitCritical:b=yes
+ }
+ 
+ onHit{
+ damageType:t="secondaryShatter"
+ fire:r=0.4
+ damage:r=200.0
+ fHitCritical:b=yes
+ }
+ 
+ onHit{
+ damageType:t="fire"
+ fire:r=0.01
+ full_expl:r=0.01
+ expl:r=0.01
+ }
+ 
+ onKill{
+ damageType:t="cumulative"
+ expl:r=0.4
+ full_expl:r=0.1
+ fire:r=0.5
+ }
+ 
+ onKill{
+ damageType:t="explosion"
+ expl:r=0.4
+ full_expl:r=0.1
+ fire:r=0.5
+ }
+ 
+ onKill{
+ damageType:t="secondaryShatter"
+ expl:r=0.4
+ full_expl:r=0.1
+ fire:r=0.5
+ }
+ 
+ onKill{
+ damageType:t="generic"
+ expl:r=0.5
+ full_expl:r=0.1
+ fire:r=0.4
+ }
+ }
+ 
+ part{
+ name:t="ammo_turret_14_dm"
+ name:t="ammo_turret_15_dm"
+ name:t="ammo_turret_16_dm"
+ name:t="ammo_turret_17_dm"
+ name:t="ammo_turret_18_dm"
+ name:t="ammo_turret_19_dm"
+ name:t="ammo_turret_20_dm"
+ name:t="ammo_turret_21_dm"
+ name:t="ammo_turret_22_dm"
+ name:t="ammo_turret_23_dm"
+ name:t="ammo_turret_24_dm"
+ name:t="ammo_turret_25_dm"
+ name:t="ammo_turret_26_dm"
+ name:t="ammo_turret_27_dm"
+ name:t="ammo_turret_28_dm"
+ name:t="ammo_turret_29_dm"
+ name:t="ammo_turret_30_dm"
+ name:t="ammo_turret_31_dm"
+ name:t="ammo_turret_32_dm"
+ name:t="ammo_turret_33_dm"
+ name:t="ammo_turret_34_dm"
+ name:t="ammo_turret_35_dm"
+ name:t="ammo_turret_36_dm"
+ name:t="ammo_turret_37_dm"
+ name:t="ammo_turret_38_dm"
+ name:t="ammo_turret_39_dm"
+ name:t="ammo_turret_40_dm"
+ name:t="ammo_turret_41_dm"
+ name:t="ammo_turret_42_dm"
+ name:t="ammo_turret_43_dm"
+ name:t="ammo_turret_44_dm"
+ name:t="ammo_turret_45_dm"
+ 
+ onHit{
+ damageType:t="cumulative"
+ expl:r=0.0
+ fire:r=0.0
+ damage:r=75.0
+ fHitCritical:b=yes
+ }
+ 
+ onHit{
+ damageType:t="cumulative"
+ expl:r=0.0
+ fire:r=0.0
+ damage:r=200.0
+ fHitCritical:b=yes
+ }
+ 
+ onHit{
+ damageType:t="explosion"
+ expl:r=0.0
+ fire:r=0.0
+ damage:r=20.0
+ fHitCritical:b=yes
+ }
+ 
+ onHit{
+ damageType:t="explosion"
+ expl:r=0.0
+ fire:r=0.0
+ damage:r=50.0
+ fHitCritical:b=yes
+ }
+ 
+ onHit{
+ damageType:t="explosion"
+ expl:r=0.0
+ fire:r=0.0
+ damage:r=200.0
+ fHitCritical:b=yes
+ }
+ 
+ onHit{
+ damageType:t="explosion"
+ expl:r=0.0
+ fire:r=0.0
+ damage:r=400.0
+ fHitCritical:b=yes
+ }
+ 
+ onHit{
+ damageType:t="generic"
+ expl:r=0.0
+ fire:r=0.0
+ damage:r=70.0
+ fHitCritical:b=yes
+ }
+ 
+ onHit{
+ damageType:t="generic"
+ expl:r=0.0
+ fire:r=0.0
+ damage:r=200.0
+ fHitCritical:b=yes
+ }
+ 
+ onHit{
+ damageType:t="generic"
+ expl:r=0.0
+ fire:r=0.0
+ damage:r=300.0
+ fHitCritical:b=yes
+ }
+ 
+ onHit{
+ damageType:t="secondaryShatter"
+ fire:r=0.0
+ damage:r=50.0
+ fHitCritical:b=yes
+ }
+ 
+ onHit{
+ damageType:t="secondaryShatter"
+ fire:r=0.0
+ damage:r=150.0
+ fHitCritical:b=yes
+ }
+ 
+ onHit{
+ damageType:t="secondaryShatter"
+ fire:r=0.0
+ damage:r=200.0
+ fHitCritical:b=yes
+ }
+ }
+ 
+ part{
+ name:t="engine_dm"
+ 
+ onHit{
+ damageType:t="cumulative"
+ fire:r=0.2
+ damage:r=75.0
+ fHitCritical:b=yes
+ }
+ 
+ onHit{
+ damageType:t="explosion"
+ fire:r=0.3
+ damage:r=30.0
+ fHitCritical:b=yes
+ }
+ 
+ onHit{
+ damageType:t="generic"
+ fire:r=0.05
+ damage:r=20.0
+ fHitCritical:b=yes
+ }
+ 
+ onHit{
+ damageType:t="generic"
+ fire:r=0.1
+ damage:r=70.0
+ fHitCritical:b=yes
+ }
+ 
+ onHit{
+ damageType:t="generic"
+ fire:r=0.3
+ damage:r=200.0
+ fHitCritical:b=yes
+ }
+ 
+ onHit{
+ damageType:t="generic"
+ fire:r=0.4
+ damage:r=300.0
+ fHitCritical:b=yes
+ }
+ 
+ onHit{
+ damageType:t="fire"
+ fire:r=0.1
+ }
+ 
+ onKill{
+ notDamageType:t="overheat"
+ fire:r=0.4
+ nothing:r=0.6
+ fHitCritical:b=yes
+ }
+ }
+ 
+ part{
+ name:t="fuel_tank_dm"
+ name:t="fuel_tank_01_dm"
+ name:t="fuel_tank_02_dm"
+ name:t="fuel_tank_03_dm"
+ name:t="fuel_tank_04_dm"
+ name:t="fuel_tank_05_dm"
+ name:t="fuel_tank_r_01_dm"
+ name:t="fuel_tank_r_02_dm"
+ name:t="fuel_tank_r_03_dm"
+ name:t="fuel_tank_r_04_dm"
+ name:t="fuel_tank_r_05_dm"
+ name:t="fuel_tank_l_01_dm"
+ name:t="fuel_tank_l_02_dm"
+ name:t="fuel_tank_l_03_dm"
+ name:t="fuel_tank_l_04_dm"
+ name:t="fuel_tank_l_05_dm"
+ name:t="fuel_tank_exterior_r_01_dm"
+ name:t="fuel_tank_exterior_r_02_dm"
+ name:t="fuel_tank_exterior_l_01_dm"
+ name:t="fuel_tank_exterior_l_02_dm"
+ 
+ onHit{
+ damageType:t="cumulative"
+ expl:r=0.08
+ fire:r=0.1
+ damage:r=100.0
+ fHitCritical:b=yes
+ }
+ 
+ onHit{
+ damageType:t="cumulative"
+ expl:r=0.15
+ fire:r=0.2
+ damage:r=250.0
+ fHitCritical:b=yes
+ }
+ 
+ onHit{
+ damageType:t="cumulative"
+ expl:r=0.6
+ fire:r=0.4
+ damage:r=400.0
+ fHitCritical:b=yes
+ }
+ 
+ onHit{
+ damageType:t="cumulative"
+ expl:r=1.0
+ damage:r=800.0
+ fHitCritical:b=yes
+ }
+ 
+ onHit{
+ damageType:t="explosion"
+ expl:r=0.125
+ fire:r=0.15
+ damage:r=25.0
+ fHitCritical:b=yes
+ }
+ 
+ onHit{
+ damageType:t="explosion"
+ expl:r=0.2
+ fire:r=0.2
+ damage:r=50.0
+ fHitCritical:b=yes
+ }
+ 
+ onHit{
+ damageType:t="generic"
+ fire:r=0.05
+ damage:r=20.0
+ fHitCritical:b=yes
+ }
+ 
+ onHit{
+ damageType:t="generic"
+ fire:r=0.1
+ damage:r=70.0
+ fHitCritical:b=yes
+ }
+ 
+ onHit{
+ damageType:t="generic"
+ fire:r=0.2
+ expl:r=0.2
+ damage:r=200.0
+ fHitCritical:b=yes
+ }
+ 
+ onHit{
+ damageType:t="generic"
+ fire:r=0.4
+ expl:r=0.6
+ damage:r=250.0
+ fHitCritical:b=yes
+ }
+ 
+ onHit{
+ damageType:t="generic"
+ fire:r=0.3
+ expl:r=0.7
+ damage:r=300.0
+ fHitCritical:b=yes
+ }
+ 
+ onHit{
+ damageType:t="generic"
+ expl:r=1.0
+ damage:r=600.0
+ fHitCritical:b=yes
+ }
+ 
+ onHit{
+ damageType:t="fire"
+ fire:r=0.2
+ }
+ 
+ onKill{
+ fire:r=1.0
+ fHitCritical:b=yes
+ }
+ }
+ 
+ part{
+ name:t="transmission_dm"
+ 
+ onHit{
+ damageType:t="cumulative"
+ fire:r=0.15
+ damage:r=75.0
+ fHitCritical:b=yes
+ }
+ 
+ onHit{
+ damageType:t="explosion"
+ fire:r=0.1
+ damage:r=30.0
+ fHitCritical:b=yes
+ }
+ 
+ onHit{
+ damageType:t="generic"
+ fire:r=0.05
+ damage:r=70.0
+ fHitCritical:b=yes
+ }
+ 
+ onHit{
+ damageType:t="generic"
+ fire:r=0.1
+ damage:r=200.0
+ fHitCritical:b=yes
+ }
+ 
+ onHit{
+ damageType:t="fire"
+ fire:r=0.02
+ }
+ }
+ 
+ part{
+ name:t="wheel_r_drive_dm"
+ 
+ onKill{
+ track_r_dm:r=1.0
+ }
+ }
+ 
+ part{
+ name:t="wheel_r_back_dm"
+ 
+ onKill{
+ track_r_dm:r=1.0
+ }
+ }
+ 
+ part{
+ name:t="wheel_r_front_dm"
+ 
+ onKill{
+ track_r_dm:r=1.0
+ }
+ }
+ 
+ part{
+ name:t="wheel_l_drive_dm"
+ 
+ onKill{
+ track_l_dm:r=1.0
+ }
+ }
+ 
+ part{
+ name:t="wheel_l_back_dm"
+ 
+ onKill{
+ track_l_dm:r=1.0
+ }
+ }
+ 
+ part{
+ name:t="wheel_l_front_dm"
+ 
+ onKill{
+ track_l_dm:r=1.0
+ }
+ }
+ }
+ 
+ tank_crew{
+ changeTimeMult:r=1.0
+ 
+ gunner{
+ dmPart:t="gunner_dm"
+ role:t="tank_gunner"
+ substitute:t="commander"
+ substitute:t="loader"
+ }
+ 
+ driver{
+ dmPart:t="driver_dm"
+ role:t="driver"
+ substitute:t="commander"
+ substitute:t="loader"
+ }
+ 
+ loader{
+ dmPart:t="loader_dm"
+ role:t="loader"
+ substitute:t="commander"
+ }
+ 
+ commander{
+ dmPart:t="commander_dm"
+ role:t="tank_gunner"
+ role:t="commander"
+ }
+ }
+ 
+ MetaParts{
+ 
+ closed_fightning_compartment{
+ part:t="driver_dm"
+ part:t="loader_dm"
+ part:t="gunner_dm"
+ part:t="commander_dm"
+ part:t="machine_gunner_dm"
+ part:t="machine_gunner_01_dm"
+ part:t="machine_gunner_02_dm"
+ part:t="gunner_01_dm"
+ part:t="gunner_02_dm"
+ part:t="loader_01_dm"
+ part:t="loader_02_dm"
+ part:t="radio_station_dm"
+ part:t="drive_turret_v_dm"
+ part:t="drive_turret_h_dm"
+ part:t="drive_turret_v_01_dm"
+ part:t="drive_turret_h_01_dm"
+ part:t="drive_turret_v_02_dm"
+ part:t="drive_turret_h_02_dm"
+ part:t="ammo_turret_dm"
+ part:t="ammo_turret_01_dm"
+ part:t="ammo_turret_02_dm"
+ part:t="ammo_turret_03_dm"
+ part:t="ammo_turret_04_dm"
+ part:t="ammo_turret_05_dm"
+ part:t="ammo_turret_06_dm"
+ part:t="ammo_turret_07_dm"
+ part:t="ammo_turret_08_dm"
+ part:t="ammo_turret_09_dm"
+ part:t="ammo_turret_10_dm"
+ part:t="ammo_turret_11_dm"
+ part:t="ammo_turret_12_dm"
+ part:t="ammo_turret_13_dm"
+ part:t="ammo_turret_14_dm"
+ part:t="ammo_turret_15_dm"
+ part:t="ammo_turret_16_dm"
+ part:t="ammo_turret_17_dm"
+ part:t="ammo_turret_18_dm"
+ part:t="ammo_turret_19_dm"
+ part:t="ammo_turret_20_dm"
+ part:t="ammo_turret_21_dm"
+ part:t="ammo_turret_22_dm"
+ part:t="ammo_turret_23_dm"
+ part:t="ammo_turret_24_dm"
+ part:t="ammo_turret_25_dm"
+ part:t="ammo_turret_26_dm"
+ part:t="ammo_turret_27_dm"
+ part:t="ammo_turret_28_dm"
+ part:t="ammo_turret_29_dm"
+ part:t="ammo_turret_30_dm"
+ part:t="ammo_turret_31_dm"
+ part:t="ammo_turret_32_dm"
+ part:t="ammo_turret_33_dm"
+ part:t="ammo_turret_34_dm"
+ part:t="ammo_turret_35_dm"
+ part:t="ammo_turret_36_dm"
+ part:t="ammo_turret_37_dm"
+ part:t="ammo_turret_38_dm"
+ part:t="ammo_turret_39_dm"
+ part:t="ammo_turret_40_dm"
+ part:t="ammo_turret_41_dm"
+ part:t="ammo_turret_42_dm"
+ part:t="ammo_turret_43_dm"
+ part:t="ammo_turret_44_dm"
+ part:t="ammo_turret_45_dm"
+ part:t="ammo_turret_46_dm"
+ part:t="ammo_turret_47_dm"
+ part:t="ammo_turret_48_dm"
+ part:t="ammo_turret_49_dm"
+ part:t="ammo_turret_50_dm"
+ part:t="ammo_turret_51_dm"
+ part:t="ammo_turret_52_dm"
+ part:t="ammo_turret_53_dm"
+ part:t="ammo_turret_54_dm"
+ part:t="ammo_turret_55_dm"
+ part:t="ammo_body_01_dm"
+ part:t="ammo_body_02_dm"
+ part:t="ammo_body_03_dm"
+ part:t="ammo_body_04_dm"
+ part:t="ammo_body_05_dm"
+ part:t="ammo_body_06_dm"
+ part:t="ammo_body_07_dm"
+ part:t="ammo_body_08_dm"
+ part:t="ammo_body_09_dm"
+ part:t="ammo_body_10_dm"
+ part:t="ammo_body_11_dm"
+ part:t="ammo_body_12_dm"
+ part:t="ammo_body_13_dm"
+ part:t="ammo_body_14_dm"
+ part:t="ammo_body_15_dm"
+ part:t="ammo_body_16_dm"
+ part:t="ammo_body_17_dm"
+ part:t="ammo_body_18_dm"
+ part:t="ammo_body_19_dm"
+ part:t="ammo_body_20_dm"
+ part:t="ammo_body_21_dm"
+ part:t="ammo_body_22_dm"
+ part:t="ammo_body_23_dm"
+ part:t="ammo_body_24_dm"
+ part:t="ammo_body_25_dm"
+ part:t="ammo_body_26_dm"
+ part:t="ammo_body_27_dm"
+ part:t="ammo_body_28_dm"
+ part:t="ammo_body_29_dm"
+ part:t="ammo_body_30_dm"
+ part:t="ammo_body_31_dm"
+ part:t="ammo_body_32_dm"
+ part:t="ammo_body_33_dm"
+ part:t="ammo_body_34_dm"
+ part:t="ammo_body_35_dm"
+ part:t="ammo_body_36_dm"
+ part:t="ammo_body_37_dm"
+ part:t="ammo_body_38_dm"
+ part:t="ammo_body_39_dm"
+ part:t="ammo_body_40_dm"
+ part:t="ammo_body_41_dm"
+ part:t="ammo_body_42_dm"
+ part:t="ammo_body_43_dm"
+ part:t="ammo_body_44_dm"
+ part:t="ammo_body_45_dm"
+ part:t="ammo_body_46_dm"
+ part:t="ammo_body_47_dm"
+ part:t="ammo_body_48_dm"
+ part:t="ammo_body_49_dm"
+ part:t="ammo_body_50_dm"
+ part:t="ammo_body_51_dm"
+ part:t="ammo_body_52_dm"
+ part:t="ammo_body_53_dm"
+ part:t="ammo_body_54_dm"
+ part:t="ammo_body_55_dm"
+ part:t="ammo_body_l_01_dm"
+ part:t="ammo_body_l_02_dm"
+ part:t="ammo_body_l_03_dm"
+ part:t="ammo_body_l_04_dm"
+ part:t="ammo_body_l_05_dm"
+ part:t="ammo_body_l_06_dm"
+ part:t="ammo_body_l_07_dm"
+ part:t="ammo_body_l_08_dm"
+ part:t="ammo_body_l_09_dm"
+ part:t="ammo_body_l_10_dm"
+ part:t="ammo_body_l_11_dm"
+ part:t="ammo_body_l_12_dm"
+ part:t="ammo_body_l_13_dm"
+ part:t="ammo_body_l_14_dm"
+ part:t="ammo_body_l_15_dm"
+ part:t="ammo_body_l_16_dm"
+ part:t="ammo_body_l_17_dm"
+ part:t="ammo_body_l_18_dm"
+ part:t="ammo_body_l_19_dm"
+ part:t="ammo_body_l_20_dm"
+ part:t="ammo_body_r_01_dm"
+ part:t="ammo_body_r_02_dm"
+ part:t="ammo_body_r_03_dm"
+ part:t="ammo_body_r_04_dm"
+ part:t="ammo_body_r_05_dm"
+ part:t="ammo_body_r_06_dm"
+ part:t="ammo_body_r_07_dm"
+ part:t="ammo_body_r_08_dm"
+ part:t="ammo_body_r_09_dm"
+ part:t="ammo_body_r_10_dm"
+ part:t="ammo_body_r_11_dm"
+ part:t="ammo_body_r_12_dm"
+ part:t="ammo_body_r_13_dm"
+ part:t="ammo_body_r_14_dm"
+ part:t="ammo_body_r_15_dm"
+ part:t="ammo_body_r_16_dm"
+ part:t="ammo_body_r_17_dm"
+ part:t="ammo_body_r_18_dm"
+ part:t="ammo_body_r_19_dm"
+ part:t="ammo_body_r_20_dm"
+ 
+ effect{
+ conditionDamageType:t="explosion"
+ conditionDamage:r=1.0
+ pressure:b=yes
+ }
+ 
+ effect{
+ conditionDamageType:t="shatter"
+ conditionDamage:r=1.0
+ pressure:b=yes
+ }
+ }
+ }
+ 
+ attachables{
+ ex_armor_03_dm:b=no
+ }
+ 
+ gunConvergence{
+ updateFromRangefinder:b=yes
+ minDistance:r=200.0
+ defaultDistance:r=1000.0
+ vertical:b=yes
+ horizontal:b=yes
+ }
+ 
+ fuelTanks{
+ 
+ r1{
+ part:t="fuel_tank_exterior_r_01_dm"
+ external:b=yes
+ }
+ 
+ r2{
+ part:t="fuel_tank_exterior_r_02_dm"
+ external:b=yes
+ }
+ 
+ r3{
+ part:t="fuel_tank_exterior_r_03_dm"
+ external:b=yes
+ }
+ 
+ r4{
+ part:t="fuel_tank_exterior_r_04_dm"
+ external:b=yes
+ }
+ 
+ l1{
+ part:t="fuel_tank_exterior_l_01_dm"
+ external:b=yes
+ }
+ 
+ l2{
+ part:t="fuel_tank_exterior_l_02_dm"
+ external:b=yes
+ }
+ 
+ l3{
+ part:t="fuel_tank_exterior_l_03_dm"
+ external:b=yes
+ }
+ 
+ l4{
+ part:t="fuel_tank_exterior_l_04_dm"
+ external:b=yes
+ }
+ }
+ 
+ xray_viewer_data{
+ 
+ armorArrayHullFront{
+ xrayDmPart:t="composite_armor_hull_01_dm"
+ 
+ armorArrayText{
+ 
+ layer{
+ dmPart:t="superstructure_front_dm"
+ }
+ 
+ layer{
+ dmPart:t="composite_armor_hull_01_dm"
+ }
+ 
+ layer{
+ dmPart:t="turret_05_back_dm"
+ }
+ }
+ }
+ 
+ armorArrayTurretFrontMask{
+ xrayDmPart:t="composite_armor_turret_03_dm"
+ titleLoc:t="tank_structural_steel"
+ 
+ armorArrayText{
+ 
+ layer{
+ dmPart:t="composite_armor_turret_03_dm"
+ }
+ }
+ }
+ 
+ armorArrayTurretFrontTop{
+ xrayDmPart:t="composite_armor_turret_06_dm"
+ titleLoc:t="CHA_tank_modern"
+ 
+ armorArrayText{
+ 
+ layer{
+ dmPart:t="gun_mask_04_dm"
+ xrayTextThickness:p2=50.0, 250.0
+ }
+ }
+ }
+ 
+ armorArrayHullSideInner{
+ xrayDmPart:t="composite_armor_hull_03_dm"
+ titleLoc:t="RHA_tank_modern"
+ 
+ armorArrayText{
+ 
+ layer{
+ dmPart:t="turret_06_back_dm"
+ }
+ }
+ }
+ 
+ armorArrayHullSideIn{
+ xrayDmPart:t="composite_armor_hull_06_dm"
+ titleLoc:t="tank_structural_steel"
+ 
+ armorArrayText{
+ 
+ layer{
+ dmPart:t="composite_armor_hull_06_dm"
+ }
+ }
+ }
+ 
+ armorArrayHullSideIn{
+ xrayDmPart:t="composite_armor_hull_07_dm"
+ titleLoc:t="tank_structural_steel"
+ 
+ armorArrayText{
+ 
+ layer{
+ dmPart:t="composite_armor_hull_07_dm"
+ }
+ }
+ }
+ 
+ armorArrayHullSideIn{
+ xrayDmPart:t="composite_armor_hull_08_dm"
+ titleLoc:t="RHA_tank_modern"
+ 
+ armorArrayText{
+ 
+ layer{
+ dmPart:t="composite_armor_hull_08_dm"
+ }
+ }
+ }
+ 
+ armorArrayTurretFront{
+ xrayDmPart:t="composite_armor_turret_02_dm"
+ 
+ armorArrayText{
+ 
+ layer{
+ dmPart:t="turret_03_bottom_dm"
+ }
+ 
+ layer{
+ dmPart:t="composite_armor_turret_02_dm"
+ }
+ 
+ layer{
+ dmPart:t="gun_mask_02_dm"
+ }
+ }
+ }
+ 
+ armorArrayTurretSide{
+ xrayDmPart:t="composite_armor_turret_09_dm"
+ 
+ armorArrayText{
+ 
+ layer{
+ dmPart:t="turret_03_bottom_dm"
+ }
+ 
+ layer{
+ dmPart:t="composite_armor_turret_09_dm"
+ }
+ }
+ }
+ 
+ armorArrayTurretSideL01{
+ xrayDmPart:t="composite_armor_turret_04_dm"
+ 
+ armorArrayText{
+ 
+ layer{
+ dmPart:t="composite_armor_turret_04_dm"
+ }
+ }
+ }
+ 
+ armorArrayTurretSideL01{
+ xrayDmPart:t="composite_armor_turret_07_dm"
+ 
+ armorArrayText{
+ 
+ layer{
+ dmPart:t="composite_armor_turret_07_dm"
+ }
+ }
+ }
+ 
+ armorArrayTurretSideL02{
+ xrayDmPart:t="composite_armor_turret_05_dm"
+ 
+ armorArrayText{
+ 
+ layer{
+ dmPart:t="composite_armor_turret_05_dm"
+ }
+ }
+ }
+ 
+ armorArrayTurretSideL02{
+ xrayDmPart:t="composite_armor_turret_08_dm"
+ 
+ armorArrayText{
+ 
+ layer{
+ dmPart:t="composite_armor_turret_08_dm"
+ }
+ }
+ }
+ 
+ armorArrayTurretSideR{
+ xrayDmPart:t="composite_armor_turret_03_dm"
+ 
+ armorArrayText{
+ 
+ layer{
+ dmPart:t="turret_04_back_dm"
+ }
+ 
+ layer{
+ dmPart:t="composite_armor_turret_03_dm"
+ }
+ 
+ layer{
+ dmPart:t="gun_mask_dm"
+ xrayTextThickness:r=60.0
+ }
+ }
+ }
+ }
+ 
+ sound{
+ EngineName:t="engine_challenger"
+ TrackSoundPath:t="tanks/engines_tanks"
+ TrackSoundPathStudio:t="ground/engines"
+ TrackSoundName:t="tracks_mbt"
+ TrackSoundNameCockpit:t="tracks_mbt_interior"
+ EngineNameAi:t="engine_tank_ai_middle"
+ TrackSoundNameAi:t="tracks_ai_mbt"
+ turret_turn:t="turret_turn_servo"
+ }
+ 
+ class_tags{
+ }
+ 
+ commonWeapons{
+ 
+ Weapon{
+ trigger:t="gunner0"
+ blk:t="gameData/Weapons/groundModels_weapons/120mm_L11A5_user_cannon.blk"
+ shotFreq:r=0.2
+ emitter:t="bone_gun_barrel"
+ flash:t="emtr_gun_flame"
+ defaultYaw:r=0.0
+ defaultPitch:r=0.0
+ barrelDP:t="gun_barrel_dm"
+ breechDP:t="cannon_breech_dm"
+ speedYaw:r=31.0
+ speedPitch:r=22.5
+ fireConeAngle:r=1.0
+ bullets:i=52
+ salvoAmount:r=100.0
+ ChainfireTime:r=0.0
+ DelayAfterShoot:r=5.0
+ AttackMaxDistance:r=1000.0
+ AttackMaxRadius:r=1000.0
+ AttackMaxHeight:r=1000.0
+ accuracyAir:r=0.0
+ accuracyGnd:r=1.5
+ errMeasureVel:r=0.0
+ errMeasureVelFast:r=0.0
+ errMeasureVelFwdShift:r=0.0
+ errMeasureVelDir:r=0.0
+ errTargettingOn100kmph:r=0.0
+ errTargetting:r=3.0
+ errExplTime:r=0.0
+ 
+ turret{
+ head:t="bone_turret"
+ gun:t="bone_gun"
+ barrel:t="bone_gun_barrel"
+ gunnerDm:t="gunner_dm"
+ secondGunnerDm:t="commander_dm"
+ 
+ linkedAnimPart{
+ verNode:t="bone_camera_gunner"
+ verLimits:p2=-10.0, 20.0
+ verOriginLimits:p2=-10.0, 20.0
+ }
+ 
+ linkedAnimPart{
+ verNode:t="bone_roll_03"
+ verLimits:p2=-10.0, 5.0
+ verOriginLimits:p2=-10.0, 5.0
+ }
+ }
+ 
+ limits{
+ yaw:p2=-180.0, 180.0
+ pitch:p2=-10.0, 20.0
+ }
+ 
+ limitsTable{
+ lim1:p4=-180.0, -140.0, 2.0, 20.0
+ lim2:p4=-140.0, -120.0, -1.0, 20.0
+ lim3:p4=-120.0, 120.0, -10.0, 20.0
+ lim4:p4=120.0, 140.0, -1.0, 20.0
+ lim5:p4=140.0, 180.0, 2.0, 20.0
+ }
+ 
+ gunStabilizer{
+ hasVerticalGunFreeMode:b=no
+ hasHorizontal:b=yes
+ horizontalOmegaMult:r=1.0
+ horizontalSpeedLimitKPH:r=75.0
+ hasVertical:b=yes
+ verticalOmegaMult:r=1.0
+ verticalSpeedLimitKPH:r=75.0
+ speedFromVehicleVerticalMult:r=-1.0
+ 
+ errorKPHToDegrees{
+ row:p2=5.0, 0.0
+ row:p2=45.0, 0.015
+ row:p2=80.0, 0.02
+ }
+ }
+ }
+ 
+ Weapon{
+ trigger:t="gunner1"
+ triggerGroup:t="coaxial"
+ blk:t="gameData/Weapons/groundModels_weapons/7_62mm_L8A2_user_machinegun.blk"
+ emitter:t="bone_mg_gun_twin"
+ flash:t="emtr_mg_flame_01"
+ barrelDP:t="gun_barrel_03_dm"
+ barrelDP:t="gun_barrel_01_dm"
+ defaultYaw:r=0.0
+ defaultPitch:r=0.0
+ speedYaw:r=5.5
+ speedPitch:r=4.0
+ fireConeAngle:r=1.0
+ fireConeAngle:r=15.0
+ bullets:i=2400
+ ChainfireTime:r=3.0
+ DelayAfterShoot:r=3.0
+ accuracyAir:r=0.0
+ accuracyGnd:r=0.0
+ errMeasureVel:r=0.0
+ errMeasureVelFast:r=0.0
+ errMeasureVelFwdShift:r=0.0
+ errMeasureVelDir:r=0.0
+ errTargettingOn100kmph:r=0.0
+ errTargetting:r=3.0
+ errExplTime:r=0.0
+ 
+ turret{
+ head:t="bone_mg_gun_twin"
+ gun:t="bone_mg_gun_twin"
+ gunnerDm:t="gunner_dm"
+ secondGunnerDm:t="commander_dm"
+ }
+ 
+ limits{
+ yaw:p2=-0.0, 0.0
+ pitch:p2=-0.0, 0.0
+ }
+ }
+ 
+ Weapon{
+ trigger:t="gunner2"
+ triggerGroup:t="machinegun"
+ blk:t="gameData/Weapons/groundModels_weapons/7_62mm_L37A2_user_machinegun.blk"
+ emitter:t="bone_mg_aa_v_01"
+ flash:t="emtr_mg_flame_02"
+ barrelDP:t="gun_barrel_02_dm"
+ defaultYaw:r=0.0
+ defaultPitch:r=0.0
+ parkInDeadzone:b=no
+ speedYaw:r=90.0
+ speedPitch:r=90.0
+ bullets:i=3600
+ isBulletBelt:b=yes
+ fireConeAngle:r=5.0
+ ChainfireTime:r=0.5
+ DelayAfterShoot:r=2.0
+ accuracyAir:r=1.5
+ accuracyGnd:r=0.0
+ errMeasureVel:r=0.0
+ errMeasureVelFast:r=0.0
+ errMeasureVelFwdShift:r=1.5
+ errMeasureVelDir:r=0.0
+ errTargettingOn100kmph:r=0.0
+ errTargetting:r=3.0
+ errExplTime:r=0.0
+ forestallTime:r=0.1
+ 
+ turret{
+ head:t="bone_mg_aa_h_01"
+ gun:t="bone_mg_aa_v_01"
+ gunnerDm:t="commander_dm"
+ rotatedTurret:t="bone_mg_aa_h_01"
+ hasNightVision:b=no
+ }
+ 
+ limits{
+ yaw:p2=-180.0, 180.0
+ pitch:p2=-10.0, 50.0
+ }
+ }
+ 
+ Weapon{
+ trigger:t="gunner3"
+ triggerGroup:t="commander"
+ blk:t="gameData/Weapons/dummy_weapon.blk"
+ emitter:t="bone_commander_sight_v"
+ defaultYaw:r=0.0
+ defaultPitch:r=0.0
+ parkInDeadzone:b=no
+ speedYaw:r=90.0
+ speedPitch:r=90.0
+ 
+ limits{
+ yaw:p2=-180.0, 180.0
+ pitch:p2=-5.0, 10.0
+ }
+ 
+ turret{
+ head:t="bone_mg_aa_h_01"
+ gun:t="bone_commander_sight_v"
+ gunnerDm:t="commander_dm"
+ verDriveDm:t="commander_panoramic_sight_dm"
+ horDriveDm:t="commander_panoramic_sight_dm"
+ rotatedTurret:t="bone_mg_aa_h_01"
+ }
+ }
+ }
+ 
+ weapon_presets{
+ 
+ preset{
+ name:t="uk_shir_2_default"
+ blk:t="gameData/units/tankModels/weaponPresets/uk_shir_2_default.blk"
+ }
+ }
+ 
+ VehiclePhys{
+ 
+ Mass{
+ Empty:r=61500.0
+ Fuel:r=1000.0
+ TakeOff:r=62500.0
+ momentOfInertia:p3=4.0, 5.0, 6.0
+ CenterOfGravity:p3=0.0, 0.5, 0.0
+ AdvancedMass:b=no
+ trackMass:r=3000.0
+ CenterOfGravityClampY:p2=0.0, 0.5
+ }
+ 
+ tracks{
+ animationMultiplier:r=0.62
+ width:r=0.61
+ height:r=0.06
+ fricFrontal:p2=1.0, 0.8
+ tracksTensionK:p3=5.0, 9.0, 5.0
+ trackMesh:t="uk_challenger_1_phys_track_line"
+ trackLen:r=0.167
+ trackCount:i=94
+ trackFadeTime:r=1.5
+ trackEmitSparks:b=no
+ trackStartOffset:r=0.06
+ }
+ 
+ collisionProps{
+ cls_turret:t="convex_hull"
+ cls_body:t="convex_hull"
+ }
+ 
+ engine{
+ horsePowers:r=1217.0
+ maxRPM:r=2300.0
+ minRPM:r=660.0
+ }
+ 
+ mechanics{
+ steerType:t="clutch_braking"
+ maxBrakeForce:r=280000.0
+ driveGearRadius:r=0.299
+ mainGearRatio:r=4.3
+ sideGearRatio:r=1.0
+ neutralGearRatio:r=15.0
+ 
+ gearRatios{
+ ratio:r=-1.65
+ ratio:r=-2.0
+ ratio:r=-2.63
+ ratio:r=-3.27
+ ratio:r=-4.11
+ ratio:r=-10.0
+ ratio:r=0.0
+ ratio:r=10.0
+ ratio:r=4.11
+ ratio:r=3.27
+ ratio:r=2.43
+ ratio:r=2.0
+ ratio:r=1.57
+ ratio:r=1.27
+ ratio:r=1.08
+ }
+ }
+ 
+ suspension{
+ suspensionOffsets:p3=-0.159, -0.15, 0.082
+ defaultGearRadius:r=0.39
+ topGearRadius:r=0.12
+ frontBackGearRadius:r=0.3
+ defaultDampeningForce:p2=170000.0, 170000.0
+ dampeningRelaxationRatio:r=0.4
+ dampeningCompressionRatio:r=0.15
+ wheel_r_drive:r=0.32
+ wheel_l_drive:r=0.32
+ wheel_r_front:r=0.32
+ wheel_l_front:r=0.32
+ }
+ }
+ 
+ PhysSys{
+ find:t="^bone_suspension_(._dd)$"
+ 
+ points{
+ 
+ suspension{
+ name:t="bone_suspension_$1"
+ }
+ 
+ wheel{
+ name:t="bone_wheel_$1"
+ limitMin:p3=-1.0, -1.0, 0.0
+ limitMax:p3=1.0, 1.0, 0.0
+ }
+ }
+ 
+ constraints{
+ 
+ edge{
+ from:t="suspension"
+ to:t="wheel"
+ }
+ }
+ }
+ 
+ trackEffects{
+ top:b=no
+ }
+ 
+ ammo{
+ combustionTime:r=7.0
+ detonateProb:r=0.5
+ detonatePortion:p2=0.5, 0.9
+ explodeHitPower:r=5000.0
+ hitPowerMult:r=1.0
+ nearHitPower:p2=1.0, 50.0
+ midHitPower:p2=0.9, 400.0
+ farHitPower:p2=0.1, 1000.0
+ endHitPower:p2=0.01, 1500.0
+ relativeVelHitShift:p2=300.0, 1000.0
+ nearArmorPower:p2=10.0, 50.0
+ midArmorPower:p2=7.0, 400.0
+ farArmorPower:p2=0.2, 700.0
+ relativeVelArmorShift:p2=200.0, 1000.0
+ explodeTreshold:r=0.0001
+ explodeArmorPower:r=30.0
+ explodeRadius:p2=1.5, 10.0
+ }
+ 
+ wreckedParts{
+ 
+ part{
+ node:t="bone_turret"
+ mass:r=17000.0
+ cutDamage:r=1700.0
+ deviation:r=0.4
+ rotation:r=1.5
+ collisionNode:t="cls_turret"
+ }
+ }
+ 
+ unitFx{
+ 
+ event{
+ lifetime:r=120.0
+ name:t="engine_fire"
+ 
+ fx{
+ name:t="tank_engine_fire"
+ emitter:t="emtr_fire_engine"
+ }
+ 
+ fx{
+ name:t="tank_engine_fire"
+ emitter:t="emtr_fire_engine_01"
+ }
+ 
+ fx{
+ name:t="tank_engine_fire"
+ emitter:t="emtr_fire_engine_02"
+ }
+ }
+ 
+ event{
+ name:t="ammo_fire"
+ lifetime:r=9.0
+ 
+ fx{
+ name:t="tank_ammo_fire"
+ emitter:t="emtr_fire_ammo"
+ useVelocity:b=no
+ }
+ 
+ fx{
+ name:t="tank_ammo_fire"
+ emitter:t="emtr_fire_ammo_01"
+ useVelocity:b=no
+ }
+ 
+ fx{
+ name:t="tank_ammo_fire"
+ emitter:t="emtr_fire_ammo_02"
+ useVelocity:b=no
+ }
+ 
+ fx{
+ name:t="tank_ammo_fire"
+ emitter:t="emtr_fire_ammo_03"
+ useVelocity:b=no
+ }
+ 
+ fx{
+ name:t="tank_ammo_fire"
+ emitter:t="emtr_fire_ammo_04"
+ useVelocity:b=no
+ }
+ 
+ fx{
+ name:t="tank_ammo_fire"
+ emitter:t="emtr_fire_ammo_05"
+ useVelocity:b=no
+ }
+ 
+ fx{
+ name:t="tank_ammo_fire"
+ emitter:t="emtr_fire_ammo_06"
+ useVelocity:b=no
+ }
+ 
+ fx{
+ name:t="tank_ammo_fire"
+ emitter:t="emtr_fire_ammo_07"
+ useVelocity:b=no
+ }
+ 
+ fx{
+ name:t="tank_ammo_fire"
+ emitter:t="emtr_fire_ammo_08"
+ useVelocity:b=no
+ }
+ 
+ fx{
+ name:t="tank_ammo_fire"
+ emitter:t="emtr_fire_ammo_09"
+ useVelocity:b=no
+ }
+ 
+ fx{
+ name:t="tank_ammo_fire"
+ emitter:t="emtr_fire_ammo_10"
+ useVelocity:b=no
+ }
+ 
+ fx{
+ name:t="fire_tank_ammo_gun_fire"
+ emitter:t="emtr_gun_flame"
+ setOrientation:b=yes
+ }
+ }
+ 
+ event{
+ name:t="light_smoke"
+ lifetime:r=60.0
+ 
+ fx{
+ name:t="tank_smoke_small"
+ emitter:t="emtr_fire_ammo"
+ }
+ 
+ fx{
+ name:t="tank_smoke_small"
+ emitter:t="emtr_fire_ammo_01"
+ }
+ 
+ fx{
+ name:t="tank_smoke_small"
+ emitter:t="emtr_fire_ammo_02"
+ }
+ }
+ 
+ event{
+ name:t="total_smoke"
+ lifetime:r=60.0
+ 
+ fx{
+ name:t="tank_smoke_big"
+ emitter:t="emtr_smoke_dmg"
+ }
+ 
+ fx{
+ name:t="tank_smoke_small"
+ emitter:t="emtr_smoke_small_dmg_01"
+ }
+ 
+ fx{
+ name:t="tank_smoke_small"
+ emitter:t="emtr_smoke_small_dmg_02"
+ }
+ 
+ fx{
+ name:t="tank_smoke_small"
+ emitter:t="emtr_smoke_small_dmg_03"
+ }
+ 
+ fx{
+ name:t="tank_smoke_small"
+ emitter:t="emtr_smoke_small_dmg_04"
+ }
+ 
+ fx{
+ name:t="tank_smoke_small"
+ emitter:t="emtr_smoke_small_dmg_05"
+ }
+ 
+ fx{
+ name:t="tank_smoke_small"
+ emitter:t="emtr_smoke_small_dmg_06"
+ }
+ 
+ fx{
+ name:t="tank_smoke_small"
+ emitter:t="emtr_smoke_small_dmg_07"
+ }
+ 
+ fx{
+ name:t="tank_smoke_small"
+ emitter:t="emtr_smoke_small_dmg_08"
+ }
+ 
+ fx{
+ name:t="tank_smoke_small"
+ emitter:t="emtr_smoke_small_dmg_09"
+ }
+ 
+ fx{
+ name:t="tank_smoke_small"
+ emitter:t="emtr_smoke_small_dmg_10"
+ }
+ 
+ fx{
+ name:t="tank_smoke_small"
+ emitter:t="emtr_smoke_small_dmg_11"
+ }
+ 
+ fx{
+ name:t="tank_smoke_small"
+ emitter:t="emtr_smoke_small_dmg_12"
+ }
+ 
+ fx{
+ name:t="tank_smoke_small"
+ emitter:t="emtr_smoke_small_dmg_13"
+ }
+ 
+ fx{
+ name:t="tank_smoke_small"
+ emitter:t="emtr_smoke_small_dmg_14"
+ }
+ 
+ fx{
+ name:t="tank_smoke_small"
+ emitter:t="emtr_smoke_small_dmg_15"
+ }
+ 
+ fx{
+ name:t="tank_smoke_small"
+ emitter:t="emtr_smoke_small_dmg_16"
+ }
+ }
+ 
+ event{
+ name:t="total_fire"
+ lifetime:r=40.0
+ 
+ fx{
+ name:t="tank_fire_big"
+ emitter:t="emtr_fire_dmg"
+ }
+ 
+ fx{
+ name:t="tank_fire_small"
+ emitter:t="emtr_fire_small_dmg_01"
+ }
+ 
+ fx{
+ name:t="tank_fire_small"
+ emitter:t="emtr_fire_small_dmg_02"
+ }
+ 
+ fx{
+ name:t="tank_fire_small"
+ emitter:t="emtr_fire_small_dmg_03"
+ }
+ 
+ fx{
+ name:t="tank_fire_small"
+ emitter:t="emtr_fire_small_dmg_04"
+ }
+ 
+ fx{
+ name:t="tank_fire_small"
+ emitter:t="emtr_fire_small_dmg_05"
+ }
+ 
+ fx{
+ name:t="tank_fire_small"
+ emitter:t="emtr_fire_small_dmg_06"
+ }
+ 
+ fx{
+ name:t="tank_fire_small"
+ emitter:t="emtr_fire_small_dmg_07"
+ }
+ 
+ fx{
+ name:t="tank_fire_small"
+ emitter:t="emtr_fire_small_dmg_08"
+ }
+ 
+ fx{
+ name:t="tank_fire_small"
+ emitter:t="emtr_fire_small_dmg_09"
+ }
+ 
+ fx{
+ name:t="tank_fire_small"
+ emitter:t="emtr_fire_small_dmg_10"
+ }
+ 
+ fx{
+ name:t="tank_fire_small"
+ emitter:t="emtr_fire_small_dmg_11"
+ }
+ 
+ fx{
+ name:t="tank_fire_small"
+ emitter:t="emtr_fire_small_dmg_12"
+ }
+ 
+ fx{
+ name:t="tank_fire_small"
+ emitter:t="emtr_fire_small_dmg_13"
+ }
+ 
+ fx{
+ name:t="tank_fire_small"
+ emitter:t="emtr_fire_small_dmg_14"
+ }
+ 
+ fx{
+ name:t="tank_fire_small"
+ emitter:t="emtr_fire_small_dmg_15"
+ }
+ 
+ fx{
+ name:t="tank_fire_small"
+ emitter:t="emtr_fire_small_dmg_16"
+ }
+ }
+ 
+ event{
+ name:t="attached_fire"
+ lifetime:r=15.0
+ 
+ fx{
+ name:t="fire_tank_napalm_smal"
+ emitter:t="emtr_fire_dmg"
+ }
+ 
+ fx{
+ name:t="fire_tank_napalm_smal"
+ emitter:t="emtr_fire_small_dmg_01"
+ }
+ 
+ fx{
+ name:t="fire_tank_napalm_smal"
+ emitter:t="emtr_fire_small_dmg_02"
+ }
+ 
+ fx{
+ name:t="fire_tank_napalm_smal"
+ emitter:t="emtr_fire_small_dmg_03"
+ }
+ 
+ fx{
+ name:t="fire_tank_napalm_smal"
+ emitter:t="emtr_fire_small_dmg_04"
+ }
+ 
+ fx{
+ name:t="fire_tank_napalm_smal"
+ emitter:t="emtr_fire_small_dmg_05"
+ }
+ 
+ fx{
+ name:t="fire_tank_napalm_smal"
+ emitter:t="emtr_fire_small_dmg_06"
+ }
+ 
+ fx{
+ name:t="fire_tank_napalm_smal"
+ emitter:t="emtr_fire_small_dmg_07"
+ }
+ 
+ fx{
+ name:t="fire_tank_napalm_smal"
+ emitter:t="emtr_fire_small_dmg_08"
+ }
+ 
+ fx{
+ name:t="fire_tank_napalm_smal"
+ emitter:t="emtr_fire_small_dmg_09"
+ }
+ 
+ fx{
+ name:t="fire_tank_napalm_smal"
+ emitter:t="emtr_fire_small_dmg_10"
+ }
+ 
+ fx{
+ name:t="fire_tank_napalm_smal"
+ emitter:t="emtr_fire_small_dmg_11"
+ }
+ 
+ fx{
+ name:t="fire_tank_napalm_smal"
+ emitter:t="emtr_fire_small_dmg_12"
+ }
+ 
+ fx{
+ name:t="fire_tank_napalm_smal"
+ emitter:t="emtr_fire_small_dmg_13"
+ }
+ 
+ fx{
+ name:t="fire_tank_napalm_smal"
+ emitter:t="emtr_fire_small_dmg_14"
+ }
+ 
+ fx{
+ name:t="fire_tank_napalm_smal"
+ emitter:t="emtr_fire_small_dmg_15"
+ }
+ 
+ fx{
+ name:t="fire_tank_napalm_smal"
+ emitter:t="emtr_fire_small_dmg_16"
+ }
+ }
+ 
+ event{
+ name:t="fuel_exterior"
+ lifetime:r=50.0
+ 
+ fx{
+ name:t="tank_ex_fuel_explosion"
+ centerDmgPart:b=yes
+ }
+ }
+ 
+ event{
+ name:t="fuel_internal"
+ lifetime:r=50.0
+ 
+ fx{
+ name:t="tank_ex_fuel_explosion"
+ centerDmgPart:b=yes
+ }
+ }
+ 
+ event{
+ name:t="hydraulic_internal"
+ lifetime:r=30.0
+ 
+ fx{
+ name:t="tank_ex_fuel_explosion"
+ centerDmgPart:b=yes
+ }
+ }
+ 
+ event{
+ name:t="powersystem_internal"
+ lifetime:r=30.0
+ 
+ fx{
+ name:t="tank_ex_fuel_explosion"
+ centerDmgPart:b=yes
+ }
+ }
+ 
+ event{
+ name:t="powersystem_exterior"
+ lifetime:r=30.0
+ 
+ fx{
+ name:t="tank_ex_fuel_explosion"
+ centerDmgPart:b=yes
+ }
+ }
+ 
+ event{
+ name:t="big_bang"
+ lifetime:r=20.0
+ 
+ fx{
+ name:t="tank_explosion"
+ emitter:t="emtr_explosion_center"
+ }
+ 
+ fx{
+ extraFx:t="fuelLeakFx"
+ emitter:t="emtr_explosion_center"
+ }
+ 
+ wreckages{
+ count:i=8
+ speed:r=20.0
+ angle:r=35.0
+ fxName:t="fire_trails_explosion_smal"
+ }
+ }
+ 
+ event{
+ name:t="big_bang"
+ lifetime:r=20.0
+ 
+ fx{
+ name:t="tank_explosion"
+ emitter:t="emtr_explosion_center"
+ }
+ 
+ fx{
+ extraFx:t="fuelLeakFx"
+ emitter:t="emtr_explosion_center"
+ }
+ 
+ wreckages{
+ count:i=10
+ speed:r=20.0
+ angle:r=35.0
+ fxName:t="fire_trails_explosion_smal"
+ }
+ }
+ 
+ event{
+ name:t="big_bang"
+ lifetime:r=20.0
+ 
+ fx{
+ name:t="tank_explosion_small"
+ emitter:t="emtr_explosion_center"
+ }
+ 
+ wreckages{
+ count:i=10
+ speed:r=13.0
+ angle:r=35.0
+ fxName:t="fire_trails_explosion_smal"
+ }
+ }
+ 
+ event{
+ name:t="big_bang"
+ lifetime:r=20.0
+ 
+ fx{
+ name:t="tank_explosion_ammo"
+ emitter:t="emtr_explosion_center"
+ }
+ 
+ fx{
+ extraFx:t="fuelLeakFx"
+ emitter:t="emtr_explosion_center"
+ }
+ 
+ wreckages{
+ count:i=12
+ speed:r=25.0
+ angle:r=35.0
+ fxName:t="fire_trails_explosion_med"
+ }
+ }
+ 
+ event{
+ name:t="big_bang"
+ lifetime:r=20.0
+ 
+ fx{
+ name:t="tank_explosion_ammo_small"
+ emitter:t="emtr_explosion_center"
+ }
+ 
+ fx{
+ extraFx:t="fuelLeakFx"
+ emitter:t="emtr_explosion_center"
+ }
+ 
+ wreckages{
+ count:i=14
+ speed:r=20.0
+ angle:r=35.0
+ fxName:t="fire_trails_explosion_smal"
+ }
+ }
+ 
+ event{
+ name:t="full_expl"
+ lifetime:r=20.0
+ 
+ fx{
+ name:t="explosion_ship_big"
+ emitter:t="emtr_explosion_center"
+ }
+ 
+ wreckages{
+ count:i=15
+ speed:r=30.0
+ angle:r=40.0
+ fxName:t="fire_trails_explosion_med"
+ }
+ }
+ 
+ event{
+ name:t="fire_after_hit_big"
+ lifetime:r=8.0
+ 
+ fx{
+ name:t="fire_after_hit_big"
+ setOrientation:b=yes
+ }
+ }
+ 
+ event{
+ name:t="fire_after_hit_big"
+ lifetime:r=8.0
+ 
+ fx{
+ name:t="smoke_after_hit_big"
+ setOrientation:b=yes
+ }
+ }
+ 
+ event{
+ name:t="fire_after_hit_med"
+ lifetime:r=8.0
+ 
+ fx{
+ name:t="fire_after_hit_med"
+ setOrientation:b=yes
+ }
+ }
+ 
+ event{
+ name:t="fire_after_hit_med"
+ lifetime:r=8.0
+ 
+ fx{
+ name:t="smoke_after_hit_med"
+ setOrientation:b=yes
+ }
+ }
+ 
+ event{
+ name:t="fire_after_hit_small"
+ lifetime:r=5.0
+ 
+ fx{
+ name:t="fire_after_hit_small"
+ setOrientation:b=yes
+ }
+ }
+ 
+ event{
+ name:t="fire_after_hit_small"
+ lifetime:r=5.0
+ 
+ fx{
+ name:t="smoke_after_hit_small"
+ setOrientation:b=yes
+ }
+ }
+ 
+ event{
+ name:t="fire_after_hit_tiny"
+ lifetime:r=5.0
+ 
+ fx{
+ name:t="fire_after_hit_tiny"
+ setOrientation:b=yes
+ }
+ }
+ 
+ event{
+ name:t="fire_after_hit_tiny"
+ lifetime:r=5.0
+ 
+ fx{
+ name:t="smoke_after_hit_tiny"
+ setOrientation:b=yes
+ }
+ }
+ 
+ event{
+ name:t="engine_overheat"
+ lifetime:r=5.0
+ 
+ fx{
+ name:t="tank_radiator_steam"
+ centerDmgPart:b=no
+ }
+ }
+ 
+ procedural{
+ name:t="default"
+ 
+ fx{
+ name:t="tank_engine_fire"
+ }
+ }
+ }
+ 
+ commanderView{
+ aimModeAvailable:b=yes
+ optics:t="commander_optics_square"
+ zoomOutFov:r=80.0
+ zoomInFov:r=7.37
+ sightSize:p2=1.775, 1.25
+ }
+ 
+ cockpit{
+ zoomOutFov:r=18.5
+ zoomInFov:r=6.4
+ sightFov:r=5.2
+ sightName:t="tls_no_10_mk1"
+ headPos:p3=0.0, 4.2, -9.0
+ headPosOnShooting:p3=-0.7, 3.5, 0.64
+ detectionHeight:r=2.5
+ bone_turret:t="bone_mg_aa_h_01"
+ }
+ 
+ modifications{
+ 
+ new_tank_tracks{
+ }
+ 
+ new_tank_suspension{
+ }
+ 
+ new_tank_filter{
+ }
+ 
+ new_tank_brakes{
+ }
+ 
+ new_tank_transmission{
+ }
+ 
+ new_tank_engine{
+ }
+ 
+ tank_camouflage{
+ }
+ 
+ tank_additional_armor{
+ }
+ 
+ manual_extinguisher{
+ }
+ 
+ tank_tool_kit{
+ }
+ 
+ new_tank_horizontal_aiming{
+ }
+ 
+ new_tank_vertical_aiming{
+ }
+ 
+ tank_new_gun{
+ }
+ 
+ tank_medical_kit{
+ image:t="#ui/gameuiskin#tank_reinforcement_uk"
+ }
+ 
+ tank_medical_kit_expendable{
+ image:t="#ui/gameuiskin#tank_reinforcement_uk"
+ }
+ 
+ modern_tank_laser_rangefinder{
+ }
+ 
+ 120mm_britain_L37A7_HESH{
+ }
+ 
+ 120mm_britain_L23_APDSFS{
+ }
+ 
+ 120mm_britain_L23_APDSFS_ammo_pack{
+ tier:i=3
+ }
+ 
+ 120mm_britain_Smoke{
+ }
+ 
+ 120mm_britain_Smoke_ammo_pack{
+ tier:i=1
+ }
+ 
+ art_support{
+ }
+ 
+ tank_smoke_screen_system_mod{
+ tier:i=4
+ modClass:t="protection"
+ 
+ effects{
+ 
+ commonWeapons{
+ 
+ Weapon{
+ trigger:t="gunner0"
+ blk:t="gameData/Weapons/groundModels_weapons/120mm_L11A5_user_cannon.blk"
+ shotFreq:r=0.2
+ emitter:t="bone_gun_barrel"
+ flash:t="emtr_gun_flame"
+ defaultYaw:r=0.0
+ defaultPitch:r=0.0
+ barrelDP:t="gun_barrel_dm"
+ breechDP:t="cannon_breech_dm"
+ speedYaw:r=31.0
+ speedPitch:r=22.5
+ fireConeAngle:r=1.0
+ bullets:i=52
+ salvoAmount:r=100.0
+ ChainfireTime:r=0.0
+ DelayAfterShoot:r=5.0
+ AttackMaxDistance:r=1000.0
+ AttackMaxRadius:r=1000.0
+ AttackMaxHeight:r=1000.0
+ accuracyAir:r=0.0
+ accuracyGnd:r=1.5
+ errMeasureVel:r=0.0
+ errMeasureVelFast:r=0.0
+ errMeasureVelFwdShift:r=0.0
+ errMeasureVelDir:r=0.0
+ errTargettingOn100kmph:r=0.0
+ errTargetting:r=3.0
+ errExplTime:r=0.0
+ 
+ turret{
+ head:t="bone_turret"
+ gun:t="bone_gun"
+ barrel:t="bone_gun_barrel"
+ gunnerDm:t="gunner_dm"
+ secondGunnerDm:t="commander_dm"
+ 
+ linkedAnimPart{
+ verNode:t="bone_camera_gunner"
+ verLimits:p2=-10.0, 20.0
+ verOriginLimits:p2=-10.0, 20.0
+ }
+ 
+ linkedAnimPart{
+ verNode:t="bone_roll_03"
+ verLimits:p2=-10.0, 5.0
+ verOriginLimits:p2=-10.0, 5.0
+ }
+ }
+ 
+ limits{
+ yaw:p2=-180.0, 180.0
+ pitch:p2=-10.0, 20.0
+ }
+ 
+ limitsTable{
+ lim1:p4=-180.0, -140.0, 2.0, 20.0
+ lim2:p4=-140.0, -120.0, -1.0, 20.0
+ lim3:p4=-120.0, 120.0, -10.0, 20.0
+ lim4:p4=120.0, 140.0, -1.0, 20.0
+ lim5:p4=140.0, 180.0, 2.0, 20.0
+ }
+ 
+ gunStabilizer{
+ hasVerticalGunFreeMode:b=no
+ hasHorizontal:b=yes
+ horizontalOmegaMult:r=1.0
+ horizontalSpeedLimitKPH:r=75.0
+ hasVertical:b=yes
+ verticalOmegaMult:r=1.0
+ verticalSpeedLimitKPH:r=75.0
+ speedFromVehicleVerticalMult:r=-1.0
+ 
+ errorKPHToDegrees{
+ row:p2=5.0, 0.0
+ row:p2=45.0, 0.015
+ row:p2=80.0, 0.02
+ }
+ }
+ }
+ 
+ Weapon{
+ trigger:t="gunner1"
+ triggerGroup:t="coaxial"
+ blk:t="gameData/Weapons/groundModels_weapons/7_62mm_L8A2_user_machinegun.blk"
+ emitter:t="bone_mg_gun_twin"
+ flash:t="emtr_mg_flame_01"
+ barrelDP:t="gun_barrel_03_dm"
+ barrelDP:t="gun_barrel_01_dm"
+ defaultYaw:r=0.0
+ defaultPitch:r=0.0
+ speedYaw:r=5.5
+ speedPitch:r=4.0
+ fireConeAngle:r=1.0
+ fireConeAngle:r=15.0
+ bullets:i=2400
+ ChainfireTime:r=3.0
+ DelayAfterShoot:r=3.0
+ accuracyAir:r=0.0
+ accuracyGnd:r=0.0
+ errMeasureVel:r=0.0
+ errMeasureVelFast:r=0.0
+ errMeasureVelFwdShift:r=0.0
+ errMeasureVelDir:r=0.0
+ errTargettingOn100kmph:r=0.0
+ errTargetting:r=3.0
+ errExplTime:r=0.0
+ 
+ turret{
+ head:t="bone_mg_gun_twin"
+ gun:t="bone_mg_gun_twin"
+ gunnerDm:t="gunner_dm"
+ secondGunnerDm:t="commander_dm"
+ }
+ 
+ limits{
+ yaw:p2=-0.0, 0.0
+ pitch:p2=-0.0, 0.0
+ }
+ }
+ 
+ Weapon{
+ trigger:t="gunner2"
+ triggerGroup:t="machinegun"
+ blk:t="gameData/Weapons/groundModels_weapons/7_62mm_L37A2_user_machinegun.blk"
+ emitter:t="bone_mg_aa_v_01"
+ flash:t="emtr_mg_flame_02"
+ barrelDP:t="gun_barrel_02_dm"
+ defaultYaw:r=0.0
+ defaultPitch:r=0.0
+ parkInDeadzone:b=no
+ speedYaw:r=90.0
+ speedPitch:r=90.0
+ bullets:i=3600
+ isBulletBelt:b=yes
+ fireConeAngle:r=5.0
+ ChainfireTime:r=0.5
+ DelayAfterShoot:r=2.0
+ accuracyAir:r=1.5
+ accuracyGnd:r=0.0
+ errMeasureVel:r=0.0
+ errMeasureVelFast:r=0.0
+ errMeasureVelFwdShift:r=1.5
+ errMeasureVelDir:r=0.0
+ errTargettingOn100kmph:r=0.0
+ errTargetting:r=3.0
+ errExplTime:r=0.0
+ forestallTime:r=0.1
+ 
+ turret{
+ head:t="bone_mg_aa_h_01"
+ gun:t="bone_mg_aa_v_01"
+ gunnerDm:t="commander_dm"
+ rotatedTurret:t="bone_mg_aa_h_01"
+ hasNightVision:b=no
+ }
+ 
+ limits{
+ yaw:p2=-180.0, 180.0
+ pitch:p2=-10.0, 50.0
+ }
+ }
+ 
+ Weapon{
+ trigger:t="gunner3"
+ triggerGroup:t="commander"
+ blk:t="gameData/Weapons/dummy_weapon.blk"
+ emitter:t="bone_commander_sight_v"
+ defaultYaw:r=0.0
+ defaultPitch:r=0.0
+ parkInDeadzone:b=no
+ speedYaw:r=90.0
+ speedPitch:r=90.0
+ 
+ limits{
+ yaw:p2=-180.0, 180.0
+ pitch:p2=-5.0, 10.0
+ }
+ 
+ turret{
+ head:t="bone_mg_aa_h_01"
+ gun:t="bone_commander_sight_v"
+ gunnerDm:t="commander_dm"
+ verDriveDm:t="commander_panoramic_sight_dm"
+ horDriveDm:t="commander_panoramic_sight_dm"
+ rotatedTurret:t="bone_mg_aa_h_01"
+ }
+ }
+ 
+ Weapon{
+ trigger:t="gunner4"
+ triggerGroup:t="smoke"
+ blk:t="gameData/Weapons/groundModels_weapons/66mm_modern_uk_smoke_grenade_launcher.blk"
+ weaponType:t="rockets"
+ useEmitter:b=yes
+ emitter:t="emtr_mortar_flame_01"
+ emitterGenRange:ip2=1, 10
+ emitterGenFmt:t="emtr_mortar_flame_%02d"
+ ignoreLoaderPenalty:b=yes
+ createGunEffects:b=yes
+ defaultYaw:r=0.0
+ defaultPitch:r=0.0
+ allowableDelta:r=360.0
+ salvo:i=2
+ salvoDelay:r=0.5
+ speedYaw:r=24.0
+ speedPitch:r=15.0
+ fireConeAngle:r=1.0
+ bullets:i=10
+ salvoAmount:r=100.0
+ ChainfireTime:r=0.0
+ DelayAfterShoot:r=5.0
+ AttackMaxDistance:r=1000.0
+ AttackMaxRadius:r=1000.0
+ AttackMaxHeight:r=1000.0
+ accuracyAir:r=0.0
+ accuracyGnd:r=1.5
+ errMeasureVel:r=0.0
+ errMeasureVelFast:r=0.0
+ errMeasureVelFwdShift:r=0.0
+ errMeasureVelDir:r=0.0
+ errTargettingOn100kmph:r=0.0
+ errTargetting:r=3.0
+ errExplTime:r=0.0
+ 
+ turret{
+ head:t="bone_grenade"
+ gun:t="bone_grenade"
+ }
+ 
+ limits{
+ yaw:p2=-0.0, 0.0
+ pitch:p2=0.0, 0.0
+ }
+ }
+ }
+ }
+ }
+ }
+ 
+ nightVision{
+ 
+ gunnerIr{
+ resolution:ip2=800, 600
+ lightMult:r=8.0
+ ghosting:r=0.75
+ noiseFactor:r=0.2
+ }
+ 
+ commanderViewIr{
+ resolution:ip2=800, 600
+ lightMult:r=8.0
+ ghosting:r=0.75
+ noiseFactor:r=0.2
+ }
+ 
+ driverIr{
+ resolution:ip2=800, 600
+ lightMult:r=5.0
+ ghosting:r=0.7
+ noiseFactor:r=0.2
+ }
+ }
+ 
+ ammoStowages{
+ 
+ ammo1{
+ weaponTrigger:t="gunner0"
+ removeLoadedAmmo:b=yes
+ fatalFire:b=yes
+ fatalExplosion:b=yes
+ replenishmentDelay:r=4.0
+ replenishmentTime:r=20.0
+ reverseFill:b=no
+ 
+ shells{
+ firstStage:b=yes
+ 
+ ammo_turret_20_dm{
+ count:i=1
+ }
+ 
+ ammo_turret_23_dm{
+ count:i=1
+ }
+ 
+ ammo_turret_25_dm{
+ count:i=1
+ }
+ }
+ 
+ shells{
+ reloadTimeMult:r=1.333
+ 
+ ammo_turret_21_dm{
+ count:i=1
+ }
+ 
+ ammo_turret_22_dm{
+ count:i=1
+ }
+ 
+ ammo_turret_24_dm{
+ count:i=1
+ }
+ 
+ ammo_turret_26_dm{
+ count:i=1
+ }
+ 
+ ammo_turret_28_dm{
+ count:i=1
+ }
+ 
+ ammo_turret_30_dm{
+ count:i=1
+ }
+ 
+ ammo_turret_32_dm{
+ count:i=1
+ }
+ 
+ ammo_turret_34_dm{
+ count:i=1
+ }
+ 
+ ammo_turret_27_dm{
+ count:i=1
+ }
+ 
+ ammo_turret_29_dm{
+ count:i=1
+ }
+ 
+ ammo_turret_31_dm{
+ count:i=1
+ }
+ 
+ ammo_turret_33_dm{
+ count:i=1
+ }
+ 
+ ammo_turret_35_dm{
+ count:i=1
+ }
+ 
+ ammo_turret_36_dm{
+ count:i=1
+ }
+ 
+ ammo_turret_38_dm{
+ count:i=1
+ }
+ 
+ ammo_turret_37_dm{
+ count:i=1
+ }
+ 
+ ammo_turret_39_dm{
+ count:i=1
+ }
+ 
+ ammo_turret_19_dm{
+ count:i=1
+ }
+ 
+ ammo_turret_18_dm{
+ count:i=1
+ }
+ 
+ ammo_turret_17_dm{
+ count:i=1
+ }
+ 
+ ammo_turret_16_dm{
+ count:i=1
+ }
+ 
+ ammo_turret_15_dm{
+ count:i=1
+ }
+ 
+ ammo_turret_14_dm{
+ count:i=1
+ }
+ 
+ ammo_turret_01_dm{
+ count:i=1
+ }
+ 
+ ammo_turret_02_dm{
+ count:i=1
+ }
+ 
+ ammo_turret_03_dm{
+ count:i=1
+ }
+ 
+ ammo_turret_05_dm{
+ count:i=1
+ }
+ 
+ ammo_turret_04_dm{
+ count:i=1
+ }
+ 
+ ammo_turret_06_dm{
+ count:i=1
+ }
+ 
+ ammo_turret_07_dm{
+ count:i=1
+ }
+ 
+ ammo_turret_08_dm{
+ count:i=1
+ }
+ 
+ ammo_turret_09_dm{
+ count:i=1
+ }
+ 
+ ammo_turret_10_dm{
+ count:i=1
+ }
+ 
+ ammo_turret_40_dm{
+ count:i=1
+ }
+ 
+ ammo_turret_41_dm{
+ count:i=1
+ }
+ 
+ ammo_turret_42_dm{
+ count:i=1
+ }
+ 
+ ammo_turret_44_dm{
+ count:i=1
+ }
+ 
+ ammo_turret_43_dm{
+ count:i=1
+ }
+ 
+ ammo_turret_45_dm{
+ count:i=1
+ }
+ 
+ ammo_body_42_dm{
+ count:i=1
+ }
+ 
+ ammo_body_43_dm{
+ count:i=1
+ }
+ 
+ ammo_body_44_dm{
+ count:i=1
+ }
+ 
+ ammo_body_45_dm{
+ count:i=1
+ }
+ 
+ ammo_body_46_dm{
+ count:i=1
+ }
+ 
+ ammo_body_47_dm{
+ count:i=1
+ }
+ 
+ ammo_body_48_dm{
+ count:i=1
+ }
+ 
+ ammo_body_49_dm{
+ count:i=1
+ }
+ 
+ ammo_body_50_dm{
+ count:i=1
+ }
+ 
+ ammo_body_51_dm{
+ count:i=1
+ }
+ }
+ 
+ charges{
+ firstStage:b=yes
+ 
+ ammo_turret_11_dm{
+ count:i=1
+ }
+ 
+ ammo_turret_12_dm{
+ count:i=1
+ }
+ 
+ ammo_turret_13_dm{
+ count:i=1
+ }
+ }
+ 
+ charges{
+ reloadTimeMult:r=1.333
+ 
+ ammo_body_02_dm{
+ count:i=1
+ }
+ 
+ ammo_body_01_dm{
+ count:i=1
+ }
+ 
+ ammo_body_03_dm{
+ count:i=1
+ }
+ 
+ ammo_body_04_dm{
+ count:i=1
+ }
+ 
+ ammo_body_05_dm{
+ count:i=1
+ }
+ 
+ ammo_body_52_dm{
+ count:i=1
+ }
+ 
+ ammo_body_06_dm{
+ count:i=1
+ }
+ 
+ ammo_body_07_dm{
+ count:i=1
+ }
+ 
+ ammo_body_53_dm{
+ count:i=1
+ }
+ 
+ ammo_body_09_dm{
+ count:i=1
+ }
+ 
+ ammo_body_55_dm{
+ count:i=1
+ }
+ 
+ ammo_body_11_dm{
+ count:i=1
+ }
+ 
+ ammo_body_57_dm{
+ count:i=1
+ }
+ 
+ ammo_body_08_dm{
+ count:i=1
+ }
+ 
+ ammo_body_54_dm{
+ count:i=1
+ }
+ 
+ ammo_body_10_dm{
+ count:i=1
+ }
+ 
+ ammo_body_56_dm{
+ count:i=1
+ }
+ 
+ ammo_body_12_dm{
+ count:i=1
+ }
+ 
+ ammo_body_58_dm{
+ count:i=1
+ }
+ 
+ ammo_body_13_dm{
+ count:i=1
+ }
+ 
+ ammo_body_59_dm{
+ count:i=1
+ }
+ 
+ ammo_body_14_dm{
+ count:i=1
+ }
+ 
+ ammo_body_15_dm{
+ count:i=1
+ }
+ 
+ ammo_body_16_dm{
+ count:i=1
+ }
+ 
+ ammo_body_17_dm{
+ count:i=1
+ }
+ 
+ ammo_body_30_dm{
+ count:i=1
+ }
+ 
+ ammo_body_31_dm{
+ count:i=1
+ }
+ 
+ ammo_body_32_dm{
+ count:i=1
+ }
+ 
+ ammo_body_33_dm{
+ count:i=1
+ }
+ 
+ ammo_body_34_dm{
+ count:i=1
+ }
+ 
+ ammo_body_35_dm{
+ count:i=1
+ }
+ 
+ ammo_body_36_dm{
+ count:i=1
+ }
+ 
+ ammo_body_37_dm{
+ count:i=1
+ }
+ 
+ ammo_body_38_dm{
+ count:i=1
+ }
+ 
+ ammo_body_39_dm{
+ count:i=1
+ }
+ 
+ ammo_body_40_dm{
+ count:i=1
+ }
+ 
+ ammo_body_41_dm{
+ count:i=1
+ }
+ 
+ ammo_body_18_dm{
+ count:i=1
+ }
+ 
+ ammo_body_19_dm{
+ count:i=1
+ }
+ 
+ ammo_body_20_dm{
+ count:i=1
+ }
+ 
+ ammo_body_21_dm{
+ count:i=1
+ }
+ 
+ ammo_body_22_dm{
+ count:i=1
+ }
+ 
+ ammo_body_23_dm{
+ count:i=1
+ }
+ 
+ ammo_body_24_dm{
+ count:i=1
+ }
+ 
+ ammo_body_25_dm{
+ count:i=1
+ }
+ 
+ ammo_body_26_dm{
+ count:i=1
+ }
+ 
+ ammo_body_27_dm{
+ count:i=1
+ }
+ 
+ ammo_body_28_dm{
+ count:i=1
+ }
+ 
+ ammo_body_29_dm{
+ count:i=1
+ }
+ }
+ }
+ }
+ 
+ user_skin{
+ name:t="shir_2"
+ 
+ replace_tex{
+ from:t="uk_camo_very_dark_drab*"
+ }
+ }
+ 
+ skin{
+ name:t="uk_camo_standart_modern_light_stone"
+ nameLocId:t="skin/uk_camo_standart_modern_light_stone"
+ descLocId:t="skin/uk_camo_standart_modern_light_stone/desc"
+ 
+ replace_tex{
+ from:t="uk_camo_very_dark_drab*"
+ to:t="uk_camo_standart_modern_light_stone*"
+ }
+ }
+ 
+ skin{
+ name:t="uk_camo_standart_modern_bicolor"
+ nameLocId:t="skin/uk_camo_standart_modern_bicolor"
+ descLocId:t="skin/uk_camo_standart_modern_bicolor/desc"
+ 
+ replace_tex{
+ from:t="uk_camo_very_dark_drab*"
+ to:t="uk_camo_standart_modern_bicolor*"
+ }
+ }
+ 
+ skin{
+ name:t="uk_camo_standart_modern_desert_bicolor"
+ nameLocId:t="skin/uk_camo_standart_modern_desert_bicolor"
+ descLocId:t="skin/uk_camo_standart_modern_desert_bicolor/desc"
+ 
+ replace_tex{
+ from:t="uk_camo_very_dark_drab*"
+ to:t="uk_camo_standart_modern_desert_bicolor*"
+ }
+ }
+ 
+ skin{
+ name:t="uk_camo_winter_olive"
+ nameLocId:t="skin/winter"
+ descLocId:t="skin/winter/desc"
+ 
+ replace_tex{
+ from:t="uk_camo_very_dark_drab*"
+ to:t="us_camo_winter_olive*"
+ }
+ }
+ 
+ skin{
+ name:t="fr_camo_winter_green_white"
+ nameLocId:t="skin/fr_camo_winter_green_white"
+ descLocId:t="skin/fr_camo_winter_green_white/desc"
+ 
+ replace_tex{
+ from:t="uk_camo_very_dark_drab*"
+ to:t="fr_camo_winter_green_white*"
+ }
+ }
```

  **Removed**:
```diff
```


- **aces.vromfs.bin_u/gamedata/units/tankmodels/weaponpresets/uk_shir_2_default.blkx**:


---
