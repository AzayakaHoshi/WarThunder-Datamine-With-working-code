### Full Changelog:

- **aces.vromfs.bin_u/config/collections.blkx**:

  **Added**:
```diff
+ collection36{
+ locId:t="collection/winter_tales_2025"
+ reqFeature:t="Collection"
+ 
+ collectionItems{
+ decal:t="befana_decal"
+ decal:t="grilla_decal"
+ decal:t="hans_trapp_decal"
+ decal:t="jack_frost_decal"
+ decal:t="krampus_decal"
+ }
+ 
+ prize{
+ decal:t="yule_cat_decal"
+ }
+ }
+ 
```

  **Removed**:
```diff
```


- **aces.vromfs.bin_u/config/rendinst_dmg.blkx**:

  **Added**:
```diff
```

  **Removed**:
```diff
- dmPreset:t="unshootable_objects"
```


- **aces.vromfs.bin_u/config/workshop.blkx**:

  **Added**:
```diff
+ winter_tales_2025_exchange{
+ locId:t="collection/winter_tales_2025"
+ reqFeature:t="DMMandPS4andXBOXAccount"
+ 
+ items{
+ alwaysVisibleItem:i=760273
+ alwaysVisibleItem:i=760274
+ alwaysVisibleItem:i=760275
+ alwaysVisibleItem:i=760276
+ alwaysVisibleItem:i=760277
+ }
+ }
+ 
```

  **Removed**:
```diff
```


- **aces.vromfs.bin_u/gamedata/flightmodels/ef_2000_block_10.blkx**:

  **Added**:
```diff
+ index:i=1
+ TV{
+ pos:p3=0.5, 1.5, 0.0
+ head:t="cockpit"
+ crosshairPreset:t="test_crosshair"
+ angularLimits:p4=-30.0, 30.0, -30.0, 30.0
+ opticType:t=""
+ turretNo:i=0
+ nvIndex:i=2
+ }
+ 
+ nvIndex:i=1
+ name:t="ef_2000_block_10_aim_9m"
+ blk:t="gameData/FlightModels/weaponPresets/ef_2000_block_10_aim_9m.blk"
+ }
+ 
+ preset{
+ name:t="ef_2000_block_10_aim_9m_x2"
+ blk:t="gameData/FlightModels/weaponPresets/ef_2000_block_10_aim_9m_x2.blk"
+ reqModification:t="us_aim_9m"
+ blk:t="gameData/Weapons/rocketGuns/us_aim9l_i_1_sidewinder.blk"
+ 
+ WeaponPreset{
+ iconType:t="missile_type_f_air_to_air"
+ name:t="aim_9m_default_slot1"
+ 
+ ShowNodes{
+ node:t="pylon_2"
+ }
+ 
+ Weapon{
+ trigger:t="aam"
+ blk:t="gameData/Weapons/rocketGuns/us_aim9m_sidewinder_default.blk"
+ emitter:t="aim_9e_001"
+ external:b=yes
+ separate:b=yes
+ bullets:i=1
+ }
+ }
+ reqModification:t="us_aim_9m"
+ reqModification:t="us_aim_9m"
+ WeaponPreset{
+ iconType:t="missile_type_f_air_to_air"
+ name:t="aim_9m_slot2"
+ reqModification:t="us_aim_9m"
+ 
+ ShowNodes{
+ node:t="pylon_4"
+ node:t="mfrl_001"
+ }
+ 
+ HideNodes{
+ node:t="pylon_4_off"
+ }
+ 
+ Weapon{
+ trigger:t="aam"
+ blk:t="gameData/Weapons/rocketGuns/us_aim9m_sidewinder.blk"
+ emitter:t="aim_9e_002"
+ external:b=yes
+ separate:b=yes
+ bullets:i=1
+ }
+ }
+ 
+ WeaponPreset{
+ iconType:t="missile_type_f_air_to_air_group"
+ name:t="aim_9m_slot2_x2"
+ reqModification:t="us_aim_9m"
+ 
+ ShowNodes{
+ node:t="pylon_4"
+ node:t="tmc_launcher_001"
+ node:t="tmc_launcher_001_mfrl_l"
+ node:t="tmc_launcher_001_mfrl_r"
+ }
+ 
+ HideNodes{
+ node:t="pylon_4_off"
+ }
+ 
+ Weapon{
+ trigger:t="aam"
+ blk:t="gameData/Weapons/containers/tmc_eurofighter_aim_9m.blk"
+ emitter:t="tmc_launcher_001"
+ external:b=yes
+ separate:b=yes
+ }
+ 
+ BannedWeaponPreset{
+ slot:i=3
+ preset:t="paveway_iv_slot3_x2"
+ }
+ }
+ 
+ reqModification:t="us_aim_9m"
+ reqModification:t="us_aim_9m"
+ WeaponPreset{
+ iconType:t="missile_type_f_air_to_air"
+ name:t="aim_9m_slot12"
+ reqModification:t="us_aim_9m"
+ 
+ ShowNodes{
+ node:t="pylon_3"
+ node:t="mfrl_002"
+ }
+ 
+ HideNodes{
+ node:t="pylon_3_off"
+ }
+ 
+ Weapon{
+ trigger:t="aam"
+ blk:t="gameData/Weapons/rocketGuns/us_aim9m_sidewinder.blk"
+ emitter:t="aim_9e_003"
+ external:b=yes
+ separate:b=yes
+ bullets:i=1
+ }
+ }
+ 
+ WeaponPreset{
+ iconType:t="missile_type_f_air_to_air_group"
+ name:t="aim_9m_slot12_x2"
+ reqModification:t="us_aim_9m"
+ 
+ ShowNodes{
+ node:t="pylon_3"
+ node:t="tmc_launcher_002"
+ node:t="tmc_launcher_002_mfrl_l"
+ node:t="tmc_launcher_002_mfrl_r"
+ }
+ 
+ HideNodes{
+ node:t="pylon_3_off"
+ }
+ 
+ Weapon{
+ trigger:t="aam"
+ blk:t="gameData/Weapons/containers/tmc_eurofighter_aim_9m.blk"
+ emitter:t="tmc_launcher_002"
+ external:b=yes
+ separate:b=yes
+ }
+ 
+ BannedWeaponPreset{
+ slot:i=11
+ preset:t="paveway_iv_slot11_x2"
+ }
+ }
+ 
+ name:t="aim_9l_i_slot13"
+ reqModification:t="us_aim_9m"
+ blk:t="gameData/Weapons/rocketGuns/us_aim9l_i_1_sidewinder.blk"
+ 
+ WeaponPreset{
+ iconType:t="missile_type_f_air_to_air"
+ name:t="aim_9m_default_slot13"
+ 
+ ShowNodes{
+ node:t="pylon_1"
+ }
+ 
+ Weapon{
+ trigger:t="aam"
+ blk:t="gameData/Weapons/rocketGuns/us_aim9m_sidewinder_default.blk"
+ emitter:t="aim_9e_004"
+ external:b=yes
+ separate:b=yes
+ bullets:i=1
+ }
+ }
+ us_aim_9m{
+ reqModification:t="us_aim_9m"
```

  **Removed**:
