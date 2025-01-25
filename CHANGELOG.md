### Full Changelog:

- **aces.vromfs.bin_u/config/damagemodel.blkx**:

  **Added**:
```diff
+ fr_m46_patton:i=140
+ uk_shir_2:i=140
```

  **Removed**:
```diff
```


- **aces.vromfs.bin_u/config/gui.blkx**:

  **Added**:
```diff
+ login_layer_m46_france:r=8.0
+ login_layer_m46_france:t="loading_screen_m46_france"
+ battlepass_season18:t="battlepass_season18_purchased_main/name"
```

  **Removed**:
```diff
```


- **aces.vromfs.bin_u/config/rendinst_dmg.blkx**:

  **Added**:
```diff
+ dmg{
+ name:t="rheinland_obelisk_a"
+ immortal:b=yes
+ useVsm:b=yes
+ }
+ 
```

  **Removed**:
```diff
```


- **aces.vromfs.bin_u/config/workshop.blkx**:

  **Added**:
```diff
+ items{
+ setId:t="storm_warning"
+ locId:t="workshop/storm_warning"
+ alwaysVisibleItem:i=660405
+ alwaysVisibleItem:i=660408
+ alwaysVisibleItem:i=660409
+ alwaysVisibleItem:i=660410
+ alwaysVisibleItem:i=660411
+ }
+ 
```

  **Removed**:
```diff
```


- **aces.vromfs.bin_u/gamedata/attachables/decor_heybox_guai.blkx**:

  **Added**:
```diff
+ model:t="decor_heybox_guai"
+ collision:t="decor_heybox_guai_collision"
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


- **aces.vromfs.bin_u/gamedata/attachables/lrac_f1.blkx**:

  **Added**:
```diff
+ model:t="lrac_f1"
+ collision:t="lrac_f1_collision"
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


- **aces.vromfs.bin_u/gamedata/attachables/mas_49_56.blkx**:

  **Added**:
```diff
+ model:t="mas_49_56"
+ collision:t="mas_49_56_collision"
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


- **aces.vromfs.bin_u/gamedata/attachables/mo_120_rt_f1.blkx**:

  **Added**:
```diff
+ model:t="mo_120_rt_f1"
+ collision:t="mo_120_rt_f1_collision"
+ bboxMult:r=0.1
+ breakFx:t="destruction_decorators_model_med"
+ mass:r=250.0
+ 
+ DamageParts{
+ 
+ body{
+ hp:r=2000.0
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
+ onKill{
+ cut:r=1.0
+ }
+ }
+ }
```

  **Removed**:
```diff
```


- **aces.vromfs.bin_u/gamedata/flightmodels/a_10c.blkx**:

  **Added**:
```diff
+ text:t="E2K"
```

  **Removed**:
```diff
- text:t="EF2K"
```


- **aces.vromfs.bin_u/gamedata/flightmodels/av_8b_na.blkx**:

  **Added**:
```diff
+ text:t="E2K"
```

  **Removed**:
```diff
- text:t="EF2K"
```


- **aces.vromfs.bin_u/gamedata/flightmodels/av_8b_plus.blkx**:

  **Added**:
```diff
+ text:t="E2K"
```

  **Removed**:
```diff
- text:t="EF2K"
```


- **aces.vromfs.bin_u/gamedata/flightmodels/av_8b_plus_italy.blkx**:

  **Added**:
```diff
+ text:t="E2K"
```

  **Removed**:
```diff
- text:t="EF2K"
```


- **aces.vromfs.bin_u/gamedata/flightmodels/f-4ej_kai.blkx**:

  **Added**:
```diff
+ text:t="E2K"
```

  **Removed**:
```diff
- text:t="EF2K"
```


- **aces.vromfs.bin_u/gamedata/flightmodels/f_14a_early.blkx**:

  **Added**:
```diff
+ text:t="E2K"
```

  **Removed**:
```diff
- text:t="EF2K"
```


- **aces.vromfs.bin_u/gamedata/flightmodels/f_14b.blkx**:

  **Added**:
```diff
+ text:t="E2K"
```

  **Removed**:
```diff
- text:t="EF2K"
```


- **aces.vromfs.bin_u/gamedata/flightmodels/f_15a.blkx**:

  **Added**:
```diff
+ text:t="E2K"
```

  **Removed**:
```diff
- text:t="EF2K"
```


- **aces.vromfs.bin_u/gamedata/flightmodels/f_15a_iaf.blkx**:

  **Added**:
```diff
+ text:t="E2K"
```

  **Removed**:
```diff
- text:t="EF2K"
```


- **aces.vromfs.bin_u/gamedata/flightmodels/f_15c_baz_msip.blkx**:

  **Added**:
```diff
+ text:t="E2K"
```

  **Removed**:
```diff
- text:t="EF2K"
```


- **aces.vromfs.bin_u/gamedata/flightmodels/f_15c_msip2.blkx**:

  **Added**:
```diff
+ text:t="E2K"
```

  **Removed**:
```diff
- text:t="EF2K"
```


- **aces.vromfs.bin_u/gamedata/flightmodels/f_15e.blkx**:

  **Added**:
```diff
+ text:t="E2K"
```

  **Removed**:
```diff
- text:t="EF2K"
```


- **aces.vromfs.bin_u/gamedata/flightmodels/f_15j.blkx**:

  **Added**:
```diff
+ text:t="E2K"
```

  **Removed**:
```diff
- text:t="EF2K"
```


- **aces.vromfs.bin_u/gamedata/flightmodels/f_15j_kai.blkx**:

  **Added**:
```diff
+ text:t="E2K"
```

  **Removed**:
```diff
- text:t="EF2K"
```


- **aces.vromfs.bin_u/gamedata/flightmodels/ffa_p16.blkx**:

  **Added**:
```diff
+ order:i=13
+ order:i=15
+ order:i=13
+ order:i=15
+ emitter:t="4_sura_rocket_pylon_008"
+ order:i=14
+ emitter:t="4_sura_rocket_pylon_007"
+ order:i=16
+ emitter:t="4_sura_rocket_pylon_008"
+ order:i=14
+ emitter:t="4_sura_rocket_pylon_007"
+ order:i=16
```

  **Removed**:
```diff
- order:i=13
- emitter:t="4_sura_rocket_pylon_007"
- emitter:t="4_sura_rocket_pylon_008"
- emitter:t="4_sura_rocket_pylon_007"
- emitter:t="4_sura_rocket_pylon_008"
```


- **aces.vromfs.bin_u/gamedata/flightmodels/fm/amx_a_1a_brazil.blkx**:

  **Added**:
```diff
+ Num:i=0
```

  **Removed**:
```diff
- Num:i=1
```


- **aces.vromfs.bin_u/gamedata/flightmodels/fm/amx_italy.blkx**:

  **Added**:
```diff
+ Num:i=0
```

  **Removed**:
```diff
- Num:i=1
```


- **aces.vromfs.bin_u/gamedata/flightmodels/fm/j7w1.blkx**:

  **Added**:
```diff
+ CdMin:r=0.0077
+ CdMin:r=0.0074
+ OswaldsEfficiencyNumber:r=0.7
+ Direction:p2=-0.0, -3.0
+ PowerConstRPMCurvature0:r=1.0
+ SpeedManifoldMultiplier:r=0.4
+ EmptyMass:r=3990.0
```

  **Removed**:
```diff
- CdMin:r=0.009
- CdMin:r=0.0079
- OswaldsEfficiencyNumber:r=0.9
- Direction:p2=-0.0, 0.0
- PowerConstRPMCurvature0:r=0.7
- SpeedManifoldMultiplier:r=0.7
- EmptyMass:r=4400.0
```


- **aces.vromfs.bin_u/gamedata/flightmodels/fm/p-61a_1.blkx**:

  **Added**:
```diff
+ Num:i=0
+ Num:i=0
```

  **Removed**:
```diff
- Num:i=1
- Num:i=1
```


- **aces.vromfs.bin_u/gamedata/flightmodels/fm/p-61c_1.blkx**:

  **Added**:
```diff
+ UseTime:r=5.0
+ Power:r=2500.0
+ UseTime:r=5.0
+ Power:r=2500.0
```

  **Removed**:
```diff
- UseTime:r=0.0
- Power:r=0.0
- UseTime:r=0.0
- Power:r=0.0
```


- **aces.vromfs.bin_u/gamedata/flightmodels/fm/rafale_c_f3.blkx**:

  **Added**:
```diff
+ MultMachMax5:r=0.7
+ MultLineCoeff5:r=0.12
+ MultMachMax5:r=0.7
+ MultLineCoeff5:r=0.12
+ FullBrakeSlidingFrictionMult:p4=2.0, 1.35, 50.0, 0.7
+ FullBrakeSlidingFrictionMult:p4=2.0, 1.35, 50.0, 0.7
+ FullBrakeSlidingFrictionMult:p4=2.0, 0.65, 50.0, 0.6
```

  **Removed**:
```diff
- MultMachMax5:r=0.81
- MultLineCoeff5:r=0.05
- MultMachMax5:r=0.81
- MultLineCoeff5:r=0.05
- FullBrakeSlidingFrictionMult:p4=2.0, 1.35, 50.0, 0.4
- FullBrakeSlidingFrictionMult:p4=2.0, 1.35, 50.0, 0.4
- FullBrakeSlidingFrictionMult:p4=2.0, 0.65, 50.0, 0.4
```


- **aces.vromfs.bin_u/gamedata/flightmodels/fm/typhoon_mk1a.blkx**:

  **Added**:
```diff
+ flapsLimByIas:p4=180.0, 315.0, 1.0, 0.0
+ mechLockIas:r=315.0
+ FlapsDestructionIndSpeedP2:p2=1.0, 315.0
```

  **Removed**:
```diff
- flapsLimByIas:p4=180.0, 280.0, 1.0, 0.0
- mechLockIas:r=280.0
- FlapsDestructionIndSpeedP2:p2=1.0, 280.0
```


- **aces.vromfs.bin_u/gamedata/flightmodels/fm/typhoon_mk1b.blkx**:

  **Added**:
```diff
+ flapsLimByIas:p4=180.0, 315.0, 1.0, 0.0
+ mechLockIas:r=315.0
+ FlapsDestructionIndSpeedP2:p2=1.0, 320.0
```

  **Removed**:
```diff
- flapsLimByIas:p4=180.0, 280.0, 1.0, 0.0
- mechLockIas:r=280.0
- FlapsDestructionIndSpeedP2:p2=1.0, 280.0
```


- **aces.vromfs.bin_u/gamedata/flightmodels/fm/typhoon_mk1b_late.blkx**:

  **Added**:
```diff
+ flapsLimByIas:p4=180.0, 315.0, 1.0, 0.0
+ mechLockIas:r=315.0
+ FlapsDestructionIndSpeedP2:p2=1.0, 320.0
```

  **Removed**:
```diff
- flapsLimByIas:p4=180.0, 280.0, 1.0, 0.0
- mechLockIas:r=280.0
- FlapsDestructionIndSpeedP2:p2=1.0, 280.0
```


- **aces.vromfs.bin_u/gamedata/flightmodels/j7w1.blkx**:

  **Added**:
```diff
+ instructorCritMult:p2=0.9, 0.9
```

  **Removed**:
```diff
- instructorCritMult:p2=0.8, 0.8
```


- **aces.vromfs.bin_u/gamedata/flightmodels/sb2c_5_thailand.blkx**:

  **Added**:
```diff
+ model:t="sb2c_5"
+ fmFile:t="fm/sb2c_4.blk"
+ MetaPartsBlk:t="gameData/FlightModels/dm/metaparts/1x_engine_bomber_metaparts.blk"
+ exhaustEffectsBlk:t="gameData/FlightModels/exhaustEffects/exhaustEffects_common.blk"
+ gyroSight:b=no
+ type:t="typeBomber"
+ type:t="typeDiveBomber"
+ paratrooper:t="usa_para"
+ flapsIsAirbrakes:b=yes
+ overheatBlk:t="gameData/FlightModels/dm/overheat.blk"
+ damagePartsToCollisionObjectsMapBlk:t="gameData/FlightModels/DM/dm_parts_to_collision_objects.blk"
+ damagePartsToFmPartsMapBlk:t="gameData/FlightModels/DM/dm_parts_to_fm_parts_map.blk"
+ damagePartsToHudPartsMapBlk:t="gameData/FlightModels/DM/dm_parts_to_hud_parts_map.blk"
+ damagePartsDependencyMapBlk:t="gameData/FlightModels/DM/dm_parts_additional_dependency_map.blk"
+ damagePartsToCollisionPointsMapBlk:t="gameData/FlightModels/DM/dm_parts_to_collision_points_map.blk"
+ damagePartsToWeaponsMapBlk:t="gameData/FlightModels/DM/dm_parts_to_weapons_map.blk"
+ damagePartsToAvionicsPartsMapBlk:t="gameData/FlightModels/DM/dm_parts_to_avionics_parts_map.blk"
+ damagePartsToVisualEffectsMapBlk:t="gameData/FlightModels/DM/dm_parts_to_visual_effects_map.blk"
+ damagePartsExcludeFromHoleBlk:t="gameData/FlightModels/DM/dm_parts_exclude_from_hole.blk"
+ explosion_dmBlk:t="gameData/FlightModels/DM/commonExplosion.blk"
+ fireParamsPreset:t="500kph"
+ fightAiBehaviour:t="diveBomber"
+ 
+ hook{
+ coeffHookJ:r=0.03
+ hookDeflectionAngles:p2=-40.0, 70.0
+ hookCxDiap:p2=0.2, 0.9
+ hookMass:r=4.0
+ }
+ 
+ Params{
+ Range:r=2100.2
+ }
+ 
+ Sound{
+ turretTurnSfxPath:t="sounds/effects"
+ turretTurnSfxPathStudio:t="aircraft/effects"
+ turretTurnSfxName:t="gun_turn_manual"
+ Engine:t="engine03"
+ gun:t="gun_default"
+ }
+ 
+ cockpit{
+ headPos:p3=-0.088, 1.1, 0.0
+ headPosOnShooting:p3=0.0, 1.1, 0.0
+ lightPos:p3=0.3, 0.743, 0.37
+ lightColor:p3=0.62, 0.3, 0.21
+ lightAttenuation:r=10.0
+ openedGunnerCockpit:b=yes
+ 
+ devices{
+ speed:p2=0.0, 221.21
+ pedals1:p2=-1.0, 1.0
+ pedals2:p2=-1.0, 1.0
+ stick_ailerons:p2=-1.0, 1.0
+ stick_elevator:p2=-1.0, 1.0
+ throttle:p2=0.0, 1.0
+ mixture:p2=0.0, 1.0
+ prop_pitch:p2=0.0, 1.0
+ supercharger:p2=0.0, 1.0
+ weapon2:p2=0.0, 1.0
+ weapon3:p2=0.0, 1.0
+ gears:p2=0.0, 1.0
+ gear_fixed:b=yes
+ flaps:p2=0.0, 1.0
+ flaps_fixed:b=yes
+ gears_lamp:p2=0.0, 0.0
+ trimmer:p2=-1.0, 1.0
+ aviahorizon_pitch:p2=-60.0, 60.0
+ aviahorizon_roll:p2=-180.0, 180.0
+ altitude_10k:p2=0.0, 40000.0
+ altitude_hour:p2=0.0, 10000.0
+ altitude_min:p2=0.0, 1000.0
+ altitude_koef:r=3.28
+ vario:p2=-30.0, 30.0
+ compass:p2=0.0, 360.0
+ compass1:p2=0.0, 360.0
+ compass2:p2=0.0, 360.0
+ bank:p2=-8.0, 8.0
+ bank1:p2=-8.0, 8.0
+ turn:p2=-0.23562, 0.23562
+ clock_hour:p2=0.0, 24.0
+ clock_min:p2=0.0, 60.0
+ clock_sec:p2=0.0, 60.0
+ manifold_pressure:p2=0.3453, 1.727
+ rpm_hour:p2=0.0, 3500.0
+ rpm_min:p2=0.0, 1000.0
+ oil_temperature:p2=0.0, 100.0
+ water_temperature:p2=0.0, 140.0
+ carb_temperature:p2=-50.0, 50.0
+ head_temperature:p2=0.0, 350.0
+ fuel:p2=0.0, 281.0
+ fuel1:p2=0.0, 332.0
+ fuel2:p2=0.0, 268.0
+ fuel3:p2=0.0, 268.0
+ oil_pressure:p2=0.0, 200.0
+ fuel_pressure:p2=0.0, 15.0
+ }
+ 
+ parts_holes_dmg{
+ part:t="fuse"
+ }
+ 
+ parts_oil_dmg{
+ part:t="engine1"
+ part:t="engine2"
+ part:t="engine3"
+ part:t="engine4"
+ }
+ }
+ 
+ flexWing{
+ wingStrainCoeff:r=0.2
+ wingOverloadCoeff:r=1.0
+ wingStrainLimitDown:r=1.0
+ }
+ 
+ commonWeapons{
+ 
+ Weapon{
+ slot:i=0
+ preset:t="default_common"
+ }
+ }
+ 
+ gunnerFps{
+ pos:p3=-0.2, 0.7, 0.0
+ head:t="turret1"
+ }
+ 
+ weapon_presets{
+ 
+ preset{
+ name:t="sb2c_5_5in_rockets"
+ blk:t="gameData/FlightModels/weaponPresets/sb2c_5_5in_rockets.blk"
+ }
+ 
+ preset{
+ name:t="sb2c_5_250lbs_bombs"
+ blk:t="gameData/FlightModels/weaponPresets/sb2c_5_250lbs_bombs.blk"
+ }
+ 
+ preset{
+ name:t="sb2c_5_500lbs_bombs"
+ blk:t="gameData/FlightModels/weaponPresets/sb2c_5_500lbs_bombs.blk"
+ }
+ 
+ preset{
+ name:t="sb2c_5_1000lbs_bombs"
+ blk:t="gameData/FlightModels/weaponPresets/sb2c_5_1000lbs_bombs.blk"
+ }
+ 
+ preset{
+ name:t="sb2c_5_1000lbs_bombs_external"
+ blk:t="gameData/FlightModels/weaponPresets/sb2c_5_1000lbs_bombs_external.blk"
+ }
+ 
+ preset{
+ name:t="sb2c_5_1600lbs_bombs"
+ blk:t="gameData/FlightModels/weaponPresets/sb2c_5_1600lbs_bombs.blk"
+ 
+ weaponConfig{
+ presetType:t="AIR_TO_SEA"
+ }
+ }
+ 
+ preset{
+ name:t="sb2c_5_1x2000lbs"
+ blk:t="gameData/FlightModels/weaponPresets/sb2c_5_1x2000lbs.blk"
+ }
+ 
+ preset{
+ name:t="sb2c_5_torpedo"
+ blk:t="gameData/FlightModels/weaponPresets/sb2c_5_torpedo.blk"
+ }
+ 
+ preset{
+ name:t="sb2c_5_torpedo_case"
+ blk:t="gameData/FlightModels/weaponPresets/sb2c_5_torpedo_case.blk"
+ }
+ 
+ preset{
+ name:t="sb2c_5_dgp_1"
+ blk:t="gameData/FlightModels/weaponPresets/sb2c_5_dgp_1.blk"
+ }
+ }
+ 
+ jetwash{
+ radius:r=10.0
+ minDist:r=50.0
+ timeToLive:r=45.0
+ maxPower:r=6.0
+ maxSegments:i=50
+ }
+ 
+ turbulence{
+ segmentlength:r=100.0
+ startSpeed:r=28.0
+ maxSpeed:r=140.0
+ maxPower:r=6.0
+ initialRadius:r=12.0
+ radiusSpeed:r=2.0
+ }
+ 
+ fireParams{
+ engineExtinguishFireSpeed:p2=82.0, 166.0
+ engineExtinguishFireSpeedChance:p2=0.01, 0.1
+ fireDamagePowerRel:r=0.05
+ nonExtinguishFireTime:r=5.0
+ }
+ 
+ wiki{
+ 
+ general{
+ length:r=11.1732
+ wingspan:r=15.1591
+ wingArea:r=39.21
+ emptyWeight:r=5222.0
+ normalWeight:r=6346.0
+ maxTakeoffWeight:r=7538.0
+ powerPlantType:i=1
+ powerMaxWep:r=1910.0
+ powerMaxMil:r=1750.0
+ }
+ 
+ performance{
+ 
+ table{
+ rpmWep:r=2800.0
+ manifoldPressureWep:r=1.64
+ airSpeedWep0:p2=0.0, 431.0
+ airSpeedWep1:p2=1000.0, 446.0
+ airSpeedWep2:p2=5200.0, 463.0
+ climbRateWep0:p2=0.0, 6.1
+ climbRateWep1:p2=400.0, 5.9
+ climbRateWep2:p2=4700.0, 1.8
+ climbTimeWep0:p2=2000.0, 196.691
+ climbTimeWep1:p2=4000.0, 466.022
+ climbTimeWep2:p2=6000.0, 766.196
+ climbTimeWep3:p2=8000.0, 1281.06
+ turnTimeWep:p2=1000.0, 23.0
+ rpmMil:r=2600.0
+ manifoldPressureMil:r=1.45
+ airSpeedMil0:p2=0.0, 414.0
+ airSpeedMil1:p2=1600.0, 438.0
+ airSpeedMil2:p2=5300.0, 465.0
+ climbRateMil0:p2=0.0, 5.0
+ climbRateMil1:p2=1100.0, 4.9
+ climbRateMil2:p2=4700.0, 1.8
+ climbTimeMil0:p2=2000.0, 199.146
+ climbTimeMil1:p2=4000.0, 459.476
+ climbTimeMil2:p2=6000.0, 759.664
+ climbTimeMil3:p2=8000.0, 1274.53
+ turnTimeMil:p2=1000.0, 23.1
+ takeoffDistance:r=589.633
+ ceiling:r=9200.0
+ rollRate:r=77.0
+ wingLoading:r=162.0
+ powerToWeightRatio:r=0.28
+ }
+ 
+ plot{
+ airSpeedWep0:p2=0.0, 431.0
+ airSpeedWep1:p2=1000.0, 446.0
+ airSpeedWep2:p2=3000.0, 426.0
+ airSpeedWep3:p2=5200.0, 463.0
+ airSpeedWep4:p2=8000.0, 442.0
+ airSpeedWep5:p2=9200.0, 417.0
+ climbRateWep0:p2=0.0, 6.1
+ climbRateWep1:p2=300.0, 6.1
+ climbRateWep2:p2=2200.0, 2.7
+ climbRateWep3:p2=2500.0, 1.6
+ climbRateWep4:p2=2600.0, 1.8
+ climbRateWep5:p2=2700.0, 0.9
+ climbRateWep6:p2=2800.0, 2.0
+ climbRateWep7:p2=4700.0, 1.8
+ climbRateWep8:p2=9200.0, -4.3
+ airSpeedMil0:p2=0.0, 414.0
+ airSpeedMil1:p2=1500.0, 440.0
+ airSpeedMil2:p2=3100.0, 427.0
+ airSpeedMil3:p2=5300.0, 465.0
+ airSpeedMil4:p2=7900.0, 443.0
+ airSpeedMil5:p2=9200.0, 420.0
+ climbRateMil0:p2=0.0, 5.0
+ climbRateMil1:p2=1100.0, 4.9
+ climbRateMil2:p2=2700.0, 2.2
+ climbRateMil3:p2=4700.0, 1.8
+ climbRateMil4:p2=9200.0, -4.3
+ }
+ }
+ }
+ 
+ balanceData{
+ accSpd:r=1.3211
+ climbSpeed:r=6.12
+ maxSpeed:r=125.1
+ turnTime:r=23.0
+ }
+ 
+ modifications{
+ 
+ CdMin_Fuse{
+ tier:i=1
+ modClass:t="lth"
+ }
+ 
+ structure_str{
+ prevModification:t="CdMin_Fuse"
+ tier:i=2
+ modClass:t="lth"
+ }
+ 
+ cd_98{
+ prevModification:t="structure_str"
+ tier:i=3
+ modClass:t="lth"
+ }
+ 
+ new_cover{
+ prevModification:t="cd_98"
+ tier:i=4
+ modClass:t="lth"
+ }
+ 
+ new_radiator{
+ tier:i=1
+ modClass:t="lth"
+ }
+ 
+ new_compressor{
+ prevModification:t="new_radiator"
+ tier:i=2
+ modClass:t="lth"
+ }
+ 
+ hp_105{
+ prevModification:t="new_compressor"
+ tier:i=3
+ modClass:t="lth"
+ }
+ 
+ new_engine_injection{
+ prevModification:t="hp_105"
+ tier:i=4
+ modClass:t="lth"
+ }
+ 
+ an_m2_universal{
+ }
+ 
+ an_m2_ground_targets{
+ }
+ 
+ an_m2_air_targets{
+ }
+ 
+ an_m2_stealth{
+ }
+ 
+ 30cal_turret_ap{
+ }
+ 
+ tbf_itc{
+ modClass:t="weapon"
+ tier:i=1
+ }
+ 
+ improved_torpedo_mod{
+ modClass:t="weapon"
+ tier:i=2
+ reqModification:t="tbf_itc"
+ }
+ 
+ btd_sbc{
+ modClass:t="weapon"
+ tier:i=3
+ reqModification:t="improved_torpedo_mod"
+ }
+ 
+ btd_mbc{
+ modClass:t="weapon"
+ tier:i=4
+ reqModification:t="btd_sbc"
+ }
+ 
+ us_2000lb_m66{
+ modClass:t="weapon"
+ tier:i=4
+ reqModification:t="btd_mbc"
+ }
+ 
+ frc_mk2{
+ tier:i=4
+ modClass:t="weapon"
+ }
+ 
+ bmg30_turret_belt_pack{
+ tier:i=2
+ }
+ 
+ bmg30_turret_new_gun{
+ reqModification:t="bmg30_turret_belt_pack"
+ tier:i=3
+ }
+ 
+ dgp-1_gunpod{
+ tier:i=1
+ modClass:t="weapon"
+ }
+ 
+ 50cal_universal{
+ }
+ 
+ 50cal_ground_targets{
+ }
+ 
+ 50cal_tracers{
+ }
+ 
+ 50cal_stealth{
+ }
+ 
+ bmg50_belt_pack{
+ reqModification:t="dgp-1_gunpod"
+ tier:i=1
+ }
+ 
+ bmg50_new_gun{
+ reqModification:t="bmg50_belt_pack"
+ tier:i=2
+ }
+ 
+ anm2_belt_pack{
+ }
+ 
+ anm2_new_gun{
+ reqModification:t="anm2_belt_pack"
+ }
+ }
+ 
+ user_skin{
+ name:t="sb2c_5"
+ 
+ replace_tex{
+ from:t="sb2c_5_a*"
+ }
+ 
+ replace_tex{
+ from:t="sb2c_5_n*"
+ }
+ }
+ 
+ cutting{
+ _emtr_break_wing0_l_from:p3=-1.18567, -0.138279, 1.13969
+ _emtr_break_wing0_l_to:p3=-1.18567, -0.138279, 2.03061
+ emtr_break_wing1_l_from:p3=-1.18567, -0.138279, 3.36699
+ emtr_break_wing1_l_to:p3=-1.18567, -0.138279, 4.12487
+ _emtr_break_wing0_r_from:p3=-1.18567, -0.138279, -1.13969
+ _emtr_break_wing0_r_to:p3=-1.18567, -0.138279, -2.03061
+ emtr_break_wing1_r_from:p3=-1.18567, -0.138279, -3.36699
+ emtr_break_wing1_r_to:p3=-1.18567, -0.138279, -4.12487
+ emtr_break_wing_tail:p3=-3.7967, 0.0, 0.0
+ finCut:b=no
+ emtr_break_stab_l_from:p3=-5.46471, 0.866208, 0.631988
+ emtr_break_stab_l_to:p3=-5.46471, 0.866208, 2.32509
+ emtr_break_stab_r_from:p3=-5.46471, 0.866208, -0.631988
+ emtr_break_stab_r_to:p3=-5.46471, 0.866208, -2.32509
+ emtr_break_fin_from:p3=-5.59832, 1.37451, 0.00188086
+ emtr_break_fin_to:p3=-5.59832, 2.60958, 0.00188086
+ }
+ 
+ DamageParts{
+ 
+ armor10{
+ 
+ cannon1_dm{
+ hp:r=15.0
+ }
+ 
+ cannon2_dm{
+ hp:r=15.0
+ }
+ 
+ gun1_dm{
+ hp:r=15.0
+ }
+ 
+ mgun1_dm{
+ hp:r=15.0
+ }
+ 
+ mgun2_dm{
+ hp:r=15.0
+ }
+ 
+ mgun3_dm{
+ hp:r=15.0
+ }
+ 
+ mgun4_dm{
+ hp:r=15.0
+ }
+ }
+ 
+ armor11_11{
+ 
+ armor1_dm{
+ hp:r=40.0
+ }
+ }
+ 
+ armor6_35{
+ 
+ armor2_dm{
+ hp:r=35.0
+ }
+ 
+ armor4_dm{
+ hp:r=35.0
+ }
+ }
+ 
+ armor8_5{
+ 
+ armor5_dm{
+ hp:r=40.0
+ }
+ }
+ 
+ armor_engine{
+ 
+ engine1_dm{
+ genericDamageMult:r=1.6
+ hp:r=60.5
+ }
+ }
+ 
+ c_dural10{
+ 
+ fuse1_dm{
+ hp:r=75.3
+ }
+ 
+ fuse2_dm{
+ hp:r=77.3
+ }
+ 
+ fuse_dm{
+ hp:r=64.5
+ }
+ 
+ tail_dm{
+ genericDamageMult:r=0.5
+ hp:r=120.5
+ }
+ 
+ wing1_l_dm{
+ genericDamageMult:r=0.3
+ hp:r=120.5
+ }
+ 
+ wing1_r_dm{
+ genericDamageMult:r=0.3
+ hp:r=120.5
+ }
+ }
+ 
+ c_dural5{
+ 
+ aileron_l_dm{
+ genericDamageMult:r=0.3
+ hp:r=42.8
+ }
+ 
+ aileron_r_dm{
+ genericDamageMult:r=0.3
+ hp:r=42.8
+ }
+ 
+ elevator0_dm{
+ genericDamageMult:r=0.3
+ hp:r=37.2
+ }
+ 
+ elevator1_dm{
+ genericDamageMult:r=0.3
+ hp:r=37.1
+ }
+ 
+ fin_dm{
+ hp:r=45.5
+ }
+ 
+ flap_airbrake1_l_dm{
+ hp:r=24.5
+ }
+ 
+ flap_airbrake1_r_dm{
+ hp:r=24.5
+ }
+ 
+ flap_airbrake_l_dm{
+ hp:r=36.6
+ }
+ 
+ flap_airbrake_r_dm{
+ hp:r=36.3
+ }
+ 
+ rudder_dm{
+ genericDamageMult:r=0.3
+ hp:r=45.5
+ }
+ 
+ stab1_dm{
+ hp:r=28.9
+ }
+ 
+ stab2_dm{
+ hp:r=28.9
+ }
+ }
+ 
+ c_dural7{
+ 
+ wing_l_dm{
+ genericDamageMult:r=0.3
+ hp:r=80.5
+ }
+ 
+ wing_r_dm{
+ genericDamageMult:r=0.3
+ hp:r=80.5
+ }
+ }
+ 
+ dural{
+ 
+ airbrake_l1_dm{
+ hp:r=19.5
+ }
+ 
+ airbrake_l_dm{
+ hp:r=19.5
+ }
+ 
+ airbrake_r1_dm{
+ hp:r=19.5
+ }
+ 
+ airbrake_r_dm{
+ hp:r=19.5
+ }
+ 
+ cover1_dm{
+ hp:r=19.5
+ }
+ 
+ cover2_dm{
+ hp:r=19.5
+ }
+ 
+ cover3_dm{
+ hp:r=19.5
+ }
+ 
+ cover4_dm{
+ hp:r=19.5
+ }
+ 
+ cover5_dm{
+ hp:r=19.5
+ }
+ }
+ 
+ dural60{
+ 
+ spar1_l_dm{
+ hp:r=55.1
+ }
+ 
+ spar1_r_dm{
+ hp:r=55.1
+ }
+ 
+ spar2_l_dm{
+ hp:r=39.5
+ }
+ 
+ spar2_r_dm{
+ hp:r=39.5
+ }
+ 
+ spar_l_dm{
+ hp:r=80.5
+ }
+ 
+ spar_r_dm{
+ hp:r=80.5
+ }
+ }
+ 
+ glass38{
+ 
+ armor3_dm{
+ hp:r=100.0
+ }
+ }
+ 
+ protected_controls{
+ 
+ tailcontrol_dm{
+ hp:r=60.5
+ }
+ 
+ wingcontrol_dm{
+ hp:r=60.5
+ }
+ }
+ 
+ steel{
+ 
+ gear_c_dm{
+ hp:r=39.5
+ }
+ 
+ gear_l_dm{
+ hp:r=60.5
+ }
+ 
+ gear_r_dm{
+ hp:r=60.5
+ }
+ }
+ 
+ steel_cooling_sys{
+ 
+ oil1_dm{
+ hp:r=19.5
+ }
+ 
+ oil2_dm{
+ hp:r=13.5
+ }
+ }
+ 
+ steel_pilot{
+ 
+ gunner1_dm{
+ hp:r=20.0
+ }
+ 
+ pilot_dm{
+ fireProtectionHp:r=20.0
+ hp:r=20.0
+ }
+ }
+ 
+ steel_tank_s{
+ 
+ tank1_dm{
+ hp:r=43.5
+ }
+ 
+ tank2_dm{
+ hp:r=56.5
+ }
+ 
+ tank3_dm{
+ hp:r=56.0
+ }
+ 
+ tank4_dm{
+ hp:r=39.5
+ }
+ 
+ tank5_dm{
+ hp:r=39.5
+ }
+ }
+ }
+ 
+ DamageEffects{
+ 
+ part{
+ name:t="aileron_l_dm"
+ 
+ onHit{
+ damage:r=10.0
+ cut:r=0.1
+ }
+ 
+ onHit{
+ damage:r=20.0
+ cut:r=0.4
+ }
+ 
+ onHit{
+ damage:r=30.0
+ cut:r=0.7
+ }
+ 
+ onHit{
+ damage:r=50.0
+ cut:r=1.0
+ }
+ 
+ onKill{
+ cut:r=1.0
+ nothing:r=4.0
+ }
+ 
+ onKill{
+ damage:r=20.0
+ cut:r=1.0
+ nothing:r=2.0
+ }
+ 
+ onKill{
+ damage:r=30.0
+ cut:r=1.0
+ nothing:r=1.0
+ }
+ 
+ onKill{
+ damage:r=50.0
+ cut:r=1.0
+ }
+ }
+ 
+ part{
+ name:t="aileron_r_dm"
+ 
+ onHit{
+ damage:r=10.0
+ cut:r=0.1
+ }
+ 
+ onHit{
+ damage:r=20.0
+ cut:r=0.4
+ }
+ 
+ onHit{
+ damage:r=30.0
+ cut:r=0.7
+ }
+ 
+ onHit{
+ damage:r=50.0
+ cut:r=1.0
+ }
+ 
+ onKill{
+ cut:r=1.0
+ nothing:r=4.0
+ }
+ 
+ onKill{
+ damage:r=20.0
+ cut:r=1.0
+ nothing:r=2.0
+ }
+ 
+ onKill{
+ damage:r=30.0
+ cut:r=1.0
+ nothing:r=1.0
+ }
+ 
+ onKill{
+ damage:r=50.0
+ cut:r=1.0
+ }
+ }
+ 
+ part{
+ name:t="airbrake_l1_dm"
+ }
+ 
+ part{
+ name:t="airbrake_l_dm"
+ }
+ 
+ part{
+ name:t="airbrake_r1_dm"
+ }
+ 
+ part{
+ name:t="airbrake_r_dm"
+ }
+ 
+ part{
+ name:t="armor1_dm"
+ }
+ 
+ part{
+ name:t="armor2_dm"
+ }
+ 
+ part{
+ name:t="armor3_dm"
+ }
+ 
+ part{
+ name:t="armor4_dm"
+ }
+ 
+ part{
+ name:t="armor5_dm"
+ }
+ 
+ part{
+ name:t="cannon1_dm"
+ }
+ 
+ part{
+ name:t="cannon2_dm"
+ }
+ 
+ part{
+ name:t="cover1_dm"
+ }
+ 
+ part{
+ name:t="cover2_dm"
+ }
+ 
+ part{
+ name:t="cover3_dm"
+ }
+ 
+ part{
+ name:t="cover4_dm"
+ }
+ 
+ part{
+ name:t="cover5_dm"
+ }
+ 
+ part{
+ name:t="elevator0_dm"
+ 
+ onHit{
+ damage:r=10.0
+ cut:r=0.1
+ }
+ 
+ onHit{
+ damage:r=20.0
+ cut:r=0.4
+ }
+ 
+ onHit{
+ damage:r=30.0
+ cut:r=0.7
+ }
+ 
+ onHit{
+ damage:r=50.0
+ cut:r=1.0
+ }
+ 
+ onKill{
+ cut:r=1.0
+ nothing:r=4.0
+ }
+ 
+ onKill{
+ damage:r=20.0
+ cut:r=1.0
+ nothing:r=2.0
+ }
+ 
+ onKill{
+ damage:r=30.0
+ cut:r=1.0
+ nothing:r=1.0
+ }
+ 
+ onKill{
+ damage:r=50.0
+ cut:r=1.0
+ }
+ }
+ 
+ part{
+ name:t="elevator1_dm"
+ 
+ onHit{
+ damage:r=10.0
+ cut:r=0.1
+ }
+ 
+ onHit{
+ damage:r=20.0
+ cut:r=0.4
+ }
+ 
+ onHit{
+ damage:r=30.0
+ cut:r=0.7
+ }
+ 
+ onHit{
+ damage:r=50.0
+ cut:r=1.0
+ }
+ 
+ onKill{
+ cut:r=1.0
+ nothing:r=4.0
+ }
+ 
+ onKill{
+ damage:r=20.0
+ cut:r=1.0
+ nothing:r=2.0
+ }
+ 
+ onKill{
+ damage:r=30.0
+ cut:r=1.0
+ nothing:r=1.0
+ }
+ 
+ onKill{
+ damage:r=50.0
+ cut:r=1.0
+ }
+ }
+ 
+ part{
+ name:t="engine1_dm"
+ 
+ onHit{
+ fire:r=0.01
+ }
+ 
+ onHit{
+ damage:r=2.7
+ fire:r=0.01
+ leak_oil:r=0.5
+ cut:r=0.0
+ }
+ 
+ onHit{
+ damage:r=30.0
+ fire:r=0.1
+ leak_oil:r=1.0
+ cut:r=0.0
+ }
+ 
+ onKill{
+ fire:r=30.0
+ leak_oil:r=10.0
+ cut:r=0.0
+ }
+ 
+ onKill{
+ damage:r=30.0
+ fire:r=44.0
+ leak_oil:r=10.0
+ cut:r=0.0
+ }
+ }
+ 
+ part{
+ name:t="fin_dm"
+ 
+ onHit{
+ tailcontrol_dm:r=0.001
+ }
+ 
+ onHit{
+ damage:r=30.0
+ cut:r=0.6
+ }
+ 
+ onHit{
+ damage:r=70.0
+ cut:r=1.0
+ }
+ 
+ onKill{
+ tailcontrol_dm:r=1.0
+ nothing:r=9.0
+ }
+ 
+ onKill{
+ damage:r=10.0
+ cut:r=1.0
+ nothing:r=14.0
+ }
+ 
+ onKill{
+ damage:r=30.0
+ cut:r=1.0
+ nothing:r=4.0
+ }
+ 
+ onKill{
+ damage:r=50.0
+ cut:r=1.0
+ nothing:r=1.0
+ }
+ }
+ 
+ part{
+ name:t="flap_airbrake1_l_dm"
+ 
+ onHit{
+ damage:r=10.0
+ cut:r=0.1
+ }
+ 
+ onHit{
+ damage:r=20.0
+ cut:r=0.4
+ }
+ 
+ onHit{
+ damage:r=30.0
+ cut:r=0.7
+ }
+ 
+ onHit{
+ damage:r=50.0
+ cut:r=1.0
+ }
+ 
+ onKill{
+ cut:r=1.0
+ nothing:r=9.0
+ }
+ 
+ onKill{
+ damage:r=10.0
+ cut:r=1.0
+ nothing:r=5.0
+ }
+ 
+ onKill{
+ damage:r=20.0
+ cut:r=1.0
+ nothing:r=3.0
+ }
+ 
+ onKill{
+ damage:r=30.0
+ cut:r=1.0
+ }
+ }
+ 
+ part{
+ name:t="flap_airbrake1_r_dm"
+ 
+ onHit{
+ damage:r=10.0
+ cut:r=0.1
+ }
+ 
+ onHit{
+ damage:r=20.0
+ cut:r=0.4
+ }
+ 
+ onHit{
+ damage:r=30.0
+ cut:r=0.7
+ }
+ 
+ onHit{
+ damage:r=50.0
+ cut:r=1.0
+ }
+ 
+ onKill{
+ cut:r=1.0
+ nothing:r=9.0
+ }
+ 
+ onKill{
+ damage:r=10.0
+ cut:r=1.0
+ nothing:r=5.0
+ }
+ 
+ onKill{
+ damage:r=20.0
+ cut:r=1.0
+ nothing:r=3.0
+ }
+ 
+ onKill{
+ damage:r=30.0
+ cut:r=1.0
+ }
+ }
+ 
+ part{
+ name:t="flap_airbrake_l_dm"
+ 
+ onHit{
+ damage:r=10.0
+ cut:r=0.1
+ }
+ 
+ onHit{
+ damage:r=20.0
+ cut:r=0.4
+ }
+ 
+ onHit{
+ damage:r=30.0
+ cut:r=0.7
+ }
+ 
+ onHit{
+ damage:r=50.0
+ cut:r=1.0
+ }
+ 
+ onKill{
+ cut:r=1.0
+ nothing:r=9.0
+ }
+ 
+ onKill{
+ damage:r=10.0
+ cut:r=1.0
+ nothing:r=5.0
+ }
+ 
+ onKill{
+ damage:r=20.0
+ cut:r=1.0
+ nothing:r=3.0
+ }
+ 
+ onKill{
+ damage:r=30.0
+ cut:r=1.0
+ }
+ }
+ 
+ part{
+ name:t="flap_airbrake_r_dm"
+ 
+ onHit{
+ damage:r=10.0
+ cut:r=0.1
+ }
+ 
+ onHit{
+ damage:r=20.0
+ cut:r=0.4
+ }
+ 
+ onHit{
+ damage:r=30.0
+ cut:r=0.7
+ }
+ 
+ onHit{
+ damage:r=50.0
+ cut:r=1.0
+ }
+ 
+ onKill{
+ cut:r=1.0
+ nothing:r=9.0
+ }
+ 
+ onKill{
+ damage:r=10.0
+ cut:r=1.0
+ nothing:r=5.0
+ }
+ 
+ onKill{
+ damage:r=20.0
+ cut:r=1.0
+ nothing:r=3.0
+ }
+ 
+ onKill{
+ damage:r=30.0
+ cut:r=1.0
+ }
+ }
+ 
+ part{
+ name:t="fuse1_dm"
+ 
+ onHit{
+ flame:r=0.2
+ smoke:r=0.2
+ }
+ 
+ onHit{
+ damage:r=50.0
+ wing_r_dm:r=0.7
+ wing_l_dm:r=0.7
+ }
+ 
+ onHit{
+ damage:r=70.0
+ wing_r_dm:r=0.9
+ wing_l_dm:r=0.9
+ }
+ 
+ onKill{
+ wingcontrol_l_dm:r=1.0
+ wingcontrol_r_dm:r=1.0
+ nothing:r=9.0
+ }
+ 
+ onKill{
+ damage:r=10.0
+ wing_l_dm:r=1.0
+ wing_r_dm:r=1.0
+ nothing:r=5.0
+ }
+ 
+ onKill{
+ damage:r=20.0
+ wing_l_dm:r=1.0
+ wing_r_dm:r=1.0
+ nothing:r=4.0
+ }
+ 
+ onKill{
+ damage:r=30.0
+ wing_l_dm:r=1.0
+ wing_r_dm:r=1.0
+ nothing:r=3.0
+ }
+ 
+ onKill{
+ damage:r=50.0
+ wing_l_dm:r=1.0
+ wing_r_dm:r=1.0
+ nothing:r=2.0
+ }
+ 
+ onKill{
+ damage:r=70.0
+ wing_l_dm:r=1.0
+ wing_r_dm:r=1.0
+ }
+ }
+ 
+ part{
+ name:t="fuse2_dm"
+ 
+ onHit{
+ flame:r=0.2
+ smoke:r=0.2
+ }
+ 
+ onHit{
+ damage:r=50.0
+ wing_r_dm:r=0.7
+ wing_l_dm:r=0.7
+ }
+ 
+ onHit{
+ damage:r=70.0
+ wing_r_dm:r=0.9
+ wing_l_dm:r=0.9
+ }
+ 
+ onKill{
+ wingcontrol_l_dm:r=1.0
+ wingcontrol_r_dm:r=1.0
+ nothing:r=9.0
+ }
+ 
+ onKill{
+ damage:r=10.0
+ wing_l_dm:r=1.0
+ wing_r_dm:r=1.0
+ nothing:r=5.0
+ }
+ 
+ onKill{
+ damage:r=20.0
+ wing_l_dm:r=1.0
+ wing_r_dm:r=1.0
+ nothing:r=4.0
+ }
+ 
+ onKill{
+ damage:r=30.0
+ wing_l_dm:r=1.0
+ wing_r_dm:r=1.0
+ nothing:r=3.0
+ }
+ 
+ onKill{
+ damage:r=50.0
+ wing_l_dm:r=1.0
+ wing_r_dm:r=1.0
+ nothing:r=2.0
+ }
+ 
+ onKill{
+ damage:r=70.0
+ wing_l_dm:r=1.0
+ wing_r_dm:r=1.0
+ }
+ }
+ 
+ part{
+ name:t="fuse_dm"
+ 
+ onHit{
+ flame:r=0.2
+ smoke:r=0.2
+ }
+ 
+ onHit{
+ damage:r=50.0
+ tail_dm:r=0.6
+ }
+ 
+ onHit{
+ damage:r=70.0
+ tail_dm:r=0.8
+ }
+ 
+ onHit{
+ damage:r=100.0
+ tail_dm:r=1.0
+ }
+ 
+ onKill{
+ tail_dm:r=1.0
+ nothing:r=12.0
+ }
+ 
+ onKill{
+ damage:r=3.0
+ tail_dm:r=1.0
+ nothing:r=9.0
+ }
+ 
+ onKill{
+ damage:r=7.0
+ tail_dm:r=1.0
+ nothing:r=8.0
+ }
+ 
+ onKill{
+ damage:r=10.0
+ tail_dm:r=1.0
+ nothing:r=7.0
+ }
+ 
+ onKill{
+ damage:r=20.0
+ tail_dm:r=1.0
+ nothing:r=6.0
+ }
+ 
+ onKill{
+ damage:r=30.0
+ tail_dm:r=1.0
+ nothing:r=5.0
+ }
+ 
+ onKill{
+ damage:r=50.0
+ tail_dm:r=1.0
+ nothing:r=4.0
+ }
+ 
+ onKill{
+ damage:r=70.0
+ tail_dm:r=1.0
+ nothing:r=3.0
+ }
+ 
+ onKill{
+ damage:r=100.0
+ tail_dm:r=1.0
+ }
+ }
+ 
+ part{
+ name:t="gear_c_dm"
+ 
+ onHit{
+ damage:r=15.0
+ cut:r=0.1
+ }
+ 
+ onHit{
+ damage:r=25.0
+ cut:r=0.4
+ }
+ 
+ onHit{
+ damage:r=40.0
+ cut:r=0.7
+ }
+ 
+ onHit{
+ damage:r=60.0
+ cut:r=1.0
+ }
+ 
+ onKill{
+ cut:r=1.0
+ }
+ }
+ 
+ part{
+ name:t="gear_l_dm"
+ 
+ onHit{
+ damage:r=15.0
+ cut:r=0.1
+ }
+ 
+ onHit{
+ damage:r=25.0
+ cut:r=0.4
+ }
+ 
+ onHit{
+ damage:r=40.0
+ cut:r=0.7
+ }
+ 
+ onHit{
+ damage:r=60.0
+ cut:r=1.0
+ }
+ 
+ onKill{
+ cut:r=1.0
+ }
+ }
+ 
+ part{
+ name:t="gear_r_dm"
+ 
+ onHit{
+ damage:r=15.0
+ cut:r=0.1
+ }
+ 
+ onHit{
+ damage:r=25.0
+ cut:r=0.4
+ }
+ 
+ onHit{
+ damage:r=40.0
+ cut:r=0.7
+ }
+ 
+ onHit{
+ damage:r=60.0
+ cut:r=1.0
+ }
+ 
+ onKill{
+ cut:r=1.0
+ }
+ }
+ 
+ part{
+ name:t="gun1_dm"
+ }
+ 
+ part{
+ name:t="gunner1_dm"
+ }
+ 
+ part{
+ name:t="mgun1_dm"
+ }
+ 
+ part{
+ name:t="mgun2_dm"
+ }
+ 
+ part{
+ name:t="mgun3_dm"
+ }
+ 
+ part{
+ name:t="mgun4_dm"
+ }
+ 
+ part{
+ name:t="oil1_dm"
+ 
+ onHit{
+ leak_oil:r=0.95
+ }
+ 
+ onKill{
+ leak_oil:r=1.0
+ }
+ }
+ 
+ part{
+ name:t="oil2_dm"
+ 
+ onHit{
+ leak_oil:r=0.95
+ }
+ 
+ onKill{
+ leak_oil:r=1.0
+ }
+ }
+ 
+ part{
+ name:t="pilot_dm"
+ }
+ 
+ part{
+ name:t="rudder_dm"
+ 
+ onHit{
+ damage:r=10.0
+ cut:r=0.1
+ }
+ 
+ onHit{
+ damage:r=20.0
+ cut:r=0.4
+ }
+ 
+ onHit{
+ damage:r=30.0
+ cut:r=0.7
+ }
+ 
+ onHit{
+ damage:r=50.0
+ cut:r=1.0
+ }
+ 
+ onKill{
+ cut:r=1.0
+ nothing:r=4.0
+ }
+ 
+ onKill{
+ damage:r=20.0
+ cut:r=1.0
+ nothing:r=2.0
+ }
+ 
+ onKill{
+ damage:r=30.0
+ cut:r=1.0
+ nothing:r=1.0
+ }
+ 
+ onKill{
+ damage:r=50.0
+ cut:r=1.0
+ }
+ }
+ 
+ part{
+ name:t="spar1_l_dm"
+ 
+ onKill{
+ nothing:r=2.0
+ cut:r=3.0
+ }
+ }
+ 
+ part{
+ name:t="spar1_r_dm"
+ 
+ onKill{
+ nothing:r=2.0
+ cut:r=3.0
+ }
+ }
+ 
+ part{
+ name:t="spar2_l_dm"
+ 
+ onKill{
+ nothing:r=2.0
+ cut:r=3.0
+ }
+ }
+ 
+ part{
+ name:t="spar2_r_dm"
+ 
+ onKill{
+ nothing:r=2.0
+ cut:r=3.0
+ }
+ }
+ 
+ part{
+ name:t="spar_l_dm"
+ 
+ onKill{
+ nothing:r=100.0
+ cut:r=0.001
+ }
+ }
+ 
+ part{
+ name:t="spar_r_dm"
+ 
+ onKill{
+ nothing:r=100.0
+ cut:r=0.001
+ }
+ }
+ 
+ part{
+ name:t="stab1_dm"
+ 
+ onHit{
+ damage:r=30.0
+ cut:r=0.6
+ }
+ 
+ onHit{
+ damage:r=70.0
+ cut:r=1.0
+ }
+ 
+ onKill{
+ damage:r=10.0
+ cut:r=1.0
+ nothing:r=14.0
+ }
+ 
+ onKill{
+ damage:r=30.0
+ cut:r=1.0
+ nothing:r=4.0
+ }
+ 
+ onKill{
+ damage:r=50.0
+ cut:r=1.0
+ nothing:r=1.0
+ }
+ }
+ 
+ part{
+ name:t="stab2_dm"
+ 
+ onHit{
+ damage:r=30.0
+ cut:r=0.6
+ }
+ 
+ onHit{
+ damage:r=70.0
+ cut:r=1.0
+ }
+ 
+ onKill{
+ damage:r=10.0
+ cut:r=1.0
+ nothing:r=14.0
+ }
+ 
+ onKill{
+ damage:r=30.0
+ cut:r=1.0
+ nothing:r=4.0
+ }
+ 
+ onKill{
+ damage:r=50.0
+ cut:r=1.0
+ nothing:r=1.0
+ }
+ }
+ 
+ part{
+ name:t="tail_dm"
+ 
+ onHit{
+ flame:r=0.2
+ smoke:r=0.2
+ }
+ 
+ onHit{
+ damage:r=30.0
+ cut:r=0.25
+ }
+ 
+ onHit{
+ damage:r=50.0
+ cut:r=0.5
+ }
+ 
+ onHit{
+ damage:r=65.0
+ cut:r=1.0
+ }
+ 
+ onKill{
+ tailcontrol_dm:r=1.0
+ nothing:r=19.0
+ }
+ 
+ onKill{
+ damage:r=10.0
+ tailcontrol_dm:r=1.0
+ nothing:r=9.0
+ }
+ 
+ onKill{
+ damage:r=20.0
+ cut:r=1.0
+ nothing:r=4.0
+ }
+ 
+ onKill{
+ damage:r=30.0
+ cut:r=1.0
+ nothing:r=3.0
+ }
+ 
+ onKill{
+ damage:r=50.0
+ cut:r=1.0
+ nothing:r=2.0
+ }
+ 
+ onKill{
+ damage:r=65.0
+ cut:r=1.0
+ }
+ }
+ 
+ part{
+ name:t="tailcontrol_dm"
+ }
+ 
+ part{
+ name:t="tank1_dm"
+ 
+ onHit{
+ fire:r=0.03
+ leak:r=0.5
+ }
+ 
+ onHit{
+ damage:r=20.0
+ fire:r=0.3
+ leak:r=0.7
+ }
+ 
+ onHit{
+ damage:r=80.0
+ expl:r=0.5
+ fire:r=0.7
+ leak:r=0.9
+ }
+ 
+ onKill{
+ fire:r=3.0
+ leak:r=12.0
+ nothing:r=85.0
+ }
+ 
+ onKill{
+ damage:r=30.0
+ fire:r=10.0
+ leak:r=30.0
+ }
+ 
+ onKill{
+ damage:r=80.0
+ fire:r=50.0
+ leak:r=30.0
+ }
+ }
+ 
+ part{
+ name:t="tank2_dm"
+ 
+ onHit{
+ fire:r=0.03
+ leak:r=0.5
+ }
+ 
+ onHit{
+ damage:r=20.0
+ fire:r=0.3
+ leak:r=0.7
+ }
+ 
+ onHit{
+ damage:r=80.0
+ expl:r=0.5
+ fire:r=0.7
+ leak:r=0.9
+ }
+ 
+ onKill{
+ fire:r=3.0
+ leak:r=12.0
+ nothing:r=85.0
+ }
+ 
+ onKill{
+ damage:r=30.0
+ fire:r=10.0
+ leak:r=30.0
+ }
+ 
+ onKill{
+ damage:r=80.0
+ fire:r=50.0
+ leak:r=30.0
+ }
+ }
+ 
+ part{
+ name:t="tank3_dm"
+ 
+ onHit{
+ fire:r=0.03
+ leak:r=0.5
+ }
+ 
+ onHit{
+ damage:r=20.0
+ fire:r=0.3
+ leak:r=0.7
+ }
+ 
+ onHit{
+ damage:r=80.0
+ expl:r=0.5
+ fire:r=0.7
+ leak:r=0.9
+ }
+ 
+ onKill{
+ fire:r=3.0
+ leak:r=12.0
+ nothing:r=85.0
+ }
+ 
+ onKill{
+ damage:r=30.0
+ fire:r=10.0
+ leak:r=30.0
+ }
+ 
+ onKill{
+ damage:r=80.0
+ fire:r=50.0
+ leak:r=30.0
+ }
+ }
+ 
+ part{
+ name:t="tank4_dm"
+ 
+ onHit{
+ fire:r=0.03
+ leak:r=0.5
+ }
+ 
+ onHit{
+ damage:r=20.0
+ fire:r=0.3
+ leak:r=0.7
+ }
+ 
+ onHit{
+ damage:r=80.0
+ expl:r=0.5
+ fire:r=0.7
+ leak:r=0.9
+ }
+ 
+ onKill{
+ fire:r=3.0
+ leak:r=12.0
+ nothing:r=85.0
+ }
+ 
+ onKill{
+ damage:r=30.0
+ fire:r=10.0
+ leak:r=30.0
+ }
+ 
+ onKill{
+ damage:r=80.0
+ fire:r=50.0
+ leak:r=30.0
+ }
+ }
+ 
+ part{
+ name:t="tank5_dm"
+ 
+ onHit{
+ fire:r=0.03
+ leak:r=0.5
+ }
+ 
+ onHit{
+ damage:r=20.0
+ fire:r=0.3
+ leak:r=0.7
+ }
+ 
+ onHit{
+ damage:r=80.0
+ expl:r=0.5
+ fire:r=0.7
+ leak:r=0.9
+ }
+ 
+ onKill{
+ fire:r=3.0
+ leak:r=12.0
+ nothing:r=85.0
+ }
+ 
+ onKill{
+ damage:r=30.0
+ fire:r=10.0
+ leak:r=30.0
+ }
+ 
+ onKill{
+ damage:r=80.0
+ fire:r=50.0
+ leak:r=30.0
+ }
+ }
+ 
+ part{
+ name:t="wing1_l_dm"
+ defaultEffectPart:t="spar1_l_dm"
+ 
+ onHit{
+ smoke:r=0.1
+ flame:r=0.2
+ }
+ 
+ onHit{
+ damage:r=10.0
+ cut:r=0.0
+ smoke:r=0.3
+ flame:r=0.3
+ 
+ part{
+ ratio:r=0.1
+ canCut:b=yes
+ }
+ }
+ 
+ onHit{
+ damage:r=20.0
+ cut:r=0.0
+ smoke:r=0.3
+ flame:r=0.3
+ 
+ part{
+ ratio:r=0.2
+ canCut:b=yes
+ }
+ }
+ 
+ onHit{
+ damage:r=30.0
+ cut:r=0.0
+ smoke:r=0.4
+ flame:r=0.4
+ 
+ part{
+ ratio:r=0.4
+ canCut:b=yes
+ }
+ }
+ 
+ onHit{
+ damage:r=50.0
+ cut:r=0.0
+ smoke:r=0.6
+ flame:r=0.6
+ 
+ part{
+ ratio:r=0.8
+ canCut:b=yes
+ }
+ }
+ 
+ onHit{
+ damage:r=70.0
+ cut:r=0.0
+ smoke:r=0.8
+ flame:r=0.8
+ 
+ part{
+ ratio:r=1.0
+ canCut:b=yes
+ }
+ }
+ 
+ onKill{
+ damage:r=10.0
+ cut:r=0.0
+ smoke:r=1.0
+ flame:r=1.0
+ nothing:r=9.0
+ 
+ part{
+ ratio:r=1.0
+ canCut:b=yes
+ }
+ }
+ 
+ onKill{
+ damage:r=20.0
+ cut:r=0.0
+ smoke:r=2.0
+ flame:r=2.0
+ nothing:r=5.0
+ 
+ part{
+ ratio:r=1.0
+ canCut:b=yes
+ }
+ }
+ 
+ onKill{
+ damage:r=30.0
+ cut:r=0.0
+ smoke:r=2.0
+ flame:r=2.0
+ nothing:r=3.0
+ 
+ part{
+ ratio:r=1.0
+ canCut:b=yes
+ }
+ }
+ 
+ onKill{
+ damage:r=50.0
+ cut:r=0.0
+ smoke:r=2.0
+ flame:r=2.0
+ nothing:r=1.0
+ 
+ part{
+ ratio:r=1.0
+ canCut:b=yes
+ }
+ }
+ 
+ onKill{
+ damage:r=70.0
+ cut:r=0.0
+ smoke:r=2.0
+ flame:r=2.0
+ 
+ part{
+ ratio:r=1.0
+ canCut:b=yes
+ }
+ }
+ }
+ 
+ part{
+ name:t="wing1_r_dm"
+ defaultEffectPart:t="spar1_r_dm"
+ 
+ onHit{
+ smoke:r=0.1
+ flame:r=0.2
+ }
+ 
+ onHit{
+ damage:r=10.0
+ cut:r=0.0
+ smoke:r=0.3
+ flame:r=0.3
+ 
+ part{
+ ratio:r=0.1
+ canCut:b=yes
+ }
+ }
+ 
+ onHit{
+ damage:r=20.0
+ cut:r=0.0
+ smoke:r=0.3
+ flame:r=0.3
+ 
+ part{
+ ratio:r=0.2
+ canCut:b=yes
+ }
+ }
+ 
+ onHit{
+ damage:r=30.0
+ cut:r=0.0
+ smoke:r=0.4
+ flame:r=0.4
+ 
+ part{
+ ratio:r=0.4
+ canCut:b=yes
+ }
+ }
+ 
+ onHit{
+ damage:r=50.0
+ cut:r=0.0
+ smoke:r=0.6
+ flame:r=0.6
+ 
+ part{
+ ratio:r=0.8
+ canCut:b=yes
+ }
+ }
+ 
+ onHit{
+ damage:r=70.0
+ cut:r=0.0
+ smoke:r=0.8
+ flame:r=0.8
+ 
+ part{
+ ratio:r=1.0
+ canCut:b=yes
+ }
+ }
+ 
+ onKill{
+ damage:r=10.0
+ cut:r=0.0
+ smoke:r=1.0
+ flame:r=1.0
+ nothing:r=9.0
+ 
+ part{
+ ratio:r=1.0
+ canCut:b=yes
+ }
+ }
+ 
+ onKill{
+ damage:r=20.0
+ cut:r=0.0
+ smoke:r=2.0
+ flame:r=2.0
+ nothing:r=5.0
+ 
+ part{
+ ratio:r=1.0
+ canCut:b=yes
+ }
+ }
+ 
+ onKill{
+ damage:r=30.0
+ cut:r=0.0
+ smoke:r=2.0
+ flame:r=2.0
+ nothing:r=3.0
+ 
+ part{
+ ratio:r=1.0
+ canCut:b=yes
+ }
+ }
+ 
+ onKill{
+ damage:r=50.0
+ cut:r=0.0
+ smoke:r=2.0
+ flame:r=2.0
+ nothing:r=1.0
+ 
+ part{
+ ratio:r=1.0
+ canCut:b=yes
+ }
+ }
+ 
+ onKill{
+ damage:r=70.0
+ cut:r=0.0
+ smoke:r=2.0
+ flame:r=2.0
+ 
+ part{
+ ratio:r=1.0
+ canCut:b=yes
+ }
+ }
+ }
+ 
+ part{
+ name:t="wing_l_dm"
+ 
+ onHit{
+ smoke:r=0.1
+ flame:r=0.2
+ }
+ 
+ onHit{
+ damage:r=10.0
+ smoke:r=0.2
+ flame:r=0.3
+ }
+ 
+ onHit{
+ damage:r=20.0
+ smoke:r=0.3
+ flame:r=0.4
+ }
+ 
+ onHit{
+ damage:r=30.0
+ smoke:r=0.4
+ flame:r=0.5
+ }
+ 
+ onHit{
+ damage:r=50.0
+ smoke:r=0.5
+ flame:r=0.6
+ }
+ 
+ onHit{
+ damage:r=70.0
+ smoke:r=0.8
+ flame:r=0.8
+ }
+ 
+ onKill{
+ damage:r=10.0
+ smoke:r=0.2
+ flame:r=0.2
+ }
+ 
+ onKill{
+ damage:r=20.0
+ smoke:r=0.2
+ flame:r=0.2
+ }
+ 
+ onKill{
+ damage:r=30.0
+ smoke:r=0.5
+ flame:r=0.6
+ }
+ 
+ onKill{
+ damage:r=50.0
+ smoke:r=1.0
+ flame:r=1.1
+ }
+ 
+ onKill{
+ damage:r=70.0
+ smoke:r=1.0
+ flame:r=1.1
+ }
+ }
+ 
+ part{
+ name:t="wing_r_dm"
+ 
+ onHit{
+ smoke:r=0.1
+ flame:r=0.2
+ }
+ 
+ onHit{
+ damage:r=10.0
+ smoke:r=0.2
+ flame:r=0.3
+ }
+ 
+ onHit{
+ damage:r=20.0
+ smoke:r=0.3
+ flame:r=0.4
+ }
+ 
+ onHit{
+ damage:r=30.0
+ smoke:r=0.4
+ flame:r=0.5
+ }
+ 
+ onHit{
+ damage:r=50.0
+ smoke:r=0.5
+ flame:r=0.6
+ }
+ 
+ onHit{
+ damage:r=70.0
+ smoke:r=0.8
+ flame:r=0.8
+ }
+ 
+ onKill{
+ damage:r=10.0
+ smoke:r=0.2
+ flame:r=0.2
+ }
+ 
+ onKill{
+ damage:r=20.0
+ smoke:r=0.2
+ flame:r=0.2
+ }
+ 
+ onKill{
+ damage:r=30.0
+ smoke:r=0.5
+ flame:r=0.6
+ }
+ 
+ onKill{
+ damage:r=50.0
+ smoke:r=1.0
+ flame:r=1.1
+ }
+ 
+ onKill{
+ damage:r=70.0
+ smoke:r=1.0
+ flame:r=1.1
+ }
+ }
+ 
+ part{
+ name:t="wingcontrol_dm"
+ }
+ }
+ 
+ ikPilot{
+ model:t="pilot_us_char"
+ maxHeadHorAngle:r=60.0
+ maxHeadDownAngle:r=60.0
+ maxHeadUpAngle:r=10.0
+ headNode:t="Bip01 Head"
+ pelvisNode:t="Bip01 Pelvis"
+ pelvisTargetNode:t="Bip01 Pelvis01"
+ 
+ ikNode{
+ downNode:t="Bip01 L Hand"
+ midNode:t="Bip01 L Forearm"
+ upNode:t="Bip01 L UpperArm"
+ targetNode:t="throttle_lhand_1"
+ flexionDir:p3=0.0, -1.0, 0.2
+ type:t="leftHand"
+ detachedNodeYpr:p3=0.0, -15.0, -90.0
+ detachedNodeScale:p3=1.0, -1.0, 1.0
+ }
+ 
+ ikNode{
+ downNode:t="Bip01 R Hand"
+ midNode:t="Bip01 R Forearm"
+ upNode:t="Bip01 R UpperArm"
+ targetNode:t="stick_rhand_1"
+ flexionDir:p3=0.0, -1.0, -0.5
+ type:t="rightHand"
+ detachedNodeYpr:p3=0.0, -15.0, 90.0
+ detachedNodeScale:p3=1.0, -1.0, 1.0
+ }
+ 
+ ikNode{
+ downNode:t="Bip01 L Foot"
+ midNode:t="Bip01 L Calf"
+ upNode:t="Bip01 L Thigh"
+ targetNode:t="pedal_lfoot_1"
+ flexionDir:p3=0.0, 1.0, 0.3
+ }
+ 
+ ikNode{
+ downNode:t="Bip01 R Foot"
+ midNode:t="Bip01 R Calf"
+ upNode:t="Bip01 R Thigh"
+ targetNode:t="pedal_rfoot_1"
+ flexionDir:p3=0.0, 1.0, -0.3
+ }
+ }
+ 
+ ikGunner{
+ model:t="gunner_us_char"
+ maxHeadHorAngle:r=60.0
+ maxHeadDownAngle:r=60.0
+ maxHeadUpAngle:r=10.0
+ headNode:t="Bip01 Head"
+ pelvisNode:t="Bip01 Pelvis"
+ pelvisTargetNode:t="Bip01 Pelvis02"
+ 
+ chestNodes{
+ leftShoulderNode:t="Bip01 L UpperArm"
+ rightShoulderNode:t="Bip01 R UpperArm"
+ neckNode:t="Bip01 Neck"
+ node:t="Bip01 R Clavicle"
+ node:t="Bip01 L Clavicle"
+ node:t="Bip01 Spine 1"
+ node:t="Bip01 Head"
+ node:t="Bip01 HeadNub"
+ node:t="Bip01 L UpperArm"
+ node:t="Bip01 R UpperArm"
+ node:t="Bip01 Neck"
+ leftHandTarget:t="throttle_lhand_2"
+ rightHandTarget:t="stick_rhand_2"
+ }
+ 
+ ikNode{
+ downNode:t="Bip01 L Hand"
+ midNode:t="Bip01 L Forearm"
+ upNode:t="Bip01 L UpperArm"
+ targetNode:t="throttle_lhand_2"
+ flexionDir:p3=0.0, -0.9, 0.3
+ }
+ 
+ ikNode{
+ downNode:t="Bip01 R Hand"
+ midNode:t="Bip01 R Forearm"
+ upNode:t="Bip01 R UpperArm"
+ targetNode:t="stick_rhand_2"
+ flexionDir:p3=0.0, -0.9, -0.3
+ }
+ 
+ ikNode{
+ downNode:t="Bip01 L Foot"
+ midNode:t="Bip01 L Calf"
+ upNode:t="Bip01 L Thigh"
+ targetNode:t="pedal_lfoot_2"
+ flexionDir:p3=0.0, 1.0, -0.2
+ }
+ 
+ ikNode{
+ downNode:t="Bip01 R Foot"
+ midNode:t="Bip01 R Calf"
+ upNode:t="Bip01 R Thigh"
+ targetNode:t="pedal_rfoot_2"
+ flexionDir:p3=0.0, 1.0, 0.2
+ }
+ }
+ 
+ attach{
+ pilot1:t="pilot_us_500"
+ gunner1:t="gunner_sit_us_500"
+ }
+ 
+ default_skin{
+ name:t="sb2c_5_thailand"
+ 
+ replace_tex{
+ from:t="sb2c_5_a*"
+ to:t="sb2c_5_thailand_a*"
+ }
+ }
+ 
+ WeaponSlots{
+ maxloadMass:r=2260.0
+ maxloadMassLeftConsoles:r=1130.0
+ maxloadMassRightConsoles:r=1130.0
+ maxDisbalance:r=850.0
+ 
+ HideNodes{
+ node:t="pylon_rocket1"
+ node:t="pylon_rocket2"
+ node:t="pylon_dgp_1"
+ node:t="pylon_dgp_2"
+ node:t="dgp_1_l"
+ node:t="dgp_1_r"
+ node:t="hatch2_open"
+ node:t="hatch1_open"
+ node:t="pylon_bomb1"
+ node:t="pylon_bomb2"
+ node:t="bomb_launcher"
+ node:t="bomb_launcher1"
+ }
+ 
+ HideDmParts{
+ node:t="cover4_dm"
+ node:t="mgun1_dm"
+ node:t="mgun2_dm"
+ node:t="cover5_dm"
+ node:t="mgun3_dm"
+ node:t="mgun4_dm"
+ }
+ 
+ WeaponSlot{
+ index:i=0
+ 
+ WeaponPreset{
+ name:t="default_common"
+ 
+ Weapon{
+ trigger:t="cannon"
+ blk:t="gameData/Weapons/cannonAN_M2.blk"
+ emitter:t="flare1"
+ flash:t="flare1"
+ shell:t="emtr_shellrejection1"
+ dm:t="cannon1_dm"
+ bullets:i=200
+ spread:r=1.5
+ }
+ 
+ Weapon{
+ trigger:t="cannon"
+ blk:t="gameData/Weapons/cannonAN_M2.blk"
+ emitter:t="flare2"
+ flash:t="flare2"
+ shell:t="emtr_shellrejection2"
+ dm:t="cannon2_dm"
+ bullets:i=200
+ spread:r=1.5
+ traceOffset:i=2
+ }
+ 
+ Weapon{
+ trigger:t="gunner0"
+ blk:t="gameData/Weapons/gunBrowning30_turret.blk"
+ breechInCockpit:b=yes
+ emitter:t="gun1"
+ flash:t="flare3"
+ dm:t="gunner1_dm"
+ gunnerDm:t="gunner1_dm"
+ gunDm:t="gun1_dm"
+ partsDP:t="gun1_dm"
+ bullets:i=2000
+ 
+ turret{
+ head:t="turret1"
+ gun:t="gun1"
+ }
+ 
+ limits{
+ yaw:p2=-90.0, 90.0
+ pitch:p2=-25.0, 80.0
+ }
+ 
+ limitsTable{
+ lim1:p4=-90.0, -50.0, -25.0, 80.0
+ lim2:p4=-50.0, -29.0, -25.0, 80.0
+ lim3:p4=-29.0, 29.0, -2.0, 80.0
+ lim4:p4=29.0, 50.0, -25.0, 80.0
+ lim5:p4=50.0, 90.0, -25.0, 80.0
+ }
+ 
+ limitsDeadzone{
+ yaw:p2=-4.0, 4.0
+ pitch:p2=-25.0, 35.0
+ }
+ 
+ limitsDeadzone{
+ yaw:p2=-45.0, -29.0
+ pitch:p2=-10.0, 0.0
+ }
+ 
+ limitsDeadzone{
+ yaw:p2=29.0, 45.0
+ pitch:p2=-10.0, 0.0
+ }
+ }
+ 
+ Weapon{
+ trigger:t="gunner0"
+ blk:t="gameData/Weapons/gunBrowning30_turret.blk"
+ breechInCockpit:b=yes
+ emitter:t="gun1"
+ flash:t="flare4"
+ dm:t="gunner1_dm"
+ bullets:i=2000
+ 
+ turret{
+ head:t="turret1"
+ gun:t="gun1"
+ }
+ 
+ limits{
+ yaw:p2=-90.0, 90.0
+ pitch:p2=-25.0, 80.0
+ }
+ 
+ limitsTable{
+ lim1:p4=-90.0, -50.0, -25.0, 80.0
+ lim2:p4=-50.0, -29.0, -25.0, 80.0
+ lim3:p4=-29.0, 29.0, -2.0, 80.0
+ lim4:p4=29.0, 50.0, -25.0, 80.0
+ lim5:p4=50.0, 90.0, -25.0, 80.0
+ }
+ 
+ limitsDeadzone{
+ yaw:p2=-4.0, 4.0
+ pitch:p2=-25.0, 35.0
+ }
+ 
+ limitsDeadzone{
+ yaw:p2=-45.0, -29.0
+ pitch:p2=-10.0, 0.0
+ }
+ 
+ limitsDeadzone{
+ yaw:p2=29.0, 45.0
+ pitch:p2=-10.0, 0.0
+ }
+ }
+ }
+ }
+ 
+ WeaponSlot{
+ index:i=1
+ tier:i=8
+ order:i=1
+ 
+ WeaponPreset{
+ iconType:t="rockets_he_middle_group_x4"
+ name:t="hvar_slot1"
+ reqModification:t="frc_mk2"
+ 
+ ShowNodes{
+ node:t="pylon_rocket1"
+ }
+ 
+ Weapon{
+ trigger:t="rockets"
+ external:b=yes
+ separate:b=yes
+ blk:t="gameData/Weapons/rocketGuns/us_5_in_hvar_a.blk"
+ emitter:t="rocket1"
+ bullets:i=1
+ order:i=11
+ }
+ 
+ Weapon{
+ trigger:t="rockets"
+ external:b=yes
+ separate:b=yes
+ blk:t="gameData/Weapons/rocketGuns/us_5_in_hvar_a.blk"
+ emitter:t="rocket2"
+ bullets:i=1
+ order:i=13
+ }
+ 
+ Weapon{
+ trigger:t="rockets"
+ external:b=yes
+ separate:b=yes
+ blk:t="gameData/Weapons/rocketGuns/us_5_in_hvar_a.blk"
+ emitter:t="rocket3"
+ bullets:i=1
+ order:i=15
+ }
+ 
+ Weapon{
+ trigger:t="rockets"
+ external:b=yes
+ separate:b=yes
+ blk:t="gameData/Weapons/rocketGuns/us_5_in_hvar_a.blk"
+ emitter:t="rocket4"
+ bullets:i=1
+ order:i=17
+ }
+ }
+ }
+ 
+ WeaponSlot{
+ index:i=2
+ tier:i=7
+ order:i=3
+ 
+ WeaponPreset{
+ iconType:t="bombs_middle"
+ name:t="250lbs"
+ 
+ ShowNodes{
+ node:t="pylon_bomb1"
+ }
+ 
+ Weapon{
+ trigger:t="bombs"
+ blk:t="gameData/Weapons/BombGuns/us_250lb_anm57.blk"
+ emitter:t="bomb4"
+ bullets:i=1
+ external:b=yes
+ separate:b=yes
+ }
+ }
+ 
+ WeaponPreset{
+ iconType:t="bombs_large"
+ name:t="500lbs"
+ reqModification:t="btd_sbc"
+ 
+ ShowNodes{
+ node:t="pylon_bomb1"
+ }
+ 
+ Weapon{
+ trigger:t="bombs"
+ blk:t="gameData/Weapons/BombGuns/us_500lb_anm64a1.blk"
+ emitter:t="bomb4"
+ bullets:i=1
+ external:b=yes
+ separate:b=yes
+ }
+ 
+ BannedWeaponPreset{
+ slot:i=1
+ preset:t="hvar_slot1"
+ }
+ }
+ 
+ WeaponPreset{
+ iconType:t="bombs_heavy_middle"
+ name:t="1000lbs_external"
+ reqModification:t="btd_mbc"
+ 
+ ShowNodes{
+ node:t="pylon_bomb1"
+ }
+ 
+ Weapon{
+ trigger:t="bombs"
+ blk:t="gameData/Weapons/BombGuns/us_1000lb_anm65a1.blk"
+ emitter:t="bomb4"
+ bullets:i=1
+ external:b=yes
+ }
+ 
+ BannedWeaponPreset{
+ slot:i=1
+ preset:t="hvar_slot1"
+ }
+ }
+ 
+ WeaponPreset{
+ iconType:t="doublebarreled_box"
+ name:t="gun_pod"
+ reqModification:t="dgp-1_gunpod"
+ 
+ ShowNodes{
+ node:t="pylon_dgp_1"
+ node:t="dgp_1_l"
+ }
+ 
+ ShowDmParts{
+ node:t="cover4_dm"
+ node:t="mgun1_dm"
+ node:t="mgun2_dm"
+ }
+ 
+ Weapon{
+ trigger:t="additional gun"
+ blk:t="gameData/Weapons/gunBrowning50_M2_underwing.blk"
+ emitter:t="flare13"
+ flash:t="flare13"
+ bullets:i=340
+ dm:t="mgun1_dm"
+ traceOffset:i=1
+ spread:r=1.0
+ counterIndex:i=1
+ external:b=yes
+ }
+ 
+ Weapon{
+ trigger:t="additional gun"
+ blk:t="gameData/Weapons/gunBrowning50_M2_underwing.blk"
+ emitter:t="flare14"
+ flash:t="flare14"
+ bullets:i=340
+ dm:t="mgun2_dm"
+ traceOffset:i=1
+ spread:r=1.0
+ counterIndex:i=1
+ external:b=yes
+ }
+ 
+ BannedWeaponPreset{
+ slot:i=1
+ preset:t="hvar_slot1"
+ }
+ }
+ }
+ 
+ WeaponSlot{
+ index:i=3
+ tier:i=6
+ order:i=5
+ notUseforDisbalanceCalculation:b=yes
+ 
+ WeaponPreset{
+ iconType:t="bombs_middle_group_x2"
+ name:t="250lbs_x2"
+ 
+ Weapon{
+ trigger:t="bombs"
+ blk:t="gameData/Weapons/BombGuns/us_250lb_anm57.blk"
+ emitter:t="bomb2"
+ bullets:i=1
+ separate:b=yes
+ }
+ 
+ Weapon{
+ trigger:t="bombs"
+ blk:t="gameData/Weapons/BombGuns/us_250lb_anm57.blk"
+ emitter:t="bomb3"
+ bullets:i=1
+ separate:b=yes
+ }
+ 
+ Bombing{
+ maxDelay:r=0.0
+ 
+ canBeDropped{
+ altitude:p2=-100.0, 20000.0
+ tangage:p2=-95.0, 60.0
+ roll:r=65.0
+ }
+ 
+ maxDispersionAt{
+ altitude:p2=20.0, 10000.0
+ tangage:p2=-100.0, 55.0
+ roll:r=65.0
+ }
+ 
+ noDispersionAt{
+ altitude:p2=20.0, 6000.0
+ tangage:p2=-90.0, 15.0
+ roll:r=40.0
+ }
+ 
+ sightDisappears{
+ altitude:p2=40.0, 10000.0
+ tangage:p2=-100.0, 45.0
+ roll:r=55.0
+ }
+ 
+ sightStartsFading{
+ altitude:p2=95.0, 6000.0
+ tangage:p2=-30.0, 18.0
+ roll:r=40.0
+ }
+ 
+ sightEnabled{
+ altitude:p2=20.0, 15000.0
+ tangage:p2=-120.0, 60.0
+ roll:r=180.0
+ }
+ 
+ maxDelayAt{
+ altitude:p2=-20000.0, 20000.0
+ tangage:p2=-180.0, 180.0
+ roll:r=180.0
+ }
+ 
+ noDelayAt{
+ altitude:p2=-19999.0, 19999.0
+ tangage:p2=-179.0, 179.0
+ roll:r=179.0
+ }
+ }
+ }
+ 
+ WeaponPreset{
+ iconType:t="bombs_large_group_x2"
+ name:t="500lbs_x2"
+ reqModification:t="btd_sbc"
+ 
+ Weapon{
+ trigger:t="bombs"
+ blk:t="gameData/Weapons/BombGuns/us_500lb_anm64a1.blk"
+ emitter:t="bomb2"
+ bullets:i=1
+ separate:b=yes
+ }
+ 
+ Weapon{
+ trigger:t="bombs"
+ blk:t="gameData/Weapons/BombGuns/us_500lb_anm64a1.blk"
+ emitter:t="bomb3"
+ bullets:i=1
+ separate:b=yes
+ }
+ 
+ Bombing{
+ maxDelay:r=0.0
+ 
+ canBeDropped{
+ altitude:p2=-100.0, 20000.0
+ tangage:p2=-95.0, 60.0
+ roll:r=65.0
+ }
+ 
+ maxDispersionAt{
+ altitude:p2=20.0, 10000.0
+ tangage:p2=-100.0, 55.0
+ roll:r=65.0
+ }
+ 
+ noDispersionAt{
+ altitude:p2=20.0, 6000.0
+ tangage:p2=-90.0, 15.0
+ roll:r=40.0
+ }
+ 
+ sightDisappears{
+ altitude:p2=40.0, 10000.0
+ tangage:p2=-100.0, 45.0
+ roll:r=55.0
+ }
+ 
+ sightStartsFading{
+ altitude:p2=95.0, 6000.0
+ tangage:p2=-30.0, 18.0
+ roll:r=40.0
+ }
+ 
+ sightEnabled{
+ altitude:p2=20.0, 15000.0
+ tangage:p2=-120.0, 60.0
+ roll:r=180.0
+ }
+ 
+ maxDelayAt{
+ altitude:p2=-20000.0, 20000.0
+ tangage:p2=-180.0, 180.0
+ roll:r=180.0
+ }
+ 
+ noDelayAt{
+ altitude:p2=-19999.0, 19999.0
+ tangage:p2=-179.0, 179.0
+ roll:r=179.0
+ }
+ }
+ }
+ 
+ WeaponPreset{
+ iconType:t="bombs_heavy_middle"
+ name:t="1000lbs"
+ reqModification:t="btd_mbc"
+ 
+ ShowNodes{
+ node:t="bomb_launcher1"
+ }
+ 
+ Weapon{
+ trigger:t="bombs"
+ blk:t="gameData/Weapons/BombGuns/us_1000lb_anm65a1.blk"
+ emitter:t="bomb1"
+ bullets:i=1
+ launcher:b=yes
+ separate:b=yes
+ }
+ 
+ Bombing{
+ maxDelay:r=0.0
+ 
+ canBeDropped{
+ altitude:p2=-100.0, 20000.0
+ tangage:p2=-95.0, 60.0
+ roll:r=65.0
+ }
+ 
+ maxDispersionAt{
+ altitude:p2=20.0, 10000.0
+ tangage:p2=-100.0, 55.0
+ roll:r=65.0
+ }
+ 
+ noDispersionAt{
+ altitude:p2=20.0, 6000.0
+ tangage:p2=-90.0, 15.0
+ roll:r=40.0
+ }
+ 
+ sightDisappears{
+ altitude:p2=40.0, 10000.0
+ tangage:p2=-100.0, 45.0
+ roll:r=55.0
+ }
+ 
+ sightStartsFading{
+ altitude:p2=95.0, 6000.0
+ tangage:p2=-30.0, 18.0
+ roll:r=40.0
+ }
+ 
+ sightEnabled{
+ altitude:p2=20.0, 15000.0
+ tangage:p2=-120.0, 60.0
+ roll:r=180.0
+ }
+ 
+ maxDelayAt{
+ altitude:p2=-20000.0, 20000.0
+ tangage:p2=-180.0, 180.0
+ roll:r=180.0
+ }
+ 
+ noDelayAt{
+ altitude:p2=-19999.0, 19999.0
+ tangage:p2=-179.0, 179.0
+ roll:r=179.0
+ }
+ }
+ }
+ 
+ WeaponPreset{
+ iconType:t="bombs_special"
+ name:t="1600lbs"
+ reqModification:t="btd_mbc"
+ 
+ ShowNodes{
+ node:t="bomb_launcher1"
+ }
+ 
+ Weapon{
+ trigger:t="bombs"
+ blk:t="gameData/Weapons/BombGuns/us_1600lb_ap_an_mk1.blk"
+ emitter:t="bomb1"
+ bullets:i=1
+ launcher:b=yes
+ separate:b=yes
+ }
+ }
+ 
+ WeaponPreset{
+ iconType:t="bombs_special"
+ name:t="2000lbs"
+ reqModification:t="us_2000lb_m66"
+ 
+ ShowNodes{
+ node:t="bomb_launcher1"
+ node:t="hatch1_open"
+ node:t="hatch2_open"
+ }
+ 
+ HideNodes{
+ node:t="hatch1"
+ node:t="hatch2"
+ node:t="hatch3"
+ node:t="hatch4"
+ node:t="hatch5"
+ node:t="hatch6"
+ }
+ 
+ Weapon{
+ trigger:t="bombs"
+ blk:t="gameData/Weapons/BombGuns/us_2000lbs_anm66.blk"
+ emitter:t="bomb1"
+ bullets:i=1
+ launcher:b=yes
+ external:b=yes
+ separate:b=yes
+ }
+ 
+ Bombing{
+ maxDelay:r=0.0
+ 
+ canBeDropped{
+ altitude:p2=-100.0, 20000.0
+ tangage:p2=-95.0, 60.0
+ roll:r=65.0
+ }
+ 
+ maxDispersionAt{
+ altitude:p2=20.0, 10000.0
+ tangage:p2=-100.0, 55.0
+ roll:r=65.0
+ }
+ 
+ noDispersionAt{
+ altitude:p2=20.0, 6000.0
+ tangage:p2=-90.0, 15.0
+ roll:r=40.0
+ }
+ 
+ sightDisappears{
+ altitude:p2=40.0, 10000.0
+ tangage:p2=-100.0, 45.0
+ roll:r=55.0
+ }
+ 
+ sightStartsFading{
+ altitude:p2=95.0, 6000.0
+ tangage:p2=-30.0, 18.0
+ roll:r=40.0
+ }
+ 
+ sightEnabled{
+ altitude:p2=20.0, 15000.0
+ tangage:p2=-120.0, 60.0
+ roll:r=180.0
+ }
+ 
+ maxDelayAt{
+ altitude:p2=-20000.0, 20000.0
+ tangage:p2=-180.0, 180.0
+ roll:r=180.0
+ }
+ 
+ noDelayAt{
+ altitude:p2=-19999.0, 19999.0
+ tangage:p2=-179.0, 179.0
+ roll:r=179.0
+ }
+ }
+ }
+ 
+ WeaponPreset{
+ iconType:t="bombs_middle_high_drag_group_x2"
+ name:t="1000lbs_ap_x2"
+ reqModification:t="btd_mbc"
+ 
+ Weapon{
+ trigger:t="bombs"
+ blk:t="gameData/Weapons/BombGuns/us_1000lb_anmk33_box_ap.blk"
+ emitter:t="bomb2"
+ bullets:i=1
+ separate:b=yes
+ }
+ 
+ Weapon{
+ trigger:t="bombs"
+ blk:t="gameData/Weapons/BombGuns/us_1000lb_anmk33_box_ap.blk"
+ emitter:t="bomb3"
+ bullets:i=1
+ separate:b=yes
+ }
+ 
+ Bombing{
+ maxDelay:r=0.0
+ 
+ canBeDropped{
+ altitude:p2=-100.0, 20000.0
+ tangage:p2=-95.0, 60.0
+ roll:r=65.0
+ }
+ 
+ maxDispersionAt{
+ altitude:p2=20.0, 10000.0
+ tangage:p2=-100.0, 55.0
+ roll:r=65.0
+ }
+ 
+ noDispersionAt{
+ altitude:p2=20.0, 6000.0
+ tangage:p2=-90.0, 15.0
+ roll:r=40.0
+ }
+ 
+ sightDisappears{
+ altitude:p2=40.0, 10000.0
+ tangage:p2=-100.0, 45.0
+ roll:r=55.0
+ }
+ 
+ sightStartsFading{
+ altitude:p2=95.0, 6000.0
+ tangage:p2=-30.0, 18.0
+ roll:r=40.0
+ }
+ 
+ sightEnabled{
+ altitude:p2=20.0, 15000.0
+ tangage:p2=-120.0, 60.0
+ roll:r=180.0
+ }
+ 
+ maxDelayAt{
+ altitude:p2=-20000.0, 20000.0
+ tangage:p2=-180.0, 180.0
+ roll:r=180.0
+ }
+ 
+ noDelayAt{
+ altitude:p2=-19999.0, 19999.0
+ tangage:p2=-179.0, 179.0
+ roll:r=179.0
+ }
+ }
+ }
+ 
+ WeaponPreset{
+ iconType:t="air_torpedo"
+ name:t="torpedo"
+ reqModification:t="tbf_itc"
+ 
+ ShowNodes{
+ node:t="hatch1_open"
+ node:t="hatch2_open"
+ }
+ 
+ HideNodes{
+ node:t="hatch1"
+ node:t="hatch2"
+ node:t="hatch3"
+ node:t="hatch4"
+ node:t="hatch5"
+ node:t="hatch6"
+ }
+ 
+ Weapon{
+ trigger:t="torpedoes"
+ blk:t="gameData/Weapons/torpedoes/us_mk13_torpedo_no_case.blk"
+ emitter:t="torp1"
+ bullets:i=1
+ external:b=yes
+ separate:b=yes
+ }
+ }
+ 
+ WeaponPreset{
+ iconType:t="air_torpedo"
+ name:t="torpedo_case"
+ reqModification:t="improved_torpedo_mod"
+ 
+ ShowNodes{
+ node:t="hatch1_open"
+ node:t="hatch2_open"
+ }
+ 
+ HideNodes{
+ node:t="hatch1"
+ node:t="hatch2"
+ node:t="hatch3"
+ node:t="hatch4"
+ node:t="hatch5"
+ node:t="hatch6"
+ }
+ 
+ Weapon{
+ trigger:t="torpedoes"
+ blk:t="gameData/Weapons/torpedoes/us_mk13_torpedo.blk"
+ emitter:t="torp1"
+ bullets:i=1
+ external:b=yes
+ separate:b=yes
+ }
+ }
+ }
+ 
+ WeaponSlot{
+ index:i=4
+ tier:i=5
+ order:i=4
+ 
+ WeaponPreset{
+ iconType:t="bombs_middle"
+ name:t="250lbs"
+ 
+ ShowNodes{
+ node:t="pylon_bomb2"
+ }
+ 
+ Weapon{
+ trigger:t="bombs"
+ blk:t="gameData/Weapons/BombGuns/us_250lb_anm57.blk"
+ emitter:t="bomb5"
+ bullets:i=1
+ external:b=yes
+ separate:b=yes
+ }
+ }
+ 
+ WeaponPreset{
+ iconType:t="bombs_large"
+ name:t="500lbs"
+ reqModification:t="btd_sbc"
+ 
+ ShowNodes{
+ node:t="pylon_bomb2"
+ }
+ 
+ Weapon{
+ trigger:t="bombs"
+ blk:t="gameData/Weapons/BombGuns/us_500lb_anm64a1.blk"
+ emitter:t="bomb5"
+ bullets:i=1
+ external:b=yes
+ separate:b=yes
+ }
+ 
+ BannedWeaponPreset{
+ slot:i=5
+ preset:t="hvar_slot5"
+ }
+ }
+ 
+ WeaponPreset{
+ iconType:t="bombs_heavy_middle"
+ name:t="1000lbs_external"
+ reqModification:t="btd_mbc"
+ 
+ ShowNodes{
+ node:t="pylon_bomb2"
+ }
+ 
+ Weapon{
+ trigger:t="bombs"
+ blk:t="gameData/Weapons/BombGuns/us_1000lb_anm65a1.blk"
+ emitter:t="bomb5"
+ bullets:i=1
+ external:b=yes
+ }
+ 
+ BannedWeaponPreset{
+ slot:i=5
+ preset:t="hvar_slot5"
+ }
+ }
+ 
+ WeaponPreset{
+ iconType:t="doublebarreled_box"
+ name:t="gun_pod"
+ reqModification:t="dgp-1_gunpod"
+ 
+ ShowNodes{
+ node:t="pylon_dgp_2"
+ node:t="dgp_1_r"
+ }
+ 
+ ShowDmParts{
+ node:t="cover5_dm"
+ node:t="mgun3_dm"
+ node:t="mgun4_dm"
+ }
+ 
+ Weapon{
+ trigger:t="additional gun"
+ blk:t="gameData/Weapons/gunBrowning50_M2_underwing.blk"
+ emitter:t="flare15"
+ flash:t="flare15"
+ bullets:i=340
+ dm:t="mgun3_dm"
+ traceOffset:i=1
+ spread:r=1.0
+ counterIndex:i=1
+ external:b=yes
+ }
+ 
+ Weapon{
+ trigger:t="additional gun"
+ blk:t="gameData/Weapons/gunBrowning50_M2_underwing.blk"
+ emitter:t="flare16"
+ flash:t="flare16"
+ bullets:i=340
+ dm:t="mgun4_dm"
+ traceOffset:i=1
+ spread:r=1.0
+ counterIndex:i=1
+ external:b=yes
+ }
+ 
+ BannedWeaponPreset{
+ slot:i=5
+ preset:t="hvar_slot5"
+ }
+ }
+ }
+ 
+ WeaponSlot{
+ index:i=5
+ tier:i=4
+ order:i=2
+ 
+ WeaponPreset{
+ iconType:t="rockets_he_middle_group_x4"
+ name:t="hvar_slot5"
+ reqModification:t="frc_mk2"
+ 
+ ShowNodes{
+ node:t="pylon_rocket2"
+ }
+ 
+ Weapon{
+ trigger:t="rockets"
+ external:b=yes
+ separate:b=yes
+ blk:t="gameData/Weapons/rocketGuns/us_5_in_hvar_a.blk"
+ emitter:t="rocket8"
+ bullets:i=1
+ order:i=12
+ }
+ 
+ Weapon{
+ trigger:t="rockets"
+ external:b=yes
+ separate:b=yes
+ blk:t="gameData/Weapons/rocketGuns/us_5_in_hvar_a.blk"
+ emitter:t="rocket7"
+ bullets:i=1
+ order:i=14
+ }
+ 
+ Weapon{
+ trigger:t="rockets"
+ external:b=yes
+ separate:b=yes
+ blk:t="gameData/Weapons/rocketGuns/us_5_in_hvar_a.blk"
+ emitter:t="rocket6"
+ bullets:i=1
+ order:i=16
+ }
+ 
+ Weapon{
+ trigger:t="rockets"
+ external:b=yes
+ separate:b=yes
+ blk:t="gameData/Weapons/rocketGuns/us_5_in_hvar_a.blk"
+ emitter:t="rocket5"
+ bullets:i=1
+ order:i=18
+ }
+ }
+ }
+ }
+ 
+ default_skin_tomoe{
+ 
+ replace_tex{
+ from:t="a_4b_c*"
+ to:t="a_4b_c_tomoe*"
+ }
+ }
```

  **Removed**:
```diff
```


- **aces.vromfs.bin_u/gamedata/flightmodels/su_33.blkx**:

  **Added**:
```diff
+ notUseforDisbalanceCalculation:b=yes
```

  **Removed**:
```diff
```


- **aces.vromfs.bin_u/gamedata/flightmodels/xp-55.blkx**:

  **Added**:
```diff
+ flexWing{
+ wingStrainCoeff:r=0.4
+ wingOverloadCoeff:r=1.0
+ wingStrainLimitDown:r=1.0
+ }
+ 
```

  **Removed**:
```diff
```


- **aces.vromfs.bin_u/gamedata/flightmodels/z_9w.blkx**:

  **Added**:
```diff
+ tpsCameraTargetOffsetAtZoom:p3=80.0, 60.0, 0.0
```

  **Removed**:
```diff
- tpsCameraTargetOffsetAtZoom:p3=2.0, -2.5, 0.0
```


- **aces.vromfs.bin_u/gamedata/flightmodels/z_9wa.blkx**:

  **Added**:
```diff
+ tpsCameraTargetOffsetAtZoom:p3=80.0, 60.0, 0.0
```

  **Removed**:
```diff
- tpsCameraTargetOffsetAtZoom:p3=2.0, -2.5, 0.0
```


- **aces.vromfs.bin_u/gamedata/sensors/bl_carapace.blkx**:

  **Added**:
```diff
+ text:t="E2K"
```

  **Removed**:
```diff
- text:t="EF2K"
```


- **aces.vromfs.bin_u/gamedata/sensors/cn_kj8602a.blkx**:

  **Added**:
```diff
+ text:t="E2K"
```

  **Removed**:
```diff
- text:t="EF2K"
```


- **aces.vromfs.bin_u/gamedata/sensors/cn_kj_8602.blkx**:

  **Added**:
```diff
+ text:t="E2K"
```

  **Removed**:
```diff
- text:t="EF2K"
```


- **aces.vromfs.bin_u/gamedata/sensors/fr_serval_rwr.blkx**:

  **Added**:
```diff
+ text:t="E2K"
```

  **Removed**:
```diff
- text:t="EF2K"
```


- **aces.vromfs.bin_u/gamedata/sensors/fr_sherloc.blkx**:

  **Added**:
```diff
+ text:t="E2K"
```

  **Removed**:
```diff
- text:t="EF2K"
```


- **aces.vromfs.bin_u/gamedata/sensors/fr_spectra_rwr.blkx**:

  **Added**:
```diff
+ text:t="E2K"
```

  **Removed**:
```diff
- text:t="EF2K"
```


- **aces.vromfs.bin_u/gamedata/sensors/il_elisra_sps_200.blkx**:

  **Added**:
```diff
+ text:t="E2K"
```

  **Removed**:
```diff
- text:t="EF2K"
```


- **aces.vromfs.bin_u/gamedata/sensors/jp_j_apr_4.blkx**:

  **Added**:
```diff
+ text:t="E2K"
```

  **Removed**:
```diff
- text:t="EF2K"
```


- **aces.vromfs.bin_u/gamedata/sensors/jp_j_apr_6.blkx**:

  **Added**:
```diff
+ text:t="E2K"
```

  **Removed**:
```diff
- text:t="EF2K"
```


- **aces.vromfs.bin_u/gamedata/sensors/su_spo-150-16m.blkx**:

  **Added**:
```diff
+ text:t="E2K"
```

  **Removed**:
```diff
- text:t="EF2K"
```


- **aces.vromfs.bin_u/gamedata/sensors/su_spo-150-28m.blkx**:

  **Added**:
```diff
+ text:t="E2K"
```

  **Removed**:
```diff
- text:t="EF2K"
```


- **aces.vromfs.bin_u/gamedata/sensors/su_spo-150-30m1.blkx**:

  **Added**:
```diff
+ text:t="E2K"
```

  **Removed**:
```diff
- text:t="EF2K"
```


- **aces.vromfs.bin_u/gamedata/sensors/su_spo-150.blkx**:

  **Added**:
```diff
+ text:t="E2K"
```

  **Removed**:
```diff
- text:t="EF2K"
```


- **aces.vromfs.bin_u/gamedata/sensors/su_tarang.blkx**:

  **Added**:
```diff
+ text:t="E2K"
```

  **Removed**:
```diff
- text:t="EF2K"
```


- **aces.vromfs.bin_u/gamedata/sensors/swd_ar830.blkx**:

  **Added**:
```diff
+ text:t="E2K"
```

  **Removed**:
```diff
- text:t="EF2K"
```


- **aces.vromfs.bin_u/gamedata/sensors/swd_bow_21.blkx**:

  **Added**:
```diff
+ text:t="E2K"
```

  **Removed**:
```diff
- text:t="EF2K"
```


- **aces.vromfs.bin_u/gamedata/sensors/uk_ari_18228_10.blkx**:

  **Added**:
```diff
+ text:t="E2K"
```

  **Removed**:
```diff
- text:t="EF2K"
```


- **aces.vromfs.bin_u/gamedata/sensors/uk_ari_18228_19.blkx**:

  **Added**:
```diff
+ text:t="E2K"
```

  **Removed**:
```diff
- text:t="EF2K"
```


- **aces.vromfs.bin_u/gamedata/sensors/uk_ari_18241_1.blkx**:

  **Added**:
```diff
+ text:t="E2K"
```

  **Removed**:
```diff
- text:t="EF2K"
```


- **aces.vromfs.bin_u/gamedata/sensors/uk_ari_23284.blkx**:

  **Added**:
```diff
+ text:t="E2K"
```

  **Removed**:
```diff
- text:t="EF2K"
```


- **aces.vromfs.bin_u/gamedata/sensors/uk_praetorian_rwr.blkx**:

  **Added**:
```diff
+ text:t="E2K"
```

  **Removed**:
```diff
- text:t="EF2K"
```


- **aces.vromfs.bin_u/gamedata/sensors/uk_sky_guardian_200.blkx**:

  **Added**:
```diff
+ text:t="E2K"
```

  **Removed**:
```diff
- text:t="EF2K"
```


- **aces.vromfs.bin_u/gamedata/sensors/us_an_alr_400.blkx**:

  **Added**:
```diff
+ text:t="E2K"
```

  **Removed**:
```diff
- text:t="EF2K"
```


- **aces.vromfs.bin_u/gamedata/sensors/us_an_alr_56c.blkx**:

  **Added**:
```diff
+ text:t="E2K"
```

  **Removed**:
```diff
- text:t="EF2K"
```


- **aces.vromfs.bin_u/gamedata/sensors/us_an_alr_56m.blkx**:

  **Added**:
```diff
+ text:t="E2K"
```

  **Removed**:
```diff
- text:t="EF2K"
```


- **aces.vromfs.bin_u/gamedata/sensors/us_an_alr_67.blkx**:

  **Added**:
```diff
+ text:t="E2K"
```

  **Removed**:
```diff
- text:t="EF2K"
```


- **aces.vromfs.bin_u/gamedata/sensors/us_an_alr_68_v.blkx**:

  **Added**:
```diff
+ text:t="E2K"
```

  **Removed**:
```diff
- text:t="EF2K"
```


- **aces.vromfs.bin_u/gamedata/sensors/us_an_alr_68_v_3.blkx**:

  **Added**:
```diff
+ text:t="E2K"
```

  **Removed**:
```diff
- text:t="EF2K"
```


- **aces.vromfs.bin_u/gamedata/sensors/us_an_alr_69.blkx**:

  **Added**:
```diff
+ text:t="E2K"
```

  **Removed**:
```diff
- text:t="EF2K"
```


- **aces.vromfs.bin_u/gamedata/units/ships/it_ciclone_class_ghibli.blkx**:

  **Added**:
```diff
+ minCrewMemberRepairCount:i=61
+ minCrewMemberAliveCount:i=53
+ crew:i=25
+ crew:i=25
+ crew:i=25
+ crew:i=24
```

  **Removed**:
```diff
- minCrewMemberRepairCount:i=53
- minCrewMemberAliveCount:i=46
- crew:i=19
- crew:i=19
- crew:i=19
- crew:i=19
```


- **aces.vromfs.bin_u/gamedata/units/ships/jp_destroyer_murasame.blkx**:

  **Added**:
```diff
+ speedYaw:r=30.0
+ speedPitch:r=15.0
+ speedYaw:r=30.0
+ speedPitch:r=15.0
+ speedYaw:r=30.0
+ speedPitch:r=15.0
```

  **Removed**:
```diff
- speedYaw:r=15.0
- speedPitch:r=30.0
- speedYaw:r=15.0
- speedPitch:r=30.0
- speedYaw:r=15.0
- speedPitch:r=30.0
```


- **aces.vromfs.bin_u/gamedata/units/ships/jp_escort_hiburi_class_syonan.blkx**:

  **Added**:
```diff
+ lim1:p4=-180.0, -150.0, 25.0, 75.0
+ lim2:p4=-150.0, -145.0, 2.0, 75.0
+ lim3:p4=-145.0, -23.0, -10.0, 75.0
+ lim5:p4=23.0, 145.0, -10.0, 75.0
+ lim6:p4=145.0, 150.0, 2.0, 75.0
+ lim7:p4=150.0, 180.0, 25.0, 75.0
+ lim1:p4=-180.0, -150.0, 25.0, 75.0
+ lim2:p4=-150.0, -145.0, 2.0, 75.0
+ lim3:p4=-145.0, -23.0, -10.0, 75.0
+ lim5:p4=23.0, 145.0, -10.0, 75.0
+ lim6:p4=145.0, 150.0, 2.0, 75.0
+ lim7:p4=150.0, 180.0, 25.0, 75.0
```

  **Removed**:
```diff
- lim1:p4=-180.0, -158.0, 25.0, 75.0
- lim2:p4=-158.0, -148.0, 2.0, 75.0
- lim3:p4=-148.0, -23.0, -10.0, 75.0
- lim5:p4=23.0, 148.0, -10.0, 75.0
- lim6:p4=148.0, 158.0, 2.0, 75.0
- lim7:p4=158.0, 180.0, 25.0, 75.0
- lim1:p4=-180.0, -158.0, 25.0, 75.0
- lim2:p4=-158.0, -148.0, 2.0, 75.0
- lim3:p4=-148.0, -23.0, -10.0, 75.0
- lim5:p4=23.0, 148.0, -10.0, 75.0
- lim6:p4=148.0, 158.0, 2.0, 75.0
- lim7:p4=158.0, 180.0, 25.0, 75.0
```


- **aces.vromfs.bin_u/gamedata/units/tankmodels/fr_m46_patton.blkx**:

  **Added**:
```diff
+ model:t="m46_france"
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
+ mass:r=43650.0
+ bulletHitFx:t="ground_model_hit"
+ partDamageFx:t="part_damage"
+ explosionFx:t="tank_explosion"
+ fireFx:t="ground_model_fire"
+ destroysRendInstances:b=yes
+ destroysTrees:b=yes
+ type:t="typeMediumTank"
+ 
+ DamageParts{
+ formatVersion:i=2
+ armorClass:t="CHA_tank"
+ hp:r=10000.0
+ 
+ hull_CHA{
+ 
+ superstructure_front_dm{
+ armorThickness:r=101.6
+ }
+ 
+ body_front_dm{
+ armorThickness:r=76.2
+ }
+ 
+ body_shield_dm{
+ armorThickness:r=162.5
+ }
+ }
+ 
+ hull_RHA{
+ armorClass:t="RHA_tank"
+ 
+ superstructure_side_dm{
+ armorThickness:r=76.2
+ }
+ 
+ body_side_dm{
+ armorThickness:r=50.8
+ }
+ 
+ superstructure_top_dm{
+ armorThickness:r=25.4
+ }
+ 
+ body_back_dm{
+ armorThickness:r=25.4
+ }
+ 
+ superstructure_back_dm{
+ armorThickness:r=50.8
+ }
+ 
+ body_bottom_dm{
+ armorThickness:r=25.4
+ }
+ 
+ superstructure_bottom_dm{
+ armorThickness:r=12.7
+ }
+ 
+ turret_top_dm{
+ armorThickness:r=25.4
+ }
+ 
+ gun_barrel_armor_dm{
+ armorThickness:r=25.4
+ armorEffectiveThicknessMax:r=30.0
+ }
+ 
+ body_top_dm{
+ armorThickness:r=20.0
+ }
+ 
+ turret_01_back_dm{
+ armorThickness:r=5.0
+ }
+ }
+ 
+ turret{
+ armorClass:t="CHA_tank"
+ 
+ turret_back_dm{
+ armorThickness:r=76.2
+ }
+ 
+ turret_side_dm{
+ armorThickness:r=76.2
+ }
+ 
+ turret_front_dm{
+ armorThickness:r=101.6
+ }
+ 
+ turret_bottom_dm{
+ armorThickness:r=101.6
+ }
+ 
+ turret_commander_dm{
+ armorThickness:r=76.2
+ }
+ 
+ gun_mask_dm{
+ armorThickness:r=114.3
+ variableThickness:b=yes
+ }
+ 
+ gun_mask_01_dm{
+ armorThickness:r=203.2
+ }
+ 
+ gun_mask_02_dm{
+ armorThickness:r=152.4
+ }
+ 
+ gun_mask_03_dm{
+ armorThickness:r=25.4
+ }
+ }
+ 
+ body_shields{
+ armorClass:t="tank_structural_steel"
+ hp:r=1000.0
+ armorThickness:r=4.0
+ stopChanceOnDeadPart:r=0.0
+ createSecondaryShatters:b=no
+ 
+ ex_decor_r_05_dm{
+ }
+ 
+ ex_decor_r_07_dm{
+ }
+ 
+ ex_decor_l_04_dm{
+ }
+ 
+ ex_decor_l_07_dm{
+ }
+ 
+ ex_armor_turret_01_dm{
+ }
+ 
+ ex_armor_turret_02_dm{
+ }
+ 
+ ex_armor_turret_03_dm{
+ }
+ 
+ ex_armor_turret_04_dm{
+ }
+ 
+ ex_armor_turret_05_dm{
+ }
+ 
+ ex_armor_turret_06_dm{
+ }
+ 
+ ex_armor_turret_07_dm{
+ }
+ 
+ ex_armor_turret_08_dm{
+ }
+ 
+ ex_decor_l_02_dm{
+ }
+ 
+ ex_decor_l_03_dm{
+ }
+ 
+ ex_decor_l_05_dm{
+ }
+ 
+ ex_decor_l_06_dm{
+ }
+ 
+ ex_decor_l_08_dm{
+ }
+ 
+ ex_decor_l_09_dm{
+ }
+ 
+ ex_decor_l_10_dm{
+ }
+ 
+ ex_decor_l_11_dm{
+ }
+ 
+ ex_decor_r_02_dm{
+ }
+ 
+ ex_decor_r_03_dm{
+ }
+ 
+ ex_decor_r_06_dm{
+ }
+ 
+ ex_decor_r_08_dm{
+ }
+ 
+ ex_decor_r_09_dm{
+ }
+ 
+ ex_decor_r_10_dm{
+ }
+ 
+ ex_decor_r_11_dm{
+ }
+ 
+ ex_armor_03_dm{
+ }
+ }
+ 
+ optics{
+ armorClass:t="optics_tank"
+ 
+ optic_gun_dm{
+ armorThickness:r=10.0
+ hp:r=50.0
+ }
+ 
+ optic_turret_01_dm{
+ armorThickness:r=3.0
+ hp:r=20.0
+ }
+ 
+ optic_turret_02_dm{
+ armorThickness:r=3.0
+ hp:r=20.0
+ }
+ 
+ optic_turret_03_dm{
+ armorThickness:r=3.0
+ hp:r=20.0
+ }
+ 
+ optic_turret_04_dm{
+ armorThickness:r=3.0
+ hp:r=20.0
+ }
+ 
+ optic_turret_05_dm{
+ armorThickness:r=3.0
+ hp:r=20.0
+ }
+ 
+ optic_turret_06_dm{
+ armorThickness:r=3.0
+ hp:r=20.0
+ }
+ 
+ optic_turret_07_dm{
+ armorThickness:r=3.0
+ hp:r=20.0
+ }
+ 
+ optic_turret_08_dm{
+ armorThickness:r=3.0
+ hp:r=20.0
+ }
+ 
+ optic_turret_09_dm{
+ armorThickness:r=3.0
+ hp:r=20.0
+ }
+ 
+ optic_body_01_dm{
+ armorThickness:r=3.0
+ hp:r=20.0
+ }
+ 
+ optic_body_02_dm{
+ armorThickness:r=3.0
+ hp:r=20.0
+ }
+ }
+ 
+ chassis{
+ armorClass:t="tank_steel_wheels"
+ hp:r=300.0
+ armorThickness:r=20.0
+ 
+ wheel_support_dm{
+ }
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
+ wheel_r_07_dm{
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
+ wheel_l_07_dm{
+ }
+ 
+ wheel_r_drive_dm{
+ }
+ 
+ wheel_l_drive_dm{
+ }
+ 
+ wheel_r_front_dm{
+ }
+ 
+ wheel_l_front_dm{
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
+ wheel_l_top_04_dm{
+ }
+ 
+ wheel_l_top_05_dm{
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
+ wheel_r_top_04_dm{
+ }
+ 
+ wheel_r_top_05_dm{
+ }
+ 
+ submodule{
+ armorClass:t="tank_traks"
+ armorThickness:r=20.0
+ hp:r=200.0
+ 
+ ex_armor_01_dm{
+ hp:r=200.0
+ }
+ 
+ ex_armor_02_dm{
+ hp:r=200.0
+ }
+ }
+ }
+ 
+ gun{
+ armorClass:t="tank_barrel"
+ hp:r=150.0
+ armorThickness:r=30.0
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
+ ignoreSolidDimension:b=yes
+ 
+ driver_dm{
+ }
+ 
+ loader_dm{
+ }
+ 
+ loader_01_dm{
+ }
+ 
+ loader_02_dm{
+ }
+ 
+ loader_03_dm{
+ }
+ 
+ gunner_dm{
+ }
+ 
+ gunner_01_dm{
+ }
+ 
+ gunner_02_dm{
+ }
+ 
+ gunner_03_dm{
+ }
+ 
+ commander_dm{
+ }
+ 
+ machine_gunner_dm{
+ }
+ 
+ machine_gunner_01_dm{
+ }
+ 
+ machine_gunner_02_dm{
+ }
+ 
+ machine_gunner_03_dm{
+ }
+ 
+ machine_gunner_04_dm{
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
+ sound{
+ EngineName:t="engine_sherman_m4a3"
+ TrackSoundPath:t="tanks/engines_tanks"
+ TrackSoundPathStudio:t="ground/engines"
+ TrackSoundName:t="tracks"
+ TrackSoundNameCockpit:t="tracks_interior"
+ turret_turn:t="turret_turn_manual_y"
+ EngineNameAi:t="engine_tank_ai_middle"
+ TrackSoundNameAi:t="tracks_ai_middle"
+ gun_turn:t="turret_turn_mg_light"
+ }
+ 
+ DamageEffects{
+ 
+ part{
+ name:t="ammo_body_dm"
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
+ name:t="ammo_body_52_dm"
+ name:t="ammo_body_53_dm"
+ name:t="ammo_body_54_dm"
+ name:t="ammo_body_55_dm"
+ name:t="ammo_body_56_dm"
+ name:t="ammo_body_57_dm"
+ name:t="ammo_body_58_dm"
+ name:t="ammo_body_59_dm"
+ name:t="ammo_body_60_dm"
+ name:t="ammo_body_61_dm"
+ name:t="ammo_body_62_dm"
+ name:t="ammo_body_63_dm"
+ name:t="ammo_body_64_dm"
+ name:t="ammo_body_65_dm"
+ name:t="ammo_body_66_dm"
+ name:t="ammo_body_67_dm"
+ name:t="ammo_body_68_dm"
+ name:t="ammo_body_69_dm"
+ name:t="ammo_body_70_dm"
+ name:t="ammo_body_l_01_dm"
+ name:t="ammo_body_l_02_dm"
+ name:t="ammo_body_l_03_dm"
+ name:t="ammo_body_l_04_dm"
+ name:t="ammo_body_l_05_dm"
+ name:t="ammo_body_l_06_dm"
+ name:t="ammo_body_l_07_dm"
+ name:t="ammo_body_l_08_dm"
+ name:t="ammo_body_l_09_dm"
+ name:t="ammo_body_l_10_dm"
+ name:t="ammo_body_l_11_dm"
+ name:t="ammo_body_l_12_dm"
+ name:t="ammo_body_l_13_dm"
+ name:t="ammo_body_l_14_dm"
+ name:t="ammo_body_l_15_dm"
+ name:t="ammo_body_l_16_dm"
+ name:t="ammo_body_l_17_dm"
+ name:t="ammo_body_l_18_dm"
+ name:t="ammo_body_l_19_dm"
+ name:t="ammo_body_l_20_dm"
+ name:t="ammo_body_l_21_dm"
+ name:t="ammo_body_l_22_dm"
+ name:t="ammo_body_l_23_dm"
+ name:t="ammo_body_l_24_dm"
+ name:t="ammo_body_r_01_dm"
+ name:t="ammo_body_r_02_dm"
+ name:t="ammo_body_r_03_dm"
+ name:t="ammo_body_r_04_dm"
+ name:t="ammo_body_r_05_dm"
+ name:t="ammo_body_r_06_dm"
+ name:t="ammo_body_r_07_dm"
+ name:t="ammo_body_r_08_dm"
+ name:t="ammo_body_r_09_dm"
+ name:t="ammo_body_r_10_dm"
+ name:t="ammo_body_r_11_dm"
+ name:t="ammo_body_r_12_dm"
+ name:t="ammo_body_r_13_dm"
+ name:t="ammo_body_r_14_dm"
+ name:t="ammo_body_r_15_dm"
+ name:t="ammo_body_r_16_dm"
+ name:t="ammo_body_r_17_dm"
+ name:t="ammo_body_r_18_dm"
+ name:t="ammo_body_r_19_dm"
+ name:t="ammo_body_r_20_dm"
+ name:t="ammo_body_r_21_dm"
+ name:t="ammo_body_r_22_dm"
+ name:t="ammo_body_r_23_dm"
+ name:t="ammo_body_r_24_dm"
+ name:t="ammo_turret_dm"
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
+ name:t="ammo_turret_11_dm"
+ name:t="ammo_turret_12_dm"
+ name:t="ammo_turret_13_dm"
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
+ name:t="ammo_turret_46_dm"
+ name:t="ammo_turret_47_dm"
+ name:t="ammo_turret_48_dm"
+ name:t="ammo_turret_49_dm"
+ name:t="ammo_turret_50_dm"
+ name:t="ammo_turret_51_dm"
+ name:t="ammo_turret_52_dm"
+ name:t="ammo_turret_53_dm"
+ name:t="ammo_turret_54_dm"
+ name:t="ammo_turret_55_dm"
+ name:t="ammo_turret_56_dm"
+ name:t="ammo_turret_57_dm"
+ name:t="ammo_turret_58_dm"
+ name:t="ammo_turret_59_dm"
+ name:t="ammo_turret_60_dm"
+ name:t="ammo_turret_61_dm"
+ name:t="ammo_turret_62_dm"
+ name:t="ammo_turret_63_dm"
+ name:t="ammo_turret_64_dm"
+ name:t="ammo_turret_65_dm"
+ name:t="ammo_turret_66_dm"
+ name:t="ammo_turret_67_dm"
+ name:t="ammo_turret_68_dm"
+ name:t="ammo_turret_69_dm"
+ name:t="ammo_turret_70_dm"
+ name:t="ammo_turret_71_dm"
+ name:t="ammo_turret_72_dm"
+ name:t="ammo_turret_73_dm"
+ name:t="ammo_turret_74_dm"
+ name:t="ammo_turret_75_dm"
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
+ expl:r=0.1
+ fire:r=0.2
+ damage:r=100.0
+ fHitCritical:b=yes
+ }
+ 
+ onHit{
+ damageType:t="cumulative"
+ expl:r=0.2
+ fire:r=0.3
+ damage:r=250.0
+ fHitCritical:b=yes
+ }
+ 
+ onHit{
+ damageType:t="cumulative"
+ expl:r=0.5
+ fire:r=0.5
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
+ fire:r=0.225
+ damage:r=25.0
+ fHitCritical:b=yes
+ }
+ 
+ onHit{
+ damageType:t="explosion"
+ expl:r=0.25
+ fire:r=0.35
+ damage:r=50.0
+ fHitCritical:b=yes
+ }
+ 
+ onHit{
+ damageType:t="generic"
+ fire:r=0.1
+ damage:r=20.0
+ fHitCritical:b=yes
+ }
+ 
+ onHit{
+ damageType:t="generic"
+ fire:r=0.25
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
+ expl:r=0.5
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
+ fire:r=0.2
+ damage:r=70.0
+ fHitCritical:b=yes
+ }
+ 
+ onHit{
+ damageType:t="generic"
+ fire:r=0.55
+ damage:r=300.0
+ fHitCritical:b=yes
+ }
+ 
+ onHit{
+ damageType:t="generic"
+ fire:r=0.35
+ damage:r=200.0
+ fHitCritical:b=yes
+ }
+ 
+ onHit{
+ damageType:t="generic"
+ fire:r=0.1
+ damage:r=20.0
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
+ fire:r=0.5
+ nothing:r=0.5
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
+ 
+ part{
+ name:t="body_top_dm"
+ name:t="body_front_dm"
+ name:t="body_side_dm"
+ name:t="body_back_dm"
+ name:t="body_bottom_dm"
+ name:t="superstructure_bottom_dm"
+ name:t="superstructure_back_dm"
+ name:t="superstructure_top_dm"
+ name:t="superstructure_front_dm"
+ name:t="superstructure_side_dm"
+ name:t="ex_armor_body_l_01_dm"
+ name:t="ex_armor_body_l_02_dm"
+ name:t="ex_armor_body_l_03_dm"
+ name:t="ex_armor_body_l_04_dm"
+ name:t="ex_armor_body_l_05_dm"
+ name:t="ex_armor_body_l_06_dm"
+ name:t="ex_armor_body_l_07_dm"
+ name:t="ex_armor_body_l_08_dm"
+ name:t="ex_armor_body_l_09_dm"
+ name:t="ex_armor_body_l_10_dm"
+ name:t="ex_armor_body_r_01_dm"
+ name:t="ex_armor_body_r_02_dm"
+ name:t="ex_armor_body_r_03_dm"
+ name:t="ex_armor_body_r_04_dm"
+ name:t="ex_armor_body_r_05_dm"
+ name:t="ex_armor_body_r_06_dm"
+ name:t="ex_armor_body_r_07_dm"
+ name:t="ex_armor_body_r_08_dm"
+ name:t="ex_armor_body_r_09_dm"
+ name:t="ex_armor_body_r_10_dm"
+ name:t="ex_armor_01_dm"
+ name:t="ex_armor_02_dm"
+ name:t="ex_armor_03_dm"
+ name:t="ex_armor_04_dm"
+ name:t="ex_armor_05_dm"
+ name:t="ex_armor_06_dm"
+ name:t="ex_armor_07_dm"
+ name:t="ex_armor_08_dm"
+ name:t="ex_armor_09_dm"
+ name:t="ex_armor_10_dm"
+ name:t="ex_armor_r_01_dm"
+ name:t="ex_armor_r_02_dm"
+ name:t="ex_armor_r_03_dm"
+ name:t="ex_armor_r_04_dm"
+ name:t="ex_armor_r_05_dm"
+ name:t="ex_armor_r_06_dm"
+ name:t="ex_armor_r_07_dm"
+ name:t="ex_armor_r_08_dm"
+ name:t="ex_armor_r_09_dm"
+ name:t="ex_armor_r_10_dm"
+ name:t="ex_armor_l_01_dm"
+ name:t="ex_armor_l_02_dm"
+ name:t="ex_armor_l_03_dm"
+ name:t="ex_armor_l_04_dm"
+ name:t="ex_armor_l_05_dm"
+ name:t="ex_armor_l_06_dm"
+ name:t="ex_armor_l_07_dm"
+ name:t="ex_armor_l_08_dm"
+ name:t="ex_armor_l_09_dm"
+ name:t="ex_armor_l_10_dm"
+ name:t="turret_front_dm"
+ name:t="turret_side_dm"
+ name:t="turret_back_dm"
+ name:t="turret_top_dm"
+ name:t="turret_01_bottom_dm"
+ name:t="turret_01_front_dm"
+ name:t="turret_01_side_dm"
+ name:t="turret_01_back_dm"
+ name:t="turret_01_top_dm"
+ name:t="turret_02_bottom_dm"
+ name:t="turret_02_front_dm"
+ name:t="turret_02_side_dm"
+ name:t="turret_02_back_dm"
+ name:t="turret_02_top_dm"
+ name:t="turret_03_bottom_dm"
+ name:t="turret_03_front_dm"
+ name:t="turret_03_side_dm"
+ name:t="turret_03_back_dm"
+ name:t="turret_03_top_dm"
+ name:t="turret_04_bottom_dm"
+ name:t="turret_04_front_dm"
+ name:t="turret_04_side_dm"
+ name:t="turret_04_back_dm"
+ name:t="turret_04_top_dm"
+ name:t="turret_05_bottom_dm"
+ name:t="turret_05_front_dm"
+ name:t="turret_05_side_dm"
+ name:t="turret_05_back_dm"
+ name:t="turret_05_top_dm"
+ name:t="turret_06_bottom_dm"
+ name:t="turret_06_front_dm"
+ name:t="turret_06_side_dm"
+ name:t="turret_06_back_dm"
+ name:t="turret_06_top_dm"
+ name:t="turret_07_bottom_dm"
+ name:t="turret_07_front_dm"
+ name:t="turret_07_side_dm"
+ name:t="turret_07_back_dm"
+ name:t="turret_07_top_dm"
+ name:t="turret_08_bottom_dm"
+ name:t="turret_08_front_dm"
+ name:t="turret_08_side_dm"
+ name:t="turret_08_back_dm"
+ name:t="turret_08_top_dm"
+ name:t="turret_09_bottom_dm"
+ name:t="turret_09_front_dm"
+ name:t="turret_09_side_dm"
+ name:t="turret_09_back_dm"
+ name:t="turret_09_top_dm"
+ name:t="gun_mask_01_dm"
+ name:t="gun_mask_02_dm"
+ name:t="gun_mask_03_dm"
+ name:t="gun_mask_04_dm"
+ 
+ onHit{
+ damageType:t="explosion"
+ damage:r=0.0
+ 
+ action{
+ type:t="fxEvent"
+ probability:r=0.05
+ fxEventName:t="fire_after_hit_tiny"
+ }
+ }
+ 
+ onHit{
+ damageType:t="generic"
+ damage:r=0.0
+ 
+ action{
+ type:t="fxEvent"
+ probability:r=0.05
+ fxEventName:t="fire_after_hit_tiny"
+ }
+ }
+ 
+ onHit{
+ damageType:t="explosion"
+ damage:r=18.0
+ 
+ action{
+ type:t="fxEvent"
+ probability:r=0.2
+ fxEventName:t="fire_after_hit_small"
+ }
+ }
+ 
+ onHit{
+ damageType:t="generic"
+ damage:r=30.0
+ 
+ action{
+ type:t="fxEvent"
+ probability:r=0.2
+ fxEventName:t="fire_after_hit_small"
+ }
+ }
+ 
+ onHit{
+ damageType:t="explosion"
+ damage:r=30.0
+ 
+ action{
+ type:t="fxEvent"
+ probability:r=0.4
+ fxEventName:t="fire_after_hit_med"
+ }
+ }
+ 
+ onHit{
+ damageType:t="generic"
+ damage:r=50.0
+ 
+ action{
+ type:t="fxEvent"
+ probability:r=0.4
+ fxEventName:t="fire_after_hit_med"
+ }
+ }
+ 
+ onHit{
+ damageType:t="cumulative"
+ damage:r=80.0
+ 
+ action{
+ type:t="fxEvent"
+ probability:r=0.4
+ fxEventName:t="fire_after_hit_med"
+ }
+ }
+ 
+ onHit{
+ damageType:t="explosion"
+ damage:r=200.0
+ 
+ action{
+ type:t="fxEvent"
+ probability:r=0.7
+ fxEventName:t="fire_after_hit_big"
+ }
+ }
+ 
+ onHit{
+ damageType:t="generic"
+ damage:r=120.0
+ 
+ action{
+ type:t="fxEvent"
+ probability:r=0.7
+ fxEventName:t="fire_after_hit_big"
+ }
+ }
+ 
+ onHit{
+ damageType:t="cumulative"
+ damage:r=200.0
+ 
+ action{
+ type:t="fxEvent"
+ probability:r=0.7
+ fxEventName:t="fire_after_hit_big"
+ }
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
+ substitute:t="machine_gunner"
+ substitute:t="commander"
+ substitute:t="loader"
+ }
+ 
+ driver{
+ dmPart:t="driver_dm"
+ role:t="driver"
+ substitute:t="machine_gunner"
+ substitute:t="commander"
+ substitute:t="loader"
+ }
+ 
+ loader{
+ dmPart:t="loader_dm"
+ role:t="loader"
+ substitute:t="machine_gunner"
+ substitute:t="commander"
+ }
+ 
+ commander{
+ dmPart:t="commander_dm"
+ role:t="commander"
+ substitute:t="machine_gunner"
+ }
+ 
+ machine_gunner{
+ dmPart:t="machine_gunner_dm"
+ role:t="radio_gunner"
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
+ gunConvergence{
+ defaultDistance:r=800.0
+ vertical:b=yes
+ horizontal:b=yes
+ }
+ 
+ class_tags{
+ }
+ 
+ commonWeapons{
+ 
+ Weapon{
+ trigger:t="gunner0"
+ blk:t="gameData/Weapons/groundModels_weapons/90mm_M3A1_user_cannon.blk"
+ emitter:t="bone_gun_barrel"
+ flash:t="emtr_gun_flame"
+ defaultYaw:r=0.0
+ defaultPitch:r=0.0
+ barrelDP:t="gun_barrel_dm"
+ breechDP:t="cannon_breech_dm"
+ speedYaw:r=21.0
+ speedPitch:r=4.0
+ fireConeAngle:r=1.0
+ bullets:i=70
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
+ }
+ 
+ limits{
+ yaw:p2=-180.0, 180.0
+ pitch:p2=-10.0, 20.0
+ }
+ 
+ limitsTable{
+ lim1:p4=-180.0, -135.0, -5.0, 20.0
+ lim2:p4=-135.0, 135.0, -10.0, 20.0
+ lim3:p4=135.0, 180.0, -5.0, 20.0
+ }
+ }
+ 
+ Weapon{
+ trigger:t="gunner1"
+ triggerGroup:t="coaxial"
+ blk:t="gameData/Weapons/groundModels_weapons/7_62mm_M1919A4_user_machinegun.blk"
+ emitter:t="bone_mg_gun_twin"
+ flash:t="emtr_mg_flame_01"
+ defaultYaw:r=0.0
+ defaultPitch:r=0.0
+ barrelDP:t="gun_barrel_01_dm"
+ speedYaw:r=5.5
+ speedPitch:r=4.0
+ fireConeAngle:r=1.0
+ fireConeAngle:r=15.0
+ bullets:i=5500
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
+ blk:t="gameData/Weapons/groundModels_weapons/12_7mm_M2_HB_user_machinegun.blk"
+ emitter:t="bone_mg_aa_v_01"
+ flash:t="emtr_mg_aa_flame_01"
+ defaultYaw:r=0.0
+ defaultPitch:r=0.0
+ barrelDP:t="gun_barrel_02_dm"
+ parkInDeadzone:b=no
+ speedYaw:r=90.0
+ speedPitch:r=90.0
+ bullets:i=600
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
+ }
+ 
+ limits{
+ yaw:p2=-120.0, 120.0
+ pitch:p2=-10.0, 50.0
+ }
+ }
+ }
+ 
+ weapon_presets{
+ 
+ preset{
+ name:t="us_m46_patton_default"
+ blk:t="gameData/units/tankModels/weaponPresets/us_m46_patton_default.blk"
+ }
+ }
+ 
+ ammoStowages{
+ 
+ ammo1{
+ removeLoadedAmmo:b=yes
+ weaponTrigger:t="gunner0"
+ fatalFire:b=yes
+ fatalExplosion:b=yes
+ replenishmentDelay:r=4.0
+ replenishmentTime:r=15.0
+ 
+ shells{
+ firstStage:b=yes
+ 
+ ammo_turret_01_dm{
+ count:i=2
+ }
+ 
+ ammo_turret_02_dm{
+ count:i=2
+ }
+ 
+ ammo_turret_03_dm{
+ count:i=2
+ }
+ 
+ ammo_turret_04_dm{
+ count:i=2
+ }
+ 
+ ammo_turret_05_dm{
+ count:i=2
+ }
+ }
+ 
+ shells{
+ reloadTimeMult:r=1.33
+ 
+ ammo_body_l_01_dm{
+ count:i=1
+ }
+ 
+ ammo_body_l_02_dm{
+ count:i=1
+ }
+ 
+ ammo_body_l_03_dm{
+ count:i=1
+ }
+ 
+ ammo_body_l_04_dm{
+ count:i=1
+ }
+ 
+ ammo_body_l_05_dm{
+ count:i=1
+ }
+ 
+ ammo_body_l_06_dm{
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
+ ammo_body_01_dm{
+ count:i=1
+ }
+ 
+ ammo_body_02_dm{
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
+ ammo_body_06_dm{
+ count:i=1
+ }
+ 
+ ammo_body_07_dm{
+ count:i=1
+ }
+ 
+ ammo_body_08_dm{
+ count:i=1
+ }
+ 
+ ammo_body_09_dm{
+ count:i=1
+ }
+ 
+ ammo_body_10_dm{
+ count:i=1
+ }
+ 
+ ammo_body_11_dm{
+ count:i=1
+ }
+ 
+ ammo_body_12_dm{
+ count:i=1
+ }
+ 
+ ammo_body_13_dm{
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
+ ammo_body_r_01_dm{
+ count:i=1
+ }
+ 
+ ammo_body_r_02_dm{
+ count:i=1
+ }
+ 
+ ammo_body_r_03_dm{
+ count:i=1
+ }
+ 
+ ammo_body_r_04_dm{
+ count:i=1
+ }
+ 
+ ammo_body_r_05_dm{
+ count:i=1
+ }
+ 
+ ammo_body_r_06_dm{
+ count:i=1
+ }
+ }
+ }
+ }
+ 
+ VehiclePhys{
+ 
+ Mass{
+ Empty:r=43450.0
+ Fuel:r=400.0
+ TakeOff:r=43850.0
+ momentOfInertia:p3=2.5, 2.5, 5.0
+ CenterOfGravity:p3=-0.3, 0.5, 0.0
+ CenterOfGravityClampY:p2=0.0, 0.7
+ AdvancedMass:b=yes
+ trackMass:r=2500.0
+ }
+ 
+ tracks{
+ animationMultiplier:r=0.58
+ height:r=0.09
+ width:r=0.5
+ tracksTensionK:p3=8.0, 10.0, 5.0
+ trackMesh:t="us_t84e1_phys_track_line"
+ trackLen:r=0.152
+ trackCount:i=86
+ trackFadeTime:r=1.1
+ trackConnector:b=yes
+ trackEmitSparks:b=no
+ trackMaxHeight:r=1.29
+ trackStartOffset:r=0.07
+ }
+ 
+ collisionProps{
+ cls_turret_01:t="convex_hull"
+ cls_turret_02:t="convex_hull"
+ cls_body_01:t="convex_hull"
+ }
+ 
+ engine{
+ horsePowers:r=810.0
+ maxRPM:r=2800.0
+ minRPM:r=500.0
+ }
+ 
+ mechanics{
+ steerType:t="clutch_braking"
+ maxBrakeForce:r=190000.0
+ driveGearRadius:r=0.33
+ mainGearRatio:r=7.1
+ sideGearRatio:r=0.227
+ neutralGearRatio:r=56.16
+ 
+ gearRatios{
+ ratio:r=-11.2
+ ratio:r=-35.6
+ ratio:r=0.0
+ ratio:r=26.0
+ ratio:r=18.5
+ ratio:r=13.0
+ ratio:r=10.16
+ ratio:r=7.33
+ ratio:r=4.5
+ }
+ }
+ 
+ suspension{
+ maxDisplacementOffsets:p2=0.0, 0.05
+ suspensionOffsets:p3=-0.16, -0.12, 0.1
+ defaultGearRadius:r=0.32
+ frontBackGearRadius:r=0.34
+ topGearRadius:r=0.18
+ defaultDampeningForce:p2=150000.0, 150000.0
+ dampeningRelaxationRatio:r=0.4
+ dampeningCompressionRatio:r=0.15
+ wheel_r_07:r=0.2
+ wheel_l_07:r=0.2
+ wheel_r_drive:r=0.3
+ wheel_l_drive:r=0.3
+ }
+ }
+ 
+ PhysSys{
+ 
+ group{
+ find:t="bone_suspension_(w)_(d+)$"
+ 
+ points{
+ 
+ lever{
+ limitMin:p3=0.0, 0.0, 0.0
+ limitMax:p3=0.0, 0.0, 0.0
+ name:t="bone_suspension_$1_$2"
+ }
+ 
+ suspension_01_01{
+ name:t="bone_suspension_$1_$2_01"
+ limitMin:p3=0.0, -1.0, 0.0
+ limitMax:p3=0.0, 1.0, 0.0
+ }
+ 
+ wheel{
+ 
+ searchChildren{
+ parent:t="lever"
+ find:t="bone_wheel_"
+ occurence:i=1
+ limitMin:p3=-1.0, -1.0, 0.0
+ limitMax:p3=1.0, 1.0, 0.0
+ }
+ }
+ 
+ suspension_01_02{
+ name:t="bone_suspension_$1_$2_02"
+ limitMin:p3=0.0, 0.0, 0.0
+ limitMax:p3=0.0, 0.0, 0.0
+ }
+ }
+ 
+ constraints{
+ 
+ edge{
+ from:t="lever"
+ to:t="wheel"
+ }
+ 
+ edge{
+ moveSecond:b=no
+ from:t="suspension_01_01"
+ to:t="wheel"
+ }
+ 
+ projection{
+ to:t="suspension_01_01"
+ from:t="lever"
+ point:t="suspension_01_02"
+ movePoint:b=no
+ moveEdgeNodes:b=no
+ }
+ }
+ }
+ 
+ group{
+ find:t="bone_suspension_tb_(w)_(d+)$"
+ 
+ points{
+ 
+ suspension{
+ limitMin:p3=0.0, 0.0, 0.0
+ limitMax:p3=0.0, 0.0, 0.0
+ name:t="bone_suspension_tb_$1_$2"
+ }
+ 
+ wheel{
+ 
+ searchChildren{
+ occurence:i=1
+ limitMin:p3=-1.0, -1.0, 0.0
+ limitMax:p3=1.0, 1.0, 0.0
+ parent:t="suspension"
+ find:t="bone_wheel_"
+ }
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
+ }
+ 
+ chainIK{
+ 
+ points{
+ 
+ point{
+ nameTemplate:t="bone_roll_01_01"
+ }
+ 
+ point{
+ nameTemplate:t="bone_roll_01_02"
+ }
+ }
+ 
+ points{
+ 
+ point{
+ nameTemplate:t="bone_roll_02_01"
+ }
+ 
+ point{
+ nameTemplate:t="bone_roll_02_02"
+ }
+ }
+ 
+ points{
+ 
+ point{
+ nameTemplate:t="bone_roll_03_01"
+ }
+ 
+ point{
+ nameTemplate:t="bone_roll_03_02"
+ }
+ }
+ 
+ points{
+ 
+ point{
+ nameTemplate:t="bone_roll_04_01"
+ }
+ 
+ point{
+ nameTemplate:t="bone_roll_04_02"
+ }
+ }
+ 
+ points{
+ 
+ point{
+ nameTemplate:t="bone_roll_05_01"
+ }
+ 
+ point{
+ nameTemplate:t="bone_roll_05_02"
+ }
+ }
+ 
+ points{
+ 
+ point{
+ nameTemplate:t="bone_roll_06_01"
+ }
+ 
+ point{
+ nameTemplate:t="bone_roll_06_02"
+ }
+ }
+ 
+ points{
+ 
+ point{
+ nameTemplate:t="bone_roll_07_01"
+ }
+ 
+ point{
+ nameTemplate:t="bone_roll_07_02"
+ }
+ }
+ 
+ points{
+ 
+ point{
+ nameTemplate:t="bone_roll_08_01"
+ }
+ 
+ point{
+ nameTemplate:t="bone_roll_08_02"
+ }
+ }
+ 
+ points{
+ 
+ point{
+ nameTemplate:t="bone_roll_09_01"
+ }
+ 
+ point{
+ nameTemplate:t="bone_roll_09_02"
+ }
+ }
+ 
+ points{
+ 
+ point{
+ nameTemplate:t="bone_roll_10_01"
+ }
+ 
+ point{
+ nameTemplate:t="bone_roll_10_02"
+ }
+ }
+ 
+ points{
+ 
+ point{
+ nameTemplate:t="bone_roll_11_01"
+ }
+ 
+ point{
+ nameTemplate:t="bone_roll_11_02"
+ }
+ }
+ 
+ points{
+ 
+ point{
+ nameTemplate:t="bone_roll_12_01"
+ }
+ 
+ point{
+ nameTemplate:t="bone_roll_12_02"
+ }
+ }
+ 
+ points{
+ 
+ point{
+ nameTemplate:t="bone_roll_13_01"
+ }
+ 
+ point{
+ nameTemplate:t="bone_roll_13_02"
+ }
+ }
+ 
+ points{
+ 
+ point{
+ nameTemplate:t="bone_roll_14_01"
+ }
+ 
+ point{
+ nameTemplate:t="bone_roll_14_02"
+ }
+ }
+ 
+ points{
+ 
+ point{
+ nameTemplate:t="bone_roll_15_01"
+ }
+ 
+ point{
+ nameTemplate:t="bone_roll_15_02"
+ }
+ }
+ 
+ points{
+ 
+ point{
+ nameTemplate:t="bone_roll_16_01"
+ }
+ 
+ point{
+ nameTemplate:t="bone_roll_16_02"
+ }
+ }
+ 
+ points{
+ 
+ point{
+ nameTemplate:t="bone_roll_17_01"
+ }
+ 
+ point{
+ nameTemplate:t="bone_roll_17_02"
+ }
+ }
+ 
+ points{
+ 
+ point{
+ nameTemplate:t="bone_roll_18_01"
+ }
+ 
+ point{
+ nameTemplate:t="bone_roll_18_02"
+ }
+ }
+ 
+ points{
+ 
+ point{
+ nameTemplate:t="bone_roll_19_01"
+ }
+ 
+ point{
+ nameTemplate:t="bone_roll_19_02"
+ }
+ }
+ 
+ points{
+ 
+ point{
+ nameTemplate:t="bone_roll_20_01"
+ }
+ 
+ point{
+ nameTemplate:t="bone_roll_20_02"
+ }
+ }
+ 
+ points{
+ 
+ point{
+ nameTemplate:t="bone_roll_21_01"
+ }
+ 
+ point{
+ nameTemplate:t="bone_roll_21_02"
+ }
+ }
+ 
+ points{
+ 
+ point{
+ nameTemplate:t="bone_roll_22_01"
+ }
+ 
+ point{
+ nameTemplate:t="bone_roll_22_02"
+ }
+ }
+ 
+ points{
+ 
+ point{
+ nameTemplate:t="bone_roll_23_01"
+ }
+ 
+ point{
+ nameTemplate:t="bone_roll_23_02"
+ }
+ }
+ 
+ points{
+ 
+ point{
+ nameTemplate:t="bone_roll_24_01"
+ }
+ 
+ point{
+ nameTemplate:t="bone_roll_24_02"
+ }
+ }
+ 
+ points{
+ 
+ point{
+ nameTemplate:t="bone_roll_25_01"
+ }
+ 
+ point{
+ nameTemplate:t="bone_roll_25_02"
+ }
+ }
+ 
+ points{
+ 
+ point{
+ nameTemplate:t="bone_roll_26_01"
+ }
+ 
+ point{
+ nameTemplate:t="bone_roll_26_02"
+ }
+ }
+ 
+ points{
+ 
+ point{
+ nameTemplate:t="bone_roll_27_01"
+ }
+ 
+ point{
+ nameTemplate:t="bone_roll_27_02"
+ }
+ }
+ 
+ points{
+ 
+ point{
+ nameTemplate:t="bone_roll_28_01"
+ }
+ 
+ point{
+ nameTemplate:t="bone_roll_28_02"
+ }
+ }
+ 
+ points{
+ 
+ point{
+ nameTemplate:t="bone_roll_29_01"
+ }
+ 
+ point{
+ nameTemplate:t="bone_roll_29_02"
+ }
+ }
+ 
+ points{
+ 
+ point{
+ nameTemplate:t="bone_roll_30_01"
+ }
+ 
+ point{
+ nameTemplate:t="bone_roll_30_02"
+ }
+ }
+ 
+ points{
+ 
+ point{
+ nameTemplate:t="bone_roll_31_01"
+ }
+ 
+ point{
+ nameTemplate:t="bone_roll_31_02"
+ }
+ }
+ 
+ points{
+ 
+ point{
+ nameTemplate:t="bone_roll_32_01"
+ }
+ 
+ point{
+ nameTemplate:t="bone_roll_32_02"
+ }
+ }
+ 
+ points{
+ 
+ point{
+ nameTemplate:t="bone_roll_33_01"
+ }
+ 
+ point{
+ nameTemplate:t="bone_roll_33_02"
+ }
+ }
+ 
+ points{
+ 
+ point{
+ nameTemplate:t="bone_roll_34_01"
+ }
+ 
+ point{
+ nameTemplate:t="bone_roll_34_02"
+ }
+ }
+ 
+ points{
+ 
+ point{
+ nameTemplate:t="bone_roll_35_01"
+ }
+ 
+ point{
+ nameTemplate:t="bone_roll_35_02"
+ }
+ }
+ }
+ 
+ ammo{
+ combustionTime:r=10.0
+ detonateProb:r=0.15
+ detonatePortion:p2=0.6, 0.9
+ explodeHitPower:r=1500.0
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
+ mass:r=8000.0
+ cutDamage:r=1000.0
+ deviation:r=0.5
+ rotation:r=0.5
+ collisionNode:t="cls_turret_01"
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
+ cockpit{
+ zoomOutFov:r=18.49
+ zoomInFov:r=9.217
+ sightFov:r=8.5
+ sightName:t="telescope_m46"
+ headPos:p3=0.0, 3.7, -8.3
+ headPosOnShooting:p3=0.1, 3.5, 0.45
+ detectionHeight:r=2.82
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
+ image:t="#ui/gameuiskin#tank_reinforcement_fr"
+ }
+ 
+ tank_medical_kit_expendable{
+ image:t="#ui/gameuiskin#tank_reinforcement_fr"
+ }
+ 
+ art_support{
+ }
+ 
+ 90mm_us_M82_APCBC_ammo_pack{
+ }
+ 
+ 90mm_us_M82_APCBC{
+ }
+ 
+ 90mm_us_M332_APCR_ammo_pack{
+ }
+ 
+ 90mm_us_M332_APCR{
+ }
+ 
+ 90mm_us_T108_HEAT{
+ }
+ 
+ 90mm_us_T108_HEAT_ammo_pack{
+ }
+ 
+ 90mm_us_M71_HE{
+ }
+ 
+ 90mm_us_M313_Smoke{
+ }
+ 
+ 90mm_us_M313_Smoke_ammo_pack{
+ }
+ }
+ 
+ default_skin{
+ name:t="default"
+ 
+ replace_tex{
+ from:t="us_camo_olive*"
+ to:t="fr_camo_vert_olive_arme*"
+ }
+ }
+ 
+ user_skin{
+ name:t="fr_m46_patton"
+ 
+ replace_tex{
+ from:t="us_camo_olive*"
+ to:t="fr_camo_vert_olive_arme*"
+ }
+ }
+ 
+ skin{
+ name:t="fr_camo_desert_storm"
+ nameLocId:t="skin/fr_camo_desert_storm"
+ descLocId:t="skin/fr_camo_desert_storm/desc"
+ 
+ replace_tex{
+ from:t="fr_camo_vert_olive_arme*"
+ to:t="fr_camo_desert_storm*"
+ }
+ }
+ 
+ skin{
+ name:t="fr_camo_green_brown"
+ nameLocId:t="skin/fr_camo_green_brown"
+ descLocId:t="skin/fr_camo_green_brown/desc"
+ 
+ replace_tex{
+ from:t="fr_camo_vert_olive_arme*"
+ to:t="fr_camo_green_brown*"
+ }
+ }
+ 
+ skin{
+ name:t="fr_camo_green_sand_brown"
+ nameLocId:t="skin/fr_camo_green_sand_brown"
+ descLocId:t="skin/fr_camo_green_sand_brown/desc"
+ 
+ replace_tex{
+ from:t="fr_camo_vert_olive_arme*"
+ to:t="fr_camo_green_sand_brown*"
+ }
+ }
+ 
+ skin{
+ name:t="fr_camo_jaune_sahara"
+ nameLocId:t="skin/fr_camo_jaune_sahara"
+ descLocId:t="skin/fr_camo_jaune_sahara/desc"
+ 
+ replace_tex{
+ from:t="fr_camo_vert_olive_arme*"
+ to:t="fr_camo_jaune_sahara*"
+ }
+ }
+ 
+ skin{
+ name:t="fr_camo_winter_green_white"
+ nameLocId:t="skin/fr_camo_winter_green_white"
+ descLocId:t="skin/fr_camo_winter_green_white/desc"
+ 
+ replace_tex{
+ from:t="fr_camo_vert_olive_arme*"
+ to:t="fr_camo_winter_green_white*"
+ }
+ }
+ 
+ skin{
+ name:t="fr_camo_winter_base"
+ nameLocId:t="skin/fr_camo_winter_base"
+ descLocId:t="skin/fr_camo_winter_base/desc"
+ 
+ replace_tex{
+ from:t="fr_camo_vert_olive_arme*"
+ to:t="fr_camo_winter_base*"
+ }
+ }
```

  **Removed**:
```diff
```


- **aces.vromfs.bin_u/gamedata/units/tankmodels/fr_vbci2_mct30.blkx**:

  **Added**:
```diff
+ Empty:r=26000.0
+ TakeOff:r=27000.0
+ manufacturer:t="volvo"
+ model:t="d13"
+ manufacturer:t="zf"
+ model:t="7hp_902"
+ type:t="auto"
+ wheel_l_01:r=24.0
+ wheel_r_01:r=24.0
+ wheel_l_02:r=13.0
+ wheel_r_02:r=13.0
+ wheel_l_04:r=-13.0
+ wheel_r_04:r=-13.0
```

  **Removed**:
```diff
- Empty:r=31000.0
- TakeOff:r=32000.0
- wheel_l_01:r=20.0
- wheel_r_01:r=20.0
- wheel_l_02:r=10.0
- wheel_r_02:r=10.0
- wheel_l_04:r=-10.0
- wheel_r_04:r=-10.0
```


- **aces.vromfs.bin_u/gamedata/units/tankmodels/germ_pzkpfw_iv_ausf_c.blkx**:

  **Added**:
```diff
+ speedYaw:r=16.0
+ speedYaw:r=16.0
```

  **Removed**:
```diff
- speedYaw:r=15.0
- speedYaw:r=15.0
```


- **aces.vromfs.bin_u/gamedata/units/tankmodels/germ_pzkpfw_iv_ausf_e.blkx**:

  **Added**:
```diff
+ speedYaw:r=16.0
+ speedYaw:r=16.0
```

  **Removed**:
```diff
- speedYaw:r=15.0
- speedYaw:r=15.0
```


- **aces.vromfs.bin_u/gamedata/units/tankmodels/germ_pzkpfw_iv_ausf_f.blkx**:

  **Added**:
```diff
+ speedYaw:r=16.0
+ speedYaw:r=16.0
```

  **Removed**:
```diff
- speedYaw:r=15.0
- speedYaw:r=15.0
```


- **aces.vromfs.bin_u/gamedata/units/tankmodels/germ_pzkpfw_iv_ausf_f2.blkx**:

  **Added**:
```diff
+ speedYaw:r=16.0
+ speedYaw:r=16.0
```

  **Removed**:
```diff
- speedYaw:r=15.0
- speedYaw:r=15.0
```


- **aces.vromfs.bin_u/gamedata/units/tankmodels/germ_pzkpfw_iv_ausf_g.blkx**:

  **Added**:
```diff
+ speedYaw:r=16.0
+ speedYaw:r=16.0
```

  **Removed**:
```diff
- speedYaw:r=15.0
- speedYaw:r=15.0
```


- **aces.vromfs.bin_u/gamedata/units/tankmodels/germ_pzkpfw_iv_ausf_h.blkx**:

  **Added**:
```diff
+ speedYaw:r=16.0
```

  **Removed**:
```diff
- speedYaw:r=15.0
```


- **aces.vromfs.bin_u/gamedata/units/tankmodels/germ_pzkpfw_vi_tiger_p.blkx**:

  **Added**:
```diff
+ Empty:r=52000.0
+ TakeOff:r=52500.0
```

  **Removed**:
```diff
- Empty:r=56500.0
- TakeOff:r=57000.0
```


- **aces.vromfs.bin_u/gamedata/units/tankmodels/germ_sdkfz_234_1.blkx**:

  **Added**:
```diff
```

  **Removed**:
```diff
- substitute:t="machine_gunner"
```


- **aces.vromfs.bin_u/gamedata/units/tankmodels/germ_sppz2_luchs_a2.blkx**:

  **Added**:
```diff
```

  **Removed**:
```diff
- substitute:t="machine_gunner"
```


- **aces.vromfs.bin_u/gamedata/units/tankmodels/il_zsu_57_2.blkx**:

  **Added**:
```diff
+ speedYaw:r=30.0
+ speedYaw:r=30.0
```

  **Removed**:
```diff
- speedYaw:r=60.0
- speedYaw:r=60.0
```


- **aces.vromfs.bin_u/gamedata/units/tankmodels/it_zsu_57_2.blkx**:

  **Added**:
```diff
+ speedYaw:r=30.0
+ speedYaw:r=30.0
```

  **Removed**:
```diff
- speedYaw:r=60.0
- speedYaw:r=60.0
```


- **aces.vromfs.bin_u/gamedata/units/tankmodels/jp_type_5_chi_ri.blkx**:

  **Added**:
```diff
+ bullets:i=102
+ bullets:i=5000
+ Empty:r=36500.0
+ Fuel:r=500.0
+ TakeOff:r=37000.0
+ sideGearRatio:r=8.0407
+ ratio:r=-2.32
+ ratio:r=-4.397
+ ratio:r=4.397
+ ratio:r=2.32
+ ratio:r=1.546
+ ratio:r=0.645
+ count:i=14
+ count:i=14
+ count:i=14
+ count:i=15
+ count:i=15
+ count:i=15
+ count:i=15
```

  **Removed**:
```diff
- bullets:i=120
- bullets:i=3000
- Empty:r=40700.0
- Fuel:r=300.0
- TakeOff:r=41000.0
- sideGearRatio:r=5.1407
- ratio:r=-5.35
- ratio:r=-8.35
- ratio:r=12.5
- ratio:r=10.5
- ratio:r=8.5
- ratio:r=6.0
- ratio:r=3.5
- ratio:r=2.5
- ratio:r=1.5
- count:i=20
- count:i=20
- count:i=20
- count:i=20
- count:i=20
- count:i=10
- count:i=10
```


- **aces.vromfs.bin_u/gamedata/units/tankmodels/jp_type_94.blkx**:

  **Added**:
```diff
+ steeringNodes{
+ wheel_r_01:t="bone_wheel_r_01"
+ wheel_l_01:t="bone_wheel_l_01"
+ }
+ 
+ PhysSys{
+ find:t="^bone_suspension_(w)_(d+)$"
+ 
+ points{
+ 
+ lever{
+ limitMin:p3=0.0, -1.0, 0.0
+ limitMax:p3=0.0, 1.0, 0.0
+ name:t="bone_suspension_c_$2"
+ }
+ 
+ wheel_r_01{
+ 
+ searchChildren{
+ occurence:i=1
+ limitMin:p3=-1.0, -1.0, 0.0
+ limitMax:p3=1.0, 1.0, 0.0
+ parent:t="lever"
+ find:t="bone_wheel_"
+ }
+ }
+ 
+ wheel_l_01{
+ 
+ searchChildren{
+ occurence:i=2
+ limitMin:p3=-1.0, -1.0, 0.0
+ limitMax:p3=1.0, 1.0, 0.0
+ parent:t="lever"
+ find:t="bone_wheel_"
+ }
+ }
+ }
+ 
+ constraints{
+ 
+ edge{
+ to:t="wheel_r_01"
+ from:t="lever"
+ }
+ 
+ edge{
+ from:t="lever"
+ to:t="wheel_l_01"
+ }
+ 
+ slider{
+ moveNodes:b=yes
+ rotateSecond:b=no
+ moveSecond:b=yes
+ moveOnly:b=no
+ point:t="lever"
+ from:t="wheel_l_01"
+ to:t="wheel_r_01"
+ }
+ }
+ }
+ 
+ chainIK{
+ 
+ points{
+ 
+ point{
+ nameTemplate:t="bone_roll_01_01"
+ }
+ 
+ point{
+ nameTemplate:t="bone_roll_01_02"
+ }
+ }
+ 
+ points{
+ 
+ point{
+ nameTemplate:t="bone_roll_02_01"
+ }
+ 
+ point{
+ nameTemplate:t="bone_roll_02_02"
+ }
+ }
+ 
+ points{
+ 
+ point{
+ nameTemplate:t="bone_roll_03_01"
+ }
+ 
+ point{
+ nameTemplate:t="bone_roll_03_02"
+ }
+ }
+ 
+ points{
+ 
+ point{
+ nameTemplate:t="bone_roll_04_01"
+ }
+ 
+ point{
+ nameTemplate:t="bone_roll_04_02"
+ }
+ }
+ 
+ points{
+ 
+ point{
+ nameTemplate:t="bone_roll_05_01"
+ }
+ 
+ point{
+ nameTemplate:t="bone_roll_05_02"
+ }
+ }
+ 
+ points{
+ 
+ point{
+ nameTemplate:t="bone_roll_06_01"
+ }
+ 
+ point{
+ nameTemplate:t="bone_roll_06_02"
+ }
+ }
+ 
+ points{
+ 
+ point{
+ nameTemplate:t="bone_roll_07_01"
+ }
+ 
+ point{
+ nameTemplate:t="bone_roll_07_02"
+ }
+ }
+ 
+ points{
+ 
+ point{
+ nameTemplate:t="bone_roll_08_01"
+ }
+ 
+ point{
+ nameTemplate:t="bone_roll_08_02"
+ }
+ }
+ 
+ points{
+ 
+ point{
+ nameTemplate:t="bone_roll_09_01"
+ }
+ 
+ point{
+ nameTemplate:t="bone_roll_09_02"
+ }
+ }
+ 
+ points{
+ 
+ point{
+ nameTemplate:t="bone_roll_10_01"
+ }
+ 
+ point{
+ nameTemplate:t="bone_roll_10_02"
+ }
+ }
+ 
+ points{
+ 
+ point{
+ nameTemplate:t="bone_roll_11_01"
+ }
+ 
+ point{
+ nameTemplate:t="bone_roll_11_02"
+ }
+ }
+ 
+ points{
+ 
+ point{
+ nameTemplate:t="bone_roll_12_01"
+ }
+ 
+ point{
+ nameTemplate:t="bone_roll_12_02"
+ }
+ }
+ 
+ points{
+ 
+ point{
+ nameTemplate:t="bone_roll_13_01"
+ }
+ 
+ point{
+ nameTemplate:t="bone_roll_13_02"
+ }
+ }
+ 
+ points{
+ 
+ point{
+ nameTemplate:t="bone_roll_14_01"
+ }
+ 
+ point{
+ nameTemplate:t="bone_roll_14_02"
+ }
+ }
+ 
+ points{
+ 
+ point{
+ nameTemplate:t="bone_roll_15_01"
+ }
+ 
+ point{
+ nameTemplate:t="bone_roll_15_02"
+ }
+ }
+ 
+ points{
+ 
+ point{
+ nameTemplate:t="bone_roll_16_01"
+ }
+ 
+ point{
+ nameTemplate:t="bone_roll_16_02"
+ }
+ }
+ 
+ points{
+ 
+ point{
+ nameTemplate:t="bone_roll_17_01"
+ }
+ 
+ point{
+ nameTemplate:t="bone_roll_17_02"
+ }
+ }
+ 
+ points{
+ 
+ point{
+ nameTemplate:t="bone_roll_18_01"
+ }
+ 
+ point{
+ nameTemplate:t="bone_roll_18_02"
+ }
+ }
+ 
+ points{
+ 
+ point{
+ nameTemplate:t="bone_roll_19_01"
+ }
+ 
+ point{
+ nameTemplate:t="bone_roll_19_02"
+ }
+ }
+ 
+ points{
+ 
+ point{
+ nameTemplate:t="bone_roll_20_01"
+ }
+ 
+ point{
+ nameTemplate:t="bone_roll_20_02"
+ }
+ }
+ 
+ points{
+ 
+ point{
+ nameTemplate:t="bone_roll_21_01"
+ }
+ 
+ point{
+ nameTemplate:t="bone_roll_21_02"
+ }
+ }
+ 
+ points{
+ 
+ point{
+ nameTemplate:t="bone_roll_22_01"
+ }
+ 
+ point{
+ nameTemplate:t="bone_roll_22_02"
+ }
+ }
+ 
+ points{
+ 
+ point{
+ nameTemplate:t="bone_roll_23_01"
+ }
+ 
+ point{
+ nameTemplate:t="bone_roll_23_02"
+ }
+ }
+ 
+ points{
+ 
+ point{
+ nameTemplate:t="bone_roll_24_01"
+ }
+ 
+ point{
+ nameTemplate:t="bone_roll_24_02"
+ }
+ }
+ 
+ points{
+ 
+ point{
+ nameTemplate:t="bone_roll_25_01"
+ }
+ 
+ point{
+ nameTemplate:t="bone_roll_25_02"
+ }
+ }
+ 
+ points{
+ 
+ point{
+ nameTemplate:t="bone_roll_26_01"
+ }
+ 
+ point{
+ nameTemplate:t="bone_roll_26_02"
+ }
+ }
+ 
+ points{
+ 
+ point{
+ nameTemplate:t="bone_roll_27_01"
+ }
+ 
+ point{
+ nameTemplate:t="bone_roll_27_02"
+ }
+ }
+ 
+ points{
+ 
+ point{
+ nameTemplate:t="bone_roll_28_01"
+ }
+ 
+ point{
+ nameTemplate:t="bone_roll_28_02"
+ }
+ }
+ 
+ points{
+ 
+ point{
+ nameTemplate:t="bone_roll_29_01"
+ }
+ 
+ point{
+ nameTemplate:t="bone_roll_29_02"
+ }
+ }
+ 
+ points{
+ 
+ point{
+ nameTemplate:t="bone_roll_30_01"
+ }
+ 
+ point{
+ nameTemplate:t="bone_roll_30_02"
+ }
+ }
+ 
+ points{
+ 
+ point{
+ nameTemplate:t="bone_roll_31_01"
+ }
+ 
+ point{
+ nameTemplate:t="bone_roll_31_02"
+ }
+ }
+ 
+ points{
+ 
+ point{
+ nameTemplate:t="bone_roll_32_01"
+ }
+ 
+ point{
+ nameTemplate:t="bone_roll_32_02"
+ }
+ }
+ 
+ points{
+ 
+ point{
+ nameTemplate:t="bone_roll_33_01"
+ }
+ 
+ point{
+ nameTemplate:t="bone_roll_33_02"
+ }
+ }
+ 
+ points{
+ 
+ point{
+ nameTemplate:t="bone_roll_34_01"
+ }
+ 
+ point{
+ nameTemplate:t="bone_roll_34_02"
+ }
+ }
+ 
+ points{
+ 
+ point{
+ nameTemplate:t="bone_roll_35_01"
+ }
+ 
+ point{
+ nameTemplate:t="bone_roll_35_02"
+ }
+ }
+ }
+ 
```

  **Removed**:
```diff
```


- **aces.vromfs.bin_u/gamedata/units/tankmodels/sw_bmp_2md.blkx**:

  **Added**:
```diff
+ thrust:r=11000.0
+ thrust:r=11000.0
```

  **Removed**:
```diff
- thrust:r=19000.0
- thrust:r=19000.0
```


- **aces.vromfs.bin_u/gamedata/units/tankmodels/sw_cv_90_mk4.blkx**:

  **Added**:
```diff
+ turret_09_front_dm{
+ turret_08_bottom_dm{
+ turret_08_front_dm{
+ zoomOutFov:r=30.0
+ zoomInFov:r=7.4
+ sightSize:p2=0.57, 0.4
```

  **Removed**:
```diff
- body_01_top_dm{
- body_01_side_dm{
- body_01_back_dm{
- zoomOutFov:r=50.74
- zoomInFov:r=3.07
- sightSize:p2=0.99, 0.69
```


- **aces.vromfs.bin_u/gamedata/units/tankmodels/sw_zsu_57_2.blkx**:

  **Added**:
```diff
+ speedYaw:r=30.0
+ speedYaw:r=30.0
```

  **Removed**:
```diff
- speedYaw:r=60.0
- speedYaw:r=60.0
```


- **aces.vromfs.bin_u/gamedata/units/tankmodels/uk_a17_mk_1_tetrarch.blkx**:

  **Added**:
```diff
+ speedYaw:r=21.0
+ speedYaw:r=21.0
```

  **Removed**:
```diff
- speedYaw:r=16.0
- speedYaw:r=16.0
```


- **aces.vromfs.bin_u/gamedata/units/tankmodels/uk_a_12_mk_2_matilda_2.blkx**:

  **Added**:
```diff
+ Empty:r=25100.0
+ Fuel:r=300.0
+ TakeOff:r=25400.0
```

  **Removed**:
```diff
- Empty:r=27104.0
- Fuel:r=227.0
- TakeOff:r=27331.0
```


- **aces.vromfs.bin_u/gamedata/units/tankmodels/us_mbt_70.blkx**:

  **Added**:
```diff
+ bullets:i=750
+ lim1:p4=-180.0, -25.0, -15.0, 65.0
+ lim2:p4=-25.0, 3.0, -10.0, 65.0
+ lim3:p4=3.0, 55.0, -5.0, 65.0
+ lim4:p4=55.0, 85.0, 20.0, 65.0
+ lim5:p4=85.0, 105.0, -3.0, 65.0
+ lim6:p4=105.0, 180.0, -6.0, 65.0
+ bullets:i=750
+ lim1:p4=-180.0, -25.0, -15.0, 65.0
+ lim2:p4=-25.0, 3.0, -10.0, 65.0
+ lim3:p4=3.0, 55.0, -5.0, 65.0
+ lim4:p4=55.0, 85.0, 20.0, 65.0
+ lim5:p4=85.0, 105.0, -3.0, 65.0
+ lim6:p4=105.0, 180.0, -6.0, 65.0
```

  **Removed**:
```diff
- bullets:i=2000
- lim1:p4=-180.0, 3.0, -15.0, 65.0
- lim2:p4=3.0, 55.0, -5.0, 65.0
- lim3:p4=55.0, 85.0, 20.0, 65.0
- lim4:p4=85.0, 105.0, -3.0, 65.0
- lim4:p4=105.0, 180.0, -6.0, 65.0
- bullets:i=2000
- lim1:p4=-180.0, 3.0, -15.0, 65.0
- lim2:p4=3.0, 55.0, -5.0, 65.0
- lim3:p4=55.0, 85.0, 20.0, 65.0
- lim4:p4=85.0, 105.0, -3.0, 65.0
- lim4:p4=105.0, 180.0, -6.0, 65.0
```


- **aces.vromfs.bin_u/gamedata/units/tankmodels/ussr_a_12_mk_2_matilda_2a_f96.blkx**:

  **Added**:
```diff
+ Fuel:r=300.0
```

  **Removed**:
```diff
- Fuel:r=227.0
```


- **aces.vromfs.bin_u/gamedata/units/tankmodels/ussr_bmp_2.blkx**:

  **Added**:
```diff
+ thrust:r=11000.0
+ thrust:r=11000.0
```

  **Removed**:
```diff
- thrust:r=19000.0
- thrust:r=19000.0
```


- **aces.vromfs.bin_u/gamedata/units/tankmodels/ussr_bmp_2m.blkx**:

  **Added**:
```diff
+ thrust:r=10000.0
+ thrust:r=10000.0
```

  **Removed**:
```diff
- thrust:r=19000.0
- thrust:r=19000.0
```


- **aces.vromfs.bin_u/gamedata/units/tankmodels/ussr_zis_30.blkx**:

  **Added**:
```diff
+ ratio:r=-11.34
+ ratio:r=9.28
+ ratio:r=4.48
+ ratio:r=2.45
+ ratio:r=1.45
```

  **Removed**:
```diff
```


- **aces.vromfs.bin_u/gamedata/units/tankmodels/ussr_zsu_57_2.blkx**:

  **Added**:
```diff
+ speedYaw:r=30.0
+ speedYaw:r=30.0
```

  **Removed**:
```diff
- speedYaw:r=60.0
- speedYaw:r=60.0
```


- **aces.vromfs.bin_u/gamedata/weapons/groundmodels_weapons/12_7mm_ksp_m88_user_machinegun.blkx**:

  **Added**:
```diff
+ bulletsCartridge:i=100
+ overheat{
+ overheat:p2=12.0, 0.0
+ overheat:p2=13.0, 0.1
+ overheat:p2=15.0, 0.5
+ }
+ 
```

  **Removed**:
```diff
- bulletsCartridge:i=200
```


- **aces.vromfs.bin_u/gamedata/weapons/groundmodels_weapons/12_7mm_m2_hb_md_user_machinegun.blkx**:

  **Added**:
```diff
+ bulletsCartridge:i=100
+ overheat{
+ overheat:p2=12.0, 0.0
+ overheat:p2=13.0, 0.1
+ overheat:p2=15.0, 0.5
+ }
+ 
```

  **Removed**:
```diff
- bulletsCartridge:i=200
```


- **aces.vromfs.bin_u/gamedata/weapons/groundmodels_weapons/12_7mm_m2_hb_t77e1_user_machinegun.blkx**:

  **Added**:
```diff
+ overheat{
+ overheat:p2=12.0, 0.0
+ overheat:p2=13.0, 0.1
+ overheat:p2=15.0, 0.5
+ }
+ 
```

  **Removed**:
```diff
```


- **aces.vromfs.bin_u/gamedata/weapons/groundmodels_weapons/12_7mm_m2_hb_user_machinegun.blkx**:

  **Added**:
```diff
+ bulletsCartridge:i=100
+ overheat{
+ overheat:p2=12.0, 0.0
+ overheat:p2=13.0, 0.1
+ overheat:p2=15.0, 0.5
+ }
+ 
```

  **Removed**:
```diff
- bulletsCartridge:i=200
```


- **aces.vromfs.bin_u/gamedata/weapons/groundmodels_weapons/12_7mm_m2_hb_user_machinegun_for_m15.blkx**:

  **Added**:
```diff
+ overheat{
+ overheat:p2=12.0, 0.0
+ overheat:p2=13.0, 0.1
+ overheat:p2=15.0, 0.5
+ }
+ 
```

  **Removed**:
```diff
```


- **aces.vromfs.bin_u/gamedata/weapons/groundmodels_weapons/12_7mm_m3p_user_machinegun.blkx**:

  **Added**:
```diff
+ bulletsCartridge:i=100
+ overheat{
+ overheat:p2=12.0, 0.0
+ overheat:p2=13.0, 0.1
+ overheat:p2=15.0, 0.5
+ }
+ 
```

  **Removed**:
```diff
- bulletsCartridge:i=200
```


- **aces.vromfs.bin_u/gamedata/weapons/groundmodels_weapons/239mm_9m331_user_cannon.blkx**:

  **Added**:
```diff
```

  **Removed**:
```diff
- bulletName:t=""
- bulletName:t=""
```


- **aces.vromfs.bin_u/gamedata/weapons/groundmodels_weapons/239mm_hq_17_user_cannon.blkx**:

  **Added**:
```diff
+ bulletName:t="239mm_hq17"
+ bulletName:t="239mm_hq17"
```

  **Removed**:
```diff
- bulletName:t="239mm_9m331"
- bulletName:t=""
- bulletName:t="239mm_9m331"
- bulletName:t=""
```


- **aces.vromfs.bin_u/gamedata/weapons/navalmodels_weapons/100mm_65_type_98_naval_user_cannon.blkx**:

  **Added**:
```diff
+ explosiveMass:r=1.4
+ explosiveMass:r=1.4
+ explosiveMass:r=1.4
```

  **Removed**:
```diff
- explosiveMass:r=0.95
- explosiveMass:r=0.95
- explosiveMass:r=0.95
```


- **aces.vromfs.bin_u/gamedata/weapons/navalmodels_weapons/152mm_6inch_47_mk_16_dp_naval_user_cannon.blkx**:

  **Added**:
```diff
+ shotFreq:r=0.2125
```

  **Removed**:
```diff
- shotFreq:r=0.2
```


---
