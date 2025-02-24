### Full Changelog:

- **aces.vromfs.bin_u/config/gameparams.blkx**:

  **Added**:
```diff
+ duplicatedTime:r=5.0
+ chatMessagesTime:r=2.0
+ collisionDamageMult:r=2.5
```

  **Removed**:
```diff
- duplicatedTime:r=10.0
- chatMessagesTime:r=10.0
```


- **aces.vromfs.bin_u/config/gui.blkx**:

  **Added**:
```diff
+ 
+ 9NW46Q333DCL{
+ }
+ 
+ 9N7PX7DZ3WX4{
+ }
+ EE01790000000000{
+ }
+ 
+ EE01800000000000{
+ }
+ 
+ JJ01790000000000{
+ }
+ 
+ JJ01800000000000{
+ }
+ 
+ 
+ UU01790000000000{
+ }
+ 
+ UU01800000000000{
+ }
+ wt_challenger_2_megatron_pack:t="9NW46Q333DCL"
+ wt_thunder_cup_2025_pack:t="9N7PX7DZ3WX4"
+ wt_challenger_2_megatron_ps_prem:t="EE01790000000000"
+ wt_thunder_cup_ps_prem:t="EE01800000000000"
+ wt_challenger_2_megatron_ps_prem:t="UU01790000000000"
+ wt_thunder_cup_ps_prem:t="UU01800000000000"
+ wt_challenger_2_megatron_ps_prem:t="JJ01790000000000"
+ wt_thunder_cup_ps_prem:t="JJ01800000000000"
+ 2025_02_air:t="unlocks/chapter/2025_02_air"
```

  **Removed**:
```diff
```


- **aces.vromfs.bin_u/config/override_circuit.blkx**:

  **Added**:
```diff
+ signUpURL:t="https://warthunder.ru/en/enjoy#/register"
```

  **Removed**:
```diff
- signUpURL:t="https://login.pixstorm.ru/ru/profile/register"
```


- **aces.vromfs.bin_u/config/rendinst_dmg.blkx**:

  **Added**:
```diff
+ dmg{
+ name:t="tree_birch_snow_bush_a"
+ destructionImpulse:r=3000.0
+ destrCollisionHeightScale:r=1.0
+ bushBehaviour:b=yes
+ dmPreset:t="bush_props"
+ }
+ 
+ dmg{
+ name:t="tree_birch_snow_bush_b"
+ destructionImpulse:r=3000.0
+ destrCollisionHeightScale:r=1.0
+ bushBehaviour:b=yes
+ dmPreset:t="bush_props"
+ }
+ 
+ dmg{
+ name:t="tree_birch_bush_a_winter"
+ destructionImpulse:r=3000.0
+ destrCollisionHeightScale:r=1.0
+ bushBehaviour:b=yes
+ dmPreset:t="bush_props"
+ }
+ 
+ dmg{
+ name:t="tree_birch_bush_b_winter"
+ destructionImpulse:r=3000.0
+ destrCollisionHeightScale:r=1.0
+ bushBehaviour:b=yes
+ dmPreset:t="bush_props"
+ }
+ 
+ dmg{
+ name:t="tree_birch_bush_c_winter"
+ destructionImpulse:r=3000.0
+ destrCollisionHeightScale:r=1.0
+ bushBehaviour:b=yes
+ dmPreset:t="bush_props"
+ }
+ 
+ dmg{
+ name:t="tree_snow_bush_a"
+ destructionImpulse:r=3000.0
+ destrCollisionHeightScale:r=1.0
+ bushBehaviour:b=yes
+ dmPreset:t="bush_props"
+ }
+ 
+ dmg{
+ name:t="tree_snow_bush_b"
+ destructionImpulse:r=3000.0
+ destrCollisionHeightScale:r=1.0
+ bushBehaviour:b=yes
+ dmPreset:t="bush_props"
+ }
+ 
+ dmg{
+ name:t="tree_snow_small_a"
+ destructionImpulse:r=3000.0
+ destrCollisionHeightScale:r=1.0
+ bushBehaviour:b=yes
+ dmPreset:t="bush_props"
+ }
+ 
+ dmg{
+ name:t="tree_snow_small_b"
+ destructionImpulse:r=3000.0
+ destrCollisionHeightScale:r=1.0
+ bushBehaviour:b=yes
+ dmPreset:t="bush_props"
+ }
+ 
+ name:t="tree_snow_large_a"
+ destructionImpulse:r=15000.0
+ name:t="tree_snow_large_b"
+ destructionImpulse:r=15000.0
+ name:t="tree_snow_large_c"
+ destructionImpulse:r=15000.0
```

  **Removed**:
```diff
- name:t="tree_snow_large_b"
- destructionImpulse:r=10000.0
- canopyTriangle:b=no
- canopyTopPart:r=0.55
- canopyTopOffset:r=0.1
- canopyWidthPart:r=0.28
- canopyOpacity:r=0.3
- name:t="tree_snow_large_a"
- destructionImpulse:r=10000.0
- canopyTriangle:b=no
- canopyTopPart:r=0.55
- canopyTopOffset:r=0.1
- canopyWidthPart:r=0.28
- canopyOpacity:r=0.3
- name:t="tree_snow_larger_c"
- destructionImpulse:r=25000.0
```


- **aces.vromfs.bin_u/gamedata/attachables/decor_bomb_on_tank.blkx**:

  **Added**:
```diff
+ model:t="decor_bomb_on_tank"
+ collision:t="decor_bomb_on_tank_collision"
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


- **aces.vromfs.bin_u/gamedata/attachables/decor_kubanka_hat.blkx**:

  **Added**:
```diff
+ model:t="decor_kubanka_hat"
+ collision:t="decor_kubanka_hat_collision"
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


- **aces.vromfs.bin_u/gamedata/environments/weather_types_air.blkx**:

  **Added**:
```diff
+ clear{
+ scatteringEffect:p2=0.0, 0.0
+ cloud_shadow_intensity:r=0.8
+ addWhiteTemp:r=-250.0
+ wind_strength:r=1.0
+ waterWindStrength:r=2.0
+ dustMul:r=1.0
+ mudMul:r=1.0
+ rainSplashEnabled:b=no
+ rainSound:t="rain"
+ rainCockpitSound:t="rain_cockpit"
+ skyLightFactor:r=1.0
+ cloudAircraftReflectMul:r=4.0
+ cloudAircraftReflectPowerMul:r=0.5
+ clouds_fly_cube_tex:t="cloud_fly_cube"
+ adaptMinMul:r=1.1
+ 
+ clouds_weather_gen{
+ "layers[0].coverage":p2=0.0, 0.2
+ "layers[1].coverage":p2=0.0, 0.2
+ "layers[0].seed":p2=0.0, 32768.0
+ "layers[1].seed":p2=0.0, 32768.0
+ }
+ 
+ clouds_form{
+ "layers[0].startAt":p2=0.8, 1.1
+ "layers[0].thickness":p2=7.0, 8.2
+ "layers[0].density":p2=1.0, 0.8
+ "layers[0].clouds_type":p2=0.0, 0.2
+ "layers[0].clouds_type_variance":p2=1.0, 1.0
+ "layers[1].startAt":p2=6.0, 6.5
+ "layers[1].thickness":p2=3.5, 4.25
+ "layers[1].density":p2=1.0, 2.0
+ "layers[1].clouds_type":p2=0.0, 0.2
+ "layers[1].clouds_type_variance":p2=0.5, 0.5
+ extinction:p2=0.75, 0.75
+ turbulenceStrength:p2=0.25, 0.3
+ shapeNoiseScale:i=11
+ cumulonimbusShapeScale:i=4
+ turbulenceFreq:i=1
+ }
+ 
+ sky{
+ mie_scale:p2=1.0, 2.0
+ mie2_thickness:r=450.0
+ mie2_scale:r=7.0
+ multiple_scattering_factor:r=1.13
+ sun_brightness:r=0.85
+ moon_brightness:r=0.85
+ }
+ 
+ clouds_gen{
+ humidity:p2=-0.1, 0.2
+ persistence:p2=0.36, 0.5
+ asymmetry:p2=0.05, 0.12
+ }
+ 
+ clouds_position{
+ sizeX:p2=111.0, 111.0
+ sizeZ:p2=99.0, 99.0
+ start_altitude:p2=1.2, 2.5
+ thickness:p2=2.2, 5.0
+ light_extinction:p2=0.25, 0.5
+ amb_extinction_mul:p2=0.5, 1.0
+ }
+ 
+ clouds_render{
+ silver_lining:p2=0.5, 0.7
+ sun_light:p2=0.5, 0.6
+ ambient:p2=0.35, 0.5
+ silver_lining_eccentricity:p2=0.4, 0.7
+ }
+ 
+ strata_clouds{
+ amount:p2=-0.15, 0.22
+ altitude:p2=8.0, 11.9
+ }
+ 
+ windParams{
+ cloudsWindSpeedMult:r=100.0
+ cloudsWindSpeedLimit:r=30.0
+ strataCloudsWindSpeedMult:r=2.0
+ defaultWindSpeed:r=0.1
+ height0:r=500.0
+ turbulence0:r=0.9
+ windMul0:r=1.0
+ height1:r=2000.0
+ turbulence1:r=0.3
+ windMul1:r=0.5
+ height2:r=8000.0
+ turbulence2:r=0.01
+ windMul2:r=0.01
+ }
+ 
+ rain{
+ probability:r=0.0
+ }
+ 
+ clouds_rendering{
+ forward_eccentricity:r=0.73
+ back_eccentricity:r=0.42
+ forward_eccentricity_weight:r=0.75
+ erosion_noise_size:r=42.0
+ ambient_desaturation:r=0.5
+ ms_contribution:r=0.7
+ ms_attenuation:r=0.3
+ ms_ecc_attenuation:r=0.3
+ erosionWindSpeed:r=50.0
+ }
+ 
+ rainDroplets{
+ droplets_reflection_min:r=0.1
+ droplets_reflection_max:r=0.3
+ droplets_size_scale:p3=20.0, 20.0, 4.0
+ droplets_speed:r=1.5
+ }
+ 
+ waterFlowmapParams{
+ simulationSpeed:r=2.0
+ crossfadeTime:r=4.0
+ }
+ 
+ puddlesPower{
+ 
+ p{
+ value:p2=0.0, 0.0
+ weight:r=1.0
+ }
+ }
+ }
+ 
+ good{
+ scatteringEffect:p2=0.0, 0.0
+ cloud_shadow_intensity:r=0.7
+ addWhiteTemp:r=-150.0
+ wind_strength:r=2.5
+ waterWindStrength:r=2.5
+ dustMul:r=1.0
+ mudMul:r=1.0
+ rainSplashEnabled:b=no
+ rainSound:t="rain"
+ rainCockpitSound:t="rain_cockpit"
+ skyLightFactor:r=1.0
+ cloudAircraftReflectMul:r=4.0
+ cloudAircraftReflectPowerMul:r=0.5
+ clouds_fly_cube_tex:t="cloud_fly_cube"
+ 
+ clouds_weather_gen{
+ "layers[0].coverage":p2=0.22, 0.37
+ "layers[1].coverage":p2=0.22, 0.37
+ "layers[0].seed":p2=0.0, 32768.0
+ "layers[1].seed":p2=0.0, 32768.0
+ epicness:r=0.09
+ }
+ 
+ clouds_form{
+ "layers[0].startAt":p2=0.8, 2.29
+ "layers[0].thickness":p2=7.2, 8.2
+ "layers[0].density":p2=1.0, 0.8
+ "layers[0].clouds_type":p2=0.5, 0.15
+ "layers[0].clouds_type_variance":p2=1.0, 0.9
+ "layers[1].startAt":p2=6.5, 6.5
+ "layers[1].thickness":p2=3.5, 4.25
+ "layers[1].density":p2=1.0, 1.2
+ "layers[1].clouds_type":p2=0.25, 0.49
+ "layers[1].clouds_type_variance":p2=0.5, 0.89
+ extinction:p2=0.75, 0.84
+ turbulenceStrength:p2=0.25, 0.3
+ shapeNoiseScale:i=11
+ cumulonimbusShapeScale:i=4
+ turbulencFreq:i=1
+ }
+ 
+ sky{
+ mie_scale:p2=1.0, 3.0
+ mie2_thickness:r=250.0
+ mie2_scale:r=13.0
+ multiple_scattering_factor:r=1.2
+ moon_brightness:r=0.775
+ }
+ 
+ clouds_gen{
+ humidity:p2=0.22, 0.37
+ persistence:p2=0.36, 0.74
+ asymmetry:p2=0.1, 0.2
+ }
+ 
+ clouds_position{
+ sizeX:p2=111.0, 111.0
+ sizeZ:p2=99.0, 99.0
+ start_altitude:p2=1.2, 2.0
+ thickness:p2=2.0, 3.5
+ amb_extinction_mul:p2=0.5, 1.2
+ 
+ light_extinction{
+ 
+ p{
+ value:p2=0.6, 0.85
+ weight:r=1.0
+ }
+ 
+ p{
+ value:p2=0.85, 1.2
+ weight:r=5.0
+ }
+ }
+ }
+ 
+ clouds_render{
+ silver_lining:p2=0.5, 1.0
+ sun_light:p2=0.4, 0.6
+ ambient:p2=0.3, 0.6
+ silver_lining_eccentricity:p2=0.4, 0.7
+ }
+ 
+ strata_clouds{
+ amount:p2=0.25, 0.5
+ altitude:p2=9.2, 11.9
+ }
+ 
+ windParams{
+ cloudsWindSpeedMult:r=100.0
+ cloudsWindSpeedLimit:r=30.0
+ strataCloudsWindSpeedMult:r=4.0
+ defaultWindSpeed:r=0.1
+ height0:r=300.0
+ turbulence0:r=1.0
+ windMul0:r=1.0
+ height1:r=2000.0
+ turbulence1:r=0.8
+ windMul1:r=1.0
+ height2:r=8000.0
+ turbulence2:r=0.2
+ windMul2:r=0.01
+ }
+ 
+ rain{
+ probability:r=0.0
+ }
+ 
+ clouds_rendering{
+ forward_eccentricity:r=0.73
+ back_eccentricity:r=0.42
+ forward_eccentricity_weight:r=0.75
+ erosion_noise_size:r=42.0
+ ambient_desaturation:r=0.5
+ ms_contribution:r=0.7
+ ms_attenuation:r=0.3
+ ms_ecc_attenuation:r=0.3
+ erosionWindSpeed:r=50.0
+ }
+ 
+ rainX7{
+ alphaFadeSpeedBegin:r=20.0
+ alphaFadeSpeedEnd:r=170.0
+ length:r=0.75
+ speed:r=8.5
+ width:r=0.02
+ density:r=2.0
+ wind:r=1.0
+ alpha:r=0.2
+ lighting:p3=0.3, 0.3, 0.32
+ perPassMul:r=5.0
+ }
+ 
+ rainDroplets{
+ droplets_reflection_min:r=0.1
+ droplets_reflection_max:r=0.3
+ droplets_size_scale:p3=20.0, 20.0, 4.0
+ droplets_speed:r=1.5
+ }
+ 
+ waterFlowmapParams{
+ simulationSpeed:r=2.0
+ crossfadeTime:r=4.0
+ }
+ 
+ puddlesPower{
+ 
+ p{
+ value:p2=0.0, 0.0
+ weight:r=1.0
+ }
+ }
+ }
+ 
+ hazy{
+ addWhiteTemp:r=-150.0
+ cloud_shadow_intensity:r=0.8
+ cloudDropletsScale:r=0.1
+ cloudDropletsLayerThickness:r=1.0
+ wind_strength:r=2.2
+ waterWindStrength:r=2.5
+ dustMul:r=1.0
+ mudMul:r=1.0
+ rainSplashEnabled:b=no
+ rainSound:t="rain"
+ rainCockpitSound:t="rain_cockpit"
+ skyLightFactor:r=1.0
+ cloudAircraftReflectMul:r=4.0
+ cloudAircraftReflectPowerMul:r=0.5
+ clouds_fly_cube_tex:t="cloud_fly_cube"
+ 
+ clouds_weather_gen{
+ "layers[0].coverage":p2=0.2, 0.3
+ "layers[0].freq":p2=3.0, 6.23
+ "layers[1].coverage":p2=0.28, 0.36
+ "layers[1].freq":p2=6.0, 8.0
+ "layers[0].seed":p2=0.0, 32768.0
+ "layers[1].seed":p2=0.0, 32768.0
+ }
+ 
+ clouds_form{
+ "layers[0].startAt":p2=0.8, 2.97
+ "layers[0].thickness":p2=8.0, 8.35
+ "layers[0].density":p2=1.0, 1.62
+ "layers[0].clouds_type":p2=0.5, 0.81
+ "layers[0].clouds_type_variance":p2=1.0, 0.9
+ "layers[1].startAt":p2=6.5, 6.87
+ "layers[1].thickness":p2=3.5, 7.1
+ "layers[1].density":p2=1.0, 1.87
+ "layers[1].clouds_type":p2=0.25, 0.52
+ "layers[1].clouds_type_variance":p2=0.5, 0.13
+ extinction:p2=0.65, 2.25
+ turbulenceStrength:p2=0.25, 0.25
+ shapeNoiseScale:i=15
+ cumulonimbusShapeScale:i=4
+ turbulenceFreq:i=2
+ }
+ 
+ sky{
+ mie_scale:p2=5.0, 11.0
+ mie2_thickness:r=570.0
+ mie2_scale:r=37.0
+ sun_brightness:r=0.85
+ moon_brightness:r=0.37
+ multiple_scattering_factor:r=1.23
+ }
+ 
+ clouds_gen{
+ humidity:p2=0.22, 0.38
+ persistence:p2=0.5, 0.8
+ asymmetry:p2=0.1, 0.2
+ }
+ 
+ clouds_position{
+ sizeX:p2=111.0, 111.0
+ sizeZ:p2=99.0, 99.0
+ start_altitude:p2=1.8, 3.0
+ thickness:p2=3.5, 5.5
+ 
+ thickness{
+ 
+ p{
+ value:p2=2.6, 3.0
+ weight:r=0.5
+ }
+ 
+ p{
+ value:p2=3.0, 4.0
+ weight:r=5.0
+ }
+ 
+ p{
+ value:p2=4.0, 5.0
+ weight:r=1.0
+ }
+ }
+ light_extinction:p2=0.6, 1.9
+ 
+ light_extinction{
+ 
+ p{
+ value:p2=0.6, 0.85
+ weight:r=1.0
+ }
+ 
+ p{
+ value:p2=0.85, 1.05
+ weight:r=5.0
+ }
+ }
+ amb_extinction_mul:p2=0.12, 0.3
+ }
+ 
+ clouds_render{
+ silver_lining:p2=0.4, 0.7
+ sun_light:p2=0.3, 0.55
+ ambient:p2=0.35, 0.6
+ silver_lining_eccentricity:p2=0.4, 0.75
+ }
+ 
+ strata_clouds{
+ amount:p2=0.25, 0.7
+ altitude:p2=8.0, 11.9
+ }
+ 
+ windParams{
+ cloudsWindSpeedLimit:r=10.0
+ defaultWindSpeed:r=0.05
+ height0:r=1000.0
+ turbulence0:r=0.3
+ windMul0:r=1.0
+ height1:r=3000.0
+ turbulence1:r=0.3
+ windMul1:r=1.0
+ height2:r=8000.0
+ turbulence2:r=0.3
+ windMul2:r=0.01
+ }
+ 
+ rain{
+ probability:r=0.0
+ }
+ 
+ clouds_rendering{
+ forward_eccentricity:r=0.73
+ back_eccentricity:r=0.42
+ forward_eccentricity_weight:r=0.75
+ erosion_noise_size:r=42.0
+ ambient_desaturation:r=0.5
+ ms_contribution:r=0.7
+ ms_attenuation:r=0.3
+ ms_ecc_attenuation:r=0.3
+ erosionWindSpeed:r=50.0
+ }
+ 
+ rainX7{
+ alphaFadeSpeedBegin:r=20.0
+ alphaFadeSpeedEnd:r=170.0
+ length:r=0.75
+ speed:r=8.5
+ width:r=0.02
+ density:r=2.0
+ wind:r=1.0
+ alpha:r=0.2
+ lighting:p3=0.3, 0.3, 0.32
+ perPassMul:r=5.0
+ }
+ 
+ rainDroplets{
+ droplets_reflection_min:r=0.1
+ droplets_reflection_max:r=0.3
+ droplets_size_scale:p3=20.0, 20.0, 4.0
+ droplets_speed:r=1.5
+ }
+ 
+ waterFlowmapParams{
+ simulationSpeed:r=2.0
+ crossfadeTime:r=4.0
+ }
+ 
+ puddlesPower{
+ 
+ p{
+ value:p2=0.0, 0.0
+ weight:r=1.0
+ }
+ }
+ }
+ 
+ cloudy{
+ scatteringEffect:p2=0.0, 0.0
+ cloud_shadow_intensity:r=0.7
+ addWhiteTemp:r=0.0
+ cloudDropletsScale:r=0.3
+ cloudDropletsLayerThickness:r=2.0
+ wind_strength:r=3.0
+ waterWindStrength:r=3.0
+ dustMul:r=1.0
+ mudMul:r=1.0
+ rainSplashEnabled:b=no
+ rainSound:t="rain"
+ rainCockpitSound:t="rain_cockpit"
+ skyLightFactor:r=1.0
+ cloudAircraftReflectMul:r=4.0
+ cloudAircraftReflectPowerMul:r=0.5
+ clouds_fly_cube_tex:t="cloud_fly_cube"
+ 
+ clouds_weather_gen{
+ "layers[0].coverage":p2=0.4, 0.5
+ "layers[1].coverage":p2=0.45, 0.55
+ "layers[0].seed":p2=0.0, 32768.0
+ "layers[1].seed":p2=0.0, 32768.0
+ epicness:r=1.0
+ }
+ 
+ clouds_form{
+ "layers[0].thickness":p2=8.0, 9.0
+ "layers[0].density":p2=1.0, 1.2
+ "layers[0].clouds_type":p2=0.45, 0.55
+ "layers[0].clouds_type_variance":p2=0.75, 1.0
+ "layers[1].thickness":p2=3.5, 3.5
+ "layers[1].density":p2=1.0, 1.0
+ "layers[1].clouds_type":p2=0.25, 0.35
+ "layers[1].clouds_type_variance":p2=0.5, 0.75
+ extinction:p2=0.75, 0.9
+ turbulenceStrength:p2=0.25, 0.25
+ shapeNoiseScale:i=9
+ cumulonimbusShapeScale:i=4
+ turbulenceFreq:i=1
+ "layers[0].startAt":p2=1.8, 2.0
+ "layers[1].startAt":p2=7.0, 7.5
+ }
+ 
+ sky{
+ mie_scale:p2=5.0, 8.0
+ mie_height:p2=0.8, 1.1
+ mie2_thickness:r=300.0
+ mie2_scale:r=15.0
+ multiple_scattering_factor:r=1.4
+ moon_brightness:r=0.32
+ }
+ 
+ clouds_gen{
+ humidity:p2=0.47, 0.62
+ persistence:p2=0.58, 0.7
+ asymmetry:p2=0.08, 0.22
+ }
+ 
+ clouds_position{
+ sizeX:p2=111.0, 111.0
+ sizeZ:p2=99.0, 99.0
+ 
+ start_altitude{
+ 
+ p{
+ value:p2=1.2, 1.4
+ weight:r=8.0
+ }
+ 
+ p{
+ value:p2=1.4, 2.0
+ weight:r=1.0
+ }
+ }
+ 
+ thickness{
+ 
+ p{
+ value:p2=2.6, 3.0
+ weight:r=0.5
+ }
+ 
+ p{
+ value:p2=3.0, 3.5
+ weight:r=5.0
+ }
+ 
+ p{
+ value:p2=3.5, 5.0
+ weight:r=1.0
+ }
+ }
+ 
+ light_extinction{
+ 
+ p{
+ value:p2=0.6, 0.85
+ weight:r=1.0
+ }
+ 
+ p{
+ value:p2=0.85, 1.05
+ weight:r=5.0
+ }
+ }
+ 
+ amb_extinction_mul{
+ 
+ p{
+ value:p2=0.3, 1.0
+ weight:r=1.0
+ }
+ }
+ }
+ 
+ strata_clouds{
+ amount:p2=0.4, 0.85
+ altitude:p2=9.0, 11.9
+ }
+ 
+ windParams{
+ cloudsWindSpeedMult:r=100.0
+ cloudsWindSpeedLimit:r=40.0
+ strataCloudsWindSpeedMult:r=4.0
+ defaultWindSpeed:r=0.1
+ height0:r=600.0
+ turbulence0:r=0.7
+ windMul0:r=1.0
+ height1:r=2000.0
+ turbulence1:r=0.7
+ windMul1:r=1.0
+ height2:r=8000.0
+ turbulence2:r=0.3
+ windMul2:r=0.01
+ }
+ 
+ rain{
+ probability:r=0.45
+ }
+ 
+ clouds_rendering{
+ forward_eccentricity:r=0.73
+ back_eccentricity:r=0.42
+ forward_eccentricity_weight:r=0.75
+ erosion_noise_size:r=42.0
+ ambient_desaturation:r=0.5
+ ms_contribution:r=0.7
+ ms_attenuation:r=0.3
+ ms_ecc_attenuation:r=0.3
+ erosionWindSpeed:r=50.0
+ }
+ 
+ rainX7{
+ alphaFadeSpeedBegin:r=20.0
+ alphaFadeSpeedEnd:r=170.0
+ length:r=0.75
+ speed:r=8.5
+ width:r=0.02
+ density:r=2.0
+ wind:r=1.0
+ alpha:r=0.2
+ lighting:p3=0.3, 0.3, 0.32
+ perPassMul:r=5.0
+ }
+ 
+ rainDroplets{
+ droplets_reflection_min:r=0.1
+ droplets_reflection_max:r=0.3
+ droplets_size_scale:p3=20.0, 20.0, 4.0
+ droplets_speed:r=1.5
+ }
+ 
+ waterFlowmapParams{
+ simulationSpeed:r=2.0
+ crossfadeTime:r=4.0
+ }
+ 
+ puddlesPower{
+ 
+ p{
+ value:p2=0.02, 0.03
+ weight:r=2.0
+ }
+ 
+ p{
+ value:p2=0.1, 0.2
+ weight:r=1.0
+ }
+ 
+ p{
+ value:p2=0.3, 0.35
+ weight:r=1.0
+ }
+ }
+ }
+ 
+ thin_clouds{
+ scatteringEffect:p2=0.0, 0.0
+ addWhiteTemp:r=0.0
+ cloud_shadow_intensity:r=0.7
+ wind_strength:r=3.0
+ waterWindStrength:r=3.0
+ dustMul:r=1.0
+ mudMul:r=1.0
+ rainSplashEnabled:b=no
+ rainSound:t="rain"
+ rainCockpitSound:t="rain_cockpit"
+ skyLightFactor:r=1.0
+ cloudAircraftReflectMul:r=4.0
+ cloudAircraftReflectPowerMul:r=0.5
+ clouds_fly_cube_tex:t="cloud_fly_cube"
+ 
+ clouds_weather_gen{
+ "layers[0].coverage":p2=0.3, 0.36
+ "layers[0].freq":p2=3.0, 3.0
+ "layers[1].coverage":p2=0.5, 0.54
+ "layers[1].freq":p2=6.0, 6.0
+ epicness:r=0.9
+ }
+ 
+ clouds_form{
+ "layers[0].thickness":p2=8.0, 3.85
+ "layers[0].density":p2=1.0, 1.0
+ "layers[0].clouds_type":p2=0.5, 0.5
+ "layers[0].clouds_type_variance":p2=1.0, 1.0
+ "layers[1].thickness":p2=3.5, 2.4
+ "layers[1].density":p2=1.0, 1.0
+ "layers[1].clouds_type":p2=0.25, 0.25
+ "layers[1].clouds_type_variance":p2=0.5, 0.5
+ extinction:p2=0.75, 0.83
+ turbulenceStrength:p2=0.25, 0.65
+ shapeNoiseScale:i=5
+ cumulonimbusShapeScale:i=15
+ turbulenceFreq:i=5
+ "layers[0].startAt":p2=1.8, 2.43
+ "layers[1].startAt":p2=7.13, 7.5
+ }
+ 
+ sky{
+ mie_scale:p2=2.7, 7.3
+ mie_height:p2=0.8, 2.43
+ mie2_thickness:r=500.0
+ mie2_scale:r=10.0
+ multiple_scattering_factor:r=1.4
+ moon_brightness:r=0.39
+ }
+ 
+ clouds_gen{
+ humidity:p2=0.38, 0.55
+ persistence:p2=0.3, 0.6
+ asymmetry:p2=0.9, 2.0
+ }
+ 
+ clouds_position{
+ sizeX:p2=111.0, 111.0
+ sizeZ:p2=99.0, 99.0
+ start_altitude:p2=2.0, 2.5
+ thickness:p2=5.0, 8.0
+ light_extinction:p2=0.5, 1.0
+ amb_extinction_mul:p2=0.5, 1.0
+ }
+ 
+ clouds_render{
+ silver_lining:p2=0.5, 1.0
+ sun_light:p2=0.35, 0.6
+ ambient:p2=0.35, 0.8
+ silver_lining_eccentricity:p2=0.4, 0.7
+ }
+ 
+ strata_clouds{
+ amount:p2=0.4, 0.85
+ altitude:p2=9.0, 11.9
+ }
+ 
+ windParams{
+ cloudsWindSpeedLimit:r=25.0
+ cloudsWindSpeedMult:r=100.0
+ strataCloudsWindSpeedMult:r=4.0
+ defaultWindSpeed:r=0.1
+ height0:r=600.0
+ turbulence0:r=0.7
+ windMul0:r=1.0
+ height1:r=2000.0
+ turbulence1:r=0.7
+ windMul1:r=1.0
+ height2:r=8000.0
+ turbulence2:r=0.3
+ windMul2:r=0.01
+ }
+ 
+ rain{
+ probability:r=0.05
+ }
+ 
+ clouds_rendering{
+ forward_eccentricity:r=0.73
+ back_eccentricity:r=0.42
+ forward_eccentricity_weight:r=0.75
+ erosion_noise_size:r=42.0
+ ambient_desaturation:r=0.5
+ ms_contribution:r=0.7
+ ms_attenuation:r=0.3
+ ms_ecc_attenuation:r=0.3
+ erosionWindSpeed:r=50.0
+ }
+ 
+ rainX7{
+ alphaFadeSpeedBegin:r=20.0
+ alphaFadeSpeedEnd:r=170.0
+ length:r=0.75
+ speed:r=8.5
+ width:r=0.02
+ density:r=2.0
+ wind:r=1.0
+ alpha:r=0.2
+ lighting:p3=0.3, 0.3, 0.32
+ perPassMul:r=5.0
+ }
+ 
+ rainDroplets{
+ droplets_reflection_min:r=0.1
+ droplets_reflection_max:r=0.3
+ droplets_size_scale:p3=20.0, 20.0, 4.0
+ droplets_speed:r=1.5
+ }
+ 
+ waterFlowmapParams{
+ simulationSpeed:r=2.0
+ crossfadeTime:r=4.0
+ }
+ 
+ puddlesPower{
+ 
+ p{
+ value:p2=0.0, 0.0
+ weight:r=1.0
+ }
+ 
+ p{
+ value:p2=0.14, 0.16
+ }
+ 
+ p{
+ value:p2=0.22, 0.25
+ }
+ }
+ }
+ 
+ thin_clouds_storm{
+ scatteringEffect:p2=0.0, 0.0
+ addWhiteTemp:r=0.0
+ cloud_shadow_intensity:r=0.7
+ wind_strength:r=5.0
+ waterWindStrength:r=2.8
+ dustMul:r=1.0
+ mudMul:r=1.0
+ rainSplashEnabled:b=no
+ rainSound:t="rain"
+ rainCockpitSound:t="rain_cockpit"
+ skyLightFactor:r=1.0
+ cloudAircraftReflectMul:r=4.0
+ cloudAircraftReflectPowerMul:r=0.5
+ clouds_fly_cube_tex:t="cloud_fly_cube"
+ 
+ clouds_weather_gen{
+ "layers[0].coverage":p2=0.3, 0.36
+ "layers[0].freq":p2=3.0, 3.0
+ "layers[1].coverage":p2=0.5, 0.54
+ "layers[1].freq":p2=6.0, 6.0
+ epicness:r=0.9
+ }
+ 
+ clouds_form{
+ "layers[0].thickness":p2=8.0, 3.85
+ "layers[0].density":p2=1.0, 1.0
+ "layers[0].clouds_type":p2=0.5, 0.5
+ "layers[0].clouds_type_variance":p2=1.0, 1.0
+ "layers[1].thickness":p2=3.5, 2.4
+ "layers[1].density":p2=1.0, 1.0
+ "layers[1].clouds_type":p2=0.25, 0.25
+ "layers[1].clouds_type_variance":p2=0.5, 0.5
+ extinction:p2=0.75, 0.83
+ turbulenceStrength:p2=0.25, 0.65
+ shapeNoiseScale:i=5
+ cumulonimbusShapeScale:i=15
+ turbulenceFreq:i=5
+ "layers[0].startAt":p2=1.8, 2.43
+ "layers[1].startAt":p2=7.13, 7.5
+ }
+ 
+ sky{
+ mie_scale:p2=2.7, 7.3
+ mie_height:p2=0.8, 2.43
+ mie2_thickness:r=500.0
+ mie2_scale:r=10.0
+ multiple_scattering_factor:r=1.4
+ moon_brightness:r=0.39
+ }
+ 
+ clouds_gen{
+ humidity:p2=0.38, 0.55
+ persistence:p2=0.3, 0.6
+ asymmetry:p2=0.9, 2.0
+ }
+ 
+ clouds_position{
+ sizeX:p2=111.0, 111.0
+ sizeZ:p2=99.0, 99.0
+ start_altitude:p2=2.0, 2.5
+ thickness:p2=5.0, 8.0
+ light_extinction:p2=0.5, 1.0
+ amb_extinction_mul:p2=0.5, 1.0
+ }
+ 
+ clouds_render{
+ silver_lining:p2=0.5, 1.0
+ sun_light:p2=0.35, 0.6
+ ambient:p2=0.35, 0.8
+ silver_lining_eccentricity:p2=0.4, 0.7
+ }
+ 
+ strata_clouds{
+ amount:p2=0.4, 0.85
+ altitude:p2=9.0, 11.9
+ }
+ 
+ windParams{
+ cloudsWindSpeedLimit:r=25.0
+ cloudsWindSpeedMult:r=100.0
+ strataCloudsWindSpeedMult:r=4.0
+ defaultWindSpeed:r=0.1
+ height0:r=600.0
+ turbulence0:r=0.7
+ windMul0:r=1.0
+ height1:r=2000.0
+ turbulence1:r=0.7
+ windMul1:r=1.0
+ height2:r=8000.0
+ turbulence2:r=0.3
+ windMul2:r=0.01
+ }
+ 
+ rain{
+ probability:r=0.05
+ }
+ 
+ clouds_rendering{
+ forward_eccentricity:r=0.73
+ back_eccentricity:r=0.42
+ forward_eccentricity_weight:r=0.75
+ erosion_noise_size:r=42.0
+ ambient_desaturation:r=0.5
+ ms_contribution:r=0.7
+ ms_attenuation:r=0.3
+ ms_ecc_attenuation:r=0.3
+ erosionWindSpeed:r=50.0
+ }
+ 
+ rainX7{
+ alphaFadeSpeedBegin:r=20.0
+ alphaFadeSpeedEnd:r=170.0
+ length:r=0.75
+ speed:r=8.5
+ width:r=0.02
+ density:r=2.0
+ wind:r=1.0
+ alpha:r=0.2
+ lighting:p3=0.3, 0.3, 0.32
+ perPassMul:r=5.0
+ }
+ 
+ rainDroplets{
+ droplets_reflection_min:r=0.1
+ droplets_reflection_max:r=0.3
+ droplets_size_scale:p3=20.0, 20.0, 4.0
+ droplets_speed:r=1.5
+ }
+ 
+ waterFlowmapParams{
+ simulationSpeed:r=2.0
+ crossfadeTime:r=4.0
+ }
+ 
+ puddlesPower{
+ 
+ p{
+ value:p2=0.0, 0.0
+ weight:r=1.0
+ }
+ 
+ p{
+ value:p2=0.14, 0.16
+ }
+ 
+ p{
+ value:p2=0.22, 0.25
+ }
+ }
+ }
+ 
+ poor{
+ scatteringEffect:p2=0.0, 0.0
+ cloud_shadow_intensity:r=0.7
+ addWhiteTemp:r=0.0
+ cloudDropletsScale:r=0.3
+ cloudDropletsLayerThickness:r=2.0
+ wind_strength:r=5.0
+ waterWindStrength:r=3.0
+ dustMul:r=1.0
+ mudMul:r=1.0
+ rainSplashEnabled:b=no
+ rainSound:t="rain"
+ rainCockpitSound:t="rain_cockpit"
+ skyLightFactor:r=1.0
+ cloudAircraftReflectMul:r=4.0
+ cloudAircraftReflectPowerMul:r=0.5
+ clouds_fly_cube_tex:t="cloud_fly_cube"
+ wetnessPower:r=0.3
+ cloudsShadowInfluence:r=0.82
+ enableCloudsHole:b=no
+ cloudsShadowWaterInfluence:r=0.0
+ 
+ clouds_weather_gen{
+ "layers[0].freq":p2=7.461, 8.461
+ "layers[1].freq":p2=6.13, 7.0
+ cumulonimbusCoverage:p2=0.17, 0.19
+ epicness:r=0.0
+ "layers[0].seed":p2=0.0, 32768.0
+ "layers[1].seed":p2=0.0, 32768.0
+ cumulonimbusSeed:p2=0.0, 32768.0
+ "layers[0].coverage":p2=0.1, 0.1
+ "layers[1].coverage":p2=0.95, 1.0
+ }
+ 
+ clouds_form{
+ "layers[0].thickness":p2=1.728, 1.74
+ "layers[0].density":p2=1.521, 1.747
+ "layers[0].clouds_type":p2=0.9, 1.0
+ "layers[0].clouds_type_variance":p2=0.652, 0.099
+ "layers[1].thickness":p2=3.68, 4.336
+ "layers[1].density":p2=1.135, 1.135
+ "layers[1].clouds_type":p2=0.5, 0.6
+ "layers[1].clouds_type_variance":p2=0.019, 0.019
+ extinction:p2=0.75, 0.75
+ turbulenceStrength:p2=0.25, 0.25
+ shapeNoiseScale:i=7
+ cumulonimbusShapeScale:i=4
+ turbulenceFreq:i=3
+ "layers[0].startAt":p2=2.5, 2.68
+ "layers[1].startAt":p2=6.0, 7.5
+ }
+ 
+ sky{
+ mie_scale:p2=11.0, 13.7
+ mie_height:p2=0.8, 1.1
+ mie2_thickness:r=220.0
+ mie2_scale:r=30.0
+ multiple_scattering_factor:r=0.04
+ moon_brightness:r=0.32
+ }
+ 
+ clouds_gen{
+ humidity:p2=0.47, 0.62
+ persistence:p2=0.58, 0.7
+ asymmetry:p2=0.08, 0.22
+ }
+ 
+ clouds_position{
+ sizeX:p2=111.0, 111.0
+ sizeZ:p2=99.0, 99.0
+ 
+ start_altitude{
+ 
+ p{
+ value:p2=1.2, 1.4
+ weight:r=8.0
+ }
+ 
+ p{
+ value:p2=1.4, 2.0
+ weight:r=1.0
+ }
+ }
+ 
+ thickness{
+ 
+ p{
+ value:p2=2.6, 3.0
+ weight:r=0.5
+ }
+ 
+ p{
+ value:p2=3.0, 3.5
+ weight:r=5.0
+ }
+ 
+ p{
+ value:p2=3.5, 5.0
+ weight:r=1.0
+ }
+ }
+ 
+ light_extinction{
+ 
+ p{
+ value:p2=0.6, 0.85
+ weight:r=1.0
+ }
+ 
+ p{
+ value:p2=0.85, 1.05
+ weight:r=5.0
+ }
+ }
+ 
+ amb_extinction_mul{
+ 
+ p{
+ value:p2=0.3, 1.0
+ weight:r=1.0
+ }
+ }
+ }
+ 
+ strata_clouds{
+ amount:p2=0.4, 0.85
+ altitude:p2=9.0, 11.9
+ }
+ 
+ windParams{
+ cloudsWindSpeedMult:r=100.0
+ cloudsWindSpeedLimit:r=40.0
+ strataCloudsWindSpeedMult:r=4.0
+ defaultWindSpeed:r=0.1
+ height0:r=600.0
+ turbulence0:r=0.7
+ windMul0:r=1.0
+ height1:r=2000.0
+ turbulence1:r=0.7
+ windMul1:r=1.0
+ height2:r=8000.0
+ turbulence2:r=0.3
+ windMul2:r=0.01
+ }
+ 
+ rain{
+ probability:r=0.15
+ }
+ 
+ clouds_rendering{
+ forward_eccentricity:r=0.73
+ back_eccentricity:r=0.42
+ forward_eccentricity_weight:r=0.75
+ erosion_noise_size:r=42.0
+ ambient_desaturation:r=0.5
+ ms_contribution:r=0.7
+ ms_attenuation:r=0.3
+ ms_ecc_attenuation:r=0.3
+ erosionWindSpeed:r=50.0
+ }
+ 
+ rainX7{
+ alphaFadeSpeedBegin:r=20.0
+ alphaFadeSpeedEnd:r=170.0
+ length:r=0.75
+ speed:r=8.5
+ width:r=0.02
+ density:r=2.0
+ wind:r=1.0
+ alpha:r=0.2
+ lighting:p3=0.3, 0.3, 0.32
+ perPassMul:r=5.0
+ }
+ 
+ rainDroplets{
+ droplets_reflection_min:r=0.1
+ droplets_reflection_max:r=0.3
+ droplets_size_scale:p3=20.0, 20.0, 4.0
+ droplets_speed:r=1.5
+ }
+ 
+ waterFlowmapParams{
+ simulationSpeed:r=2.0
+ crossfadeTime:r=4.0
+ }
+ 
+ puddlesPower{
+ 
+ p{
+ value:p2=0.0, 0.1
+ weight:r=1.0
+ }
+ 
+ p{
+ value:p2=0.1, 0.2
+ weight:r=3.0
+ }
+ 
+ p{
+ value:p2=0.2, 0.32
+ weight:r=9.0
+ }
+ 
+ p{
+ value:p2=0.32, 0.35
+ weight:r=3.0
+ }
+ }
+ }
+ 
+ blind{
+ cloudDropletsScale:r=0.8
+ cloudDropletsLayerThickness:r=3.5
+ addWhiteTemp:r=600.0
+ scatteringEffect:p2=0.9, 1.0
+ weatherScaleSearchLight:r=0.2
+ cloud_shadow_intensity:r=0.8
+ wind_strength:r=6.5
+ waterWindStrength:r=4.5
+ dustMul:r=0.0
+ mudMul:r=2.0
+ rainSplashEnabled:b=no
+ rainSound:t="rain"
+ rainCockpitSound:t="rain_cockpit"
+ skyLightFactor:r=1.0
+ cloudAircraftReflectMul:r=4.0
+ cloudAircraftReflectPowerMul:r=0.5
+ clouds_fly_cube_tex:t="cloud_fly_cube"
+ 
+ clouds_weather_gen{
+ "layers[0].freq":p2=2.5, 3.4298
+ "layers[1].freq":p2=4.16, 5.19
+ cumulonimbusCoverage:p2=0.89, 0.95
+ epicness:r=0.0
+ "layers[0].seed":p2=0.0, 32768.0
+ "layers[1].seed":p2=0.0, 32768.0
+ cumulonimbusSeed:p2=1.78, 1.78
+ worldSize:r=65536.0
+ "layers[0].coverage":p2=0.72, 0.9
+ "layers[1].coverage":p2=0.9, 0.97
+ }
+ 
+ clouds_form{
+ "layers[0].thickness":p2=8.0, 2.05
+ "layers[0].density":p2=1.0, 1.21313
+ "layers[0].clouds_type":p2=0.5, 0.88
+ "layers[0].clouds_type_variance":p2=1.0, 1.0
+ "layers[1].thickness":p2=3.25, 3.5
+ "layers[1].density":p2=1.0, 1.0
+ "layers[1].clouds_type":p2=0.25, 0.61
+ "layers[1].clouds_type_variance":p2=0.5, 0.75
+ extinction:p2=0.75, 0.897926
+ turbulenceStrength:p2=0.25, 0.25039
+ shapeNoiseScale:i=7
+ cumulonimbusShapeScale:i=4
+ turbulenceFreq:i=1
+ "layers[0].startAt":p2=1.8, 2.68
+ "layers[1].startAt":p2=6.5, 7.2
+ }
+ 
+ sky{
+ mie_scale:p2=37.0, 73.0
+ mie2_thickness:r=500.0
+ mie2_scale:r=570.0
+ mie2_altitude:r=850.0
+ multiple_scattering_factor:r=1.6
+ sun_brightness:r=0.71
+ moon_brightness:r=0.47
+ }
+ 
+ clouds_gen{
+ humidity:p2=0.75, 0.95
+ persistence:p2=0.5, 0.8
+ asymmetry:p2=0.1, 0.2
+ }
+ 
+ clouds_position{
+ sizeX:p2=111.0, 111.0
+ sizeZ:p2=99.0, 99.0
+ start_altitude:p2=1.0, 2.0
+ thickness:p2=3.0, 6.0
+ light_extinction:p2=0.8, 2.8
+ amb_extinction_mul:p2=0.9, 1.5
+ }
+ 
+ strata_clouds{
+ amount:p2=0.9, 1.0
+ altitude:p2=9.0, 11.9
+ }
+ 
+ windParams{
+ cloudsWindSpeedLimit:r=30.0
+ defaultWindSpeed:r=0.1
+ height0:r=600.0
+ turbulence0:r=0.1
+ windMul0:r=1.0
+ height1:r=2000.0
+ turbulence1:r=0.7
+ windMul1:r=1.0
+ height2:r=8000.0
+ turbulence2:r=0.1
+ windMul2:r=0.01
+ }
+ 
+ rain{
+ probability:r=0.05
+ }
+ 
+ clouds_rendering{
+ forward_eccentricity:r=0.73
+ back_eccentricity:r=0.42
+ forward_eccentricity_weight:r=0.75
+ erosion_noise_size:r=42.0
+ ambient_desaturation:r=0.5
+ ms_contribution:r=0.7
+ ms_attenuation:r=0.3
+ ms_ecc_attenuation:r=0.3
+ erosionWindSpeed:r=50.0
+ }
+ 
+ rainDroplets{
+ droplets_reflection_min:r=0.1
+ droplets_reflection_max:r=0.3
+ droplets_size_scale:p3=20.0, 20.0, 4.0
+ droplets_speed:r=1.5
+ }
+ 
+ puddlesPower{
+ 
+ p{
+ value:p2=0.0, 0.1
+ weight:r=1.0
+ }
+ 
+ p{
+ value:p2=0.1, 0.2
+ weight:r=2.0
+ }
+ 
+ p{
+ value:p2=0.2, 0.3
+ weight:r=4.0
+ }
+ 
+ p{
+ value:p2=0.3, 0.4
+ weight:r=3.0
+ }
+ }
+ 
+ waterFlowmapParams{
+ simulationSpeed:r=2.0
+ crossfadeTime:r=4.0
+ }
+ }
+ 
+ rain{
+ scatteringEffect:p2=0.3, 1.0
+ addWhiteTemp:r=400.0
+ weatherScaleSearchLight:r=0.2
+ cloud_shadow_intensity:r=0.8
+ cloudDropletsScale:r=5.0
+ cloudDropletsLayerThickness:r=3.5
+ cloudsShadowWaterInfluence:r=0.0
+ rainSplashEnabled:b=yes
+ rainSplashEnabled:b=no
+ wind_strength:r=5.0
+ waterWindStrength:r=4.0
+ dustMul:r=0.0
+ mudMul:r=2.0
+ rainSound:t="rain"
+ rainCockpitSound:t="rain_cockpit"
+ skyLightFactor:r=1.0
+ cloudAircraftReflectMul:r=4.0
+ cloudAircraftReflectPowerMul:r=0.5
+ clouds_fly_cube_tex:t="cloud_fly_cube"
+ wetnessPower:p2=0.7, 0.9
+ 
+ clouds_weather_gen{
+ "layers[0].freq":p2=3.0, 5.85953
+ "layers[1].freq":p2=6.0, 5.94466
+ cumulonimbusCoverage:p2=0.3, 0.57
+ epicness:r=0.93
+ "layers[0].seed":p2=0.0, 32768.0
+ "layers[1].seed":p2=0.0, 32768.0
+ cumulonimbusSeed:p2=0.0, 32768.0
+ "layers[0].coverage":p2=0.58, 0.69
+ "layers[1].coverage":p2=0.77, 0.83
+ }
+ 
+ clouds_form{
+ "layers[0].thickness":p2=8.0, 7.67274
+ "layers[0].density":p2=1.0, 1.2372
+ "layers[0].clouds_type":p2=0.5, 0.787738
+ "layers[0].clouds_type_variance":p2=1.0, 1.0
+ "layers[1].thickness":p2=3.5, 3.80162
+ "layers[1].density":p2=1.0, 1.34507
+ "layers[1].clouds_type":p2=0.25, 0.936038
+ "layers[1].clouds_type_variance":p2=0.5, 0.918658
+ extinction:p2=0.75, 2.23208
+ turbulenceStrength:p2=0.25, 0.75
+ shapeNoiseScale:i=9
+ cumulonimbusShapeScale:i=8
+ turbulenceFreq:i=5
+ "layers[0].startAt":p2=1.8, 2.09744
+ "layers[1].startAt":p2=7.5, 8.0
+ }
+ 
+ sky{
+ mie_scale:p2=9.0, 13.2
+ mie_height:p2=1.1, 2.02208
+ mie2_thickness:r=370.0
+ mie2_altitude:r=800.0
+ mie2_scale:r=26.0
+ multiple_scattering_factor:r=1.4
+ moon_brightness:r=0.73
+ }
+ 
+ clouds_gen{
+ humidity:p2=0.7, 0.85
+ persistence:p2=0.6, 0.8
+ asymmetry:p2=0.11, 0.2
+ }
+ 
+ clouds_position{
+ sizeX:p2=111.0, 111.0
+ sizeZ:p2=99.0, 99.0
+ start_altitude:p2=1.3, 2.5
+ thickness:p2=3.0, 6.0
+ light_extinction:p2=0.8, 1.4
+ amb_extinction_mul:p2=0.5, 1.0
+ }
+ 
+ clouds_render{
+ silver_lining:p2=0.5, 0.8
+ sun_light:p2=0.2, 0.5
+ ambient:p2=0.3, 0.8
+ silver_lining_eccentricity:p2=0.5, 0.8
+ }
+ 
+ strata_clouds{
+ amount:p2=0.3, 0.95
+ altitude:p2=10.0, 11.9
+ }
+ 
+ windParams{
+ cloudsWindSpeedMult:r=120.0
+ strataCloudsWindSpeedMult:r=1.0
+ defaultWindSpeed:r=0.5
+ height0:r=1200.0
+ turbulence0:r=2.0
+ windMul0:r=1.0
+ height1:r=2000.0
+ turbulence1:r=1.5
+ windMul1:r=1.0
+ height2:r=8000.0
+ turbulence2:r=0.5
+ windMul2:r=0.01
+ }
+ 
+ rain{
+ rainFromInvisibleClouds:b=yes
+ probability:r=1.0
+ }
+ 
+ clouds_rendering{
+ forward_eccentricity:r=0.73
+ back_eccentricity:r=0.42
+ forward_eccentricity_weight:r=0.75
+ erosion_noise_size:r=42.0
+ ambient_desaturation:r=0.5
+ ms_contribution:r=0.7
+ ms_attenuation:r=0.3
+ ms_ecc_attenuation:r=0.3
+ erosionWindSpeed:r=50.0
+ }
+ 
+ rainX7{
+ alphaFadeSpeedBegin:r=20.0
+ alphaFadeSpeedEnd:r=170.0
+ length:r=0.75
+ speed:r=8.5
+ width:r=0.02
+ density:r=2.0
+ wind:r=1.0
+ alpha:r=0.2
+ lighting:p3=0.3, 0.3, 0.32
+ perPassMul:r=5.0
+ }
+ 
+ rainDroplets{
+ droplets_reflection_min:r=0.1
+ droplets_reflection_max:r=0.3
+ droplets_size_scale:p3=20.0, 20.0, 4.0
+ droplets_speed:r=1.5
+ }
+ 
+ waterFlowmapParams{
+ simulationSpeed:r=2.0
+ crossfadeTime:r=4.0
+ }
+ 
+ puddlesPower{
+ 
+ p{
+ value:p2=0.35, 0.45
+ weight:r=5.0
+ }
+ }
+ 
+ dafx_rain{
+ density:r=10.0
+ speed:r=1.0
+ width:r=1.0
+ length:r=1.0
+ alpha:r=1.0
+ fmaxDensity:r=10.0
+ 
+ effect_templates{
+ template:t="camera_rain_light_effect"
+ template:t="camera_rain_drop_splashes_effect"
+ }
+ }
+ }
+ 
+ thunder{
+ scatteringEffect:p2=0.95, 1.0
+ addWhiteTemp:r=600.0
+ weatherScaleSearchLight:r=0.2
+ cloudDropletsScale:r=5.0
+ cloudDropletsLayerThickness:r=6.0
+ cloud_shadow_intensity:r=1.0
+ rainSplashEnabled:b=yes
+ rainSplashEnabled:b=no
+ adaptationMultiplierMul:r=0.7
+ wind_strength:r=5.0
+ waterWindStrength:r=7.0
+ dustMul:r=0.0
+ mudMul:r=2.0
+ rainSound:t="rain"
+ rainCockpitSound:t="rain_cockpit"
+ skyLightFactor:r=1.0
+ cloudAircraftReflectMul:r=4.0
+ cloudAircraftReflectPowerMul:r=0.5
+ clouds_fly_cube_tex:t="cloud_fly_cube"
+ wetnessPower:r=0.3
+ cloudsShadowInfluence:r=0.82
+ enableCloudsHole:b=no
+ 
+ clouds_weather_gen{
+ "layers[0].coverage":p2=0.89, 0.92
+ "layers[0].freq":p2=7.85, 3.79
+ "layers[0].seed":p2=0.0, 32768.0
+ "layers[1].coverage":p2=0.73, 0.79
+ "layers[1].freq":p2=5.39352, 7.53
+ "layers[1].seed":p2=0.0, 32768.0
+ epicness:r=0.02
+ cumulonimbusCoverage:p2=0.46, 0.55
+ cumulonimbusSeed:p2=0.0, 7.12
+ worldSize:r=65536.0
+ }
+ 
+ clouds_form{
+ "layers[0].thickness":p2=1.7, 2.1
+ "layers[0].density":p2=1.64, 1.72
+ "layers[0].clouds_type":p2=0.72944, 0.96
+ "layers[0].clouds_type_variance":p2=0.954509, 1.0
+ "layers[1].thickness":p2=2.45, 2.87
+ "layers[1].density":p2=1.04319, 1.15
+ "layers[1].clouds_type":p2=0.270934, 0.8
+ "layers[1].clouds_type_variance":p2=0.199411, 0.58
+ extinction:p2=0.73, 1.94
+ turbulenceStrength:p2=1.019, 1.349
+ shapeNoiseScale:i=17
+ cumulonimbusShapeScale:i=6
+ turbulenceFreq:i=5
+ "layers[0].startAt":p2=2.11, 2.37
+ "layers[1].startAt":p2=4.86, 5.06
+ }
+ 
+ sky{
+ mie_scale:p2=40.0, 40.0
+ mie_height:p2=0.8, 1.1
+ mie2_thickness:r=300.0
+ mie2_scale:r=40.0
+ moon_brightness:r=0.77
+ multiple_scattering_factor:r=0.4
+ }
+ 
+ clouds_gen{
+ humidity:p2=0.98, 1.0
+ persistence:p2=0.55, 0.9
+ asymmetry:p2=0.12, 0.2
+ }
+ 
+ clouds_position{
+ start_altitude:p2=1.2, 2.5
+ thickness:p2=6.0, 9.5
+ light_extinction:p2=1.55, 2.2
+ amb_extinction_mul:p2=1.9, 2.0
+ }
+ 
+ clouds_render{
+ silver_lining:p2=0.5, 0.9
+ sun_light:p2=0.25, 0.55
+ ambient:p2=0.3, 0.8
+ silver_lining_eccentricity:p2=0.5, 0.8
+ }
+ 
+ strata_clouds{
+ amount:p2=0.9, 1.0
+ altitude:p2=9.0, 11.9
+ }
+ 
+ rain{
+ rainFromInvisibleClouds:b=yes
+ probability:r=0.0
+ }
+ 
+ windParams{
+ cloudsWindSpeedMult:r=80.0
+ strataCloudsWindSpeedMult:r=2.0
+ defaultWindSpeed:r=1.0
+ height0:r=300.0
+ turbulence0:r=4.0
+ windMul0:r=1.0
+ height1:r=2000.0
+ turbulence1:r=4.0
+ windMul1:r=1.0
+ height2:r=8000.0
+ turbulence2:r=0.5
+ windMul2:r=0.01
+ }
+ 
+ clouds_rendering{
+ forward_eccentricity:r=0.73
+ back_eccentricity:r=0.42
+ forward_eccentricity_weight:r=0.75
+ erosion_noise_size:r=42.0
+ ambient_desaturation:r=0.5
+ ms_contribution:r=0.7
+ ms_attenuation:r=0.3
+ ms_ecc_attenuation:r=0.3
+ erosionWindSpeed:r=50.0
+ }
+ 
+ rainDroplets{
+ droplets_reflection_min:r=0.1
+ droplets_reflection_max:r=0.3
+ droplets_size_scale:p3=20.0, 20.0, 4.0
+ droplets_speed:r=1.5
+ }
+ 
+ waterFlowmapParams{
+ simulationSpeed:r=2.0
+ crossfadeTime:r=4.0
+ }
+ 
+ puddlesPower{
+ 
+ p{
+ value:p2=0.4, 0.55
+ weight:r=5.0
+ }
+ }
+ 
+ rainX7{
+ alphaFadeSpeedBegin:r=140.0
+ alphaFadeSpeedEnd:r=400.0
+ length:r=0.75
+ speed:r=8.5
+ width:r=0.025
+ density:r=2.0
+ wind:r=7.0
+ alpha:r=0.2
+ lighting:p3=0.4, 0.4, 0.4
+ perPassMul:r=5.0
+ }
+ }
+ 
+ storm{
+ scatteringEffect:p2=0.95, 1.0
+ addWhiteTemp:r=600.0
+ weatherScaleSearchLight:r=0.2
+ cloudDropletsScale:r=5.0
+ cloudDropletsLayerThickness:r=6.0
+ cloud_shadow_intensity:r=1.0
+ rainSplashEnabled:b=yes
+ rainSplashEnabled:b=no
+ adaptationMultiplierMul:r=0.7
+ wind_strength:r=7.0
+ waterWindStrength:r=7.0
+ dustMul:r=0.0
+ mudMul:r=2.0
+ rainSound:t="rain"
+ rainCockpitSound:t="rain_cockpit"
+ skyLightFactor:r=1.0
+ cloudAircraftReflectMul:r=4.0
+ cloudAircraftReflectPowerMul:r=0.5
+ clouds_fly_cube_tex:t="cloud_fly_cube"
+ wetnessPower:r=0.3
+ cloudsShadowInfluence:r=0.82
+ enableCloudsHole:b=no
+ 
+ clouds_weather_gen{
+ "layers[0].coverage":p2=0.89, 0.92
+ "layers[0].freq":p2=7.85, 3.79
+ "layers[0].seed":p2=0.0, 32768.0
+ "layers[1].coverage":p2=0.73, 0.79
+ "layers[1].freq":p2=5.39352, 7.53
+ "layers[1].seed":p2=0.0, 32768.0
+ epicness:r=0.02
+ cumulonimbusCoverage:p2=0.46, 0.55
+ cumulonimbusSeed:p2=0.0, 7.12
+ worldSize:r=65536.0
+ }
+ 
+ clouds_form{
+ "layers[0].thickness":p2=1.7, 2.1
+ "layers[0].density":p2=1.64, 1.72
+ "layers[0].clouds_type":p2=0.72944, 0.96
+ "layers[0].clouds_type_variance":p2=0.954509, 1.0
+ "layers[1].thickness":p2=2.45, 2.87
+ "layers[1].density":p2=1.04319, 1.15
+ "layers[1].clouds_type":p2=0.270934, 0.8
+ "layers[1].clouds_type_variance":p2=0.199411, 0.58
+ extinction:p2=0.73, 1.94
+ turbulenceStrength:p2=1.019, 1.349
+ shapeNoiseScale:i=17
+ cumulonimbusShapeScale:i=6
+ turbulenceFreq:i=5
+ "layers[0].startAt":p2=2.11, 2.37
+ "layers[1].startAt":p2=4.86, 5.06
+ }
+ 
+ sky{
+ mie_scale:p2=40.0, 40.0
+ mie_height:p2=0.8, 1.1
+ mie2_thickness:r=300.0
+ mie2_scale:r=40.0
+ moon_brightness:r=0.77
+ multiple_scattering_factor:r=0.4
+ }
+ 
+ clouds_gen{
+ humidity:p2=0.98, 1.0
+ persistence:p2=0.55, 0.9
+ asymmetry:p2=0.12, 0.2
+ }
+ 
+ clouds_position{
+ start_altitude:p2=1.2, 2.5
+ thickness:p2=6.0, 9.5
+ light_extinction:p2=1.55, 2.2
+ amb_extinction_mul:p2=1.9, 2.0
+ }
+ 
+ clouds_render{
+ silver_lining:p2=0.5, 0.9
+ sun_light:p2=0.25, 0.55
+ ambient:p2=0.3, 0.8
+ silver_lining_eccentricity:p2=0.5, 0.8
+ }
+ 
+ strata_clouds{
+ amount:p2=0.9, 1.0
+ altitude:p2=9.0, 11.9
+ }
+ 
+ rain{
+ rainFromInvisibleClouds:b=yes
+ probability:r=0.0
+ }
+ 
+ windParams{
+ cloudsWindSpeedMult:r=80.0
+ strataCloudsWindSpeedMult:r=2.0
+ defaultWindSpeed:r=1.0
+ height0:r=300.0
+ turbulence0:r=4.0
+ windMul0:r=1.0
+ height1:r=2000.0
+ turbulence1:r=4.0
+ windMul1:r=1.0
+ height2:r=8000.0
+ turbulence2:r=0.5
+ windMul2:r=0.01
+ }
+ 
+ clouds_rendering{
+ forward_eccentricity:r=0.73
+ back_eccentricity:r=0.42
+ forward_eccentricity_weight:r=0.75
+ erosion_noise_size:r=42.0
+ ambient_desaturation:r=0.5
+ ms_contribution:r=0.7
+ ms_attenuation:r=0.3
+ ms_ecc_attenuation:r=0.3
+ erosionWindSpeed:r=50.0
+ }
+ 
+ rainDroplets{
+ droplets_reflection_min:r=0.1
+ droplets_reflection_max:r=0.3
+ droplets_size_scale:p3=20.0, 20.0, 4.0
+ droplets_speed:r=1.5
+ }
+ 
+ waterFlowmapParams{
+ simulationSpeed:r=2.0
+ crossfadeTime:r=4.0
+ }
+ 
+ puddlesPower{
+ 
+ p{
+ value:p2=0.4, 0.55
+ weight:r=5.0
+ }
+ }
+ 
+ rainX7{
+ alphaFadeSpeedBegin:r=140.0
+ alphaFadeSpeedEnd:r=400.0
+ length:r=0.75
+ speed:r=8.5
+ width:r=0.025
+ density:r=2.0
+ wind:r=7.0
+ alpha:r=0.2
+ lighting:p3=0.4, 0.4, 0.4
+ perPassMul:r=5.0
+ }
+ }
+ 
+ cloudy_windy{
+ scatteringEffect:p2=0.0, 0.0
+ cloud_shadow_intensity:r=0.7
+ addWhiteTemp:r=0.0
+ cloudDropletsScale:r=0.3
+ cloudDropletsLayerThickness:r=2.0
+ wind_strength:r=5.5
+ waterWindStrength:r=3.0
+ dustMul:r=1.0
+ mudMul:r=1.0
+ rainSplashEnabled:b=no
+ rainSound:t="rain"
+ rainCockpitSound:t="rain_cockpit"
+ skyLightFactor:r=1.0
+ cloudAircraftReflectMul:r=4.0
+ cloudAircraftReflectPowerMul:r=0.5
+ clouds_fly_cube_tex:t="cloud_fly_cube"
+ 
+ clouds_weather_gen{
+ "layers[0].coverage":p2=0.604, 0.701
+ "layers[0].freq":p2=16.765, 16.765
+ "layers[0].seed":p2=0.0, 32768.0
+ "layers[1].coverage":p2=0.629, 0.478
+ "layers[1].freq":p2=5.0, 8.0
+ "layers[1].seed":p2=0.0, 32768.0
+ epicness:r=0.0
+ cumulonimbusCoverage:p2=0.101, 0.195
+ cumulonimbusSeed:p2=0.0, 32768.0
+ }
+ 
+ clouds_form{
+ "layers[0].thickness":p2=2.906, 1.995
+ "layers[0].density":p2=0.768, 0.902
+ "layers[0].clouds_type":p2=0.8, 1.0
+ "layers[0].clouds_type_variance":p2=0.0, 0.2
+ "layers[1].thickness":p2=6.336, 3.795
+ "layers[1].density":p2=0.5, 0.784
+ "layers[1].clouds_type":p2=1.0, 0.621
+ "layers[1].clouds_type_variance":p2=0.016, 0.016
+ extinction:p2=3.182, 4.784
+ turbulenceStrength:p2=0.503, 0.749
+ shapeNoiseScale:i=15
+ cumulonimbusShapeScale:i=5
+ turbulenceFreq:i=1
+ "layers[0].startAt":p2=1.7, 2.0
+ "layers[1].startAt":p2=7.0, 8.01
+ }
+ 
+ sky{
+ mie_scale:p2=5.0, 8.0
+ mie_height:p2=0.8, 1.1
+ mie2_thickness:r=220.0
+ mie2_scale:r=30.0
+ multiple_scattering_factor:r=0.4
+ moon_brightness:r=0.32
+ }
+ 
+ clouds_gen{
+ humidity:p2=0.47, 0.62
+ persistence:p2=0.58, 0.7
+ asymmetry:p2=0.08, 0.22
+ }
+ 
+ clouds_position{
+ sizeX:p2=111.0, 111.0
+ sizeZ:p2=99.0, 99.0
+ 
+ start_altitude{
+ 
+ p{
+ value:p2=1.2, 1.4
+ weight:r=8.0
+ }
+ 
+ p{
+ value:p2=1.4, 2.0
+ weight:r=1.0
+ }
+ }
+ 
+ thickness{
+ 
+ p{
+ value:p2=2.6, 3.0
+ weight:r=0.5
+ }
+ 
+ p{
+ value:p2=3.0, 3.5
+ weight:r=5.0
+ }
+ 
+ p{
+ value:p2=3.5, 5.0
+ weight:r=1.0
+ }
+ }
+ 
+ light_extinction{
+ 
+ p{
+ value:p2=0.6, 0.85
+ weight:r=1.0
+ }
+ 
+ p{
+ value:p2=0.85, 1.05
+ weight:r=5.0
+ }
+ }
+ 
+ amb_extinction_mul{
+ 
+ p{
+ value:p2=0.3, 1.0
+ weight:r=1.0
+ }
+ }
+ }
+ 
+ strata_clouds{
+ amount:p2=0.4, 0.85
+ altitude:p2=9.0, 11.9
+ }
+ 
+ windParams{
+ cloudsWindSpeedMult:r=100.0
+ cloudsWindSpeedLimit:r=40.0
+ strataCloudsWindSpeedMult:r=4.0
+ defaultWindSpeed:r=0.1
+ height0:r=600.0
+ turbulence0:r=0.7
+ windMul0:r=1.0
+ height1:r=2000.0
+ turbulence1:r=0.7
+ windMul1:r=1.0
+ height2:r=8000.0
+ turbulence2:r=0.3
+ windMul2:r=0.01
+ }
+ 
+ rain{
+ probability:r=0.25
+ }
+ 
+ clouds_rendering{
+ forward_eccentricity:r=0.73
+ back_eccentricity:r=0.42
+ forward_eccentricity_weight:r=0.75
+ erosion_noise_size:r=42.0
+ ambient_desaturation:r=0.5
+ ms_contribution:r=0.7
+ ms_attenuation:r=0.3
+ ms_ecc_attenuation:r=0.3
+ erosionWindSpeed:r=50.0
+ }
+ 
+ rainX7{
+ alphaFadeSpeedBegin:r=20.0
+ alphaFadeSpeedEnd:r=170.0
+ length:r=0.75
+ speed:r=8.5
+ width:r=0.02
+ density:r=2.0
+ wind:r=1.0
+ alpha:r=0.2
+ lighting:p3=0.3, 0.3, 0.32
+ perPassMul:r=5.0
+ }
+ 
+ rainDroplets{
+ droplets_reflection_min:r=0.1
+ droplets_reflection_max:r=0.3
+ droplets_size_scale:p3=20.0, 20.0, 4.0
+ droplets_speed:r=1.5
+ }
+ 
+ waterFlowmapParams{
+ simulationSpeed:r=2.0
+ crossfadeTime:r=4.0
+ }
+ 
+ puddlesPower{
+ 
+ p{
+ value:p2=0.03, 0.06
+ weight:r=1.0
+ }
+ 
+ p{
+ value:p2=0.15, 0.2
+ weight:r=1.0
+ }
+ 
+ p{
+ value:p2=0.3, 0.35
+ weight:r=1.0
+ }
+ }
+ }
+ 
+ mist{
+ scatteringEffect:p2=0.95, 1.0
+ addWhiteTemp:r=600.0
+ weatherScaleSearchLight:r=0.2
+ cloudDropletsScale:r=5.0
+ cloudDropletsLayerThickness:r=6.0
+ cloud_shadow_intensity:r=1.0
+ adaptationMultiplierMul:r=0.7
+ wind_strength:r=3.0
+ waterWindStrength:r=2.0
+ dustMul:r=0.0
+ mudMul:r=1.2
+ rainSplashEnabled:b=no
+ rainSound:t="rain"
+ rainCockpitSound:t="rain_cockpit"
+ skyLightFactor:r=1.0
+ cloudAircraftReflectMul:r=4.0
+ cloudAircraftReflectPowerMul:r=0.5
+ clouds_fly_cube_tex:t="cloud_fly_cube"
+ wetnessPower:r=0.2
+ cloudsShadowWaterInfluence:r=0.0
+ 
+ clouds_weather_gen{
+ "layers[0].coverage":p2=0.146, 0.202
+ "layers[0].freq":p2=2.993, 3.0
+ "layers[0].seed":p2=32.721, 32.721
+ "layers[1].coverage":p2=0.367, 0.415
+ "layers[1].freq":p2=5.776, 6.0
+ "layers[1].seed":p2=22.059, 22.059
+ epicness:r=0.0
+ cumulonimbusCoverage:p2=0.068, 0.0
+ cumulonimbusSeed:p2=0.0, 0.0
+ worldSize:r=65536.0
+ }
+ 
+ clouds_form{
+ "layers[0].thickness":p2=1.708, 2.39
+ "layers[0].density":p2=0.721, 0.721
+ "layers[0].clouds_type":p2=0.5, 0.5
+ "layers[0].clouds_type_variance":p2=1.0, 1.0
+ "layers[1].thickness":p2=1.751, 2.324
+ "layers[1].density":p2=1.0, 1.0
+ "layers[1].clouds_type":p2=0.25, 0.25
+ "layers[1].clouds_type_variance":p2=0.5, 0.5
+ extinction:p2=0.75, 0.75
+ turbulenceStrength:p2=0.25, 0.25
+ shapeNoiseScale:i=9
+ cumulonimbusShapeScale:i=4
+ turbulenceFreq:i=1
+ "layers[0].startAt":p2=2.4, 3.0
+ "layers[1].startAt":p2=7.0, 7.5
+ }
+ 
+ sky{
+ mie_height:p2=1.1, 2.0
+ mie_scale:p2=13.0, 26.5
+ mie2_thickness:r=250.0
+ mie2_scale:r=430.0
+ moon_brightness:r=0.77
+ multiple_scattering_factor:r=1.2
+ }
+ 
+ clouds_gen{
+ humidity:p2=0.98, 1.0
+ persistence:p2=0.55, 0.9
+ asymmetry:p2=0.12, 0.2
+ }
+ 
+ clouds_position{
+ start_altitude:p2=1.2, 2.5
+ thickness:p2=6.0, 9.5
+ light_extinction:p2=1.55, 2.2
+ amb_extinction_mul:p2=1.9, 2.0
+ }
+ 
+ clouds_render{
+ silver_lining:p2=0.5, 0.9
+ sun_light:p2=0.25, 0.55
+ ambient:p2=0.3, 0.8
+ silver_lining_eccentricity:p2=0.5, 0.8
+ }
+ 
+ strata_clouds{
+ amount:p2=0.5, 0.75
+ altitude:p2=9.0, 12.0
+ }
+ 
+ rain{
+ probability:r=0.0
+ }
+ 
+ windParams{
+ cloudsWindSpeedMult:r=80.0
+ strataCloudsWindSpeedMult:r=2.0
+ defaultWindSpeed:r=1.0
+ height0:r=300.0
+ turbulence0:r=4.0
+ windMul0:r=1.0
+ height1:r=2000.0
+ turbulence1:r=4.0
+ windMul1:r=1.0
+ height2:r=8000.0
+ turbulence2:r=0.5
+ windMul2:r=0.01
+ }
+ 
+ clouds_rendering{
+ forward_eccentricity:r=0.73
+ back_eccentricity:r=0.42
+ forward_eccentricity_weight:r=0.75
+ erosion_noise_size:r=42.0
+ ambient_desaturation:r=0.5
+ ms_contribution:r=0.7
+ ms_attenuation:r=0.3
+ ms_ecc_attenuation:r=0.3
+ erosionWindSpeed:r=50.0
+ }
+ 
+ rainX7{
+ alphaFadeSpeedBegin:r=20.0
+ alphaFadeSpeedEnd:r=170.0
+ length:r=0.75
+ speed:r=8.5
+ width:r=0.02
+ density:r=2.0
+ wind:r=1.0
+ alpha:r=0.2
+ lighting:p3=0.3, 0.3, 0.32
+ perPassMul:r=5.0
+ }
+ 
+ rainDroplets{
+ droplets_reflection_min:r=0.1
+ droplets_reflection_max:r=0.3
+ droplets_size_scale:p3=20.0, 20.0, 4.0
+ droplets_speed:r=1.5
+ }
+ 
+ waterFlowmapParams{
+ simulationSpeed:r=2.0
+ crossfadeTime:r=4.0
+ }
+ 
+ puddlesPower{
+ 
+ p{
+ value:p2=0.0, 0.0
+ weight:r=1.0
+ }
+ 
+ p{
+ value:p2=0.12, 0.15
+ weight:r=1.0
+ }
+ }
+ }
+ 
+ overcast{
+ scatteringEffect:p2=0.0, 0.0
+ cloud_shadow_intensity:r=0.7
+ addWhiteTemp:r=0.0
+ cloudDropletsScale:r=0.3
+ cloudDropletsLayerThickness:r=2.0
+ wind_strength:r=5.0
+ waterWindStrength:r=3.0
+ dustMul:r=1.0
+ mudMul:r=1.0
+ rainSplashEnabled:b=no
+ rainSound:t="rain"
+ rainCockpitSound:t="rain_cockpit"
+ skyLightFactor:r=1.0
+ cloudAircraftReflectMul:r=4.0
+ cloudAircraftReflectPowerMul:r=0.5
+ clouds_fly_cube_tex:t="cloud_fly_cube"
+ wetnessPower:r=0.3
+ cloudsShadowInfluence:r=0.82
+ enableCloudsHole:b=no
+ cloudsShadowWaterInfluence:r=0.0
+ 
+ clouds_weather_gen{
+ "layers[0].coverage":p2=0.5, 0.71
+ "layers[0].freq":p2=1.461, 2.461
+ "layers[1].coverage":p2=1.0, 1.0
+ "layers[1].freq":p2=6.0, 6.0
+ cumulonimbusCoverage:p2=0.0, 0.179
+ epicness:r=0.0
+ "layers[0].seed":p2=0.0, 32768.0
+ "layers[1].seed":p2=0.0, 32768.0
+ cumulonimbusSeed:p2=0.0, 32768.0
+ }
+ 
+ clouds_form{
+ "layers[0].thickness":p2=1.728, 4.04
+ "layers[0].density":p2=0.821, 1.047
+ "layers[0].clouds_type":p2=0.9, 1.0
+ "layers[0].clouds_type_variance":p2=0.652, 0.099
+ "layers[1].thickness":p2=4.68, 5.336
+ "layers[1].density":p2=1.135, 1.135
+ "layers[1].clouds_type":p2=1.0, 1.0
+ "layers[1].clouds_type_variance":p2=0.019, 0.019
+ extinction:p2=0.75, 0.75
+ turbulenceStrength:p2=0.25, 0.25
+ shapeNoiseScale:i=12
+ cumulonimbusShapeScale:i=4
+ turbulenceFreq:i=1
+ "layers[0].startAt":p2=1.996, 3.184
+ "layers[1].startAt":p2=7.938, 9.065
+ }
+ 
+ sky{
+ mie_scale:p2=60.0, 90.0
+ mie_height:p2=0.8, 1.1
+ mie2_thickness:r=220.0
+ mie2_scale:r=30.0
+ multiple_scattering_factor:r=0.04
+ moon_brightness:r=0.32
+ }
+ 
+ clouds_gen{
+ humidity:p2=0.47, 0.62
+ persistence:p2=0.58, 0.7
+ asymmetry:p2=0.08, 0.22
+ }
+ 
+ clouds_position{
+ sizeX:p2=111.0, 111.0
+ sizeZ:p2=99.0, 99.0
+ 
+ start_altitude{
+ 
+ p{
+ value:p2=1.2, 1.4
+ weight:r=8.0
+ }
+ 
+ p{
+ value:p2=1.4, 2.0
+ weight:r=1.0
+ }
+ }
+ 
+ thickness{
+ 
+ p{
+ value:p2=2.6, 3.0
+ weight:r=0.5
+ }
+ 
+ p{
+ value:p2=3.0, 3.5
+ weight:r=5.0
+ }
+ 
+ p{
+ value:p2=3.5, 5.0
+ weight:r=1.0
+ }
+ }
+ 
+ light_extinction{
+ 
+ p{
+ value:p2=0.6, 0.85
+ weight:r=1.0
+ }
+ 
+ p{
+ value:p2=0.85, 1.05
+ weight:r=5.0
+ }
+ }
+ 
+ amb_extinction_mul{
+ 
+ p{
+ value:p2=0.3, 1.0
+ weight:r=1.0
+ }
+ }
+ }
+ 
+ strata_clouds{
+ amount:p2=0.4, 0.85
+ altitude:p2=9.0, 11.9
+ }
+ 
+ windParams{
+ cloudsWindSpeedMult:r=100.0
+ cloudsWindSpeedLimit:r=40.0
+ strataCloudsWindSpeedMult:r=4.0
+ defaultWindSpeed:r=0.1
+ height0:r=600.0
+ turbulence0:r=0.7
+ windMul0:r=1.0
+ height1:r=2000.0
+ turbulence1:r=0.7
+ windMul1:r=1.0
+ height2:r=8000.0
+ turbulence2:r=0.3
+ windMul2:r=0.01
+ }
+ 
+ rain{
+ probability:r=0.15
+ }
+ 
+ clouds_rendering{
+ forward_eccentricity:r=0.73
+ back_eccentricity:r=0.42
+ forward_eccentricity_weight:r=0.75
+ erosion_noise_size:r=42.0
+ ambient_desaturation:r=0.5
+ ms_contribution:r=0.7
+ ms_attenuation:r=0.3
+ ms_ecc_attenuation:r=0.3
+ erosionWindSpeed:r=50.0
+ }
+ 
+ rainX7{
+ alphaFadeSpeedBegin:r=20.0
+ alphaFadeSpeedEnd:r=170.0
+ length:r=0.75
+ speed:r=8.5
+ width:r=0.02
+ density:r=2.0
+ wind:r=1.0
+ alpha:r=0.2
+ lighting:p3=0.3, 0.3, 0.32
+ perPassMul:r=5.0
+ }
+ 
+ rainDroplets{
+ droplets_reflection_min:r=0.1
+ droplets_reflection_max:r=0.3
+ droplets_size_scale:p3=20.0, 20.0, 4.0
+ droplets_speed:r=1.5
+ }
+ 
+ waterFlowmapParams{
+ simulationSpeed:r=2.0
+ crossfadeTime:r=4.0
+ }
+ 
+ puddlesPower{
+ 
+ p{
+ value:p2=0.0, 0.1
+ weight:r=1.0
+ }
+ 
+ p{
+ value:p2=0.1, 0.2
+ weight:r=3.0
+ }
+ 
+ p{
+ value:p2=0.2, 0.32
+ weight:r=9.0
+ }
+ 
+ p{
+ value:p2=0.32, 0.35
+ weight:r=3.0
+ }
+ }
+ }
```

  **Removed**:
```diff
```


- **aces.vromfs.bin_u/gamedata/environments/weather_types_canyon.blkx**:

  **Added**:
```diff
+ "layers[0].coverage":p2=0.0, 0.0
+ "layers[0].coverage":p2=0.1, 0.0
+ "layers[0].coverage":p2=0.0, 0.0
+ "layers[0].coverage":p2=0.0, 0.0
+ "layers[0].coverage":p2=0.0, 0.0
+ "layers[0].coverage":p2=0.1, 0.1
+ "layers[1].coverage":p2=0.95, 1.0
+ "layers[1].startAt":p2=3.5, 5.0
+ "layers[0].coverage":p2=0.0, 0.0
+ "layers[1].coverage":p2=0.77, 0.83
+ "layers[0].coverage":p2=0.0, 0.0
+ cumulonimbusCoverage:p2=0.0, 0.0
```

  **Removed**:
```diff
- "layers[0].coverage":p2=0.0, 0.2
- "layers[0].coverage":p2=0.22, 0.37
- "layers[0].coverage":p2=0.2, 0.3
- "layers[0].coverage":p2=0.5, 0.61
- "layers[0].coverage":p2=0.3, 0.36
- "layers[0].coverage":p2=1.0, 1.0
- "layers[1].coverage":p2=0.4, 0.41
- "layers[1].startAt":p2=4.5, 6.0
- "layers[0].coverage":p2=0.77, 0.83
- "layers[1].coverage":p2=0.58, 0.69
- "layers[0].coverage":p2=0.604, 0.701
- cumulonimbusCoverage:p2=0.101, 0.195
```


- **aces.vromfs.bin_u/gamedata/environments/weather_types_winter.blkx**:

  **Added**:
```diff
+ "layers[0].startAt":p2=1.8, 2.0
+ "layers[1].startAt":p2=7.0, 7.5
+ "layers[0].startAt":p2=1.8, 2.43
+ "layers[1].startAt":p2=7.13, 7.5
+ wind_strength:r=5.0
+ "layers[0].startAt":p2=1.8, 2.43
+ "layers[1].startAt":p2=7.13, 7.5
+ "layers[0].coverage":p2=0.1, 0.1
+ "layers[1].coverage":p2=0.95, 1.0
+ "layers[0].startAt":p2=2.5, 2.68
+ "layers[1].startAt":p2=6.0, 7.5
+ "layers[0].coverage":p2=0.72, 0.9
+ "layers[1].coverage":p2=0.9, 0.97
+ "layers[0].startAt":p2=1.8, 2.68
+ "layers[1].startAt":p2=6.5, 7.2
+ "layers[0].coverage":p2=0.58, 0.69
+ "layers[1].coverage":p2=0.77, 0.83
+ "layers[0].startAt":p2=1.8, 2.09744
+ "layers[1].startAt":p2=7.5, 8.0
+ "layers[0].startAt":p2=2.11, 2.37
+ "layers[1].startAt":p2=4.86, 5.06
+ "layers[0].startAt":p2=2.11, 2.37
+ "layers[1].startAt":p2=4.86, 5.06
+ "layers[0].startAt":p2=1.7, 2.0
+ "layers[1].startAt":p2=7.0, 8.01
+ "layers[0].startAt":p2=2.4, 3.0
+ "layers[1].startAt":p2=7.0, 7.5
+ scatteringEffect:p2=0.0, 0.0
+ cloud_shadow_intensity:r=0.7
+ addWhiteTemp:r=0.0
+ cloudDropletsScale:r=0.3
+ cloudDropletsLayerThickness:r=2.0
+ wind_strength:r=5.0
+ waterWindStrength:r=3.0
+ dustMul:r=1.0
+ mudMul:r=1.0
+ rainSplashEnabled:b=no
+ skyLightFactor:r=1.0
+ cloudAircraftReflectMul:r=4.0
+ cloudAircraftReflectPowerMul:r=0.5
+ clouds_fly_cube_tex:t="cloud_fly_cube"
+ wetnessPower:r=0.3
+ cloudsShadowInfluence:r=0.82
+ enableCloudsHole:b=no
+ cloudsShadowWaterInfluence:r=0.0
+ clouds_weather_gen{
+ "layers[0].coverage":p2=0.5, 0.71
+ "layers[0].freq":p2=1.461, 2.461
+ "layers[1].coverage":p2=1.0, 1.0
+ "layers[1].freq":p2=6.0, 6.0
+ cumulonimbusCoverage:p2=0.0, 0.179
+ epicness:r=0.0
+ "layers[0].seed":p2=0.0, 32768.0
+ "layers[1].seed":p2=0.0, 32768.0
+ cumulonimbusSeed:p2=0.0, 32768.0
+ }
+ 
+ clouds_form{
+ "layers[0].thickness":p2=1.728, 4.04
+ "layers[0].density":p2=0.821, 1.047
+ "layers[0].clouds_type":p2=0.9, 1.0
+ "layers[0].clouds_type_variance":p2=0.652, 0.099
+ "layers[1].thickness":p2=4.68, 5.336
+ "layers[1].density":p2=1.135, 1.135
+ "layers[1].clouds_type":p2=1.0, 1.0
+ "layers[1].clouds_type_variance":p2=0.019, 0.019
+ extinction:p2=0.75, 0.75
+ turbulenceStrength:p2=0.25, 0.25
+ shapeNoiseScale:i=12
+ cumulonimbusShapeScale:i=4
+ turbulenceFreq:i=1
+ "layers[0].startAt":p2=1.996, 3.184
+ "layers[1].startAt":p2=7.938, 9.065
+ }
+ 
+ sky{
+ mie_scale:p2=60.0, 90.0
+ mie_height:p2=0.8, 1.1
+ mie2_thickness:r=220.0
+ mie2_scale:r=30.0
+ multiple_scattering_factor:r=0.04
+ moon_brightness:r=0.32
+ }
+ 
+ clouds_gen{
+ humidity:p2=0.47, 0.62
+ persistence:p2=0.58, 0.7
+ asymmetry:p2=0.08, 0.22
+ }
+ 
+ clouds_position{
+ sizeX:p2=111.0, 111.0
+ sizeZ:p2=99.0, 99.0
+ 
+ start_altitude{
+ 
+ p{
+ value:p2=1.2, 1.4
+ weight:r=8.0
+ }
+ 
+ p{
+ value:p2=1.4, 2.0
+ weight:r=1.0
+ }
+ }
+ 
+ thickness{
+ 
+ p{
+ value:p2=2.6, 3.0
+ weight:r=0.5
+ }
+ 
+ p{
+ value:p2=3.0, 3.5
+ weight:r=5.0
+ }
+ 
+ p{
+ value:p2=3.5, 5.0
+ weight:r=1.0
+ }
+ }
+ 
+ light_extinction{
+ 
+ p{
+ value:p2=0.6, 0.85
+ weight:r=1.0
+ }
+ 
+ p{
+ value:p2=0.85, 1.05
+ weight:r=5.0
+ }
+ }
+ 
+ amb_extinction_mul{
+ 
+ p{
+ value:p2=0.3, 1.0
+ weight:r=1.0
+ }
+ }
+ }
+ 
+ strata_clouds{
+ amount:p2=0.4, 0.85
+ altitude:p2=9.0, 11.9
+ }
+ 
+ windParams{
+ cloudsWindSpeedMult:r=100.0
+ cloudsWindSpeedLimit:r=40.0
+ strataCloudsWindSpeedMult:r=4.0
+ defaultWindSpeed:r=0.1
+ height0:r=600.0
+ turbulence0:r=0.7
+ windMul0:r=1.0
+ height1:r=2000.0
+ turbulence1:r=0.7
+ windMul1:r=1.0
+ height2:r=8000.0
+ turbulence2:r=0.3
+ windMul2:r=0.01
+ }
+ 
+ clouds_rendering{
+ forward_eccentricity:r=0.73
+ back_eccentricity:r=0.42
+ forward_eccentricity_weight:r=0.75
+ erosion_noise_size:r=42.0
+ ambient_desaturation:r=0.5
+ ms_contribution:r=0.7
+ ms_attenuation:r=0.3
+ ms_ecc_attenuation:r=0.3
+ erosionWindSpeed:r=50.0
+ }
+ 
+ rainDroplets{
+ droplets_reflection_min:r=0.1
+ droplets_reflection_max:r=0.3
+ droplets_size_scale:p3=20.0, 20.0, 4.0
+ droplets_speed:r=1.5
+ }
+ 
+ waterFlowmapParams{
+ simulationSpeed:r=2.0
+ crossfadeTime:r=4.0
+ }
+ 
+ puddlesPower{
+ 
+ p{
+ value:p2=0.0, 0.1
+ weight:r=1.0
+ }
+ 
+ p{
+ value:p2=0.1, 0.2
+ weight:r=3.0
+ }
+ 
+ p{
+ value:p2=0.2, 0.32
+ weight:r=9.0
+ }
+ 
+ p{
+ value:p2=0.32, 0.35
+ weight:r=3.0
+ }
+ }
+ 
```

  **Removed**:
```diff
- "layers[0].startAt":p2=0.8, 1.0
- "layers[1].startAt":p2=6.5, 6.5
- "layers[0].startAt":p2=0.8, 2.43
- "layers[1].startAt":p2=6.5, 6.13
- wind_strength:r=7.0
- "layers[0].startAt":p2=0.8, 2.43
- "layers[1].startAt":p2=6.5, 6.13
- "layers[0].coverage":p2=1.0, 1.0
- "layers[1].coverage":p2=0.4, 0.41
- "layers[0].startAt":p2=0.916, 1.118
- "layers[1].startAt":p2=2.438, 3.165
- "layers[0].coverage":p2=0.9, 1.0
- "layers[1].coverage":p2=0.72, 0.9
- "layers[0].startAt":p2=0.8, 1.01
- "layers[1].startAt":p2=6.5, 3.18
- "layers[0].coverage":p2=0.77, 0.83
- "layers[1].coverage":p2=0.58, 0.69
- "layers[0].startAt":p2=0.8, 1.09744
- "layers[1].startAt":p2=6.5, 6.33745
- "layers[0].startAt":p2=1.11, 1.37
- "layers[1].startAt":p2=3.86, 4.06
- "layers[0].startAt":p2=1.11, 1.37
- "layers[1].startAt":p2=3.86, 4.06
- "layers[0].startAt":p2=0.658, 1.078
- "layers[1].startAt":p2=7.065, 5.914
- "layers[0].startAt":p2=1.399, 1.399
- "layers[1].startAt":p2=6.5, 6.5
```


- **aces.vromfs.bin_u/gamedata/flightmodels/a_7k.blkx**:

  **Added**:
```diff
+ maxloadMass:r=8130.0
+ maxloadMassLeftConsoles:r=4065.0
+ maxloadMassRightConsoles:r=4065.0
```

  **Removed**:
```diff
- maxloadMass:r=7260.0
- maxloadMassLeftConsoles:r=3630.0
- maxloadMassRightConsoles:r=3630.0
```


- **aces.vromfs.bin_u/gamedata/flightmodels/f-4c.blkx**:

  **Added**:
```diff
+ tier:i=1
+ tier:i=2
```

  **Removed**:
```diff
- tier:i=2
- tier:i=3
```


- **aces.vromfs.bin_u/gamedata/flightmodels/f-5ag_norway.blkx**:

  **Added**:
```diff
+ model:t="f_5ag_norway"
+ fmFile:t="fm/f_5a.blk"
+ viewDistKInSight:r=6.0
+ MetaPartsBlk:t="gameData/FlightModels/dm/metaparts/jet_fighter_metaparts.blk"
+ harmonizationSuffix:t="_tomoe"
+ gearSinkRangeLR:r=0.234
+ gearSinkRangeC:r=0.221
+ jetEnginePowerFullScale:b=yes
+ rwrIndicator:t="AN/ALR-46"
+ isBwOpticSight:b=yes
+ gyroSight:b=yes
+ havePointOfInterestDesignator:b=yes
+ ilsElbit967:b=yes
+ mfdCamTads:b=yes
+ type:t="typeFighter"
+ advancedInstructor:b=yes
+ advancedMouseAim:b=yes
+ standardExhaustFxType:t="jet_exhaust"
+ afterburnerExhaustFxType:t="jet_afterburner_exhaust"
+ startExhaustFxType:t="jet_start_exhaust"
+ disableExhaustFxIfContrailIsActive:b=yes
+ overheatBlk:t="gameData/FlightModels/DM/overheat.blk"
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
+ fireParamsPreset:t="1800kph"
+ fightAiBehaviour:t="fighter"
+ autopilotImpl:t="FBW"
+ paratrooper:t="usa_irvin_5000_ejection_para"
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
+ cannon3_dm{
+ hp:r=15.0
+ }
+ }
+ 
+ armor_jet_engine{
+ 
+ engine1_dm{
+ genericDamageMult:r=1.6
+ hp:r=50.5
+ }
+ 
+ engine2_dm{
+ genericDamageMult:r=1.6
+ hp:r=50.5
+ }
+ }
+ 
+ c_dural3{
+ 
+ aileron_l_dm{
+ genericDamageMult:r=0.3
+ hp:r=14.5
+ }
+ 
+ aileron_r_dm{
+ genericDamageMult:r=0.3
+ hp:r=14.5
+ }
+ 
+ elevator0_dm{
+ genericDamageMult:r=0.3
+ hp:r=30.5
+ }
+ 
+ elevator1_dm{
+ genericDamageMult:r=0.3
+ hp:r=30.5
+ }
+ 
+ fin_dm{
+ hp:r=30.5
+ }
+ 
+ flap_l_dm{
+ hp:r=25.3
+ }
+ 
+ flap_r_dm{
+ hp:r=24.8
+ }
+ 
+ rudder_dm{
+ genericDamageMult:r=0.3
+ hp:r=14.5
+ }
+ }
+ 
+ c_dural7{
+ 
+ fuse1_dm{
+ hp:r=79.7
+ }
+ 
+ fuse_dm{
+ hp:r=95.5
+ }
+ 
+ tail_dm{
+ genericDamageMult:r=0.5
+ hp:r=100.5
+ }
+ 
+ wing1_l_dm{
+ genericDamageMult:r=0.3
+ hp:r=40.5
+ }
+ 
+ wing1_r_dm{
+ genericDamageMult:r=0.3
+ hp:r=40.5
+ }
+ 
+ wing2_l_dm{
+ genericDamageMult:r=0.3
+ hp:r=40.5
+ }
+ 
+ wing2_r_dm{
+ genericDamageMult:r=0.3
+ hp:r=40.5
+ }
+ 
+ wing_l_dm{
+ genericDamageMult:r=0.3
+ hp:r=60.5
+ }
+ 
+ wing_r_dm{
+ genericDamageMult:r=0.3
+ hp:r=60.5
+ }
+ }
+ 
+ dural{
+ 
+ cover1_dm{
+ hp:r=19.5
+ }
+ 
+ cover2_dm{
+ hp:r=19.5
+ }
+ }
+ 
+ dural40{
+ 
+ spar1_l_dm{
+ hp:r=19.5
+ }
+ 
+ spar1_r_dm{
+ hp:r=19.5
+ }
+ 
+ spar2_l_dm{
+ hp:r=19.5
+ }
+ 
+ spar2_r_dm{
+ hp:r=19.5
+ }
+ 
+ spar_l_dm{
+ hp:r=19.5
+ }
+ 
+ spar_r_dm{
+ hp:r=19.5
+ }
+ }
+ 
+ dural5{
+ 
+ radar_dm{
+ hp:r=35.0
+ }
+ }
+ 
+ protected_controls{
+ 
+ tailcontrol_dm{
+ hp:r=60.5
+ }
+ 
+ wingcontrol_l_dm{
+ hp:r=60.5
+ }
+ 
+ wingcontrol_r_dm{
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
+ hp:r=39.5
+ }
+ 
+ gear_r_dm{
+ hp:r=39.5
+ }
+ }
+ 
+ steel_cooling_sys{
+ 
+ oil1_dm{
+ hp:r=11.5
+ }
+ 
+ oil2_dm{
+ hp:r=11.5
+ }
+ }
+ 
+ steel_pilot{
+ 
+ pilot_dm{
+ fireProtectionHp:r=20.0
+ hp:r=20.0
+ }
+ }
+ 
+ steel_tank_armor{
+ 
+ tank1_dm{
+ hp:r=106.1
+ }
+ 
+ tank2_dm{
+ hp:r=120.5
+ }
+ }
+ 
+ steel_tank_s{
+ 
+ tank3_dm{
+ hp:r=80.5
+ }
+ 
+ tank4_dm{
+ hp:r=78.2
+ }
+ 
+ tank5_dm{
+ hp:r=80.5
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
+ name:t="cannon1_dm"
+ }
+ 
+ part{
+ name:t="cannon2_dm"
+ }
+ 
+ part{
+ name:t="cannon3_dm"
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
+ fire:r=0.001
+ cut:r=0.0
+ }
+ 
+ onHit{
+ damage:r=30.0
+ fire:r=0.005
+ cut:r=0.0
+ }
+ 
+ onKill{
+ fire:r=0.1
+ cut:r=0.0
+ }
+ 
+ onKill{
+ damage:r=30.0
+ fire:r=1.0
+ cut:r=0.0
+ }
+ }
+ 
+ part{
+ name:t="engine2_dm"
+ 
+ onHit{
+ fire:r=0.001
+ cut:r=0.0
+ }
+ 
+ onHit{
+ damage:r=30.0
+ fire:r=0.005
+ cut:r=0.0
+ }
+ 
+ onKill{
+ fire:r=0.1
+ cut:r=0.0
+ }
+ 
+ onKill{
+ damage:r=30.0
+ fire:r=1.0
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
+ damage:r=60.0
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
+ nothing:r=10.0
+ }
+ 
+ onKill{
+ damage:r=30.0
+ cut:r=2.0
+ nothing:r=5.0
+ }
+ 
+ onKill{
+ damage:r=50.0
+ cut:r=1.0
+ nothing:r=0.0
+ }
+ }
+ 
+ part{
+ name:t="flap_l_dm"
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
+ nothing:r=2.0
+ }
+ 
+ onKill{
+ damage:r=20.0
+ cut:r=1.0
+ nothing:r=1.0
+ }
+ 
+ onKill{
+ damage:r=30.0
+ cut:r=1.0
+ }
+ }
+ 
+ part{
+ name:t="flap_r_dm"
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
+ nothing:r=2.0
+ }
+ 
+ onKill{
+ damage:r=20.0
+ cut:r=1.0
+ nothing:r=1.0
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
+ damage:r=30.0
+ wing_r_dm:r=0.3
+ wing_l_dm:r=0.3
+ }
+ 
+ onHit{
+ damage:r=50.0
+ wing_r_dm:r=0.5
+ wing_l_dm:r=0.5
+ }
+ 
+ onHit{
+ damage:r=200.0
+ wingcontrol_dm:r=0.2
+ wingcontrol_l_dm:r=0.2
+ wingcontrol_r_dm:r=0.2
+ }
+ 
+ onKill{
+ wingcontrol_l_dm:r=1.0
+ wingcontrol_r_dm:r=1.0
+ nothing:r=9.0
+ }
+ 
+ onKill{
+ damage:r=7.0
+ wing_l_dm:r=1.0
+ wing_r_dm:r=1.0
+ nothing:r=5.0
+ }
+ 
+ onKill{
+ damage:r=10.0
+ wing_l_dm:r=1.0
+ wing_r_dm:r=1.0
+ nothing:r=4.0
+ }
+ 
+ onKill{
+ damage:r=20.0
+ wing_l_dm:r=1.0
+ wing_r_dm:r=1.0
+ nothing:r=3.0
+ }
+ 
+ onKill{
+ damage:r=30.0
+ wing_l_dm:r=1.0
+ wing_r_dm:r=1.0
+ nothing:r=2.0
+ }
+ 
+ onKill{
+ damage:r=50.0
+ fire:r=5.0
+ wing_l_dm:r=1.0
+ wing_r_dm:r=1.0
+ }
+ 
+ onKill{
+ damage:r=200.0
+ wingcontrol_dm:r=0.4
+ wingcontrol_l_dm:r=0.4
+ wingcontrol_r_dm:r=0.4
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
+ damage:r=45.0
+ tail_dm:r=0.4
+ }
+ 
+ onHit{
+ damage:r=40.0
+ tail_dm:r=0.6
+ }
+ 
+ onHit{
+ damage:r=50.0
+ tail_dm:r=1.0
+ }
+ 
+ onHit{
+ damage:r=200.0
+ wingcontrol_dm:r=0.2
+ wingcontrol_l_dm:r=0.2
+ wingcontrol_r_dm:r=0.2
+ }
+ 
+ onKill{
+ tail_dm:r=1.0
+ nothing:r=10.0
+ }
+ 
+ onKill{
+ damage:r=3.0
+ tail_dm:r=1.0
+ nothing:r=7.0
+ }
+ 
+ onKill{
+ damage:r=7.0
+ tail_dm:r=1.0
+ nothing:r=6.0
+ }
+ 
+ onKill{
+ damage:r=10.0
+ tail_dm:r=1.0
+ nothing:r=5.0
+ }
+ 
+ onKill{
+ damage:r=20.0
+ tail_dm:r=1.0
+ nothing:r=4.0
+ }
+ 
+ onKill{
+ damage:r=30.0
+ tail_dm:r=1.0
+ nothing:r=3.0
+ }
+ 
+ onKill{
+ damage:r=40.0
+ tail_dm:r=1.0
+ nothing:r=2.0
+ }
+ 
+ onKill{
+ damage:r=50.0
+ tail_dm:r=1.0
+ nothing:r=1.0
+ }
+ 
+ onKill{
+ damage:r=200.0
+ wingcontrol_dm:r=0.4
+ wingcontrol_l_dm:r=0.4
+ wingcontrol_r_dm:r=0.4
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
+ name:t="radar_dm"
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
+ name:t="tail_dm"
+ 
+ onHit{
+ flame:r=0.2
+ smoke:r=0.2
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
+ fire:r=0.0001
+ leak:r=0.3
+ }
+ 
+ onHit{
+ damage:r=3.0
+ fire:r=0.001
+ leak:r=0.5
+ }
+ 
+ onHit{
+ damage:r=20.0
+ fire:r=0.005
+ leak:r=0.7
+ }
+ 
+ onHit{
+ damage:r=80.0
+ expl:r=0.5
+ fire:r=0.01
+ leak:r=0.9
+ }
+ 
+ onKill{
+ fire:r=0.01
+ leak:r=9.99
+ }
+ 
+ onKill{
+ damage:r=50.0
+ fire:r=50.0
+ leak:r=15.0
+ }
+ 
+ onKill{
+ damage:r=80.0
+ fire:r=50.0
+ leak:r=10.0
+ }
+ }
+ 
+ part{
+ name:t="tank2_dm"
+ 
+ onHit{
+ fire:r=0.0001
+ leak:r=0.3
+ }
+ 
+ onHit{
+ damage:r=3.0
+ fire:r=0.001
+ leak:r=0.5
+ }
+ 
+ onHit{
+ damage:r=20.0
+ fire:r=0.005
+ leak:r=0.7
+ }
+ 
+ onHit{
+ damage:r=80.0
+ expl:r=0.5
+ fire:r=0.01
+ leak:r=0.9
+ }
+ 
+ onKill{
+ fire:r=0.01
+ leak:r=9.99
+ }
+ 
+ onKill{
+ damage:r=50.0
+ fire:r=50.0
+ leak:r=15.0
+ }
+ 
+ onKill{
+ damage:r=80.0
+ fire:r=50.0
+ leak:r=10.0
+ }
+ }
+ 
+ part{
+ name:t="tank3_dm"
+ 
+ onHit{
+ fire:r=0.05
+ leak:r=0.7
+ }
+ 
+ onHit{
+ damage:r=20.0
+ fire:r=0.3
+ leak:r=0.8
+ }
+ 
+ onHit{
+ damage:r=50.0
+ fire:r=0.9
+ leak:r=0.9
+ }
+ 
+ onHit{
+ damage:r=80.0
+ expl:r=0.5
+ fire:r=0.9
+ leak:r=0.9
+ }
+ 
+ onKill{
+ fire:r=10.0
+ leak:r=10.0
+ nothing:r=80.0
+ }
+ 
+ onKill{
+ damage:r=50.0
+ fire:r=25.0
+ leak:r=35.0
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
+ fire:r=0.05
+ leak:r=0.7
+ }
+ 
+ onHit{
+ damage:r=20.0
+ fire:r=0.3
+ leak:r=0.8
+ }
+ 
+ onHit{
+ damage:r=50.0
+ fire:r=0.9
+ leak:r=0.9
+ }
+ 
+ onHit{
+ damage:r=80.0
+ expl:r=0.5
+ fire:r=0.9
+ leak:r=0.9
+ }
+ 
+ onKill{
+ fire:r=10.0
+ leak:r=10.0
+ nothing:r=80.0
+ }
+ 
+ onKill{
+ damage:r=50.0
+ fire:r=25.0
+ leak:r=35.0
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
+ fire:r=0.05
+ leak:r=0.7
+ }
+ 
+ onHit{
+ damage:r=20.0
+ fire:r=0.3
+ leak:r=0.8
+ }
+ 
+ onHit{
+ damage:r=50.0
+ fire:r=0.9
+ leak:r=0.9
+ }
+ 
+ onHit{
+ damage:r=80.0
+ expl:r=0.5
+ fire:r=0.9
+ leak:r=0.9
+ }
+ 
+ onKill{
+ fire:r=10.0
+ leak:r=10.0
+ nothing:r=80.0
+ }
+ 
+ onKill{
+ damage:r=50.0
+ fire:r=25.0
+ leak:r=35.0
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
+ name:t="wing2_l_dm"
+ defaultEffectPart:t="spar2_l_dm"
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
+ name:t="wing2_r_dm"
+ defaultEffectPart:t="spar2_r_dm"
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
+ name:t="wingcontrol_l_dm"
+ }
+ 
+ part{
+ name:t="wingcontrol_r_dm"
+ }
+ }
+ 
+ ikPilot{
+ model:t="pilot_italy_late_char"
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
+ attach{
+ pilot1:t="pilot_it_late_500"
+ }
+ 
+ Params{
+ Range:r=1050.0
+ }
+ 
+ Sound{
+ Engine:t="engine05_J85_N1_WEP"
+ gun:t="gun_default"
+ }
+ 
+ cockpit{
+ headPos:p3=2.9, 0.827, 0.0
+ headPosOnShooting:p3=3.0, 0.827, 0.0
+ sightInFov:r=50.5
+ sightInFov:r=1.5
+ sightOutFov:r=40.5
+ sightOutFov:r=6.5
+ sightFov:r=1.0
+ sightFov:r=1.0
+ mirror:b=yes
+ mirrorPos:p3=3.56, 0.452, 0.0
+ mirrorNorm:p3=-1.0, 0.12, 0.0
+ mirrorNode:t="blister3"
+ mirrorNode:t="blister4"
+ lightPos:p3=3.442, 0.36, 0.0
+ lightColor:p3=0.9, 0.11, 0.0
+ lightRadius:r=0.45
+ lightPos1:p3=3.436, 0.206, 0.415
+ lightColor1:p3=0.9, 0.11, 0.0
+ lightRadius1:r=0.2
+ lightPos2:p3=3.474, 0.236, -0.47
+ lightColor2:p3=0.9, 0.11, 0.0
+ lightRadius2:r=0.2
+ lightPos3:p3=3.236, 0.197, -0.489
+ lightColor3:p3=0.9, 0.11, 0.0
+ lightRadius3:r=0.2
+ 
+ devices{
+ stick_ailerons:p2=-1.0, 1.0
+ stick_elevator:p2=-1.0, 1.0
+ pedals1:p2=-1.0, 1.0
+ pedals2:p2=-1.0, 1.0
+ pedals3:p2=-1.0, 1.0
+ pedals4:p2=-1.0, 1.0
+ pedals5:p2=-1.0, 1.0
+ pedals6:p2=-1.0, 1.0
+ throttle:p2=0.0, 1.0
+ weapon2:p2=0.0, 1.0
+ weapon4:p2=0.0, 1.0
+ gears:p2=0.0, 1.0
+ gear_fixed:b=yes
+ flaps:p2=0.0, 1.0
+ flaps_fixed:b=yes
+ trimmer_indicator:p2=-1.0, 1.0
+ speed:p2=0.0, 514.444
+ mach:p2=0.5, 2.4
+ vario:p2=-30.48, 30.48
+ altitude_10k:p2=0.0, 100000.0
+ altitude_hour:p2=0.0, 10000.0
+ altitude_min:p2=0.0, 1000.0
+ altitude1_10k:p2=0.0, 100000.0
+ altitude1_min:p2=0.0, 1000.0
+ altitude_koef:r=3.28
+ bank:p2=-8.0, 8.0
+ turn:p2=-0.23562, 0.23562
+ aviahorizon_pitch:p2=-90.0, 90.0
+ aviahorizon_roll:p2=-180.0, 180.0
+ aviahorizon_pitch1:p2=-80.0, 80.0
+ aviahorizon_roll1:p2=-180.0, 180.0
+ aoa:p2=-10.0, 40.0
+ aoa_indexer1:p2=19.5, 30.0
+ aoa_indexer2:p2=17.9, 20.1
+ aoa_indexer3:p2=0.0, 18.5
+ compass:p2=0.0, 360.0
+ compass1:p2=0.0, 360.0
+ clock_hour:p2=0.0, 12.0
+ clock_min:p2=0.0, 60.0
+ clock_sec:p2=0.0, 60.0
+ rpm_hour:p2=0.0, 16550.0
+ rpm_min:p2=0.0, 1000.0
+ rpm1_hour:p2=0.0, 16550.0
+ rpm1_min:p2=0.0, 1000.0
+ oil_pressure:p2=0.0, 160.0
+ oil_pressure1:p2=0.0, 160.0
+ water_temperature:p2=0.0, 1200.0
+ water_temperature1:p2=0.0, 1200.0
+ fuel_pressure:p2=0.0, 15.0
+ fuel_pressure1:p2=0.0, 15.0
+ fuel:p2=0.0, 1090.0
+ fuel1:p2=0.0, 1090.0
+ fuel_consume:p2=0.0, 100.0
+ fuel_consume1:p2=0.0, 100.0
+ g_meter:p2=-5.0, 10.0
+ g_meter_min:p2=-5.0, 10.0
+ g_meter_max:p2=-5.0, 10.0
+ gears_lamp:p2=0.0, 0.0
+ }
+ 
+ rwr{
+ 
+ modeLamps{
+ launchLamp:i=0
+ launchLampBlinkingPeriod:r=0.25
+ }
+ }
+ 
+ multifunctionDisplays{
+ 
+ display{
+ textureArea:p4=0.0, 0.0, 1.0, 1.0
+ 
+ page{
+ type:t="rwr"
+ scale:r=1.15
+ hideBackground:b=yes
+ }
+ }
+ 
+ display{
+ textureArea:p4=0.0, 0.0, 1.0, 1.0
+ 
+ page{
+ type:t="plane_ils"
+ ilsSize:p2=0.25, 0.25
+ ilsOffsetForce:r=0.0
+ brightnessMult:r=3.5
+ ilsColor:c=10, 255, 10, 100
+ lineWidthScale:r=0.5
+ }
+ }
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
+ nightVision{
+ 
+ sightThermal{
+ resolution:ip2=500, 300
+ noiseFactor:r=0.05
+ index:i=1
+ }
+ }
+ 
+ gunnerOpticFps{
+ pos:p3=0.2, -0.05, 0.0
+ head:t="optic1_turret"
+ crosshairPreset:t="test_crosshair"
+ angularLimits:p4=-20.0, 20.0, -20.0, 20.0
+ opticType:t="tv"
+ nvIndex:i=1
+ }
+ 
+ sensors{
+ 
+ sensor{
+ blk:t="gameData/sensors/us_an_alr_46_v3.blk"
+ }
+ }
+ 
+ commonWeapons{
+ 
+ Weapon{
+ slot:i=0
+ preset:t="m39a3_common"
+ }
+ }
+ 
+ weapon_presets{
+ 
+ preset{
+ name:t="f_5ag_default"
+ blk:t="gameData/FlightModels/weaponPresets/f_5ag_default.blk"
+ }
+ 
+ preset{
+ name:t="f_5ag_aim_9l"
+ blk:t="gameData/FlightModels/weaponPresets/f_5ag_aim_9l.blk"
+ }
+ 
+ preset{
+ name:t="f_5ag_bomb_m117"
+ blk:t="gameData/FlightModels/weaponPresets/f_5ag_bomb_m117.blk"
+ }
+ 
+ preset{
+ name:t="f_5ag_bomb_mk82"
+ blk:t="gameData/FlightModels/weaponPresets/f_5ag_bomb_mk82.blk"
+ }
+ 
+ preset{
+ name:t="f_5ag_bomb_mk82_snakeye"
+ blk:t="gameData/FlightModels/weaponPresets/f_5ag_bomb_mk82_snakeye.blk"
+ }
+ 
+ preset{
+ name:t="f_5ag_bomb_mk83"
+ blk:t="gameData/FlightModels/weaponPresets/f_5ag_bomb_mk83.blk"
+ }
+ 
+ preset{
+ name:t="f_5ag_bomb_mk84"
+ blk:t="gameData/FlightModels/weaponPresets/f_5ag_bomb_mk84.blk"
+ }
+ 
+ preset{
+ name:t="f_5ag_rockets_lau18"
+ blk:t="gameData/FlightModels/weaponPresets/f_5ag_rockets_lau18.blk"
+ }
+ 
+ preset{
+ name:t="f_5ag_rockets_zuni"
+ blk:t="gameData/FlightModels/weaponPresets/f_5ag_rockets_zuni.blk"
+ }
+ 
+ preset{
+ name:t="f_5ag_agm_119a"
+ blk:t="gameData/FlightModels/weaponPresets/f_5ag_agm_119a.blk"
+ }
+ 
+ preset{
+ name:t="f_5ag_bomb_blu_1"
+ blk:t="gameData/FlightModels/weaponPresets/f_5ag_bomb_blu_1.blk"
+ }
+ 
+ preset{
+ name:t="f_5ag_rockets_agm_12b"
+ blk:t="gameData/FlightModels/weaponPresets/f_5ag_rockets_agm_12b.blk"
+ }
+ }
+ 
+ WeaponSlots{
+ maxloadMass:r=7257.0
+ maxloadMassLeftConsoles:r=3000.0
+ maxloadMassRightConsoles:r=3000.0
+ maxDisbalance:r=1500.0
+ 
+ HideNodes{
+ node:t="pylon_001"
+ node:t="pylon_001_upor"
+ node:t="slat1_l"
+ node:t="pylon_002"
+ node:t="pylon_002_upor"
+ node:t="pylon_003"
+ node:t="pylon_003_upor"
+ node:t="us_agm_119a_penguin_launcher"
+ node:t="pylon_004"
+ node:t="pylon_004_upor"
+ node:t="pylon_005"
+ node:t="pylon_005_upor"
+ node:t="slat1_r"
+ node:t="aero_5a_001"
+ node:t="aero_5a_002"
+ node:t="aero_5a_003"
+ node:t="aero_5a_004"
+ node:t="us_lau_117a_001"
+ node:t="us_lau_117a_002"
+ node:t="us_lau_117a_003"
+ node:t="us_lau_117a_004"
+ node:t="us_gpu_5a_pod_001"
+ node:t="flare3"
+ node:t="rwr"
+ node:t="gear_l26"
+ node:t="an_ale_40_dispenser"
+ }
+ 
+ HideDmParts{
+ node:t="cannon3_dm"
+ node:t="cover2_dm"
+ node:t="tank3_dm"
+ node:t="tank4_dm"
+ node:t="tank5_dm"
+ }
+ 
+ WeaponSlot{
+ index:i=0
+ notUseforDisbalanceCalculation:b=yes
+ 
+ WeaponPreset{
+ name:t="m39a3_common"
+ 
+ ShowNodes{
+ node:t="rwr"
+ node:t="gear_l26"
+ node:t="an_ale_40_dispenser"
+ }
+ 
+ Weapon{
+ dummy:b=yes
+ trigger:t="gunner0"
+ triggerGroup:t="primary"
+ blk:t="gameData/Weapons/dummy_weapon.blk"
+ emitter:t="optic1_gun"
+ defaultYaw:r=0.0
+ defaultPitch:r=0.0
+ speedYaw:r=25.0
+ speedPitch:r=25.0
+ parkInDeadzone:b=no
+ aimForOperatedShell:b=yes
+ 
+ turret{
+ head:t="optic1_turret"
+ gun:t="optic1_gun"
+ mainTurret:b=yes
+ }
+ 
+ limits{
+ yaw:p2=-20.0, 20.0
+ pitch:p2=-20.0, 20.0
+ }
+ }
+ 
+ Weapon{
+ trigger:t="cannon"
+ blk:t="gameData/Weapons/cannonM39A3.blk"
+ emitter:t="flare1"
+ flash:t="flare1"
+ dm:t="cannon1_dm"
+ bullets:i=280
+ light:b=no
+ spread:r=1.2
+ traceOffset:i=1
+ }
+ 
+ Weapon{
+ trigger:t="cannon"
+ blk:t="gameData/Weapons/cannonM39A3.blk"
+ emitter:t="flare2"
+ flash:t="flare2"
+ dm:t="cannon2_dm"
+ bullets:i=280
+ light:b=no
+ spread:r=1.2
+ traceOffset:i=1
+ }
+ 
+ Weapon{
+ trigger:t="countermeasures"
+ blk:t="gameData/Weapons/rocketGuns/countermeasure_split_launcher_jet.blk"
+ emitter:t="emtr_flare1"
+ bullets:i=30
+ bulletsCartridge:i=1
+ external:b=yes
+ separate:b=no
+ }
+ 
+ Weapon{
+ trigger:t="countermeasures"
+ blk:t="gameData/Weapons/rocketGuns/countermeasure_split_launcher_jet.blk"
+ emitter:t="emtr_flare2"
+ bullets:i=30
+ bulletsCartridge:i=1
+ external:b=yes
+ separate:b=no
+ }
+ }
+ }
+ 
+ WeaponSlot{
+ index:i=1
+ tier:i=9
+ order:i=1
+ 
+ WeaponPreset{
+ iconType:t="missile_type_f_air_to_air"
+ name:t="aim_9l"
+ 
+ Weapon{
+ trigger:t="aam"
+ blk:t="gameData/Weapons/rocketGuns/us_aim9l_sidewinder.blk"
+ emitter:t="lau_100_aim_9"
+ bullets:i=1
+ external:b=yes
+ separate:b=yes
+ }
+ }
+ }
+ 
+ WeaponSlot{
+ index:i=2
+ tier:i=8
+ order:i=3
+ 
+ WeaponPreset{
+ iconType:t="bombs_middle"
+ name:t="mk82"
+ reqModification:t="us_500lb_mk82"
+ 
+ ShowNodes{
+ node:t="pylon_001"
+ node:t="pylon_001_upor"
+ }
+ 
+ Weapon{
+ trigger:t="bombs"
+ blk:t="gameData/Weapons/BombGuns/us_500lb_mk_82_ldgp.blk"
+ emitter:t="750lb_m117_001"
+ bullets:i=1
+ external:b=yes
+ separate:b=yes
+ machLimit:r=1.01
+ }
+ }
+ 
+ WeaponPreset{
+ iconType:t="bombs_middle_high_drag"
+ name:t="mk82_snakeye"
+ reqModification:t="us_500lb_mk82"
+ 
+ ShowNodes{
+ node:t="pylon_001"
+ node:t="pylon_001_upor"
+ }
+ 
+ Weapon{
+ trigger:t="bombs"
+ blk:t="gameData/Weapons/BombGuns/us_500lb_mk_82_ldgp_snakeye.blk"
+ emitter:t="750lb_m117_001"
+ bullets:i=1
+ external:b=yes
+ separate:b=yes
+ machLimit:r=1.01
+ }
+ }
+ 
+ WeaponPreset{
+ iconType:t="bombs_large"
+ name:t="m117"
+ reqModification:t="us_750lb_m117"
+ 
+ ShowNodes{
+ node:t="pylon_001"
+ node:t="pylon_001_upor"
+ }
+ 
+ Weapon{
+ trigger:t="bombs"
+ blk:t="gameData/Weapons/BombGuns/us_750lb_m117_cone_45.blk"
+ emitter:t="750lb_m117_001"
+ bullets:i=1
+ external:b=yes
+ separate:b=yes
+ machLimit:r=1.01
+ }
+ }
+ 
+ WeaponPreset{
+ iconType:t="napalm_large"
+ name:t="blu27"
+ reqModification:t="us_blu_1"
+ 
+ ShowNodes{
+ node:t="pylon_001"
+ node:t="pylon_001_upor"
+ }
+ 
+ Weapon{
+ trigger:t="bombs"
+ blk:t="gameData/Weapons/BombGuns/us_blu_1.blk"
+ emitter:t="750lb_m117_001"
+ bullets:i=1
+ external:b=yes
+ separate:b=yes
+ machLimit:r=1.01
+ }
+ }
+ 
+ WeaponPreset{
+ iconType:t="nar_ap_large"
+ name:t="aero_7a"
+ reqModification:t="us_2_75_in_ffar_lau_3a"
+ 
+ ShowNodes{
+ node:t="pylon_001"
+ node:t="pylon_001_upor"
+ }
+ 
+ Weapon{
+ trigger:t="rockets"
+ blk:t="gameData/Weapons/containers/aero_7a_2_75_in_ffar_mighty_mouse.blk"
+ emitter:t="aero_7_b001"
+ external:b=yes
+ }
+ }
+ 
+ WeaponPreset{
+ iconType:t="nar_ap_special"
+ name:t="lau_10a"
+ reqModification:t="f4c_zuni"
+ 
+ ShowNodes{
+ node:t="pylon_001"
+ node:t="pylon_001_upor"
+ }
+ 
+ Weapon{
+ trigger:t="rockets"
+ blk:t="gameData/Weapons/containers/lau_10a_zuni_wafar_mk32.blk"
+ emitter:t="zuni_lau_10a_b001"
+ external:b=yes
+ }
+ }
+ 
+ WeaponPreset{
+ iconType:t="missile_air_to_uni"
+ name:t="agm_12b"
+ reqModification:t="fj_4b_agm_12b"
+ 
+ ShowNodes{
+ node:t="pylon_001"
+ node:t="aero_5a_001"
+ }
+ 
+ Weapon{
+ trigger:t="atgm"
+ blk:t="gameData/Weapons/rocketGuns/us_agm_12b_bullpup.blk"
+ emitter:t="agm_12b_001"
+ bullets:i=1
+ external:b=yes
+ separate:b=yes
+ }
+ }
+ }
+ 
+ WeaponSlot{
+ index:i=3
+ tier:i=7
+ order:i=5
+ 
+ WeaponPreset{
+ iconType:t="bombs_middle"
+ name:t="mk82"
+ reqModification:t="us_500lb_mk82"
+ 
+ ShowNodes{
+ node:t="pylon_002"
+ node:t="pylon_002_upor"
+ }
+ 
+ Weapon{
+ trigger:t="bombs"
+ blk:t="gameData/Weapons/BombGuns/us_500lb_mk_82_ldgp.blk"
+ emitter:t="750lb_m117_002"
+ bullets:i=1
+ external:b=yes
+ separate:b=yes
+ machLimit:r=1.01
+ }
+ }
+ 
+ WeaponPreset{
+ iconType:t="bombs_middle_high_drag"
+ name:t="mk82_snakeye"
+ reqModification:t="us_500lb_mk82"
+ 
+ ShowNodes{
+ node:t="pylon_002"
+ node:t="pylon_002_upor"
+ }
+ 
+ Weapon{
+ trigger:t="bombs"
+ blk:t="gameData/Weapons/BombGuns/us_500lb_mk_82_ldgp_snakeye.blk"
+ emitter:t="750lb_m117_002"
+ bullets:i=1
+ external:b=yes
+ separate:b=yes
+ machLimit:r=1.01
+ }
+ }
+ 
+ WeaponPreset{
+ iconType:t="bombs_large"
+ name:t="m117"
+ reqModification:t="us_750lb_m117"
+ 
+ ShowNodes{
+ node:t="pylon_002"
+ node:t="pylon_002_upor"
+ }
+ 
+ Weapon{
+ trigger:t="bombs"
+ blk:t="gameData/Weapons/BombGuns/us_750lb_m117_cone_45.blk"
+ emitter:t="750lb_m117_002"
+ bullets:i=1
+ external:b=yes
+ separate:b=yes
+ machLimit:r=1.01
+ }
+ }
+ 
+ WeaponPreset{
+ iconType:t="napalm_large"
+ name:t="blu27"
+ reqModification:t="us_blu_1"
+ 
+ ShowNodes{
+ node:t="pylon_002"
+ node:t="pylon_002_upor"
+ }
+ 
+ Weapon{
+ trigger:t="bombs"
+ blk:t="gameData/Weapons/BombGuns/us_blu_1.blk"
+ emitter:t="750lb_m117_002"
+ bullets:i=1
+ external:b=yes
+ separate:b=yes
+ machLimit:r=1.01
+ }
+ }
+ 
+ WeaponPreset{
+ iconType:t="bombs_special"
+ name:t="mk83"
+ reqModification:t="us_1000lb_mk83"
+ 
+ ShowNodes{
+ node:t="pylon_002"
+ node:t="pylon_002_upor"
+ }
+ 
+ Weapon{
+ trigger:t="bombs"
+ blk:t="gameData/Weapons/BombGuns/us_1000lb_mk_83_ldgp.blk"
+ emitter:t="1000lb_mk_83_001"
+ bullets:i=1
+ external:b=yes
+ separate:b=yes
+ machLimit:r=1.01
+ }
+ }
+ 
+ WeaponPreset{
+ iconType:t="nar_ap_large"
+ name:t="aero_7a"
+ reqModification:t="us_2_75_in_ffar_lau_3a"
+ 
+ ShowNodes{
+ node:t="pylon_002"
+ node:t="pylon_002_upor"
+ }
+ 
+ Weapon{
+ trigger:t="rockets"
+ blk:t="gameData/Weapons/containers/aero_7a_2_75_in_ffar_mighty_mouse.blk"
+ emitter:t="aero_7_b002"
+ external:b=yes
+ }
+ }
+ 
+ WeaponPreset{
+ iconType:t="missile_air_to_uni"
+ name:t="agm_12b"
+ reqModification:t="fj_4b_agm_12b"
+ 
+ ShowNodes{
+ node:t="pylon_002"
+ node:t="aero_5a_002"
+ }
+ 
+ Weapon{
+ trigger:t="atgm"
+ blk:t="gameData/Weapons/rocketGuns/us_agm_12b_bullpup.blk"
+ emitter:t="agm_12b_002"
+ bullets:i=1
+ external:b=yes
+ separate:b=yes
+ }
+ }
+ 
+ WeaponPreset{
+ iconType:t="ptb"
+ name:t="ptb_slot3"
+ showInWeaponMenu:b=yes
+ 
+ ShowNodes{
+ node:t="pylon_002"
+ node:t="pylon_002_upor"
+ }
+ 
+ ShowDmParts{
+ node:t="tank3_dm"
+ }
+ 
+ Weapon{
+ trigger:t="fuel tanks"
+ blk:t="gameData/Weapons/drop_tank/us_150gal_early_drop_tank_1.blk"
+ emitter:t="us_150gal_early_drop_tank_001"
+ bullets:i=1
+ external:b=yes
+ }
+ 
+ DependentWeaponPreset{
+ slot:i=5
+ preset:t="ptb_slot5"
+ }
+ }
+ }
+ 
+ WeaponSlot{
+ index:i=4
+ tier:i=6
+ order:i=7
+ notUseforDisbalanceCalculation:b=yes
+ 
+ WeaponPreset{
+ iconType:t="bombs_middle"
+ name:t="mk82"
+ reqModification:t="us_500lb_mk82"
+ 
+ ShowNodes{
+ node:t="pylon_003"
+ node:t="pylon_003_upor"
+ }
+ 
+ Weapon{
+ trigger:t="bombs"
+ blk:t="gameData/Weapons/BombGuns/us_500lb_mk_82_ldgp.blk"
+ emitter:t="750lb_m117_003"
+ bullets:i=1
+ external:b=yes
+ separate:b=yes
+ machLimit:r=1.01
+ }
+ }
+ 
+ WeaponPreset{
+ iconType:t="bombs_middle_high_drag"
+ name:t="mk82_snakeye"
+ reqModification:t="us_500lb_mk82"
+ 
+ ShowNodes{
+ node:t="pylon_003"
+ node:t="pylon_003_upor"
+ }
+ 
+ Weapon{
+ trigger:t="bombs"
+ blk:t="gameData/Weapons/BombGuns/us_500lb_mk_82_ldgp_snakeye.blk"
+ emitter:t="750lb_m117_003"
+ bullets:i=1
+ external:b=yes
+ separate:b=yes
+ machLimit:r=1.01
+ }
+ }
+ 
+ WeaponPreset{
+ iconType:t="bombs_large"
+ name:t="m117"
+ reqModification:t="us_750lb_m117"
+ 
+ ShowNodes{
+ node:t="pylon_003"
+ node:t="pylon_003_upor"
+ }
+ 
+ Weapon{
+ trigger:t="bombs"
+ blk:t="gameData/Weapons/BombGuns/us_750lb_m117_cone_45.blk"
+ emitter:t="750lb_m117_003"
+ bullets:i=1
+ external:b=yes
+ separate:b=yes
+ machLimit:r=1.01
+ }
+ }
+ 
+ WeaponPreset{
+ iconType:t="napalm_large"
+ name:t="blu27"
+ reqModification:t="us_blu_1"
+ 
+ ShowNodes{
+ node:t="pylon_003"
+ node:t="pylon_003_upor"
+ }
+ 
+ Weapon{
+ trigger:t="bombs"
+ blk:t="gameData/Weapons/BombGuns/us_blu_1.blk"
+ emitter:t="750lb_m117_003"
+ bullets:i=1
+ external:b=yes
+ separate:b=yes
+ machLimit:r=1.01
+ }
+ }
+ 
+ WeaponPreset{
+ iconType:t="bombs_special"
+ name:t="mk83"
+ reqModification:t="us_1000lb_mk83"
+ 
+ ShowNodes{
+ node:t="pylon_003"
+ node:t="pylon_003_upor"
+ }
+ 
+ Weapon{
+ trigger:t="bombs"
+ blk:t="gameData/Weapons/BombGuns/us_1000lb_mk_83_ldgp.blk"
+ emitter:t="1000lb_mk_83_002"
+ bullets:i=1
+ external:b=yes
+ separate:b=yes
+ machLimit:r=1.01
+ }
+ }
+ 
+ WeaponPreset{
+ iconType:t="bombs_heavy_middle"
+ name:t="mk84"
+ reqModification:t="us_2000lb_mk84"
+ 
+ ShowNodes{
+ node:t="pylon_003"
+ node:t="pylon_003_upor"
+ }
+ 
+ Weapon{
+ trigger:t="bombs"
+ blk:t="gameData/Weapons/BombGuns/us_2000lb_mk_84_ldgp.blk"
+ emitter:t="2000lb_mk_84_001"
+ bullets:i=1
+ external:b=yes
+ separate:b=yes
+ machLimit:r=1.01
+ }
+ }
+ 
+ WeaponPreset{
+ iconType:t="missile_air_to_earth"
+ name:t="agm_119a"
+ 
+ ShowNodes{
+ node:t="pylon_003"
+ node:t="pylon_003_upor"
+ node:t="us_agm_119a_penguin_launcher"
+ }
+ 
+ Weapon{
+ trigger:t="atgm"
+ blk:t="gameData/Weapons/rocketGuns/us_agm_119a_penguin.blk"
+ emitter:t="us_agm_119a_penguin_missile"
+ bullets:i=1
+ external:b=yes
+ separate:b=yes
+ }
+ }
+ 
+ WeaponPreset{
+ iconType:t="ptb"
+ name:t="ptb_slot4"
+ showInWeaponMenu:b=yes
+ 
+ ShowNodes{
+ node:t="pylon_003"
+ node:t="pylon_003_upor"
+ }
+ 
+ ShowDmParts{
+ node:t="tank4_dm"
+ }
+ 
+ Weapon{
+ trigger:t="fuel tanks"
+ blk:t="gameData/Weapons/drop_tank/us_150gal_early_fuse_drop_tank.blk"
+ emitter:t="us_150gal_early_fuse_drop_tank"
+ bullets:i=1
+ external:b=yes
+ }
+ }
+ }
+ 
+ WeaponSlot{
+ index:i=5
+ tier:i=5
+ order:i=6
+ 
+ WeaponPreset{
+ iconType:t="bombs_middle"
+ name:t="mk82"
+ reqModification:t="us_500lb_mk82"
+ 
+ ShowNodes{
+ node:t="pylon_004"
+ node:t="pylon_004_upor"
+ }
+ 
+ Weapon{
+ trigger:t="bombs"
+ blk:t="gameData/Weapons/BombGuns/us_500lb_mk_82_ldgp.blk"
+ emitter:t="750lb_m117_004"
+ bullets:i=1
+ external:b=yes
+ separate:b=yes
+ machLimit:r=1.01
+ }
+ }
+ 
+ WeaponPreset{
+ iconType:t="bombs_middle_high_drag"
+ name:t="mk82_snakeye"
+ reqModification:t="us_500lb_mk82"
+ 
+ ShowNodes{
+ node:t="pylon_004"
+ node:t="pylon_004_upor"
+ }
+ 
+ Weapon{
+ trigger:t="bombs"
+ blk:t="gameData/Weapons/BombGuns/us_500lb_mk_82_ldgp_snakeye.blk"
+ emitter:t="750lb_m117_004"
+ bullets:i=1
+ external:b=yes
+ separate:b=yes
+ machLimit:r=1.01
+ }
+ }
+ 
+ WeaponPreset{
+ iconType:t="bombs_large"
+ name:t="m117"
+ reqModification:t="us_750lb_m117"
+ 
+ ShowNodes{
+ node:t="pylon_004"
+ node:t="pylon_004_upor"
+ }
+ 
+ Weapon{
+ trigger:t="bombs"
+ blk:t="gameData/Weapons/BombGuns/us_750lb_m117_cone_45.blk"
+ emitter:t="750lb_m117_004"
+ bullets:i=1
+ external:b=yes
+ separate:b=yes
+ machLimit:r=1.01
+ }
+ }
+ 
+ WeaponPreset{
+ iconType:t="napalm_large"
+ name:t="blu27"
+ reqModification:t="us_blu_1"
+ 
+ ShowNodes{
+ node:t="pylon_004"
+ node:t="pylon_004_upor"
+ }
+ 
+ Weapon{
+ trigger:t="bombs"
+ blk:t="gameData/Weapons/BombGuns/us_blu_1.blk"
+ emitter:t="750lb_m117_004"
+ bullets:i=1
+ external:b=yes
+ separate:b=yes
+ machLimit:r=1.01
+ }
+ }
+ 
+ WeaponPreset{
+ iconType:t="bombs_special"
+ name:t="mk83"
+ reqModification:t="us_1000lb_mk83"
+ 
+ ShowNodes{
+ node:t="pylon_004"
+ node:t="pylon_004_upor"
+ }
+ 
+ Weapon{
+ trigger:t="bombs"
+ blk:t="gameData/Weapons/BombGuns/us_1000lb_mk_83_ldgp.blk"
+ emitter:t="1000lb_mk_83_003"
+ bullets:i=1
+ external:b=yes
+ separate:b=yes
+ machLimit:r=1.01
+ }
+ }
+ 
+ WeaponPreset{
+ iconType:t="nar_ap_large"
+ name:t="aero_7a"
+ reqModification:t="us_2_75_in_ffar_lau_3a"
+ 
+ ShowNodes{
+ node:t="pylon_004"
+ node:t="pylon_004_upor"
+ }
+ 
+ Weapon{
+ trigger:t="rockets"
+ blk:t="gameData/Weapons/containers/aero_7a_2_75_in_ffar_mighty_mouse.blk"
+ emitter:t="aero_7_b003"
+ external:b=yes
+ }
+ }
+ 
+ WeaponPreset{
+ iconType:t="missile_air_to_uni"
+ name:t="agm_12b"
+ reqModification:t="fj_4b_agm_12b"
+ 
+ ShowNodes{
+ node:t="pylon_004"
+ node:t="aero_5a_003"
+ }
+ 
+ Weapon{
+ trigger:t="atgm"
+ blk:t="gameData/Weapons/rocketGuns/us_agm_12b_bullpup.blk"
+ emitter:t="agm_12b_003"
+ bullets:i=1
+ external:b=yes
+ separate:b=yes
+ }
+ }
+ 
+ WeaponPreset{
+ iconType:t="ptb"
+ name:t="ptb_slot5"
+ showInWeaponMenu:b=yes
+ 
+ ShowNodes{
+ node:t="pylon_004"
+ node:t="pylon_004_upor"
+ }
+ 
+ ShowDmParts{
+ node:t="tank5_dm"
+ }
+ 
+ Weapon{
+ trigger:t="fuel tanks"
+ blk:t="gameData/Weapons/drop_tank/us_150gal_early_drop_tank_2.blk"
+ emitter:t="us_150gal_early_drop_tank_002"
+ bullets:i=1
+ external:b=yes
+ }
+ 
+ DependentWeaponPreset{
+ slot:i=3
+ preset:t="ptb_slot3"
+ }
+ }
+ }
+ 
+ WeaponSlot{
+ index:i=6
+ tier:i=4
+ order:i=4
+ 
+ WeaponPreset{
+ iconType:t="bombs_middle"
+ name:t="mk82"
+ reqModification:t="us_500lb_mk82"
+ 
+ ShowNodes{
+ node:t="pylon_005"
+ node:t="pylon_005_upor"
+ }
+ 
+ Weapon{
+ trigger:t="bombs"
+ blk:t="gameData/Weapons/BombGuns/us_500lb_mk_82_ldgp.blk"
+ emitter:t="750lb_m117_005"
+ bullets:i=1
+ external:b=yes
+ separate:b=yes
+ machLimit:r=1.01
+ }
+ }
+ 
+ WeaponPreset{
+ iconType:t="bombs_middle_high_drag"
+ name:t="mk82_snakeye"
+ reqModification:t="us_500lb_mk82"
+ 
+ ShowNodes{
+ node:t="pylon_005"
+ node:t="pylon_005_upor"
+ }
+ 
+ Weapon{
+ trigger:t="bombs"
+ blk:t="gameData/Weapons/BombGuns/us_500lb_mk_82_ldgp_snakeye.blk"
+ emitter:t="750lb_m117_005"
+ bullets:i=1
+ external:b=yes
+ separate:b=yes
+ machLimit:r=1.01
+ }
+ }
+ 
+ WeaponPreset{
+ iconType:t="bombs_large"
+ name:t="m117"
+ reqModification:t="us_750lb_m117"
+ 
+ ShowNodes{
+ node:t="pylon_005"
+ node:t="pylon_005_upor"
+ }
+ 
+ Weapon{
+ trigger:t="bombs"
+ blk:t="gameData/Weapons/BombGuns/us_750lb_m117_cone_45.blk"
+ emitter:t="750lb_m117_005"
+ bullets:i=1
+ external:b=yes
+ separate:b=yes
+ machLimit:r=1.01
+ }
+ }
+ 
+ WeaponPreset{
+ iconType:t="napalm_large"
+ name:t="blu27"
+ reqModification:t="us_blu_1"
+ 
+ ShowNodes{
+ node:t="pylon_005"
+ node:t="pylon_005_upor"
+ }
+ 
+ Weapon{
+ trigger:t="bombs"
+ blk:t="gameData/Weapons/BombGuns/us_blu_1.blk"
+ emitter:t="750lb_m117_005"
+ bullets:i=1
+ external:b=yes
+ separate:b=yes
+ machLimit:r=1.01
+ }
+ }
+ 
+ WeaponPreset{
+ iconType:t="nar_ap_large"
+ name:t="aero_7a"
+ reqModification:t="us_2_75_in_ffar_lau_3a"
+ 
+ ShowNodes{
+ node:t="pylon_005"
+ node:t="pylon_005_upor"
+ }
+ 
+ Weapon{
+ trigger:t="rockets"
+ blk:t="gameData/Weapons/containers/aero_7a_2_75_in_ffar_mighty_mouse.blk"
+ emitter:t="aero_7_b004"
+ external:b=yes
+ }
+ }
+ 
+ WeaponPreset{
+ iconType:t="nar_ap_special"
+ name:t="lau_10a"
+ reqModification:t="f4c_zuni"
+ 
+ ShowNodes{
+ node:t="pylon_005"
+ node:t="pylon_005_upor"
+ }
+ 
+ Weapon{
+ trigger:t="rockets"
+ blk:t="gameData/Weapons/containers/lau_10a_zuni_wafar_mk32.blk"
+ emitter:t="zuni_lau_10a_b002"
+ external:b=yes
+ }
+ }
+ 
+ WeaponPreset{
+ iconType:t="missile_air_to_uni"
+ name:t="agm_12b"
+ reqModification:t="fj_4b_agm_12b"
+ 
+ ShowNodes{
+ node:t="pylon_005"
+ node:t="aero_5a_004"
+ }
+ 
+ Weapon{
+ trigger:t="atgm"
+ blk:t="gameData/Weapons/rocketGuns/us_agm_12b_bullpup.blk"
+ emitter:t="agm_12b_004"
+ bullets:i=1
+ external:b=yes
+ separate:b=yes
+ }
+ }
+ }
+ 
+ WeaponSlot{
+ index:i=7
+ tier:i=3
+ order:i=2
+ 
+ WeaponPreset{
+ iconType:t="missile_type_f_air_to_air"
+ name:t="aim_9l"
+ 
+ Weapon{
+ trigger:t="aam"
+ blk:t="gameData/Weapons/rocketGuns/us_aim9l_sidewinder.blk"
+ emitter:t="lau_101_aim_9"
+ bullets:i=1
+ external:b=yes
+ separate:b=yes
+ }
+ }
+ }
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
+ engineExtinguishFireSpeed:p2=467.0, 511.0
+ engineExtinguishFireSpeedChance:p2=0.01, 0.1
+ fireDamagePowerRel:r=0.05
+ nonExtinguishFireTime:r=5.0
+ }
+ 
+ arcadeOverride{
+ maxSpeedMultiplier:r=1.3
+ wepOverspeed:r=1.3
+ }
+ 
+ wiki{
+ 
+ general{
+ length:r=19.96
+ wingspan:r=19.51
+ wingArea:r=88.8
+ emptyWeight:r=10300.0
+ normalWeight:r=15340.0
+ maxTakeoffWeight:r=20865.0
+ powerPlantType:i=2
+ thrustMaxMil:r=52000.0
+ }
+ 
+ performance{
+ 
+ table{
+ rpmMil:r=7800.0
+ airSpeedMil0:p2=0.0, 854.0
+ airSpeedMil1:p2=3000.0, 880.0
+ climbRateMil0:p2=0.0, 20.0
+ climbTimeMil0:p2=2000.0, 71.717
+ climbTimeMil1:p2=4000.0, 147.402
+ climbTimeMil2:p2=6000.0, 231.172
+ climbTimeMil3:p2=8000.0, 339.877
+ turnTimeMil:p2=1000.0, 26.0
+ takeoffDistance:r=648.446
+ ceiling:r=12400.0
+ rollRate:r=69.0
+ wingLoading:r=173.0
+ thrustToWeightRatio:r=0.37
+ }
+ 
+ plot{
+ airSpeedMil0:p2=0.0, 854.0
+ airSpeedMil1:p2=1400.0, 878.0
+ airSpeedMil2:p2=5700.0, 866.0
+ airSpeedMil3:p2=12400.0, 791.0
+ climbRateMil0:p2=0.0, 20.0
+ climbRateMil1:p2=3000.0, 18.0
+ climbRateMil2:p2=6100.0, 13.8
+ climbRateMil3:p2=9100.0, 1.5
+ climbRateMil4:p2=12400.0, -2.1
+ }
+ }
+ }
+ 
+ balanceData{
+ accSpd:r=4.0345
+ climbSpeed:r=20.0
+ maxSpeed:r=240.27
+ turnTime:r=28.1492
+ }
+ 
+ modifications{
+ 
+ new_compressor_jet{
+ tier:i=1
+ }
+ 
+ hydravlic_power{
+ prevModification:t="new_compressor_jet"
+ tier:i=2
+ 
+ effects{
+ aileronBooster:r=0.9
+ elevatorBooster:r=0.9
+ }
+ }
+ 
+ cd_98{
+ prevModification:t="hydravlic_power"
+ tier:i=3
+ }
+ 
+ hp_105_jet{
+ prevModification:t="cd_98"
+ tier:i=4
+ }
+ 
+ f_4c_CdMin_Fuse{
+ tier:i=1
+ modClass:t="lth"
+ }
+ 
+ structure_str{
+ tier:i=2
+ modClass:t="lth"
+ }
+ 
+ new_cover{
+ modClass:t="lth"
+ tier:i=4
+ }
+ 
+ countermeasures_launcher_chaff{
+ }
+ 
+ countermeasures_belt_pack{
+ tier:i=1
+ modClass:t="armor"
+ turn_it_off:b=no
+ invertEnableLogic:b=no
+ group:t="mi-24_EVU"
+ }
+ 
+ f_4c_g_suit{
+ tier:i=2
+ modClass:t="armor"
+ }
+ 
+ t_160_universal{
+ }
+ 
+ t_160_air_targets{
+ }
+ 
+ t_160_armor_targets{
+ }
+ 
+ t_160_stealth{
+ }
+ 
+ t_160_belt_pack{
+ tier:i=1
+ }
+ 
+ t_160_new_gun{
+ reqModification:t="t_160_belt_pack"
+ tier:i=3
+ }
+ 
+ us_2_75_in_ffar_lau_3a{
+ prevModification:t="us_blu_1"
+ tier:i=2
+ modClass:t="weapon"
+ }
+ 
+ f4c_zuni{
+ reqModification:t="us_2_75_in_ffar_lau_3a"
+ tier:i=3
+ modClass:t="weapon"
+ }
+ 
+ fj_4b_agm_12b{
+ reqModification:t="f4c_zuni"
+ tier:i=4
+ modClass:t="weapon"
+ }
+ 
+ us_500lb_mk82{
+ modClass:t="weapon"
+ tier:i=1
+ }
+ 
+ us_750lb_m117{
+ modClass:t="weapon"
+ tier:i=2
+ reqModification:t="us_500lb_mk82"
+ }
+ 
+ us_1000lb_mk83{
+ modClass:t="weapon"
+ tier:i=3
+ reqModification:t="us_750lb_m117"
+ }
+ 
+ us_2000lb_mk84{
+ modClass:t="weapon"
+ tier:i=4
+ reqModification:t="us_1000lb_mk83"
+ }
+ 
+ us_blu_1{
+ tier:i=1
+ modClass:t="weapon"
+ }
+ }
+ 
+ user_skin{
+ name:t="f-5ag_norway"
+ 
+ replace_tex{
+ from:t="f_5ag_norway_c*"
+ }
+ 
+ replace_tex{
+ from:t="f_5ag_norway_n*"
+ }
+ }
+ 
+ default_skin{
+ 
+ replace_tex{
+ from:t="us_150gal_early_drop_tank_c*"
+ to:t="no_150gal_early_drop_tank_c*"
+ }
+ 
+ replace_tex{
+ from:t="us_agm_119a_penguin_missile_c*"
+ to:t="no_agm_119a_penguin_missile_c*"
+ }
+ }
+ 
+ default_skin_tomoe{
+ 
+ replace_tex{
+ from:t="f_5ag_norway_c*"
+ to:t="f_5ag_norway_c*"
+ }
+ 
+ replace_tex{
+ from:t="f_5ag_norway_n*"
+ to:t="f_5ag_norway_n*"
+ }
+ }
+ 
+ parachutes{
+ emitterRange:ip2=1, 1
+ emitterName:t="emtr_chute"
+ chuteModel:t="chute_f_100_char"
+ chuteAnimVarName:t="chute_state_switch"
+ chuteFlapVarName:t="fire_chute"
+ chuteTimeScaleParam:t="chute_time_scale"
+ chuteFallSpeed:r=1.0
+ }
+ 
+ bailout{
+ buttonHoldTime:r=1.0
+ wreckSpeed:r=10.0
+ wreckDir:p3=-1.0, 1.0, 0.0
+ seatEjectDelay:r=0.5
+ seatVel:p3=-10.0, 20.0, 0.0
+ minHeight:r=0.0
+ minSpeed:r=0.0
+ hasSafeExit:b=yes
+ wreck:t="blister1"
+ hide:t="seat_01"
+ seat:t="seat_01"
+ fxEmitter:t="blister1"
+ fxType:t="catapult_expl_ejection"
+ }
+ 
+ cutting{
+ _emtr_break_wing0_l_from:p3=0.0904795, -0.196779, 1.30583
+ _emtr_break_wing0_l_to:p3=0.0904795, -0.196779, 1.76905
+ emtr_break_wing1_l_from:p3=0.0904795, -0.196779, 2.46389
+ emtr_break_wing1_l_to:p3=0.0904795, -0.196779, 2.66544
+ emtr_break_wing2_l_from:p3=0.0904795, -0.196779, 2.96776
+ emtr_break_wing2_l_to:p3=0.0904795, -0.196779, 3.34694
+ _emtr_break_wing0_r_from:p3=0.0904788, -0.196779, -1.30583
+ _emtr_break_wing0_r_to:p3=0.0904788, -0.196779, -1.76905
+ emtr_break_wing1_r_from:p3=0.0904788, -0.196779, -2.46389
+ emtr_break_wing1_r_to:p3=0.0904788, -0.196779, -2.66544
+ emtr_break_wing2_r_from:p3=0.0904788, -0.196779, -2.96776
+ emtr_break_wing2_r_to:p3=0.0904788, -0.196779, -3.34694
+ emtr_break_wing_tail:p3=-2.82787, 0.0, 0.0
+ finCut:b=yes
+ emtr_break_tail_from:p3=-3.2629, 0.122295, 8.34465e-09
+ emtr_break_tail_to:p3=-5.11483, 0.122295, 8.34465e-09
+ }
+ 
+ AfterBurner0{
+ 
+ volumetricAfterBurner{
+ name:t="jet_blue_f_5"
+ maxHeight:r=8.0
+ minHeight:r=6.5
+ heightNoiseStrength:r=0.02
+ heightNoiseSpeed:r=30.0
+ maxRadius:r=0.18
+ minRadius:r=0.17
+ maxBaseRadius:r=0.19
+ minBaseRadius:r=0.15
+ relativeCylinderHeightMax:r=0.35
+ relativeCylinderHeightMin:r=0.35
+ outerCylinderAbsorptionMax:r=0.6
+ outerCylinderAbsorptionMin:r=0.7
+ outerCylinderHeightFadeMax:r=5.0
+ outerCylinderHeightFadeMin:r=3.0
+ tailHeightFadeMax:r=2.5
+ tailHeightFadeMin:r=0.5
+ outerCylinderHeightFadeNoiseStrength:r=2.0
+ outerCylinderHeightFadeNoiseSpeed:r=10.0
+ minOuterCylinderRadius:r=0.22
+ maxOuterCylinderRadius:r=0.22
+ absorption:r=1.0
+ colorIntensityMax:r=10.0
+ colorIntensityMin:r=1.0
+ colorOverHeightMult:r=0.7
+ colorOverDepthMult:r=4.0
+ colorOverRadiusMult:r=3.5
+ colorOverRadiusFadeOverHeight:r=2.0
+ maxRingOffset:r=0.0
+ minRingOffset:r=0.0
+ ringAbsorption:r=1.2
+ maxRingCount:i=17
+ minRingCount:i=17
+ ringIntensityMin:r=0.0
+ ringIntensityMax:r=1.0
+ ringIntensityNoiseStrength:r=0.0
+ ringIntensityNoiseSpeed:r=0.0
+ ringOffsetNoiseStrength:r=1.0
+ ringOffsetNoiseSpeed:r=30.0
+ rampTextureOffset:i=0
+ radiusNoiseStrength:r=0.03
+ radiusNoiseSpeed:r=30.0
+ shakeNoiseStrength:r=0.02
+ shakeNoiseSpeed:r=40.0
+ ringAngleFadeMult:r=0.5
+ colorOverHeightNoiseStrength:r=0.1
+ colorOverHeightNoiseSpeed:r=10.0
+ colorOverRadiusNoiseStrength:r=0.25
+ colorOverRadiusNoiseSpeed:r=10.0
+ colorOverDepthNoiseStrength:r=0.1
+ colorOverDepthNoiseSpeed:r=1.0
+ colorIntensityNoiseStrength:r=2.0
+ colorIntensityNoiseSpeed:r=20.0
+ minStartingRingHeight:r=0.7
+ maxStartingRingHeight:r=0.8
+ ringIntensity:r=2.0
+ ringFrequency:r=11.3097
+ 
+ preNominalEasingParams{
+ animationTime:r=2.5
+ ascendingSmoothIntensityParams:r=0.8
+ }
+ 
+ postNominalEasingParams{
+ animationTime:r=1.5
+ ascendingSmoothIntensityParams:r=1.0
+ }
+ 
+ lightProperties{
+ color:p3=1.0, 0.641762, 0.387255
+ angle:r=1.0
+ brightness:r=25.0
+ radius:r=20.0
+ attenuation:r=0.75
+ brightnessNoiseStrength:r=3.0
+ brightnessNoiseSpeed:r=6.0
+ ignitionTextureIntensity:r=1.0
+ ignitionBrightnessNoiseStrength:r=0.1
+ ignitionBrightnessNoiseSpeed:r=16.0
+ }
+ }
+ }
+ 
+ lerxVapors{
+ 
+ lerxVapor{
+ entryPoint:p3=1.6, -0.2, 1.237
+ exitPoint:p3=-3.918, 0.0, 2.268
+ entryTangent:p3=0.0, 0.206, 1.413
+ exitTangent:p3=-1.443, 0.206, 1.618
+ exitTangentHeight:p2=0.0, 0.0
+ exitTangentWidth:p2=0.0, 0.0
+ exitPointHeight:p2=0.0, 1.0
+ exitPointWidth:p2=-1.0, 1.0
+ maxRadius:p2=0.05, 0.4
+ minRadius:p2=0.05, 0.25
+ noiseParms:p2=0.218, 0.674
+ smoothIntensityParams:p3=0.518, 1.505, 0.246
+ density:r=1.0
+ intensityMult:r=7.0
+ criticalAOA:p4=6.0, 22.0, 35.0, 40.0
+ absoluteCriticalAOS:p2=2.0, 15.0
+ absoluteCriticalAOA:p2=5.0, 40.0
+ }
+ 
+ lerxVapor{
+ entryPoint:p3=1.6, -0.2, -1.237
+ exitPoint:p3=-3.918, 0.0, -2.268
+ entryTangent:p3=0.0, 0.206, -1.413
+ exitTangent:p3=-1.443, 0.206, -1.618
+ exitTangentHeight:p2=0.0, 0.0
+ exitTangentWidth:p2=-0.0, -0.0
+ exitPointHeight:p2=0.0, 1.0
+ exitPointWidth:p2=1.0, -1.0
+ maxRadius:p2=0.05, 0.4
+ minRadius:p2=0.05, 0.25
+ noiseParms:p2=0.218, 0.674
+ smoothIntensityParams:p3=0.518, 1.505, 0.246
+ density:r=1.0
+ intensityMult:r=7.0
+ criticalAOA:p4=6.0, 22.0, 35.0, 40.0
+ absoluteCriticalAOS:p2=2.0, 15.0
+ absoluteCriticalAOA:p2=5.0, 40.0
+ }
+ 
+ lerxVapor{
+ entryPoint:p3=1.226, -0.3, 1.413
+ exitPoint:p3=-3.299, -0.6, 1.825
+ entryTangent:p3=0.206, -0.35, 1.206
+ exitTangent:p3=-2.062, -0.5, 1.825
+ exitTangentHeight:p2=0.0, 0.0
+ exitTangentWidth:p2=0.0, 0.0
+ exitPointHeight:p2=0.0, 0.0
+ exitPointWidth:p2=-0.5, 0.5
+ maxRadius:p2=0.05, 0.4
+ minRadius:p2=0.05, 0.2
+ noiseParms:p2=0.2, 0.5
+ smoothIntensityParams:p3=0.486, 1.646, 0.209
+ density:r=1.0
+ intensityMult:r=5.0
+ criticalAOA:p4=-5.0, -15.0, -25.0, -30.0
+ absoluteCriticalAOS:p2=2.0, 20.0
+ absoluteCriticalAOA:p2=-2.0, -20.0
+ }
+ 
+ lerxVapor{
+ entryPoint:p3=1.226, -0.3, -1.413
+ exitPoint:p3=-3.299, -0.6, -1.825
+ entryTangent:p3=0.206, -0.35, -1.206
+ exitTangent:p3=-2.062, -0.5, -1.825
+ exitTangentHeight:p2=0.0, 0.0
+ exitTangentWidth:p2=-0.0, -0.0
+ exitPointHeight:p2=0.0, 0.0
+ exitPointWidth:p2=0.5, -0.5
+ maxRadius:p2=0.05, 0.4
+ minRadius:p2=0.05, 0.2
+ noiseParms:p2=0.2, 0.5
+ smoothIntensityParams:p3=0.486, 1.646, 0.209
+ density:r=1.0
+ intensityMult:r=5.0
+ criticalAOA:p4=-5.0, -15.0, -25.0, -30.0
+ absoluteCriticalAOS:p2=2.0, 20.0
+ absoluteCriticalAOA:p2=-2.0, -20.0
+ }
+ }
```

  **Removed**:
```diff
```


- **aces.vromfs.bin_u/gamedata/flightmodels/f-8e.blkx**:

  **Added**:
```diff
+ haveCCRPForGun:b=yes
```

  **Removed**:
```diff
```


- **aces.vromfs.bin_u/gamedata/flightmodels/f-8e_fn.blkx**:

  **Added**:
```diff
+ haveCCRPForGun:b=yes
```

  **Removed**:
```diff
```


- **aces.vromfs.bin_u/gamedata/flightmodels/f_111c_raaf.blkx**:

  **Added**:
```diff
+ isBwOpticSight:b=yes
+ opticsInBombBay:b=yes
+ laserDesignator:b=yes
+ sightThermal{
+ resolution:ip2=500, 300
+ noiseFactor:r=0.05
+ index:i=1
+ }
+ 
+ index:i=2
+ TV{
+ pos:p3=12.0, 0.7, 0.0
+ head:t="optic1_turret"
+ crosshairPreset:t="test_crosshair"
+ angularLimits:p4=-38.0, 38.0, -55.0, 38.0
+ opticType:t="tv"
+ turretNo:i=0
+ nvIndex:i=1
+ }
+ 
+ TV1{
+ pos:p3=12.0, 0.7, 0.0
+ head:t="optic1_turret"
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
+ node:t="optic1_gun"
+ }
+ 
+ preset{
+ name:t="f_111c_gbu_15_ir"
+ blk:t="gameData/FlightModels/weaponPresets/f_111c_gbu_15_ir.blk"
+ }
+ tier:i=9
+ node:t="aero_3b_1"
+ emitter:t="aim_9_1"
+ bullets:i=1
+ external:b=yes
+ separate:b=yes
+ jettisonable:b=no
+ }
+ 
+ BannedWeaponPreset{
+ slot:i=2
+ preset:t="gbu15v2_out"
+ }
+ }
+ }
+ 
+ WeaponSlot{
+ index:i=2
+ tier:i=8
+ order:i=3
+ 
+ WeaponPreset{
+ iconType:t="missile_type_b_air_to_air"
+ name:t="aim_9l"
+ reqModification:t="us_aim_9l"
+ 
+ ShowNodes{
+ node:t="aero_3b_2"
+ node:t="pylon_pivot1"
+ }
+ 
+ Weapon{
+ trigger:t="aam"
+ blk:t="gameData/Weapons/rocketGuns/us_aim9l_sidewinder.blk"
+ WeaponPreset{
+ iconType:t="guided_bomb_green"
+ name:t="gbu15v2_out"
+ reqModification:t="us_gbu_15v1"
+ 
+ ShowNodes{
+ node:t="pylon_pivot1_lapa"
+ node:t="pylon_pivot1"
+ }
+ 
+ Weapon{
+ trigger:t="guided bombs"
+ blk:t="gameData/Weapons/BombGuns/us_2000lb_gbu_15v2.blk"
+ emitter:t="bomb3_gbu"
+ bullets:i=1
+ external:b=yes
+ separate:b=yes
+ machLimit:r=1.01
+ flapsRange:p2=0.0, 0.1
+ }
+ }
+ 
+ index:i=3
+ order:i=5
+ WeaponPreset{
+ iconType:t="guided_bomb_green"
+ name:t="gbu15v2"
+ reqModification:t="us_gbu_15v1"
+ 
+ ShowNodes{
+ node:t="pylon_pivot2_lapa"
+ node:t="pylon_pivot2"
+ }
+ 
+ Weapon{
+ trigger:t="guided bombs"
+ blk:t="gameData/Weapons/BombGuns/us_2000lb_gbu_15v2.blk"
+ emitter:t="bomb4_gbu"
+ bullets:i=1
+ external:b=yes
+ separate:b=yes
+ machLimit:r=1.01
+ flapsRange:p2=0.0, 0.1
+ sweepRange:p2=0.0, 0.75
+ }
+ }
+ 
+ index:i=4
+ order:i=7
+ index:i=5
+ order:i=6
+ WeaponPreset{
+ iconType:t="guided_bomb_green"
+ name:t="gbu15v2"
+ reqModification:t="us_gbu_15v1"
+ 
+ ShowNodes{
+ node:t="pylon_pivot3_lapa"
+ node:t="pylon_pivot3"
+ }
+ 
+ Weapon{
+ trigger:t="guided bombs"
+ blk:t="gameData/Weapons/BombGuns/us_2000lb_gbu_15v2.blk"
+ emitter:t="bomb5_gbu"
+ bullets:i=1
+ external:b=yes
+ separate:b=yes
+ machLimit:r=1.01
+ flapsRange:p2=0.0, 0.1
+ sweepRange:p2=0.0, 0.75
+ }
+ }
+ 
+ index:i=6
+ order:i=4
+ name:t="aim_9l"
+ reqModification:t="us_aim_9l"
+ blk:t="gameData/Weapons/rocketGuns/us_aim9l_sidewinder.blk"
+ WeaponPreset{
+ iconType:t="guided_bomb_green"
+ name:t="gbu15v2_out"
+ reqModification:t="us_gbu_15v1"
+ 
+ ShowNodes{
+ node:t="pylon_pivot4_lapa"
+ node:t="pylon_pivot4"
+ }
+ 
+ Weapon{
+ trigger:t="guided bombs"
+ blk:t="gameData/Weapons/BombGuns/us_2000lb_gbu_15v2.blk"
+ emitter:t="bomb6_gbu"
+ bullets:i=1
+ external:b=yes
+ separate:b=yes
+ machLimit:r=1.01
+ flapsRange:p2=0.0, 0.1
+ }
+ }
+ 
+ 
+ WeaponSlot{
+ index:i=7
+ tier:i=3
+ order:i=2
+ 
+ WeaponPreset{
+ iconType:t="missile_type_b_air_to_air"
+ name:t="aim_9l_default"
+ 
+ ShowNodes{
+ node:t="aero_3b_8"
+ node:t="pylon_pivot4"
+ }
+ 
+ Weapon{
+ trigger:t="aam"
+ blk:t="gameData/Weapons/rocketGuns/us_aim9l_sidewinder_default.blk"
+ emitter:t="aim_9_8"
+ bullets:i=1
+ external:b=yes
+ separate:b=yes
+ jettisonable:b=no
+ }
+ 
+ BannedWeaponPreset{
+ slot:i=6
+ preset:t="gbu15v2_out"
+ }
+ }
+ }
+ tier:i=3
+ us_gbu_15v1{
+ modClass:t="weapon"
+ tier:i=4
+ reqModification:t="us_gbu_10_gbu_24"
+ }
+ 
```

  **Removed**:
```diff
- laserDesignator:b=yes
- tier:i=8
- node:t="aero_3b_2"
- index:i=2
- order:i=3
- index:i=3
- order:i=5
- index:i=4
- order:i=4
- index:i=5
- order:i=2
- name:t="aim_9l_default"
- blk:t="gameData/Weapons/rocketGuns/us_aim9l_sidewinder_default.blk"
- tier:i=4
```


- **aces.vromfs.bin_u/gamedata/flightmodels/f_14a_early.blkx**:

  **Added**:
```diff
+ tier:i=1
+ tier:i=2
```

  **Removed**:
```diff
- reqModification:t="us_aim_9d"
- reqModification:t="us_aim_9d"
- us_aim_9d{
- tier:i=1
- modClass:t="weapon"
- }
- 
- reqModification:t="us_aim_9d"
- tier:i=2
- tier:i=3
```


- **aces.vromfs.bin_u/gamedata/flightmodels/f_16a_block_15_ocu_thailand.blkx**:

  **Added**:
```diff
+ hmdF16c:b=yes
+ hasHelmetDesignator:b=yes
+ helmetDesignatorZone0:p3=-40.0, -50.0, 50.0
+ helmetDesignatorZone1:p3=-20.0, -30.0, 50.0
+ helmetDesignatorZone2:p3=0.0, -15.0, 50.0
+ helmetDesignatorZone3:p3=20.0, -30.0, 50.0
+ helmetDesignatorZone4:p3=40.0, -50.0, 50.0
+ hmdBlockIlsArea:p4=0.5, -0.4, 0.55, 0.6
+ hmdEnabledByDefault:b=yes
```

  **Removed**:
```diff
```


- **aces.vromfs.bin_u/gamedata/flightmodels/la_200_toriy.blkx**:

  **Added**:
```diff
+ emtr_break_wing_tail:p3=-7.49959, 0.0, 0.0
+ emtr_break_stab_l_from:p3=-7.81212, 1.64319, 0.541073
+ emtr_break_stab_r_from:p3=-7.81212, 1.64319, -0.541073
+ emtr_break_fin_from:p3=-6.6801, 1.776487, -1.49012e-08
```

  **Removed**:
```diff
- emtr_break_wing_tail:p3=-6.09959, 0.0, 0.0
- emtr_break_stab_l_from:p3=-7.81212, 1.94319, 0.541073
- emtr_break_stab_r_from:p3=-7.81212, 1.94319, -0.541073
- emtr_break_fin_from:p3=-6.6801, 0.776487, -1.49012e-08
```


- **aces.vromfs.bin_u/gamedata/flightmodels/mirage_2000_5f.blkx**:

  **Added**:
```diff
+ hmdBlockIlsArea:p4=0.5, -0.4, 0.55, 0.6
```

  **Removed**:
```diff
- hmdBlockIlsArea:p4=0.25, -0.4, 0.65, 0.75
```


- **aces.vromfs.bin_u/gamedata/flightmodels/mirage_2000_5f_missile_test.blkx**:

  **Added**:
```diff
+ hmdBlockIlsArea:p4=0.5, -0.4, 0.55, 0.6
```

  **Removed**:
```diff
- hmdBlockIlsArea:p4=0.25, -0.4, 0.65, 0.75
```


- **aces.vromfs.bin_u/gamedata/flightmodels/rafale_c_f3.blkx**:

  **Added**:
```diff
+ scale:r=0.83
+ scale:r=0.85
```

  **Removed**:
```diff
- scale:r=1.0
```


- **aces.vromfs.bin_u/gamedata/flightmodels/saab_jas39a.blkx**:

  **Added**:
```diff
+ emtr_break_wing_tail:p3=-3.91985, 0.0, 0.0
+ emtr_break_tail_from:p3=-3.91985, -0.0792358, 0.0
```

  **Removed**:
```diff
- emtr_break_wing_tail:p3=-1.95921, 0.0, 0.0
- emtr_break_tail_from:p3=-3.21985, -0.0792358, 0.0
```


- **aces.vromfs.bin_u/gamedata/flightmodels/saab_jas39c.blkx**:

  **Added**:
```diff
+ emtr_break_wing_tail:p3=-3.91985, 0.0, 0.0
+ emtr_break_tail_from:p3=-3.91985, -0.0792358, 0.0
```

  **Removed**:
```diff
- emtr_break_wing_tail:p3=-1.95921, 0.0, 0.0
- emtr_break_tail_from:p3=-3.21985, -0.0792358, 0.0
```


- **aces.vromfs.bin_u/gamedata/flightmodels/saab_jas39c_hungary.blkx**:

  **Added**:
```diff
+ emtr_break_wing_tail:p3=-3.91985, 0.0, 0.0
+ emtr_break_tail_from:p3=-3.91985, -0.0792358, 0.0
```

  **Removed**:
```diff
- emtr_break_wing_tail:p3=-1.95921, 0.0, 0.0
- emtr_break_tail_from:p3=-3.21985, -0.0792358, 0.0
```


- **aces.vromfs.bin_u/gamedata/flightmodels/saab_jas39c_south_africa.blkx**:

  **Added**:
```diff
+ emtr_break_wing_tail:p3=-3.91985, 0.0, 0.0
+ emtr_break_tail_from:p3=-3.91985, -0.0792358, 0.0
```

  **Removed**:
```diff
- emtr_break_wing_tail:p3=-1.95921, 0.0, 0.0
- emtr_break_tail_from:p3=-3.21985, -0.0792358, 0.0
```


- **aces.vromfs.bin_u/gamedata/flightmodels/saab_jas39c_south_africa_missile_test.blkx**:

  **Added**:
```diff
+ emtr_break_wing_tail:p3=-3.91985, 0.0, 0.0
+ emtr_break_tail_from:p3=-3.91985, -0.0792358, 0.0
```

  **Removed**:
```diff
- emtr_break_wing_tail:p3=-1.95921, 0.0, 0.0
- emtr_break_tail_from:p3=-3.21985, -0.0792358, 0.0
```


- **aces.vromfs.bin_u/gamedata/flightmodels/saab_jas39c_thailand.blkx**:

  **Added**:
```diff
+ emtr_break_wing_tail:p3=-3.91985, 0.0, 0.0
+ emtr_break_tail_from:p3=-3.91985, -0.0792358, 0.0
```

  **Removed**:
```diff
- emtr_break_wing_tail:p3=-1.95921, 0.0, 0.0
- emtr_break_tail_from:p3=-3.21985, -0.0792358, 0.0
```


- **aces.vromfs.bin_u/gamedata/flightmodels/su-11.blkx**:

  **Added**:
```diff
+ _emtr_break_wing0_l_from:p3=-0.683855, 0.00882936, 0.810993
+ _emtr_break_wing0_l_to:p3=-0.683855, 0.00882936, 1.46305
+ emtr_break_wing1_l_from:p3=-0.683855, 0.00882936, 2.81688
+ emtr_break_wing1_l_to:p3=-0.683855, 0.00882936, 2.82885
+ emtr_break_wing2_l_from:p3=-0.683855, 0.00882936, 3.85781
+ emtr_break_wing2_l_to:p3=-0.683855, 0.00882936, 4.5599
+ _emtr_break_wing0_r_from:p3=-0.683855, 0.00882882, -0.810993
+ _emtr_break_wing0_r_to:p3=-0.683855, 0.00882882, -1.46305
+ emtr_break_wing1_r_from:p3=-0.683855, 0.00882882, -2.81688
+ emtr_break_wing1_r_to:p3=-0.683855, 0.00882882, -2.82885
+ emtr_break_wing2_r_from:p3=-0.683855, 0.00882882, -3.85781
+ emtr_break_wing2_r_to:p3=-0.683855, 0.00882882, -4.5599
+ emtr_break_wing_tail:p3=-5.05777, 0.0, 0.0
+ emtr_break_stab_l_from:p3=-5.05777, 0.95966, 0.402864
+ emtr_break_stab_l_to:p3=-5.05777, 0.95966, 1.61145
+ emtr_break_stab_r_from:p3=-5.05777, 0.95966, -0.402864
+ emtr_break_stab_r_to:p3=-5.05777, 0.95966, -1.61145
+ emtr_break_fin_from:p3=-4.62791, 1.876152, 0.0
```

  **Removed**:
```diff
- emtr_break_wing2_l_from:p3=-0.683855, 0.0261557, 4.15628
- emtr_break_wing2_l_to:p3=-0.683855, 0.0261557, 4.88087
- emtr_break_wing2_r_from:p3=-0.683855, 0.0261558, -4.15628
- emtr_break_wing2_r_to:p3=-0.683855, 0.0261558, -4.88087
- emtr_break_wing_tail:p3=-3.32647, 0.0, 0.0
- emtr_break_stab_l_from:p3=-5.05777, 1.01032, 0.402864
- emtr_break_stab_l_to:p3=-5.05777, 1.01032, 1.61145
- emtr_break_stab_r_from:p3=-5.05777, 1.01032, -0.402864
- emtr_break_stab_r_to:p3=-5.05777, 1.01032, -1.61145
- emtr_break_fin_from:p3=-4.62791, 0.876152, 0.0
```


- **aces.vromfs.bin_u/gamedata/flightmodels/su-9.blkx**:

  **Added**:
```diff
+ emtr_break_wing_tail:p3=-5.05777, 0.0, 0.0
+ emtr_break_fin_from:p3=-4.62791, 1.876152, 0.0
```

  **Removed**:
```diff
- emtr_break_wing_tail:p3=-3.32647, 0.0, 0.0
- emtr_break_fin_from:p3=-4.62791, 0.876152, 0.0
```


- **aces.vromfs.bin_u/gamedata/flightmodels/tu-2_postwar.blkx**:

  **Added**:
```diff
+ blk:t="gameData/Weapons/BombGuns/su_fab_250m_43.blk"
+ blk:t="gameData/Weapons/BombGuns/su_fab_500m_43.blk"
+ blk:t="gameData/Weapons/BombGuns/su_fab_1000m_43.blk"
+ blk:t="gameData/Weapons/BombGuns/su_fab_250m_43.blk"
+ blk:t="gameData/Weapons/BombGuns/su_fab_250m_43.blk"
+ blk:t="gameData/Weapons/BombGuns/su_fab_250m_43.blk"
+ blk:t="gameData/Weapons/BombGuns/su_fab_250m_43.blk"
+ blk:t="gameData/Weapons/BombGuns/su_fab_250m_43.blk"
+ blk:t="gameData/Weapons/BombGuns/su_fab_250m_43.blk"
+ blk:t="gameData/Weapons/BombGuns/su_fab_500m_43.blk"
+ blk:t="gameData/Weapons/BombGuns/su_fab_1000m_43.blk"
+ blk:t="gameData/Weapons/BombGuns/su_fab_250m_43.blk"
+ blk:t="gameData/Weapons/BombGuns/su_fab_500m_43.blk"
+ blk:t="gameData/Weapons/BombGuns/su_fab_1000m_43.blk"
```

  **Removed**:
```diff
- blk:t="gameData/Weapons/BombGuns/su_fab_250m_44.blk"
- blk:t="gameData/Weapons/BombGuns/su_fab_500m_44.blk"
- blk:t="gameData/Weapons/BombGuns/su_fab_1000m_44.blk"
- blk:t="gameData/Weapons/BombGuns/su_fab_250m_44.blk"
- blk:t="gameData/Weapons/BombGuns/su_fab_250m_44.blk"
- blk:t="gameData/Weapons/BombGuns/su_fab_250m_44.blk"
- blk:t="gameData/Weapons/BombGuns/su_fab_250m_44.blk"
- blk:t="gameData/Weapons/BombGuns/su_fab_250m_44.blk"
- blk:t="gameData/Weapons/BombGuns/su_fab_250m_44.blk"
- blk:t="gameData/Weapons/BombGuns/su_fab_500m_44.blk"
- blk:t="gameData/Weapons/BombGuns/su_fab_1000m_44.blk"
- blk:t="gameData/Weapons/BombGuns/su_fab_250m_44.blk"
- blk:t="gameData/Weapons/BombGuns/su_fab_500m_44.blk"
- blk:t="gameData/Weapons/BombGuns/su_fab_1000m_44.blk"
```


- **aces.vromfs.bin_u/gamedata/flightmodels/tu-2_postwar_china.blkx**:

  **Added**:
```diff
+ blk:t="gameData/Weapons/BombGuns/su_fab_500m_43.blk"
+ blk:t="gameData/Weapons/BombGuns/su_fab_1000m_43.blk"
+ blk:t="gameData/Weapons/BombGuns/su_fab_500m_43.blk"
+ blk:t="gameData/Weapons/BombGuns/su_fab_1000m_43.blk"
+ blk:t="gameData/Weapons/BombGuns/su_fab_500m_43.blk"
+ blk:t="gameData/Weapons/BombGuns/su_fab_1000m_43.blk"
```

  **Removed**:
```diff
- blk:t="gameData/Weapons/BombGuns/su_fab_500m_44.blk"
- blk:t="gameData/Weapons/BombGuns/su_fab_1000m_44.blk"
- blk:t="gameData/Weapons/BombGuns/su_fab_500m_44.blk"
- blk:t="gameData/Weapons/BombGuns/su_fab_1000m_44.blk"
- blk:t="gameData/Weapons/BombGuns/su_fab_500m_44.blk"
- blk:t="gameData/Weapons/BombGuns/su_fab_1000m_44.blk"
```


- **aces.vromfs.bin_u/gamedata/flightmodels/tu-2_postwar_late.blkx**:

  **Added**:
```diff
+ blk:t="gameData/Weapons/BombGuns/su_fab_250m_43.blk"
+ blk:t="gameData/Weapons/BombGuns/su_fab_500m_43.blk"
+ blk:t="gameData/Weapons/BombGuns/su_fab_1000m_43.blk"
+ blk:t="gameData/Weapons/BombGuns/su_fab_250m_43.blk"
+ blk:t="gameData/Weapons/BombGuns/su_fab_250m_43.blk"
+ blk:t="gameData/Weapons/BombGuns/su_fab_250m_43.blk"
+ blk:t="gameData/Weapons/BombGuns/su_fab_250m_43.blk"
+ blk:t="gameData/Weapons/BombGuns/su_fab_250m_43.blk"
+ blk:t="gameData/Weapons/BombGuns/su_fab_250m_43.blk"
+ blk:t="gameData/Weapons/BombGuns/su_fab_500m_43.blk"
+ blk:t="gameData/Weapons/BombGuns/su_fab_1000m_43.blk"
+ blk:t="gameData/Weapons/BombGuns/su_fab_250m_43.blk"
+ blk:t="gameData/Weapons/BombGuns/su_fab_500m_43.blk"
+ blk:t="gameData/Weapons/BombGuns/su_fab_1000m_43.blk"
```

  **Removed**:
```diff
- blk:t="gameData/Weapons/BombGuns/su_fab_250m_44.blk"
- blk:t="gameData/Weapons/BombGuns/su_fab_500m_44.blk"
- blk:t="gameData/Weapons/BombGuns/su_fab_1000m_44.blk"
- blk:t="gameData/Weapons/BombGuns/su_fab_250m_44.blk"
- blk:t="gameData/Weapons/BombGuns/su_fab_250m_44.blk"
- blk:t="gameData/Weapons/BombGuns/su_fab_250m_44.blk"
- blk:t="gameData/Weapons/BombGuns/su_fab_250m_44.blk"
- blk:t="gameData/Weapons/BombGuns/su_fab_250m_44.blk"
- blk:t="gameData/Weapons/BombGuns/su_fab_250m_44.blk"
- blk:t="gameData/Weapons/BombGuns/su_fab_500m_44.blk"
- blk:t="gameData/Weapons/BombGuns/su_fab_1000m_44.blk"
- blk:t="gameData/Weapons/BombGuns/su_fab_250m_44.blk"
- blk:t="gameData/Weapons/BombGuns/su_fab_500m_44.blk"
- blk:t="gameData/Weapons/BombGuns/su_fab_1000m_44.blk"
```


- **aces.vromfs.bin_u/gamedata/flightmodels/tu-2_postwar_late_hungary.blkx**:

  **Added**:
```diff
+ blk:t="gameData/Weapons/BombGuns/su_fab_250m_43.blk"
+ blk:t="gameData/Weapons/BombGuns/su_fab_500m_43.blk"
+ blk:t="gameData/Weapons/BombGuns/su_fab_1000m_43.blk"
+ blk:t="gameData/Weapons/BombGuns/su_fab_250m_43.blk"
+ blk:t="gameData/Weapons/BombGuns/su_fab_250m_43.blk"
+ blk:t="gameData/Weapons/BombGuns/su_fab_250m_43.blk"
+ blk:t="gameData/Weapons/BombGuns/su_fab_250m_43.blk"
+ blk:t="gameData/Weapons/BombGuns/su_fab_250m_43.blk"
+ blk:t="gameData/Weapons/BombGuns/su_fab_250m_43.blk"
+ blk:t="gameData/Weapons/BombGuns/su_fab_500m_43.blk"
+ blk:t="gameData/Weapons/BombGuns/su_fab_1000m_43.blk"
+ blk:t="gameData/Weapons/BombGuns/su_fab_250m_43.blk"
+ blk:t="gameData/Weapons/BombGuns/su_fab_500m_43.blk"
+ blk:t="gameData/Weapons/BombGuns/su_fab_1000m_43.blk"
```

  **Removed**:
```diff
- blk:t="gameData/Weapons/BombGuns/su_fab_250m_44.blk"
- blk:t="gameData/Weapons/BombGuns/su_fab_500m_44.blk"
- blk:t="gameData/Weapons/BombGuns/su_fab_1000m_44.blk"
- blk:t="gameData/Weapons/BombGuns/su_fab_250m_44.blk"
- blk:t="gameData/Weapons/BombGuns/su_fab_250m_44.blk"
- blk:t="gameData/Weapons/BombGuns/su_fab_250m_44.blk"
- blk:t="gameData/Weapons/BombGuns/su_fab_250m_44.blk"
- blk:t="gameData/Weapons/BombGuns/su_fab_250m_44.blk"
- blk:t="gameData/Weapons/BombGuns/su_fab_250m_44.blk"
- blk:t="gameData/Weapons/BombGuns/su_fab_500m_44.blk"
- blk:t="gameData/Weapons/BombGuns/su_fab_1000m_44.blk"
- blk:t="gameData/Weapons/BombGuns/su_fab_250m_44.blk"
- blk:t="gameData/Weapons/BombGuns/su_fab_500m_44.blk"
- blk:t="gameData/Weapons/BombGuns/su_fab_1000m_44.blk"
```


- **aces.vromfs.bin_u/gamedata/flightmodels/weaponpresets/f_111c_aim9l.blkx**:

  **Added**:
```diff
+ slot:i=3
+ preset:t="aim_9l"
+ }
+ 
+ Weapon{
+ slot:i=6
+ preset:t="aim_9l"
+ }
+ 
+ Weapon{
+ slot:i=7
```

  **Removed**:
```diff
- slot:i=4
```


- **aces.vromfs.bin_u/gamedata/flightmodels/weaponpresets/f_111c_default.blkx**:

  **Added**:
```diff
+ slot:i=4
+ slot:i=7
```

  **Removed**:
```diff
- slot:i=3
- slot:i=5
```


- **aces.vromfs.bin_u/gamedata/flightmodels/weaponpresets/f_111c_default_ptb.blkx**:

  **Added**:
```diff
+ slot:i=2
+ slot:i=3
+ slot:i=5
+ slot:i=6
```

  **Removed**:
```diff
- slot:i=1
- slot:i=2
- slot:i=4
- slot:i=5
```


- **aces.vromfs.bin_u/gamedata/flightmodels/weaponpresets/f_111c_gbu_10.blkx**:

  **Added**:
```diff
+ slot:i=2
+ slot:i=3
+ slot:i=4
+ slot:i=5
+ slot:i=6
```

  **Removed**:
```diff
- slot:i=1
- slot:i=2
- slot:i=3
- slot:i=4
- slot:i=5
```


- **aces.vromfs.bin_u/gamedata/flightmodels/weaponpresets/f_111c_gbu_12.blkx**:

  **Added**:
```diff
+ slot:i=2
+ slot:i=3
+ slot:i=4
+ slot:i=5
+ slot:i=6
```

  **Removed**:
```diff
- slot:i=1
- slot:i=2
- slot:i=3
- slot:i=4
- slot:i=5
```


- **aces.vromfs.bin_u/gamedata/flightmodels/weaponpresets/f_111c_gbu_15_ir.blkx**:

  **Added**:
```diff
+ Weapon{
+ slot:i=2
+ preset:t="gbu15v2_out"
+ }
+ 
+ Weapon{
+ slot:i=3
+ preset:t="gbu15v2"
+ }
+ 
+ Weapon{
+ slot:i=5
+ preset:t="gbu15v2"
+ }
+ 
+ Weapon{
+ slot:i=6
+ preset:t="gbu15v2_out"
+ }
```

  **Removed**:
```diff
```


- **aces.vromfs.bin_u/gamedata/flightmodels/weaponpresets/f_111c_gbu_24.blkx**:

  **Added**:
```diff
+ slot:i=2
+ slot:i=3
+ slot:i=4
+ slot:i=5
+ slot:i=6
```

  **Removed**:
```diff
- slot:i=1
- slot:i=2
- slot:i=3
- slot:i=4
- slot:i=5
```


- **aces.vromfs.bin_u/gamedata/flightmodels/weaponpresets/f_111c_mk82_bru_supersonic.blkx**:

  **Added**:
```diff
+ slot:i=2
+ slot:i=3
+ slot:i=5
+ slot:i=6
```

  **Removed**:
```diff
- slot:i=1
- slot:i=2
- slot:i=4
- slot:i=5
```


- **aces.vromfs.bin_u/gamedata/flightmodels/weaponpresets/f_111c_mk82_snakeye_bru_supersonic.blkx**:

  **Added**:
```diff
+ slot:i=2
+ slot:i=3
+ slot:i=5
+ slot:i=6
```

  **Removed**:
```diff
- slot:i=1
- slot:i=2
- slot:i=4
- slot:i=5
```


- **aces.vromfs.bin_u/gamedata/flightmodels/weaponpresets/f_111c_mk84.blkx**:

  **Added**:
```diff
+ slot:i=2
+ slot:i=3
+ slot:i=5
+ slot:i=6
```

  **Removed**:
```diff
- slot:i=1
- slot:i=2
- slot:i=4
- slot:i=5
```


- **aces.vromfs.bin_u/gamedata/flightmodels/weaponpresets/f_5ag_agm_119a.blkx**:

  **Added**:
```diff
+ Weapon{
+ slot:i=4
+ preset:t="agm_119a"
+ }
```

  **Removed**:
```diff
```


- **aces.vromfs.bin_u/gamedata/flightmodels/weaponpresets/f_5ag_aim_9l.blkx**:

  **Added**:
```diff
+ Weapon{
+ slot:i=1
+ preset:t="aim_9l"
+ }
+ 
+ Weapon{
+ slot:i=7
+ preset:t="aim_9l"
+ }
```

  **Removed**:
```diff
```


- **aces.vromfs.bin_u/gamedata/flightmodels/weaponpresets/f_5ag_bomb_blu27.blkx**:

  **Added**:
```diff
+ Weapon{
+ slot:i=2
+ preset:t="blu27"
+ }
+ 
+ Weapon{
+ slot:i=3
+ preset:t="blu27"
+ }
+ 
+ Weapon{
+ slot:i=4
+ preset:t="blu27"
+ }
+ 
+ Weapon{
+ slot:i=5
+ preset:t="blu27"
+ }
+ 
+ Weapon{
+ slot:i=6
+ preset:t="blu27"
+ }
```

  **Removed**:
```diff
```


- **aces.vromfs.bin_u/gamedata/flightmodels/weaponpresets/f_5ag_bomb_blu_1.blkx**:

  **Added**:
```diff
+ Weapon{
+ slot:i=2
+ preset:t="blu27"
+ }
+ 
+ Weapon{
+ slot:i=3
+ preset:t="blu27"
+ }
+ 
+ Weapon{
+ slot:i=4
+ preset:t="blu27"
+ }
+ 
+ Weapon{
+ slot:i=5
+ preset:t="blu27"
+ }
+ 
+ Weapon{
+ slot:i=6
+ preset:t="blu27"
+ }
```

  **Removed**:
```diff
```


- **aces.vromfs.bin_u/gamedata/flightmodels/weaponpresets/f_5ag_bomb_m117.blkx**:

  **Added**:
```diff
+ Weapon{
+ slot:i=2
+ preset:t="m117"
+ }
+ 
+ Weapon{
+ slot:i=3
+ preset:t="m117"
+ }
+ 
+ Weapon{
+ slot:i=4
+ preset:t="m117"
+ }
+ 
+ Weapon{
+ slot:i=5
+ preset:t="m117"
+ }
+ 
+ Weapon{
+ slot:i=6
+ preset:t="m117"
+ }
```

  **Removed**:
```diff
```


- **aces.vromfs.bin_u/gamedata/flightmodels/weaponpresets/f_5ag_bomb_mk82.blkx**:

  **Added**:
```diff
+ Weapon{
+ slot:i=2
+ preset:t="mk82"
+ }
+ 
+ Weapon{
+ slot:i=3
+ preset:t="mk82"
+ }
+ 
+ Weapon{
+ slot:i=4
+ preset:t="mk82"
+ }
+ 
+ Weapon{
+ slot:i=5
+ preset:t="mk82"
+ }
+ 
+ Weapon{
+ slot:i=6
+ preset:t="mk82"
+ }
```

  **Removed**:
```diff
```


- **aces.vromfs.bin_u/gamedata/flightmodels/weaponpresets/f_5ag_bomb_mk82_snakeye.blkx**:

  **Added**:
```diff
+ Weapon{
+ slot:i=2
+ preset:t="mk82_snakeye"
+ }
+ 
+ Weapon{
+ slot:i=3
+ preset:t="mk82_snakeye"
+ }
+ 
+ Weapon{
+ slot:i=4
+ preset:t="mk82_snakeye"
+ }
+ 
+ Weapon{
+ slot:i=5
+ preset:t="mk82_snakeye"
+ }
+ 
+ Weapon{
+ slot:i=6
+ preset:t="mk82_snakeye"
+ }
```

  **Removed**:
```diff
```


- **aces.vromfs.bin_u/gamedata/flightmodels/weaponpresets/f_5ag_bomb_mk83.blkx**:

  **Added**:
```diff
+ Weapon{
+ slot:i=3
+ preset:t="mk83"
+ }
+ 
+ Weapon{
+ slot:i=4
+ preset:t="mk83"
+ }
+ 
+ Weapon{
+ slot:i=5
+ preset:t="mk83"
+ }
```

  **Removed**:
```diff
```


- **aces.vromfs.bin_u/gamedata/flightmodels/weaponpresets/f_5ag_bomb_mk84.blkx**:

  **Added**:
```diff
+ Weapon{
+ slot:i=4
+ preset:t="mk84"
+ }
```

  **Removed**:
```diff
```


- **aces.vromfs.bin_u/gamedata/flightmodels/weaponpresets/f_5ag_default.blkx**:

  **Added**:
```diff
+ Weapon{
+ slot:i=1
+ preset:t="aim_9l"
+ }
+ 
+ Weapon{
+ slot:i=3
+ preset:t="ptb_slot3"
+ }
+ 
+ Weapon{
+ slot:i=4
+ preset:t="ptb_slot4"
+ }
+ 
+ Weapon{
+ slot:i=5
+ preset:t="ptb_slot5"
+ }
+ 
+ Weapon{
+ slot:i=7
+ preset:t="aim_9l"
+ }
```

  **Removed**:
```diff
```


- **aces.vromfs.bin_u/gamedata/flightmodels/weaponpresets/f_5ag_gau_5a.blkx**:

  **Added**:
```diff
+ Weapon{
+ slot:i=4
+ preset:t="gau_5a_gunpod"
+ }
```

  **Removed**:
```diff
```


- **aces.vromfs.bin_u/gamedata/flightmodels/weaponpresets/f_5ag_rockets_agm_12b.blkx**:

  **Added**:
```diff
+ Weapon{
+ slot:i=2
+ preset:t="agm_12b"
+ }
+ 
+ Weapon{
+ slot:i=3
+ preset:t="agm_12b"
+ }
+ 
+ Weapon{
+ slot:i=5
+ preset:t="agm_12b"
+ }
+ 
+ Weapon{
+ slot:i=6
+ preset:t="agm_12b"
+ }
```

  **Removed**:
```diff
```


- **aces.vromfs.bin_u/gamedata/flightmodels/weaponpresets/f_5ag_rockets_lau18.blkx**:

  **Added**:
```diff
+ Weapon{
+ slot:i=2
+ preset:t="aero_7a"
+ }
+ 
+ Weapon{
+ slot:i=3
+ preset:t="aero_7a"
+ }
+ 
+ Weapon{
+ slot:i=5
+ preset:t="aero_7a"
+ }
+ 
+ Weapon{
+ slot:i=6
+ preset:t="aero_7a"
+ }
```

  **Removed**:
```diff
```


- **aces.vromfs.bin_u/gamedata/flightmodels/weaponpresets/f_5ag_rockets_zuni.blkx**:

  **Added**:
```diff
+ Weapon{
+ slot:i=2
+ preset:t="lau_10a"
+ }
+ 
+ Weapon{
+ slot:i=6
+ preset:t="lau_10a"
+ }
```

  **Removed**:
```diff
```


- **aces.vromfs.bin_u/gamedata/units/ships/germ_cruiser_nurnberg.blkx**:

  **Added**:
```diff
+ count:i=360
+ count:i=360
+ count:i=360
+ count:i=180
+ count:i=180
+ count:i=360
+ count:i=180
+ count:i=180
```

  **Removed**:
```diff
- count:i=450
- count:i=450
- count:i=450
- count:i=225
- count:i=225
- count:i=450
- count:i=225
- count:i=225
```


- **aces.vromfs.bin_u/gamedata/units/ships/germ_cruiser_nurnberg_ec.blkx**:

  **Added**:
```diff
+ count:i=360
+ count:i=360
+ count:i=360
+ count:i=180
+ count:i=180
+ count:i=360
+ count:i=180
+ count:i=180
```

  **Removed**:
```diff
- count:i=450
- count:i=450
- count:i=450
- count:i=225
- count:i=225
- count:i=450
- count:i=225
- count:i=225
```


- **aces.vromfs.bin_u/gamedata/units/ships/it_battleship_caio_duilio.blkx**:

  **Added**:
```diff
+ armorThickness:r=70.0
+ armorThickness:r=70.0
+ armorThickness:r=70.0
+ armorThickness:r=70.0
```

  **Removed**:
```diff
- armorThickness:r=20.0
- armorThickness:r=20.0
- armorThickness:r=20.0
- armorThickness:r=20.0
```


- **aces.vromfs.bin_u/gamedata/units/ships/jp_sehatei_mod1.blkx**:

  **Added**:
```diff
+ 
+ gunStabilizer{
+ hasVerticalGunFreeMode:b=yes
+ hasHorizontal:b=yes
+ horizontalOmegaMult:r=1.0
+ horizontalSpeedLimitKPH:r=80.0
+ hasVertical:b=yes
+ verticalOmegaMult:r=1.0
+ verticalSpeedLimitKPH:r=80.0
+ }
```

  **Removed**:
```diff
```


- **aces.vromfs.bin_u/gamedata/units/ships/jp_type5_escortboat.blkx**:

  **Added**:
```diff
+ 
+ gunStabilizer{
+ hasVerticalGunFreeMode:b=yes
+ hasHorizontal:b=yes
+ horizontalOmegaMult:r=1.0
+ horizontalSpeedLimitKPH:r=80.0
+ hasVertical:b=yes
+ verticalOmegaMult:r=1.0
+ verticalSpeedLimitKPH:r=80.0
+ }
```

  **Removed**:
```diff
```


- **aces.vromfs.bin_u/gamedata/units/ships/uk_frigate_river.blkx**:

  **Added**:
```diff
+ pitch:p2=-10.0, 85.0
+ lim1:p4=-180.0, -175.0, -5.0, 85.0
+ lim2:p4=-175.0, -15.0, -10.0, 85.0
+ lim3:p4=-15.0, 25.0, 18.0, 85.0
+ lim4:p4=25.0, 80.0, 0.0, 85.0
+ lim5:p4=80.0, 180.0, 20.0, 85.0
+ pitch:p2=-10.0, 85.0
+ lim1:p4=-180.0, -80.0, 20.0, 85.0
+ lim2:p4=-80.0, -25.0, 0.0, 85.0
+ lim3:p4=-25.0, 15.0, 18.0, 85.0
+ lim4:p4=15.0, 175.0, -10.0, 85.0
+ lim5:p4=175.0, 180.0, -5.0, 85.0
```

  **Removed**:
```diff
- pitch:p2=-10.0, 90.0
- lim1:p4=-180.0, -175.0, -5.0, 90.0
- lim2:p4=-175.0, -15.0, -10.0, 90.0
- lim3:p4=-15.0, 25.0, 18.0, 90.0
- lim4:p4=25.0, 80.0, 0.0, 90.0
- lim5:p4=80.0, 180.0, 20.0, 90.0
- pitch:p2=-10.0, 90.0
- lim1:p4=-180.0, -80.0, 20.0, 90.0
- lim2:p4=-80.0, -25.0, 0.0, 90.0
- lim3:p4=-25.0, 15.0, 18.0, 90.0
- lim4:p4=15.0, 175.0, -10.0, 90.0
- lim5:p4=175.0, 180.0, -5.0, 90.0
```


- **aces.vromfs.bin_u/gamedata/units/ships/ussr_1124_ack.blkx**:

  **Added**:
```diff
+ 
+ gunStabilizer{
+ hasVerticalGunFreeMode:b=yes
+ hasHorizontal:b=yes
+ horizontalOmegaMult:r=1.0
+ horizontalSpeedLimitKPH:r=80.0
+ hasVertical:b=yes
+ verticalOmegaMult:r=1.0
+ verticalSpeedLimitKPH:r=80.0
+ }
+ 
+ gunStabilizer{
+ hasVerticalGunFreeMode:b=yes
+ hasHorizontal:b=yes
+ horizontalOmegaMult:r=1.0
+ horizontalSpeedLimitKPH:r=80.0
+ hasVertical:b=yes
+ verticalOmegaMult:r=1.0
+ verticalSpeedLimitKPH:r=80.0
+ }
```

  **Removed**:
```diff
```


- **aces.vromfs.bin_u/gamedata/units/ships/ussr_1124_art.blkx**:

  **Added**:
```diff
+ 
+ gunStabilizer{
+ hasVerticalGunFreeMode:b=yes
+ hasHorizontal:b=yes
+ horizontalOmegaMult:r=1.0
+ horizontalSpeedLimitKPH:r=80.0
+ hasVertical:b=yes
+ verticalOmegaMult:r=1.0
+ verticalSpeedLimitKPH:r=80.0
+ }
+ 
+ gunStabilizer{
+ hasVerticalGunFreeMode:b=yes
+ hasHorizontal:b=yes
+ horizontalOmegaMult:r=1.0
+ horizontalSpeedLimitKPH:r=80.0
+ hasVertical:b=yes
+ verticalOmegaMult:r=1.0
+ verticalSpeedLimitKPH:r=80.0
+ }
```

  **Removed**:
```diff
```


- **aces.vromfs.bin_u/gamedata/units/ships/ussr_1124_rct.blkx**:

  **Added**:
```diff
+ 
+ gunStabilizer{
+ hasVerticalGunFreeMode:b=yes
+ hasHorizontal:b=yes
+ horizontalOmegaMult:r=1.0
+ horizontalSpeedLimitKPH:r=80.0
+ hasVertical:b=yes
+ verticalOmegaMult:r=1.0
+ verticalSpeedLimitKPH:r=80.0
+ }
```

  **Removed**:
```diff
```


- **aces.vromfs.bin_u/gamedata/units/ships/ussr_battleship_arhangelsk.blkx**:

  **Added**:
```diff
+ isBulletBelt:b=yes
+ isBulletBelt:b=yes
+ isBulletBelt:b=yes
+ isBulletBelt:b=yes
+ isBulletBelt:b=yes
+ isBulletBelt:b=yes
+ isBulletBelt:b=yes
+ isBulletBelt:b=yes
```

  **Removed**:
```diff
```


- **aces.vromfs.bin_u/gamedata/units/ships/ussr_mbk_161_1943.blkx**:

  **Added**:
```diff
+ 
+ gunStabilizer{
+ hasVerticalGunFreeMode:b=yes
+ hasHorizontal:b=yes
+ horizontalOmegaMult:r=1.0
+ horizontalSpeedLimitKPH:r=80.0
+ hasVertical:b=yes
+ verticalOmegaMult:r=1.0
+ verticalSpeedLimitKPH:r=80.0
+ }
+ 
+ gunStabilizer{
+ hasVerticalGunFreeMode:b=yes
+ hasHorizontal:b=yes
+ horizontalOmegaMult:r=1.0
+ horizontalSpeedLimitKPH:r=80.0
+ hasVertical:b=yes
+ verticalOmegaMult:r=1.0
+ verticalSpeedLimitKPH:r=80.0
+ }
```

  **Removed**:
```diff
```


- **aces.vromfs.bin_u/gamedata/units/ships/ussr_mbk_161_1944.blkx**:

  **Added**:
```diff
+ 
+ gunStabilizer{
+ hasVerticalGunFreeMode:b=yes
+ hasHorizontal:b=yes
+ horizontalOmegaMult:r=1.0
+ horizontalSpeedLimitKPH:r=80.0
+ hasVertical:b=yes
+ verticalOmegaMult:r=1.0
+ verticalSpeedLimitKPH:r=80.0
+ }
+ 
+ gunStabilizer{
+ hasVerticalGunFreeMode:b=yes
+ hasHorizontal:b=yes
+ horizontalOmegaMult:r=1.0
+ horizontalSpeedLimitKPH:r=80.0
+ hasVertical:b=yes
+ verticalOmegaMult:r=1.0
+ verticalSpeedLimitKPH:r=80.0
+ }
```

  **Removed**:
```diff
```


- **aces.vromfs.bin_u/gamedata/units/ships/ussr_mkl_186.blkx**:

  **Added**:
```diff
+ 
+ gunStabilizer{
+ hasVerticalGunFreeMode:b=yes
+ hasHorizontal:b=yes
+ horizontalOmegaMult:r=1.0
+ horizontalSpeedLimitKPH:r=80.0
+ hasVertical:b=yes
+ verticalOmegaMult:r=1.0
+ verticalSpeedLimitKPH:r=80.0
+ }
+ 
+ gunStabilizer{
+ hasVerticalGunFreeMode:b=yes
+ hasHorizontal:b=yes
+ horizontalOmegaMult:r=1.0
+ horizontalSpeedLimitKPH:r=80.0
+ hasVertical:b=yes
+ verticalOmegaMult:r=1.0
+ verticalSpeedLimitKPH:r=80.0
+ }
```

  **Removed**:
```diff
```


- **aces.vromfs.bin_u/gamedata/units/ships/ussr_mkl_186_mk85.blkx**:

  **Added**:
```diff
+ 
+ gunStabilizer{
+ hasVerticalGunFreeMode:b=yes
+ hasHorizontal:b=yes
+ horizontalOmegaMult:r=1.0
+ horizontalSpeedLimitKPH:r=80.0
+ hasVertical:b=yes
+ verticalOmegaMult:r=1.0
+ verticalSpeedLimitKPH:r=80.0
+ }
+ 
+ gunStabilizer{
+ hasVerticalGunFreeMode:b=yes
+ hasHorizontal:b=yes
+ horizontalOmegaMult:r=1.0
+ horizontalSpeedLimitKPH:r=80.0
+ hasVertical:b=yes
+ verticalOmegaMult:r=1.0
+ verticalSpeedLimitKPH:r=80.0
+ }
```

  **Removed**:
```diff
```


- **aces.vromfs.bin_u/gamedata/units/ships/ussr_pr_1204_late.blkx**:

  **Added**:
```diff
+ 
+ gunStabilizer{
+ hasVerticalGunFreeMode:b=yes
+ hasHorizontal:b=yes
+ horizontalOmegaMult:r=1.0
+ horizontalSpeedLimitKPH:r=120.0
+ hasVertical:b=yes
+ verticalOmegaMult:r=1.0
+ verticalSpeedLimitKPH:r=120.0
+ }
+ 
+ gunStabilizer{
+ hasVerticalGunFreeMode:b=yes
+ hasHorizontal:b=yes
+ horizontalOmegaMult:r=1.0
+ horizontalSpeedLimitKPH:r=120.0
+ hasVertical:b=yes
+ verticalOmegaMult:r=1.0
+ verticalSpeedLimitKPH:r=120.0
+ }
+ 
+ gunStabilizer{
+ hasVerticalGunFreeMode:b=yes
+ hasHorizontal:b=yes
+ horizontalOmegaMult:r=1.0
+ horizontalSpeedLimitKPH:r=120.0
+ hasVertical:b=yes
+ verticalOmegaMult:r=1.0
+ verticalSpeedLimitKPH:r=120.0
+ }
+ 
+ gunStabilizer{
+ hasVerticalGunFreeMode:b=yes
+ hasHorizontal:b=yes
+ horizontalOmegaMult:r=1.0
+ horizontalSpeedLimitKPH:r=120.0
+ hasVertical:b=yes
+ verticalOmegaMult:r=1.0
+ verticalSpeedLimitKPH:r=120.0
+ }
```

  **Removed**:
```diff
```


- **aces.vromfs.bin_u/gamedata/units/ships/ussr_pr_191.blkx**:

  **Added**:
```diff
+ 
+ gunStabilizer{
+ hasVerticalGunFreeMode:b=yes
+ hasHorizontal:b=yes
+ horizontalOmegaMult:r=1.0
+ horizontalSpeedLimitKPH:r=80.0
+ hasVertical:b=yes
+ verticalOmegaMult:r=1.0
+ verticalSpeedLimitKPH:r=80.0
+ }
```

  **Removed**:
```diff
```


- **aces.vromfs.bin_u/gamedata/units/ships/ussr_pr_191m.blkx**:

  **Added**:
```diff
+ 
+ gunStabilizer{
+ hasVerticalGunFreeMode:b=yes
+ hasHorizontal:b=yes
+ horizontalOmegaMult:r=1.0
+ horizontalSpeedLimitKPH:r=80.0
+ hasVertical:b=yes
+ verticalOmegaMult:r=1.0
+ verticalSpeedLimitKPH:r=80.0
+ }
```

  **Removed**:
```diff
```


- **aces.vromfs.bin_u/gamedata/units/tankmodels/cn_antelope_tc_1l_ads.blkx**:

  **Added**:
```diff
+ tier:i=2
```

  **Removed**:
```diff
```


- **aces.vromfs.bin_u/gamedata/units/tankmodels/il_mim_72_chaparral.blkx**:

  **Added**:
```diff
+ tier:i=3
+ tier:i=2
```

  **Removed**:
```diff
```


- **aces.vromfs.bin_u/gamedata/units/tankmodels/jp_type_81_tansam.blkx**:

  **Added**:
```diff
+ tier:i=2
```

  **Removed**:
```diff
```


- **aces.vromfs.bin_u/gamedata/units/tankmodels/us_mim_72_chaparral.blkx**:

  **Added**:
```diff
+ tier:i=2
```

  **Removed**:
```diff
```


- **aces.vromfs.bin_u/gamedata/weapons/cannonho203.blkx**:

  **Added**:
```diff
+ explosiveType:t="rdx"
```

  **Removed**:
```diff
- explosiveType:t="tnt"
```


- **aces.vromfs.bin_u/gamedata/weapons/cannonmk214a.blkx**:

  **Added**:
```diff
+ maxDeltaAngle:r=0.12
+ maxDeltaAngle:r=0.14
```

  **Removed**:
```diff
- maxDeltaAngle:r=0.42
- maxDeltaAngle:r=0.75
```


- **aces.vromfs.bin_u/gamedata/weapons/groundmodels_weapons/152mm_mim146.blkx**:

  **Added**:
```diff
+ CxK:r=0.83
+ timeFire:r=3.17
+ force:r=14655.0
+ startSpeed:r=35.0
+ endSpeed:r=1065.0
+ crossDistToReqCrossVelMult:r=2.75
+ reqCrossVelRationMax:r=0.75
+ velDiffToReqAccelMult:r=17.5
+ velFrameReference:b=yes
+ baseIndSpeed:r=1800.0
+ accelControlProp:r=0.0131
+ accelControlDiff:r=0.0003
+ distance:r=8.5
+ damage:r=900.0
```

  **Removed**:
```diff
- CxK:r=0.975
- timeFire:r=2.0
- force:r=22540.0
- startSpeed:r=0.0
- endSpeed:r=1027.0
- spawnExplosionWreckage:b=no
- timeToGain3:p2=5.0, 0.9
- timeToGain4:p2=11.0, 0.6
- timeToGain5:p2=18.0, 0.4
- crossDistToReqCrossVelMult:r=9.0
- reqCrossVelRationMax:r=0.45
- velDiffToReqAccelMult:r=5.5
- accelControlProp:r=0.0146
- accelControlDiff:r=0.0002
- distance:r=5.5
- damage:r=600.0
```


- **aces.vromfs.bin_u/gamedata/weapons/groundmodels_weapons/152mm_mim146_launcher_user_cannon.blkx**:

  **Added**:
```diff
+ CxK:r=0.83
+ timeFire:r=3.17
+ force:r=14655.0
+ startSpeed:r=35.0
+ endSpeed:r=1065.0
+ crossDistToReqCrossVelMult:r=2.75
+ reqCrossVelRationMax:r=0.75
+ velDiffToReqAccelMult:r=17.5
+ velFrameReference:b=yes
+ baseIndSpeed:r=1800.0
+ accelControlProp:r=0.0131
+ accelControlDiff:r=0.0003
+ distance:r=8.5
+ damage:r=900.0
+ CxK:r=0.83
+ timeFire:r=3.17
+ force:r=14655.0
+ startSpeed:r=35.0
+ endSpeed:r=1065.0
+ crossDistToReqCrossVelMult:r=2.75
+ reqCrossVelRationMax:r=0.75
+ velDiffToReqAccelMult:r=17.5
+ velFrameReference:b=yes
+ baseIndSpeed:r=1800.0
+ accelControlProp:r=0.0131
+ accelControlDiff:r=0.0003
+ distance:r=8.5
+ damage:r=900.0
```

  **Removed**:
```diff
- CxK:r=0.975
- timeFire:r=2.0
- force:r=22540.0
- startSpeed:r=0.0
- endSpeed:r=1027.0
- spawnExplosionWreckage:b=no
- timeToGain3:p2=5.0, 0.9
- timeToGain4:p2=11.0, 0.6
- timeToGain5:p2=18.0, 0.4
- crossDistToReqCrossVelMult:r=9.0
- reqCrossVelRationMax:r=0.45
- velDiffToReqAccelMult:r=5.5
- accelControlProp:r=0.0146
- accelControlDiff:r=0.0002
- distance:r=5.5
- damage:r=600.0
- CxK:r=0.975
- timeFire:r=2.0
- force:r=22540.0
- startSpeed:r=0.0
- endSpeed:r=1027.0
- spawnExplosionWreckage:b=no
- timeToGain3:p2=5.0, 0.9
- timeToGain4:p2=11.0, 0.6
- timeToGain5:p2=18.0, 0.4
- crossDistToReqCrossVelMult:r=9.0
- reqCrossVelRationMax:r=0.45
- velDiffToReqAccelMult:r=5.5
- accelControlProp:r=0.0146
- accelControlDiff:r=0.0002
- distance:r=5.5
- damage:r=600.0
```


- **aces.vromfs.bin_u/gamedata/weapons/rocketguns/fr_r_550_magic_2.blkx**:

  **Added**:
```diff
+ timeFire:r=2.0
+ force:r=27950.0
```

  **Removed**:
```diff
- timeFire:r=2.2
- force:r=25000.0
```


- **aces.vromfs.bin_u/gamedata/weapons/rocketguns/fr_r_550_magic_2_default.blkx**:

  **Added**:
```diff
+ timeFire:r=2.0
+ force:r=27950.0
```

  **Removed**:
```diff
- timeFire:r=2.2
- force:r=25000.0
```


- **aces.vromfs.bin_u/gamedata/weapons/rocketguns/us_agm_119a_penguin.blkx**:

  **Added**:
```diff
+ rocketGun:b=yes
+ preset_cost:i=20
+ bullets:i=1
+ shotFreq:r=1000.25
+ sound:t="weapon.rocketgun_132"
+ helicopterGroup:i=2
+ mesh:t="us_agm_119a_penguin_missile"
+ 
+ tags{
+ }
+ 
+ rocket{
+ bulletName:t="us_agm_119a_penguin_missile"
+ statType:t="hydra"
+ caliber:r=0.28
+ length:r=3.2
+ CxK:r=1.95
+ wingAreaMult:r=3.25
+ finsAoaHor:r=0.2
+ finsAoaVer:r=0.2
+ distFromCmToStab:r=0.15
+ mass:r=370.0
+ massEnd:r=290.0
+ timeFire:r=120.0
+ force:r=1400.0
+ fireDelay:r=1.0
+ timeLife:r=200.0
+ useStartSpeed:b=yes
+ startSpeed:r=0.0
+ machMax:r=0.9
+ endSpeed:r=0.0
+ maxDistance:r=55000.0
+ minDistance:r=5000.0
+ rangeMax:r=55000.0
+ launchZoneDistance:r=200.0
+ guidanceType:t="ir"
+ rollStabilization:b=yes
+ rollStabilizationDelay:r=1.0
+ dragCx:r=0.025
+ normalizationPreset:t="heat"
+ ricochetPreset:t="he"
+ groundRicochetPreset:t="he_ground"
+ secondaryShattersPreset:t="ap_rocket"
+ stabilityThreshold:r=0.05
+ stabilityCaliberToArmorThreshold:r=5.0
+ stabilityReductionAfterRicochet:r=0.5
+ stabilityReductionAfterPenetration:r=0.15
+ bulletType:t="rocket_tank"
+ slopeEffectPreset:t="ap"
+ fresnel:p3=0.23, 0.1, 2.0
+ explodeOnRendinst:b=yes
+ useEffectiveArmorThicknessForShatter:b=yes
+ explosiveType:t="comp_h6"
+ explosiveMass:r=43.0
+ fuseDelayDist:r=4.0
+ fuseDelayDist:r=0.1
+ maxDeltaAngle:r=0.02
+ spawnExplosionFx:b=no
+ explosionEffect:t="explosion_midair_rocket_big"
+ groundCollisionEffect:t="bomb_expl_200kg"
+ ricochetEffect:t="hit_59_80mm_metal_ap"
+ waterCollisionEffect:t="hit_59_80mm_water"
+ explosionPatchRadius:r=8.0
+ waterRicochetEffect:t="hit_81_105mm_water_ap"
+ groundRicochetEffect:t="hit_81_105mm_dirt_ap"
+ visualShattersWaterOffset:r=1.2
+ visualShattersGroundOffset:r=1.2
+ distanceFuse:b=no
+ effectOffset:p3=-1.9, 0.0, 0.0
+ rendinstDamageRadius:r=9.0
+ hitPowerMult:r=400.0
+ explodeTreshold:r=0.1
+ fireEffect:t="fires_exhaust_jet_early_med"
+ smokeEffect:t="smoke_rocket_tail_light_big"
+ smokeEffect2:t=""
+ hazeEffect:t="haze_missile"
+ endSmokeViscosity:r=0.05
+ price:r=3000.0
+ amountPerTier:r=1.0
+ iconType:t="missile_air_to_uni"
+ 
+ arcadeProp{
+ finsAoaHor:r=0.25
+ finsAoaVer:r=0.25
+ }
+ 
+ guidance{
+ warmUpTime:r=1.0
+ acquisitionTime:r=0.1
+ workTime:r=3600.0
+ useTrippleClickLockInTpv:b=yes
+ applyExtraDifficultyParameters:b=yes
+ uncageBeforeLaunch:b=yes
+ inertialNavigation:b=yes
+ breakLockMaxTime:r=200.0
+ 
+ irSeeker{
+ visibilityType:t="infraRed"
+ rangeBand0:r=2500.0
+ rangeBand1:r=2500.0
+ rangeMax:r=50000.0
+ rangeSurface:r=50000.0
+ fov:r=1.0
+ gateWidth:r=0.1
+ minAngleToSun:r=0.0
+ lockAngleMax:r=40.0
+ angleMax:r=45.0
+ rateMax:r=15.0
+ prolongationTimeMax:r=1.0
+ designationSourceTypeMask:i=1
+ constantDesignationSourceTypeMask:i=0
+ groundVehiclesAsTarget:b=yes
+ aircraftAsTarget:b=no
+ surfaceAsTarget:b=yes
+ boundaryTrack:b=yes
+ filterAlpha:r=0.85
+ filterBetta:r=0.2
+ }
+ 
+ guidanceAutopilot{
+ timeOut:r=0.1
+ loftEnabled:b=yes
+ loftElevation:r=2.0
+ loftTargetElevation:r=-10.0
+ loftAngleToAccelMult:r=8.0
+ loftTargetOmegaMax:r=0.425
+ baseIndSpeed:r=1800.0
+ propNavMult:r=4.0
+ reqAccelMax:r=2.5
+ accelControlProp:r=0.0836
+ accelControlIntg:r=0.0665
+ accelControlIntgLim:r=1.0
+ accelControlDiff:r=0.0003
+ }
+ }
+ 
+ pressureDamage{
+ damageType:t="pressure"
+ }
+ 
+ stabilityRicochetModifier{
+ mod1:p2=0.0, 0.5
+ mod2:p2=20.0, 0.6
+ mod3:p2=30.0, 1.0
+ }
+ 
+ damage{
+ 
+ explosive{
+ offset:r=1.0
+ }
+ }
+ 
+ shatterDamage{
+ breachConeAngle:r=45.0
+ }
+ 
+ armorpower{
+ ArmorPower0m:p2=90.0, 10.0
+ ArmorPower50000m:p2=90.0, 50000.0
+ ArmorPower60000m:p2=70.0, 60000.0
+ }
+ 
+ hitpower{
+ HitPower0m:p2=400.0, 500.0
+ HitPower20000m:p2=400.0, 20000.0
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


- **aces.vromfs.bin_u/levels/air_africa_desert.blkx**:

  **Added**:
```diff
+ weatherTypes:t="gameData/environments/weather_types_air.blk"
```

  **Removed**:
```diff
- weatherTypes:t="gameData/environments/weather_types.blk"
```


- **aces.vromfs.bin_u/levels/air_denmark.blkx**:

  **Added**:
```diff
+ weatherTypes:t="gameData/environments/weather_types_air.blk"
```

  **Removed**:
```diff
- weatherTypes:t="gameData/environments/weather_types.blk"
```


- **aces.vromfs.bin_u/levels/air_equatorial_island.blkx**:

  **Added**:
```diff
+ weatherTypes:t="gameData/environments/weather_types_air.blk"
```

  **Removed**:
```diff
- weatherTypes:t="gameData/environments/weather_types.blk"
```


- **aces.vromfs.bin_u/levels/air_israel.blkx**:

  **Added**:
```diff
+ weatherTypes:t="gameData/environments/weather_types_air.blk"
```

  **Removed**:
```diff
- weatherTypes:t="gameData/environments/weather_types.blk"
```


- **aces.vromfs.bin_u/levels/air_kamchatka.blkx**:

  **Added**:
```diff
+ weatherTypes:t="gameData/environments/weather_types_air.blk"
```

  **Removed**:
```diff
- weatherTypes:t="gameData/environments/weather_types.blk"
```


- **aces.vromfs.bin_u/levels/air_mysterious_valley.blkx**:

  **Added**:
```diff
+ weatherTypes:t="gameData/environments/weather_types_air.blk"
```

  **Removed**:
```diff
- weatherTypes:t="gameData/environments/weather_types.blk"
```


- **aces.vromfs.bin_u/levels/air_normandy.blkx**:

  **Added**:
```diff
+ weatherTypes:t="gameData/environments/weather_types_air.blk"
```

  **Removed**:
```diff
- weatherTypes:t="gameData/environments/weather_types.blk"
```


- **aces.vromfs.bin_u/levels/air_race_africa_canyon.blkx**:

  **Added**:
```diff
+ weatherTypes:t="gameData/environments/weather_types_air.blk"
```

  **Removed**:
```diff
- weatherTypes:t="gameData/environments/weather_types.blk"
```


- **aces.vromfs.bin_u/levels/air_race_phiphi_islands.blkx**:

  **Added**:
```diff
+ weatherTypes:t="gameData/environments/weather_types_air.blk"
```

  **Removed**:
```diff
- weatherTypes:t="gameData/environments/weather_types.blk"
```


- **aces.vromfs.bin_u/levels/air_skyscraper_city.blkx**:

  **Added**:
```diff
+ weatherTypes:t="gameData/environments/weather_types_air.blk"
```

  **Removed**:
```diff
- weatherTypes:t="gameData/environments/weather_types.blk"
```


- **aces.vromfs.bin_u/levels/air_smolensk.blkx**:

  **Added**:
```diff
+ weatherTypes:t="gameData/environments/weather_types_air.blk"
```

  **Removed**:
```diff
- weatherTypes:t="gameData/environments/weather_types.blk"
```


- **aces.vromfs.bin_u/levels/air_south_eastern_city.blkx**:

  **Added**:
```diff
+ weatherTypes:t="gameData/environments/weather_types_air.blk"
```

  **Removed**:
```diff
- weatherTypes:t="gameData/environments/weather_types.blk"
```


- **aces.vromfs.bin_u/levels/air_vietnam.blkx**:

  **Added**:
```diff
+ weatherTypes:t="gameData/environments/weather_types_air.blk"
```

  **Removed**:
```diff
- weatherTypes:t="gameData/environments/weather_types.blk"
```


- **aces.vromfs.bin_u/levels/arcade_africa_canyon.blkx**:

  **Added**:
```diff
+ weatherTypes:t="gameData/environments/weather_types_air.blk"
```

  **Removed**:
```diff
- weatherTypes:t="gameData/environments/weather_types.blk"
```


- **aces.vromfs.bin_u/levels/arcade_africa_seashore.blkx**:

  **Added**:
```diff
+ weatherTypes:t="gameData/environments/weather_types_air.blk"
```

  **Removed**:
```diff
- weatherTypes:t="gameData/environments/weather_types.blk"
```


- **aces.vromfs.bin_u/levels/arcade_alps.blkx**:

  **Added**:
```diff
+ weatherTypes:t="gameData/environments/weather_types_air.blk"
```

  **Removed**:
```diff
- weatherTypes:t="gameData/environments/weather_types.blk"
```


- **aces.vromfs.bin_u/levels/arcade_canyon_snow.blkx**:

  **Added**:
```diff
+ weatherTypes:t="gameData/environments/weather_types_air.blk"
```

  **Removed**:
```diff
- weatherTypes:t="gameData/environments/weather_types.blk"
```


- **aces.vromfs.bin_u/levels/arcade_ireland.blkx**:

  **Added**:
```diff
+ weatherTypes:t="gameData/environments/weather_types_air.blk"
```

  **Removed**:
```diff
- weatherTypes:t="gameData/environments/weather_types.blk"
```


- **aces.vromfs.bin_u/levels/arcade_mediterranean.blkx**:

  **Added**:
```diff
+ weatherTypes:t="gameData/environments/weather_types_air.blk"
```

  **Removed**:
```diff
- weatherTypes:t="gameData/environments/weather_types.blk"
```


- **aces.vromfs.bin_u/levels/arcade_norway_fjords.blkx**:

  **Added**:
```diff
+ weatherTypes:t="gameData/environments/weather_types_air.blk"
```

  **Removed**:
```diff
- weatherTypes:t="gameData/environments/weather_types.blk"
```


- **aces.vromfs.bin_u/levels/arcade_norway_green.blkx**:

  **Added**:
```diff
+ weatherTypes:t="gameData/environments/weather_types_air.blk"
```

  **Removed**:
```diff
- weatherTypes:t="gameData/environments/weather_types.blk"
```


- **aces.vromfs.bin_u/levels/arcade_norway_plain.blkx**:

  **Added**:
```diff
+ weatherTypes:t="gameData/environments/weather_types_air.blk"
```

  **Removed**:
```diff
- weatherTypes:t="gameData/environments/weather_types.blk"
```


- **aces.vromfs.bin_u/levels/arcade_phiphi_crater.blkx**:

  **Added**:
```diff
+ weatherTypes:t="gameData/environments/weather_types_air.blk"
```

  **Removed**:
```diff
- weatherTypes:t="gameData/environments/weather_types.blk"
```


- **aces.vromfs.bin_u/levels/arcade_phiphi_crater_rocks.blkx**:

  **Added**:
```diff
+ weatherTypes:t="gameData/environments/weather_types_air.blk"
```

  **Removed**:
```diff
- weatherTypes:t="gameData/environments/weather_types.blk"
```


- **aces.vromfs.bin_u/levels/arcade_rice_terraces.blkx**:

  **Added**:
```diff
+ weatherTypes:t="gameData/environments/weather_types_air.blk"
```

  **Removed**:
```diff
- weatherTypes:t="gameData/environments/weather_types.blk"
```


- **aces.vromfs.bin_u/levels/arcade_snow_rocks.blkx**:

  **Added**:
```diff
+ weatherTypes:t="gameData/environments/weather_types_air.blk"
```

  **Removed**:
```diff
- weatherTypes:t="gameData/environments/weather_types.blk"
```


- **aces.vromfs.bin_u/levels/arcade_zhang_park.blkx**:

  **Added**:
```diff
+ weatherTypes:t="gameData/environments/weather_types_air.blk"
```

  **Removed**:
```diff
- weatherTypes:t="gameData/environments/weather_types.blk"
```


- **aces.vromfs.bin_u/levels/avg_sector_montmedy_snow.blkx**:

  **Added**:
```diff
+ max_wind_strength:r=2.0
```

  **Removed**:
```diff
```


- **aces.vromfs.bin_u/levels/berlin.blkx**:

  **Added**:
```diff
+ weatherTypes:t="gameData/environments/weather_types_air.blk"
```

  **Removed**:
```diff
- weatherTypes:t="gameData/environments/weather_types.blk"
```


- **aces.vromfs.bin_u/levels/britain.blkx**:

  **Added**:
```diff
+ weatherTypes:t="gameData/environments/weather_types_air.blk"
```

  **Removed**:
```diff
- weatherTypes:t="gameData/environments/weather_types.blk"
```


- **aces.vromfs.bin_u/levels/caribbean_islands.blkx**:

  **Added**:
```diff
+ weatherTypes:t="gameData/environments/weather_types_air.blk"
```

  **Removed**:
```diff
- weatherTypes:t="gameData/environments/weather_types.blk"
```


- **aces.vromfs.bin_u/levels/guam.blkx**:

  **Added**:
```diff
+ weatherTypes:t="gameData/environments/weather_types_air.blk"
```

  **Removed**:
```diff
- weatherTypes:t="gameData/environments/weather_types.blk"
```


- **aces.vromfs.bin_u/levels/honolulu.blkx**:

  **Added**:
```diff
+ weatherTypes:t="gameData/environments/weather_types_air.blk"
```

  **Removed**:
```diff
- weatherTypes:t="gameData/environments/weather_types.blk"
```


- **aces.vromfs.bin_u/levels/hurtgen.blkx**:

  **Added**:
```diff
+ weatherTypes:t="gameData/environments/weather_types_air.blk"
```

  **Removed**:
```diff
- weatherTypes:t="gameData/environments/weather_types.blk"
```


- **aces.vromfs.bin_u/levels/iwo_jima.blkx**:

  **Added**:
```diff
+ weatherTypes:t="gameData/environments/weather_types_air.blk"
```

  **Removed**:
```diff
- weatherTypes:t="gameData/environments/weather_types.blk"
```


- **aces.vromfs.bin_u/levels/khalkhin_gol.blkx**:

  **Added**:
```diff
+ weatherTypes:t="gameData/environments/weather_types_air.blk"
```

  **Removed**:
```diff
- weatherTypes:t="gameData/environments/weather_types.blk"
```


- **aces.vromfs.bin_u/levels/korea.blkx**:

  **Added**:
```diff
+ weatherTypes:t="gameData/environments/weather_types_air.blk"
```

  **Removed**:
```diff
- weatherTypes:t="gameData/environments/weather_types.blk"
```


- **aces.vromfs.bin_u/levels/krymsk.blkx**:

  **Added**:
```diff
+ weatherTypes:t="gameData/environments/weather_types_air.blk"
```

  **Removed**:
```diff
- weatherTypes:t="gameData/environments/weather_types.blk"
```


- **aces.vromfs.bin_u/levels/kursk.blkx**:

  **Added**:
```diff
+ weatherTypes:t="gameData/environments/weather_types_air.blk"
```

  **Removed**:
```diff
- weatherTypes:t="gameData/environments/weather_types.blk"
```


- **aces.vromfs.bin_u/levels/moscow.blkx**:

  **Added**:
```diff
+ weatherTypes:t="gameData/environments/weather_types_air.blk"
```

  **Removed**:
```diff
- weatherTypes:t="gameData/environments/weather_types.blk"
```


- **aces.vromfs.bin_u/levels/mozdok.blkx**:

  **Added**:
```diff
+ weatherTypes:t="gameData/environments/weather_types_air.blk"
```

  **Removed**:
```diff
- weatherTypes:t="gameData/environments/weather_types.blk"
```


- **aces.vromfs.bin_u/levels/norway.blkx**:

  **Added**:
```diff
+ weatherTypes:t="gameData/environments/weather_types_air.blk"
```

  **Removed**:
```diff
- weatherTypes:t="gameData/environments/weather_types.blk"
```


- **aces.vromfs.bin_u/levels/peleliu.blkx**:

  **Added**:
```diff
+ weatherTypes:t="gameData/environments/weather_types_air.blk"
```

  **Removed**:
```diff
- weatherTypes:t="gameData/environments/weather_types.blk"
```


- **aces.vromfs.bin_u/levels/ruhr.blkx**:

  **Added**:
```diff
+ weatherTypes:t="gameData/environments/weather_types_air.blk"
```

  **Removed**:
```diff
- weatherTypes:t="gameData/environments/weather_types.blk"
```


- **aces.vromfs.bin_u/levels/sector_montmedy.blkx**:

  **Added**:
```diff
+ weatherTypes:t="gameData/environments/weather_types_air.blk"
```

  **Removed**:
```diff
- weatherTypes:t="gameData/environments/weather_types.blk"
```


- **aces.vromfs.bin_u/levels/sicily.blkx**:

  **Added**:
```diff
+ weatherTypes:t="gameData/environments/weather_types_air.blk"
```

  **Removed**:
```diff
- weatherTypes:t="gameData/environments/weather_types.blk"
```


- **aces.vromfs.bin_u/levels/spain.blkx**:

  **Added**:
```diff
+ weatherTypes:t="gameData/environments/weather_types_air.blk"
```

  **Removed**:
```diff
- weatherTypes:t="gameData/environments/weather_types.blk"
```


- **aces.vromfs.bin_u/levels/stalingrad.blkx**:

  **Added**:
```diff
+ weatherTypes:t="gameData/environments/weather_types_air.blk"
```

  **Removed**:
```diff
- weatherTypes:t="gameData/environments/weather_types.blk"
```


- **aces.vromfs.bin_u/levels/tunisia.blkx**:

  **Added**:
```diff
+ weatherTypes:t="gameData/environments/weather_types_air.blk"
```

  **Removed**:
```diff
- weatherTypes:t="gameData/environments/weather_types.blk"
```


- **aces.vromfs.bin_u/levels/wake_island.blkx**:

  **Added**:
```diff
+ weatherTypes:t="gameData/environments/weather_types_air.blk"
```

  **Removed**:
```diff
- weatherTypes:t="gameData/environments/weather_types.blk"
```


- **aces.vromfs.bin_u/levels/water.blkx**:

  **Added**:
```diff
+ weatherTypes:t="gameData/environments/weather_types_air.blk"
```

  **Removed**:
```diff
- weatherTypes:t="gameData/environments/weather_types.blk"
```


- **aces.vromfs.bin_u/levels/zhengzhou.blkx**:

  **Added**:
```diff
+ weatherTypes:t="gameData/environments/weather_types_air.blk"
```

  **Removed**:
```diff
- weatherTypes:t="gameData/environments/weather_types.blk"
```


---