```diff
- name:t="ef_2000_block_10_aim_9l_i"
- blk:t="gameData/FlightModels/weaponPresets/ef_2000_block_10_aim_9l_i.blk"
- blk:t="gameData/Weapons/rocketGuns/us_aim9l_i_1_sidewinder_default.blk"
- reqModification:t="us_aim_9l_i_1"
- reqModification:t="us_aim_9l_i_1"
- reqModification:t="us_aim_9l_i_1"
- reqModification:t="us_aim_9l_i_1"
- name:t="aim_9l_i_default_slot13"
- blk:t="gameData/Weapons/rocketGuns/us_aim9l_i_1_sidewinder_default.blk"
- us_aim_9l_i_1{
- reqModification:t="us_aim_9l_i_1"
```


- **aces.vromfs.bin_u/gamedata/flightmodels/f_111f.blkx**:

  **Added**:
```diff
+ index:i=1
+ index:i=2
+ nvIndex:i=1
+ nvIndex:i=1
+ TV2{
+ pos:p3=1.5, 0.0, 0.0
+ head:t="optic2_turret"
+ crosshairPreset:t="test_crosshair"
+ angularLimits:p4=-38.0, 38.0, -55.0, 38.0
+ opticType:t="tv"
+ turretNo:i=0
+ nvIndex:i=1
+ name:t="GBU15V2"
+ }
+ 
+ nvIndex:i=2
+ 
+ sensor{
+ blk:t="gameData/sensors/ir_tracker_tgp.blk"
+ node:t="optic2_gun"
+ }
+ blk:t="gameData/Weapons/BombGuns/us_2000lb_agm_130a_12.blk"
+ external:b=yes
+ blk:t="gameData/Weapons/BombGuns/us_2000lb_agm_130a_12.blk"
+ external:b=yes
```

  **Removed**:
```diff
- blk:t="gameData/Weapons/BombGuns/us_2000lb_agm_130a.blk"
- external:b=no
- blk:t="gameData/Weapons/BombGuns/us_2000lb_agm_130a.blk"
- external:b=no
```


- **aces.vromfs.bin_u/gamedata/flightmodels/f_15e.blkx**:

  **Added**:
```diff
+ emitter:t="mer_001"
+ blk:t="gameData/Weapons/BombGuns/us_2000lb_agm_130a_12.blk"
+ blk:t="gameData/Weapons/BombGuns/us_2000lb_agm_130a_12.blk"
```

  **Removed**:
```diff
- emitter:t="us_2000lb_gbu_8_001"
- blk:t="gameData/Weapons/BombGuns/us_2000lb_agm_130a.blk"
- blk:t="gameData/Weapons/BombGuns/us_2000lb_agm_130a.blk"
```


- **aces.vromfs.bin_u/gamedata/flightmodels/fm/ef_2000_block_10.blkx**:

  **Added**:
```diff
+ EmptyMass:r=11220.0
```

  **Removed**:
```diff
- EmptyMass:r=11300.0
```


- **aces.vromfs.bin_u/gamedata/flightmodels/fm/f_2000a.blkx**:

  **Added**:
```diff
+ EmptyMass:r=11220.0
```

  **Removed**:
```diff
- EmptyMass:r=11300.0
```


- **aces.vromfs.bin_u/gamedata/flightmodels/fm/typhoon_fgr4.blkx**:

  **Added**:
```diff
+ EmptyMass:r=11220.0
```

  **Removed**:
```diff
- EmptyMass:r=11300.0
```


- **aces.vromfs.bin_u/gamedata/flightmodels/rafale_c_f3.blkx**:

  **Added**:
```diff
+ Weapon{
+ trigger:t="countermeasures"
+ blk:t="gameData/Weapons/rocketGuns/countermeasure_split_launcher_jet_maw.blk"
+ emitter:t="emtr_flare2"
+ bullets:i=18
+ external:b=yes
+ separate:b=yes
+ bulletsCartridge:i=1
+ }
+ 
+ Weapon{
+ trigger:t="countermeasures"
+ blk:t="gameData/Weapons/rocketGuns/countermeasure_split_launcher_jet_maw.blk"
+ emitter:t="emtr_flare5"
+ bullets:i=18
+ external:b=yes
+ separate:b=yes
+ bulletsCartridge:i=1
+ }
+ 
+ bullets:i=8
+ bullets:i=8
+ Weapon{
+ trigger:t="countermeasures"
+ blk:t="gameData/Weapons/rocketGuns/countermeasure_split_launcher_jet_maw.blk"
+ emitter:t="emtr_flare2"
+ bullets:i=18
+ external:b=yes
+ separate:b=yes
+ bulletsCartridge:i=1
+ }
+ 
+ Weapon{
+ trigger:t="countermeasures"
+ blk:t="gameData/Weapons/rocketGuns/countermeasure_split_launcher_jet_maw.blk"
+ emitter:t="emtr_flare5"
+ bullets:i=18
+ external:b=yes
+ separate:b=yes
+ bulletsCartridge:i=1
+ }
+ 
+ bullets:i=8
+ bullets:i=8
+ tier:i=12
+ tier:i=11
+ node:t="pylon_rafale_mica_aux_001"
+ node:t="pylon_rafale_mica_aux_rail_001"
+ emitter:t="rocket_mica_002"
+ bullets:i=1
+ }
+ }
+ }
+ 
+ WeaponSlot{
+ index:i=3
+ tier:i=10
+ order:i=5
+ 
+ WeaponPreset{
+ iconType:t="missile_type_f_air_to_air_midrange"
+ name:t="mica_em_slot3"
+ reqModification:t="fr_mica_em"
+ 
+ ShowNodes{
+ node:t="pylon_rafale_mica_001"
+ }
+ 
+ Weapon{
+ trigger:t="aam"
+ external:b=yes
+ separate:b=yes
+ blk:t="gameData/Weapons/rocketGuns/fr_mica_em.blk"
+ name:t="us_500lb_mk_82_ldgp_x2_slot3"
+ name:t="250kg_type_25c_x3_slot3"
+ name:t="auf2_gbu_12_x2_slot3"
+ name:t="auf2_gbu_22_x2_slot3"
+ name:t="auf2_gbu_49_x2_slot3"
+ name:t="us_gbu_16_slot3"
+ name:t="us_gbu_24_slot3"
+ name:t="us_gbu_12_x3_slot3"
+ name:t="us_gbu_22_x3_slot3"
+ name:t="us_gbu_49_x3_slot3"
+ name:t="aasm_250_sbu_38_x3_slot3"
+ name:t="aasm_250_sbu_64_x3_slot3"
+ name:t="aasm_250_sbu_54_x3_slot3"
+ index:i=4
+ order:i=7
+ index:i=5
+ order:i=9
+ name:t="mica_em_slot5"
+ index:i=6
+ order:i=11
+ index:i=7
+ order:i=12
+ name:t="us_gbu_24_slot7"
+ index:i=8
+ order:i=10
+ name:t="mica_em_slot8"
+ index:i=9
+ order:i=8
+ index:i=10
+ order:i=6
+ name:t="mica_em_slot10"
+ reqModification:t="fr_mica_em"
+ blk:t="gameData/Weapons/rocketGuns/fr_mica_em.blk"
+ name:t="us_500lb_mk_82_ldgp_x2_slot10"
+ name:t="250kg_type_25c_x3_slot10"
+ name:t="auf2_gbu_12_x2_slot10"
+ name:t="auf2_gbu_22_x2_slot10"
+ name:t="auf2_gbu_49_x2_slot10"
+ name:t="us_gbu_16_slot10"
+ name:t="us_gbu_24_slot10"
+ name:t="us_gbu_12_x3_slot10"
+ name:t="us_gbu_22_x3_slot10"
+ name:t="us_gbu_49_x3_slot10"
+ name:t="aasm_250_sbu_38_x3_slot10"
+ name:t="aasm_250_sbu_64_x3_slot10"
+ name:t="aasm_250_sbu_54_x3_slot10"
+ index:i=11
+ order:i=4
+ 
+ WeaponPreset{
+ iconType:t="missile_type_f_air_to_air_midrange"
+ name:t="mica_em_slot11_default"
+ 
+ ShowNodes{
+ node:t="pylon_rafale_mica_aux_002"
+ node:t="pylon_rafale_mica_aux_rail_002"
+ }
+ 
+ Weapon{
+ trigger:t="aam"
+ external:b=yes
+ separate:b=yes
+ blk:t="gameData/Weapons/rocketGuns/fr_mica_em_default.blk"
+ emitter:t="rocket_mica_007"
+ bullets:i=1
+ }
+ }
+ }
+ 
+ WeaponSlot{
+ index:i=12
+ tier:i=0
+ name:t="r550_magic_2_slot12_default"
+ name:t="mica_em_slot12"
+ maw_countermeasures_launcher_chaff{
+ }
+ 
```

  **Removed**:
```diff
- bullets:i=16
- bullets:i=16
- bullets:i=16
- bullets:i=16
- tier:i=11
- tier:i=10
- node:t="pylon_rafale_mica_001"
- name:t="us_500lb_mk_82_ldgp_x2_slot2"
- name:t="250kg_type_25c_x3_slot2"
- name:t="auf2_gbu_12_x2_slot2"
- name:t="auf2_gbu_22_x2_slot2"
- name:t="auf2_gbu_49_x2_slot2"
- name:t="us_gbu_16_slot2"
- name:t="us_gbu_24_slot2"
- name:t="us_gbu_12_x3_slot2"
- name:t="us_gbu_22_x3_slot2"
- name:t="us_gbu_49_x3_slot2"
- name:t="aasm_250_sbu_38_x3_slot2"
- name:t="aasm_250_sbu_64_x3_slot2"
- name:t="aasm_250_sbu_54_x3_slot2"
- index:i=3
- order:i=5
- index:i=4
- order:i=7
- name:t="mica_em_slot4"
- index:i=5
- order:i=9
- index:i=6
- order:i=10
- name:t="us_gbu_24_slot6"
- index:i=7
- order:i=8
- name:t="mica_em_slot7"
- index:i=8
- order:i=6
- index:i=9
- order:i=4
- name:t="mica_em_slot9_default"
- blk:t="gameData/Weapons/rocketGuns/fr_mica_em_default.blk"
- name:t="us_500lb_mk_82_ldgp_x2_slot9"
- name:t="250kg_type_25c_x3_slot9"
- name:t="auf2_gbu_12_x2_slot9"
- name:t="auf2_gbu_22_x2_slot9"
- name:t="auf2_gbu_49_x2_slot9"
- name:t="us_gbu_16_slot9"
- name:t="us_gbu_24_slot9"
- name:t="us_gbu_12_x3_slot9"
- name:t="us_gbu_22_x3_slot9"
- name:t="us_gbu_49_x3_slot9"
- name:t="aasm_250_sbu_38_x3_slot9"
- name:t="aasm_250_sbu_64_x3_slot9"
- name:t="aasm_250_sbu_54_x3_slot9"
- index:i=10
- name:t="r550_magic_2_slot10_default"
- name:t="mica_em_slot10"
```


- **aces.vromfs.bin_u/gamedata/flightmodels/weaponpresets/alpha_jet_th_phase_1_default.blkx**:

  **Added**:
```diff
+ preset:t="aim_9p4_deafult"
+ preset:t="aim_9p4_deafult"
```

  **Removed**:
```diff
- preset:t="ptb_1"
- preset:t="ptb_2"
```


- **aces.vromfs.bin_u/gamedata/flightmodels/weaponpresets/ef_2000_block_10_aim_9m.blkx**:

  **Added**:
```diff
+ Weapon{
+ slot:i=1
+ preset:t="aim_9m_default_slot1"
+ }
+ 
+ Weapon{
+ slot:i=2
+ preset:t="aim_9m_slot2"
+ }
+ 
+ Weapon{
+ slot:i=12
+ preset:t="aim_9m_slot12"
+ }
+ 
+ Weapon{
+ slot:i=13
+ preset:t="aim_9m_default_slot13"
+ }
```

  **Removed**:
```diff
```


- **aces.vromfs.bin_u/gamedata/flightmodels/weaponpresets/ef_2000_block_10_aim_9m_x2.blkx**:

  **Added**:
```diff
+ Weapon{
+ slot:i=1
+ preset:t="aim_9m_default_slot1"
+ }
+ 
+ Weapon{
+ slot:i=2
+ preset:t="aim_9m_slot2_x2"
+ }
+ 
+ Weapon{
+ slot:i=12
+ preset:t="aim_9m_slot12_x2"
+ }
+ 
+ Weapon{
+ slot:i=13
+ preset:t="aim_9m_default_slot13"
+ }
```

  **Removed**:
```diff
```


- **aces.vromfs.bin_u/gamedata/flightmodels/weaponpresets/ef_2000_block_10_default.blkx**:

  **Added**:
```diff
+ preset:t="aim_9m_default_slot1"
+ preset:t="aim_9m_default_slot13"
```

  **Removed**:
```diff
- preset:t="aim_9l_i_default_slot1"
- preset:t="aim_9l_i_default_slot13"
```


- **aces.vromfs.bin_u/gamedata/flightmodels/weaponpresets/rafale_c_f3_aasm_250_sbu_38.blkx**:

  **Added**:
```diff
+ slot:i=3
+ preset:t="aasm_250_sbu_38_x3_slot3"
+ slot:i=6
+ slot:i=10
+ preset:t="aasm_250_sbu_38_x3_slot10"
```

  **Removed**:
```diff
- slot:i=2
- preset:t="aasm_250_sbu_38_x3_slot2"
- slot:i=5
- slot:i=9
- preset:t="aasm_250_sbu_38_x3_slot9"
```


- **aces.vromfs.bin_u/gamedata/flightmodels/weaponpresets/rafale_c_f3_aasm_250_sbu_54.blkx**:

  **Added**:
```diff
+ slot:i=3
+ preset:t="aasm_250_sbu_54_x3_slot3"
+ slot:i=6
+ slot:i=10
+ preset:t="aasm_250_sbu_54_x3_slot10"
```

  **Removed**:
```diff
- slot:i=2
- preset:t="aasm_250_sbu_54_x3_slot2"
- slot:i=5
- slot:i=9
- preset:t="aasm_250_sbu_54_x3_slot9"
```


- **aces.vromfs.bin_u/gamedata/flightmodels/weaponpresets/rafale_c_f3_aasm_250_sbu_64.blkx**:

  **Added**:
```diff
+ slot:i=3
+ preset:t="aasm_250_sbu_64_x3_slot3"
+ slot:i=6
+ slot:i=10
+ preset:t="aasm_250_sbu_64_x3_slot10"
```

  **Removed**:
```diff
- slot:i=2
- preset:t="aasm_250_sbu_64_x3_slot2"
- slot:i=5
- slot:i=9
- preset:t="aasm_250_sbu_64_x3_slot9"
```


- **aces.vromfs.bin_u/gamedata/flightmodels/weaponpresets/rafale_c_f3_default.blkx**:

  **Added**:
```diff
+ slot:i=4
+ slot:i=7
+ slot:i=9
+ slot:i=11
+ preset:t="mica_em_slot11_default"
+ slot:i=12
+ preset:t="r550_magic_2_slot12_default"
```

  **Removed**:
```diff
- slot:i=3
- slot:i=6
- slot:i=8
- slot:i=9
- preset:t="mica_em_slot9_default"
- slot:i=10
- preset:t="r550_magic_2_slot10_default"
```


- **aces.vromfs.bin_u/gamedata/flightmodels/weaponpresets/rafale_c_f3_gbu_12.blkx**:

  **Added**:
```diff
+ slot:i=3
+ preset:t="us_gbu_12_x3_slot3"
+ slot:i=6
+ slot:i=10
+ preset:t="us_gbu_12_x3_slot10"
```

  **Removed**:
```diff
- slot:i=2
- preset:t="us_gbu_12_x3_slot2"
- slot:i=5
- slot:i=9
- preset:t="us_gbu_12_x3_slot9"
```


- **aces.vromfs.bin_u/gamedata/flightmodels/weaponpresets/rafale_c_f3_gbu_16.blkx**:

  **Added**:
```diff
+ slot:i=3
+ preset:t="us_gbu_16_slot3"
+ slot:i=6
+ slot:i=10
+ preset:t="us_gbu_16_slot10"
```

  **Removed**:
```diff
- slot:i=2
- preset:t="us_gbu_16_slot2"
- slot:i=5
- slot:i=9
- preset:t="us_gbu_16_slot9"
```


- **aces.vromfs.bin_u/gamedata/flightmodels/weaponpresets/rafale_c_f3_gbu_22.blkx**:

  **Added**:
```diff
+ slot:i=3
+ preset:t="us_gbu_22_x3_slot3"
+ slot:i=6
+ slot:i=10
+ preset:t="us_gbu_22_x3_slot10"
```

  **Removed**:
```diff
- slot:i=2
- preset:t="us_gbu_22_x3_slot2"
- slot:i=5
- slot:i=9
- preset:t="us_gbu_22_x3_slot9"
```


- **aces.vromfs.bin_u/gamedata/flightmodels/weaponpresets/rafale_c_f3_gbu_24.blkx**:

  **Added**:
```diff
+ slot:i=3
+ preset:t="us_gbu_24_slot3"
+ slot:i=6
+ slot:i=7
+ preset:t="us_gbu_24_slot7"
+ slot:i=10
+ preset:t="us_gbu_24_slot10"
```

  **Removed**:
```diff
- slot:i=2
- preset:t="us_gbu_24_slot2"
- slot:i=5
- slot:i=6
- preset:t="us_gbu_24_slot6"
- slot:i=9
- preset:t="us_gbu_24_slot9"
```


- **aces.vromfs.bin_u/gamedata/flightmodels/weaponpresets/rafale_c_f3_gbu_49.blkx**:

  **Added**:
```diff
+ slot:i=3
+ preset:t="us_gbu_49_x3_slot3"
+ slot:i=6
+ slot:i=10
+ preset:t="us_gbu_49_x3_slot10"
```

  **Removed**:
```diff
- slot:i=2
- preset:t="us_gbu_49_x3_slot2"
- slot:i=5
- slot:i=9
- preset:t="us_gbu_49_x3_slot9"
```


- **aces.vromfs.bin_u/gamedata/flightmodels/weaponpresets/rafale_c_f3_mica_em.blkx**:

  **Added**:
```diff
+ slot:i=3
+ preset:t="mica_em_slot3"
+ slot:i=5
+ preset:t="mica_em_slot5"
+ slot:i=8
+ preset:t="mica_em_slot8"
+ }
+ 
+ Weapon{
+ slot:i=11
+ preset:t="mica_em_slot11_default"
+ }
+ 
+ Weapon{
+ slot:i=12
+ preset:t="mica_em_slot12"
```

  **Removed**:
```diff
- slot:i=4
- preset:t="mica_em_slot4"
- slot:i=7
- preset:t="mica_em_slot7"
- slot:i=9
- preset:t="mica_em_slot9_default"
```


- **aces.vromfs.bin_u/gamedata/flightmodels/weaponpresets/rafale_c_f3_r550.blkx**:

  **Added**:
```diff
+ slot:i=12
+ preset:t="r550_magic_2_slot12_default"
```

  **Removed**:
```diff
- slot:i=10
- preset:t="r550_magic_2_slot10_default"
```


- **aces.vromfs.bin_u/gamedata/flightmodels/weaponpresets/rafale_c_f3_samp_mk82.blkx**:

  **Added**:
```diff
+ slot:i=3
+ preset:t="250kg_type_25c_x3_slot3"
+ slot:i=10
+ preset:t="250kg_type_25c_x3_slot10"
```

  **Removed**:
```diff
- slot:i=2
- preset:t="250kg_type_25c_x3_slot2"
- slot:i=9
- preset:t="250kg_type_25c_x3_slot9"
```


- **aces.vromfs.bin_u/gamedata/sensors/fr_spectra_mlws.blkx**:

  **Added**:
```diff
+ name:t="Thales SPECTRA DDM-NG"
+ elevationWidth:r=180.0
+ elevationWidth:r=180.0
```

  **Removed**:
```diff
- name:t="Thales SPECTRA"
- elevationWidth:r=90.0
- elevationWidth:r=90.0
```


- **aces.vromfs.bin_u/gamedata/sensors/fr_thales_rbe2.blkx**:

  **Added**:
```diff
+ weaponTargetsMax:i=8
+ launchedMissilesPredictedPositionsMax:i=8
```

  **Removed**:
```diff
- weaponTargetsMax:i=6
- launchedMissilesPredictedPositionsMax:i=6
```


- **aces.vromfs.bin_u/gamedata/units/ships/uk_battleship_rodney.blkx**:

  **Added**:
```diff
+ weight:r=0.6
+ critWaterLevel:r=0.85
+ critWaterLevel:r=0.85
+ critWaterLevel:r=0.95
+ critWaterLevel:r=0.95
+ critWaterLevel:r=0.85
+ critWaterLevel:r=0.85
```

  **Removed**:
```diff
- weight:r=0.5
- critWaterLevel:r=0.5
- critWaterLevel:r=0.5
- critWaterLevel:r=0.6
- critWaterLevel:r=0.6
- critWaterLevel:r=0.8
- critWaterLevel:r=0.8
```


- **aces.vromfs.bin_u/gamedata/units/tankmodels/fr_vbci.blkx**:

  **Added**:
```diff
+ turret_10_top_dm{
+ }
+ 
+ turret_07_side_dm{
+ }
+ }
+ 
+ inner_parts{
+ armorThickness:r=5.0
+ armorClass:t="RHA_tank"
+ hidableInXrayViewer:b=yes
+ 
+ composite_armor_hull_05_dm{
+ 
+ armorArrayHull{
+ xrayDmPart:t="composite_armor_hull_05_dm"
+ titleLoc:t="RHA_tank_modern"
+ 
+ armorArrayText{
+ 
+ layer{
+ dmPart:t="composite_armor_hull_05_dm"
+ }
+ }
+ }
+ maxRPM:r=2100.0
+ sideGearRatio:r=0.88
```

  **Removed**:
```diff
- armorThickness:r=5.0
- hidableInXrayViewer:b=yes
- armorThickness:r=5.0
- hidableInXrayViewer:b=yes
- armorThickness:r=5.0
- hidableInXrayViewer:b=yes
- armorThickness:r=5.0
- hidableInXrayViewer:b=yes
- turret_10_top_dm{
- }
- 
- turret_07_side_dm{
- maxRPM:r=2400.0
- sideGearRatio:r=1.0
```


- **aces.vromfs.bin_u/gamedata/units/tankmodels/germ_pzh_2000.blkx**:

  **Added**:
```diff
+ replenishmentDelay:r=5.0
+ replenishmentTime:r=5.0
+ firstStage:b=yes
+ }
+ 
+ shells{
+ reloadTimeMult:r=1.5
+ firstStage:b=yes
+ }
+ 
+ charges{
+ reloadTimeMult:r=1.5
```

  **Removed**:
```diff
- replenishmentDelay:r=8.0
- replenishmentTime:r=10.0
- autoLoad:b=yes
- fireEvent:t="ammo_fire"
- explosionEvent:t="ammo_explosion"
- wreckedPartId:i=0
- autoLoad:b=yes
- fireParamsPreset:t="turret_bustle"
- fatalFire:b=no
- fatalExplosion:b=no
```


- **aces.vromfs.bin_u/gamedata/units/tankmodels/il_sholef.blkx**:

  **Added**:
```diff
+ firstStage:b=yes
+ }
+ 
+ shells{
+ reloadTimeMult:r=1.5867
+ fireEvent:t="ammo_fire"
+ explosionEvent:t="ammo_explosion"
+ wreckedPartId:i=0
+ autoloader:t="autoloader_dm"
+ reloadTimeMult:r=3.1733
+ firstStage:b=yes
+ }
+ 
+ charges{
+ reloadTimeMult:r=1.5867
+ fireEvent:t="ammo_fire"
+ explosionEvent:t="ammo_explosion"
+ wreckedPartId:i=0
+ reloadTimeMult:r=3.1733
```

  **Removed**:
```diff
- autoLoad:b=yes
- reloadTimeMult:r=2.0
- autoLoad:b=yes
- reloadTimeMult:r=2.0
```


- **aces.vromfs.bin_u/gamedata/units/tankmodels/it_pzh_2000_hu.blkx**:

  **Added**:
```diff
+ replenishmentDelay:r=5.0
+ replenishmentTime:r=5.0
+ firstStage:b=yes
+ }
+ 
+ shells{
+ reloadTimeMult:r=1.5
+ firstStage:b=yes
+ }
+ 
+ charges{
+ reloadTimeMult:r=1.5
```

  **Removed**:
```diff
- replenishmentDelay:r=8.0
- replenishmentTime:r=10.0
- autoLoad:b=yes
- fireEvent:t="ammo_fire"
- explosionEvent:t="ammo_explosion"
- wreckedPartId:i=0
- autoLoad:b=yes
- fireParamsPreset:t="turret_bustle"
- fatalFire:b=no
- fatalExplosion:b=no
```


- **aces.vromfs.bin_u/gamedata/units/tankmodels/jp_icv_ifv_prototype.blkx**:

  **Added**:
```diff
```

  **Removed**:
```diff
- part:t="drive_turret_h_dm"
```


- **aces.vromfs.bin_u/gamedata/units/tankmodels/us_m56_scorpion.blkx**:

  **Added**:
```diff
+ yaw:p2=-30.0, 30.0
```

  **Removed**:
```diff
- yaw:p2=-30.0, 15.0
```


- **aces.vromfs.bin_u/gamedata/units/tankmodels/ussr_bmd_4m.blkx**:

  **Added**:
```diff
+ node:t="ex_decor_10"
```

  **Removed**:
```diff
```


- **aces.vromfs.bin_u/gamedata/weapons/bombguns/su_kab_1500kr.blkx**:

  **Added**:
```diff
+ boundaryTrack:b=yes
```

  **Removed**:
```diff
```


- **aces.vromfs.bin_u/gamedata/weapons/bombguns/su_kab_500kr.blkx**:

  **Added**:
```diff
+ boundaryTrack:b=yes
```

  **Removed**:
```diff
```


- **aces.vromfs.bin_u/gamedata/weapons/bombguns/su_kab_500kr_e.blkx**:

  **Added**:
```diff
+ boundaryTrack:b=yes
```

  **Removed**:
```diff
```


- **aces.vromfs.bin_u/gamedata/weapons/bombguns/su_kab_500kr_m.blkx**:

  **Added**:
```diff
+ boundaryTrack:b=yes
```

  **Removed**:
```diff
```


- **aces.vromfs.bin_u/gamedata/weapons/bombguns/su_kab_50tv.blkx**:

  **Added**:
```diff
+ boundaryTrack:b=yes
```

  **Removed**:
```diff
```


- **aces.vromfs.bin_u/gamedata/weapons/bombguns/uk_pgm_2000.blkx**:

  **Added**:
```diff
+ effectOffset:p3=-2.48, -0.25, 0.0
+ boundaryTrack:b=yes
```

  **Removed**:
```diff
- effectOffset:p3=-2.0, -0.25, 0.0
```


- **aces.vromfs.bin_u/gamedata/weapons/bombguns/uk_pgm_2000_iir.blkx**:

  **Added**:
```diff
+ effectOffset:p3=-2.48, -0.25, 0.0
+ boundaryTrack:b=yes
```

  **Removed**:
```diff
- effectOffset:p3=-2.0, -0.25, 0.0
```


- **aces.vromfs.bin_u/gamedata/weapons/bombguns/uk_pgm_500.blkx**:

  **Added**:
```diff
+ boundaryTrack:b=yes
```

  **Removed**:
```diff
```


- **aces.vromfs.bin_u/gamedata/weapons/bombguns/uk_pgm_500_iir.blkx**:

  **Added**:
```diff
+ boundaryTrack:b=yes
```

  **Removed**:
```diff
```


- **aces.vromfs.bin_u/gamedata/weapons/bombguns/us_2000lb_agm_130a.blkx**:

  **Added**:
```diff
+ effectOffset:p3=-2.0, -0.64, 0.0
+ boundaryTrack:b=yes
```

  **Removed**:
```diff
- effectOffset:p3=-2.0, -0.59, 0.0
```


- **aces.vromfs.bin_u/gamedata/weapons/bombguns/us_2000lb_agm_130a_12.blkx**:

  **Added**:
```diff
+ rocketGun:b=yes
+ preset_cost:i=20
+ mesh:t="us_2000lb_agm_130a"
+ mesh_deployed:t="us_2000lb_agm_130a_animated"
+ shellAnimChar:t="us_2000lb_agm_130a_animated_char"
+ helicopterGroup:i=2
+ bullets:i=1
+ shotFreq:r=1000.25
+ sound:t="weapon.rocketgun_132"
+ 
+ tags{
+ }
+ 
+ rocket{
+ bulletName:t="us_2000lb_agm_130a_12"
+ statType:t="hydra"
+ caliber:r=0.4572
+ length:r=3.9243
+ WdK:p3=2.5, 2.5, 2.5
+ CxK:r=1.375
+ brakeTime:p2=51.1, 52.5
+ brakeCxK:r=0.0
+ brakeArm:r=0.0
+ wingAreaMult:r=3.25
+ finsAoaHor:r=0.1512
+ finsAoaVer:r=0.1512
+ distFromCmToStab:r=0.6
+ mass:r=1323.0
+ massEnd:r=1188.0
+ massEnd1:r=1140.0
+ timeFire:r=45.0
+ timeFire1:r=0.0
+ force:r=6300.5
+ force1:r=0.0
+ fireDelay:r=6.0
+ timeLife:r=300.0
+ useStartSpeed:b=yes
+ startSpeed:r=0.0
+ machMax:r=1.0
+ endSpeed:r=0.0
+ maxDistance:r=70000.0
+ minDistance:r=5000.0
+ rangeMax:r=70000.0
+ isHasTVChannel:b=yes
+ opticSightFov:p2=30.0, 15.0
+ guidanceType:t="ir"
+ rollStabilization:b=yes
+ rollStabilizationDelay:r=1.0
+ dragCx:r=0.025
+ normalizationPreset:t="heat"
+ ricochetPreset:t="heat_fs"
+ groundRicochetPreset:t="heat_fs"
+ secondaryShattersPreset:t="ap"
+ stabilityThreshold:r=0.5
+ stabilityCaliberToArmorThreshold:r=5.0
+ stabilityReductionAfterRicochet:r=0.3
+ stabilityReductionAfterPenetration:r=0.15
+ bulletType:t="heat_fs_tank"
+ cumulativeSecondaryShattersPreset:t="heat_fs"
+ explodeOnRendinst:b=yes
+ fresnel:p3=0.23, 0.1, 2.0
+ shellAnimation:t="video/shells_animations/heat_fs.ivf"
+ explosiveType:t="comp_h6"
+ explosiveMass:r=428.6
+ maxDeltaAngle:r=0.02
+ spawnExplosionFx:b=no
+ spawnExplosionWreckage:b=no
+ explosionEffect:t="explosion_midair_rocket_big"
+ groundCollisionEffect:t="bomb_expl_1000kg"
+ ricochetEffect:t="hit_59_80mm_metal_ap"
+ waterCollisionEffect:t="hit_59_80mm_water"
+ explosionPatchRadius:r=17.0
+ waterRicochetEffect:t="hit_81_105mm_water_ap"
+ groundRicochetEffect:t="hit_81_105mm_dirt_ap"
+ visualShattersWaterOffset:r=1.2
+ visualShattersGroundOffset:r=1.2
+ distanceFuse:b=no
+ effectOffset:p3=-2.0, -0.64, 0.0
+ rendinstDamageRadius:r=9.0
+ hitPowerMult:r=400.0
+ fuseDelayDist:r=0.1
+ explodeTreshold:r=0.1
+ fireEffect:t="fires_exhaust_jet_early_med"
+ smokeEffect:t="smoke_rocket_tail_light_big"
+ smokeEffect2:t=""
+ hazeEffect:t="haze_missile"
+ endSmokeViscosity:r=0.05
+ price:r=3000.0
+ amountPerTier:r=1.0
+ iconType:t="guided_bomb_heavy_laser"
+ gunnerOpticsName:t="GBU15V2"
+ 
+ arcadeProp{
+ finsAoaHor:r=0.16
+ finsAoaVer:r=0.16
+ }
+ 
+ guidance{
+ warmUpTime:r=1.0
+ acquisitionTime:r=0.1
+ workTime:r=3600.0
+ useTrippleClickLockInTpv:b=yes
+ applyExtraDifficultyParameters:b=yes
+ breakLockMaxTime:r=120.0
+ uncageBeforeLaunch:b=yes
+ 
+ irSeeker{
+ visibilityType:t="infraRed"
+ rangeBand0:r=20000.0
+ rangeMax:r=40000.0
+ rangeSurface:r=40000.0
+ fov:r=0.1
+ gateWidth:r=0.1
+ minAngleToSun:r=1.0
+ lockAngleMax:r=30.0
+ angleMax:r=54.0
+ rateMax:r=2.5
+ prolongationTimeMax:r=1.0
+ designationSourceTypeMask:i=1
+ constantDesignationSourceTypeMask:i=0
+ aircraftAsTarget:b=no
+ groundVehiclesAsTarget:b=yes
+ surfaceAsTarget:b=yes
+ boundaryTrack:b=yes
+ rangeBand1:r=20000.0
+ }
+ 
+ guidanceAutopilot{
+ timeOut:r=1.5
+ loftEnabled:b=yes
+ loftElevation:r=10.0
+ loftTargetElevation:r=-15.0
+ loftAngleToAccelMult:r=10.0
+ loftTargetOmegaMax:r=0.75
+ baseIndSpeed:r=1800.0
+ propNavMult:r=4.0
+ reqAccelMax:r=2.5
+ accelControlProp:r=0.0701
+ accelControlIntg:r=0.09
+ accelControlIntgLim:r=1.0
+ accelControlDiff:r=0.0005
+ }
+ }
+ 
+ stabilityRicochetModifier{
+ mod1:p2=0.0, 0.5
+ mod2:p2=15.0, 0.7
+ mod3:p2=30.0, 0.99
+ }
+ 
+ pressureDamage{
+ damageType:t="pressure"
+ }
+ 
+ damage{
+ 
+ explosive{
+ offset:r=1.0
+ }
+ }
+ 
+ DamageParts{
+ 
+ body{
+ hp:r=50.0
+ armorClass:t="tank_structural_steel"
+ armorThickness:r=1.0
+ }
+ }
+ 
+ DamageEffects{
+ 
+ part{
+ name:t="body"
+ 
+ onHit{
+ shellState:t="inFlight"
+ expl:r=1.0
+ }
+ 
+ onHit{
+ shellState:t="onUnit"
+ damageType:t="generic"
+ expl:r=0.05
+ fire:r=0.45
+ break:r=0.5
+ damage:r=3.0
+ fHitCritical:b=yes
+ }
+ 
+ onHit{
+ shellState:t="onUnit"
+ damageType:t="generic"
+ expl:r=0.5
+ fire:r=0.3
+ break:r=0.2
+ damage:r=30.0
+ fHitCritical:b=yes
+ }
+ 
+ onHit{
+ shellState:t="onUnit"
+ damageType:t="explosion"
+ expl:r=0.45
+ fire:r=0.45
+ break:r=0.1
+ damage:r=50.0
+ fHitCritical:b=yes
+ }
+ 
+ onHit{
+ shellState:t="onUnit"
+ damageType:t="cumulative"
+ expl:r=0.4
+ fire:r=0.4
+ break:r=0.1
+ damage:r=100.0
+ fHitCritical:b=yes
+ }
+ 
+ onKill{
+ shellState:t="inFlight"
+ destruction:r=1.0
+ }
+ 
+ onKill{
+ shellState:t="onUnit"
+ expl:r=0.05
+ fire:r=0.05
+ break:r=0.9
+ fHitCritical:b=yes
+ }
+ }
+ }
+ 
+ shatterCollisions{
+ groundCollisionEffect:t="hit_12_18mm_dirt_ap"
+ waterCollisionEffect:t="hit_8_11mm_water"
+ 
+ default{
+ fx:t="hit_12_18mm_dirt_ap"
+ }
+ 
+ horLandMesh{
+ fx:t="hit_12_18mm_dirt_ap"
+ }
+ 
+ soil{
+ fx:t="hit_12_18mm_dirt_ap"
+ }
+ 
+ dirt{
+ fx:t="hit_12_18mm_dirt_ap"
+ }
+ 
+ road{
+ fx:t="hit_12_18mm_dirt_ap"
+ }
+ 
+ bricks_red{
+ fx:t="hit_12_18mm_red_brick_ap"
+ }
+ 
+ roadSoil{
+ fx:t="hit_12_18mm_dirt_ap"
+ }
+ 
+ sand{
+ fx:t="hit_12_18mm_sand_ap"
+ }
+ 
+ duneSand{
+ fx:t="hit_12_18mm_sand_ap"
+ }
+ 
+ roadSand{
+ fx:t="hit_12_18mm_sand_ap"
+ }
+ 
+ quickSand{
+ fx:t="hit_12_18mm_sand_ap"
+ }
+ 
+ snow{
+ fx:t="hit_12_18mm_snow_ap"
+ }
+ 
+ ice{
+ fx:t="hit_12_18mm_snow_ap"
+ }
+ 
+ roadSnow{
+ fx:t="hit_12_18mm_snow_ap"
+ }
+ 
+ snowLower{
+ fx:t="hit_12_18mm_snow_ap"
+ }
+ 
+ glass{
+ fx:t="hit_12_18mm_metal_ap"
+ }
+ 
+ wood{
+ fx:t="hit_12_18mm_wood_ap"
+ }
+ 
+ steel{
+ fx:t="hit_12_18mm_metal_ap"
+ }
+ 
+ metal{
+ fx:t="hit_12_18mm_metal_ap"
+ }
+ 
+ tank_structural_steel{
+ fx:t="hit_12_18mm_metal_ap"
+ }
+ 
+ aluminum_armor{
+ fx:t="hit_12_18mm_metal_ap"
+ }
+ 
+ tank_rubber_screens{
+ fx:t="hit_12_18mm_stone_ap"
+ }
+ 
+ buildings{
+ fx:t="hit_12_18mm_stone_ap"
+ }
+ 
+ verLandMesh{
+ fx:t="hit_12_18mm_stone_ap"
+ }
+ 
+ concrete{
+ fx:t="hit_12_18mm_stone_ap"
+ }
+ 
+ rocks{
+ fx:t="hit_12_18mm_stone_ap"
+ }
+ 
+ rocksSlippery{
+ fx:t="hit_12_18mm_stone_ap"
+ }
+ 
+ fabric{
+ fx:t="hit_12_18mm_stone_ap"
+ }
+ 
+ stone_snow{
+ fx:t="hit_12_18mm_snow_ap"
+ }
+ 
+ armorPierceLowCal{
+ fx:t="hit_12_18mm_metal_ap"
+ }
+ 
+ armorPierceMedCal{
+ fx:t="hit_12_18mm_metal_ap"
+ }
+ 
+ armorPierceHiCal{
+ fx:t="hit_12_18mm_metal_ap"
+ }
+ 
+ armorNPLowCal{
+ fx:t="hit_12_18mm_metal_ap"
+ }
+ 
+ armorNPMedCal{
+ fx:t="hit_12_18mm_metal_ap"
+ }
+ 
+ armorNPHiCal{
+ fx:t="hit_12_18mm_metal_ap"
+ }
+ }
+ 
+ collisions{
+ 
+ steel{
+ fx:t="explosion_midair_big"
+ ricochetFx:t="hit_81_105mm_metal_ap"
+ }
+ 
+ aluminum_armor{
+ fx:t="explosion_midair_big"
+ ricochetFx:t="hit_81_105mm_metal_ap"
+ }
+ 
+ tank_structural_steel{
+ fx:t="explosion_midair_big"
+ ricochetFx:t="hit_81_105mm_metal_ap"
+ }
+ 
+ armor{
+ fx:t="explosion_midair_big"
+ ricochetFx:t="hit_81_105mm_metal_ap"
+ }
+ 
+ buildings{
+ fx:t="explosion_midair_big"
+ ricochetFx:t="hit_106_132mm_stone_ap"
+ }
+ 
+ wood{
+ fx:t="explosion_midair_big"
+ ricochetFx:t="hit_106_132mm_wood_ap"
+ }
+ }
+ }
```

  **Removed**:
```diff
```


- **aces.vromfs.bin_u/gamedata/weapons/bombguns/us_2000lb_gbu_15v1.blkx**:

  **Added**:
```diff
+ boundaryTrack:b=yes
```

  **Removed**:
```diff
```


- **aces.vromfs.bin_u/gamedata/weapons/bombguns/us_2000lb_gbu_15v2.blkx**:

  **Added**:
```diff
+ boundaryTrack:b=yes
```

  **Removed**:
```diff
```


- **aces.vromfs.bin_u/gamedata/weapons/bombguns/us_2000lb_gbu_15v21.blkx**:

  **Added**:
```diff
+ boundaryTrack:b=yes
```

  **Removed**:
```diff
```


- **aces.vromfs.bin_u/gamedata/weapons/bombguns/us_2000lb_gbu_15v22.blkx**:

  **Added**:
```diff
+ boundaryTrack:b=yes
```

  **Removed**:
```diff
```


- **aces.vromfs.bin_u/gamedata/weapons/bombguns/us_2000lb_gbu_8_hobos.blkx**:

  **Added**:
```diff
+ boundaryTrack:b=yes
```

  **Removed**:
```diff
```


- **aces.vromfs.bin_u/gamedata/weapons/bombguns/us_agm_62a.blkx**:

  **Added**:
```diff
+ boundaryTrack:b=yes
```

  **Removed**:
```diff
```


- **aces.vromfs.bin_u/gamedata/weapons/bombguns/us_agm_62a_er.blkx**:

  **Added**:
```diff
+ boundaryTrack:b=yes
```

  **Removed**:
```diff
```


- **aces.vromfs.bin_u/gamedata/weapons/groundmodels_weapons/155mm_l52_user_cannon.blkx**:

  **Added**:
```diff
+ shotFreq:r=0.2
+ speed:r=945.0
+ speed:r=945.0
+ speed:r=945.0
+ speed:r=945.0
```

  **Removed**:
```diff
- shotFreq:r=0.1
- speed:r=563.0
- speed:r=563.0
- speed:r=580.0
- speed:r=563.0
```


- **aces.vromfs.bin_u/gamedata/weapons/groundmodels_weapons/155mm_soltam_user_cannon.blkx**:

  **Added**:
```diff
+ shotFreq:r=0.1334
```

  **Removed**:
```diff
- shotFreq:r=0.084
```


- **aces.vromfs.bin_u/gamedata/weapons/groundmodels_weapons/239mm_9m331_user_cannon.blkx**:

  **Added**:
```diff
+ beaconBand:i=5
+ beaconBand:i=5
```

  **Removed**:
```diff
```


- **aces.vromfs.bin_u/gamedata/weapons/groundmodels_weapons/239mm_hq_17_user_cannon.blkx**:

  **Added**:
```diff
+ beaconBand:i=5
+ beaconBand:i=5
```

  **Removed**:
```diff
```


- **aces.vromfs.bin_u/gamedata/weapons/rocketguns/us_aim9l_i_1_sidewinder.blkx**:

  **Added**:
```diff
+ fireEffect:t="fires_exhaust_jet_mach_discs_small"
+ smokeEffect:t="smoke_rocket_tail_light"
+ smokeEffect2:t=""
+ hazeEffect:t="haze_missile"
+ endSmokeViscosity:r=0.05
```

  **Removed**:
```diff
- smokeEffect:t="smoke_rocket_tail_short"
- smokeEffect2:t=""
- hazeEffect:t="haze_missile"
- endSmokeViscosity:r=0.05
- fireEffect:t="fires_exhaust_jet_mach_discs_small"
```


- **aces.vromfs.bin_u/gamedata/weapons/rocketguns/us_aim9l_i_1_sidewinder_default.blkx**:

  **Added**:
```diff
+ fireEffect:t="fires_exhaust_jet_mach_discs_small"
+ smokeEffect:t="smoke_rocket_tail_light"
+ smokeEffect2:t=""
+ hazeEffect:t="haze_missile"
+ endSmokeViscosity:r=0.05
```

  **Removed**:
```diff
- smokeEffect:t="smoke_rocket_tail_short"
- smokeEffect2:t=""
- hazeEffect:t="haze_missile"
- endSmokeViscosity:r=0.05
- fireEffect:t="fires_exhaust_jet_mach_discs_small"
```


---
