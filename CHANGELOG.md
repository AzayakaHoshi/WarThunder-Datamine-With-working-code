### Full Changelog:

- **aces.vromfs.bin_u/config/sound_studio.blkx**:

  **Added**:
```diff
+ country_colombia:t="Spanish"
```

  **Removed**:
```diff
```


- **aces.vromfs.bin_u/gamedata/attachables/christmas_gnome_girl.blkx**:

  **Added**:
```diff
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
- bboxMult:r=0.1
```


- **aces.vromfs.bin_u/gamedata/attachables/decor_hut_on_chicken_legs.blkx**:

  **Added**:
```diff
+ breakFx:t="destruction_decorators_model_small"
+ mass:r=15.0
+ }
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
```

  **Removed**:
```diff
```


- **aces.vromfs.bin_u/gamedata/attachables/decor_nutcraker.blkx**:

  **Added**:
```diff
+ animVarName:t="play_timer_anim"
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
- animVarName:t="play_timer_anim"
```


- **aces.vromfs.bin_u/gamedata/flightmodels/fm/f_15a.blkx**:

  **Added**:
```diff
+ UseTime:r=5.0
+ Power:r=2500.0
```

  **Removed**:
```diff
- UseTime:r=0.0
- Power:r=0.0
```


- **aces.vromfs.bin_u/gamedata/flightmodels/fm/f_15c_baz_msip.blkx**:

  **Added**:
```diff
+ UseTime:r=5.0
+ Power:r=2500.0
```

  **Removed**:
```diff
- UseTime:r=0.0
- Power:r=0.0
```


- **aces.vromfs.bin_u/gamedata/flightmodels/fm/f_15c_msip2.blkx**:

  **Added**:
```diff
+ UseTime:r=5.0
+ Power:r=2500.0
```

  **Removed**:
```diff
- UseTime:r=0.0
- Power:r=0.0
```


- **aces.vromfs.bin_u/gamedata/flightmodels/fm/f_15e.blkx**:

  **Added**:
```diff
+ UseTime:r=5.0
+ Power:r=2500.0
```

  **Removed**:
```diff
- UseTime:r=0.0
- Power:r=0.0
```


- **aces.vromfs.bin_u/gamedata/flightmodels/fm/f_15i_raam.blkx**:

  **Added**:
```diff
+ UseTime:r=5.0
+ Power:r=2500.0
```

  **Removed**:
```diff
- UseTime:r=0.0
- Power:r=0.0
```


- **aces.vromfs.bin_u/gamedata/flightmodels/fm/f_15j.blkx**:

  **Added**:
```diff
+ UseTime:r=5.0
+ Power:r=2500.0
```

  **Removed**:
```diff
- UseTime:r=0.0
- Power:r=0.0
```


- **aces.vromfs.bin_u/gamedata/flightmodels/fm/f_15j_kai.blkx**:

  **Added**:
```diff
+ UseTime:r=5.0
+ Power:r=2500.0
```

  **Removed**:
```diff
- UseTime:r=0.0
- Power:r=0.0
```


- **aces.vromfs.bin_u/gamedata/flightmodels/kfir_c10_colombia.blkx**:

  **Added**:
```diff
+ hmdBlockIlsArea:p4=0.47, -0.8, 0.55, 0.6
+ mfdTextureSize:ip2=1024, 1024
+ scale:r=0.85
+ blk:t="gameData/sensors/il_el_m_2052.blk"
+ preset{
+ name:t="kfir_c10_colombia_mk118"
+ blk:t="gameData/FlightModels/weaponPresets/kfir_c10_colombia_mk118.blk"
+ }
+ 
+ WeaponPreset{
+ iconType:t="bombs_heavy"
+ name:t="us_m118"
+ reqModification:t="us_3000lb_mk118"
+ 
+ Weapon{
+ trigger:t="bombs"
+ blk:t="gameData/Weapons/containers/pylon_kfir_central_us_3000lb_m118.blk"
+ emitter:t="pylon_central_3000lb"
+ bullets:i=1
+ external:b=yes
+ separate:b=yes
+ machLimit:r=1.01
+ }
+ }
+ 
+ us_3000lb_mk118{
+ modClass:t="weapon"
+ tier:i=4
+ prevModification:t="f4c_zuni"
+ reqModification:t="us_2000lb_mk84"
+ }
+ 
```

  **Removed**:
```diff
- hmdBlockIlsArea:p4=0.47, 0.4, 0.55, 0.6
- scale:r=1.0
- blk:t="gameData/sensors/il_el_m_2032.blk"
```


- **aces.vromfs.bin_u/gamedata/flightmodels/rafale_c_f3.blkx**:

  **Added**:
```diff
+ hmdRafale:b=yes
```

  **Removed**:
```diff
- hmdA10c:b=yes
```


- **aces.vromfs.bin_u/gamedata/flightmodels/saab_jas39a.blkx**:

  **Added**:
```diff
+ hmdBlockIlsArea:p4=0.15, 0.01, 0.73, 0.85
```

  **Removed**:
```diff
```


- **aces.vromfs.bin_u/gamedata/flightmodels/weaponpresets/kfir_c10_colombia_mk118.blkx**:

  **Added**:
```diff
+ Weapon{
+ slot:i=5
+ preset:t="us_m118"
+ }
```

  **Removed**:
```diff
```


- **aces.vromfs.bin_u/gamedata/sensors/il_el_m_2052.blkx**:

  **Added**:
```diff
+ type:t="radar"
+ name:t="ELTA EL/M-2052"
+ showMissileLaunchZone:b=yes
+ showMissileDgftLaunchZone:b=yes
+ weaponTargetsMax:i=4
+ launchedMissilesPredictedPositionsMax:i=4
+ 
+ transivers{
+ 
+ mprf{
+ sideLobesAttenuation:r=-20.0
+ power:r=1000.0
+ band:i=8
+ rcs:r=5.0
+ range:r=100000.0
+ rangeMax:r=150000.0
+ multipathEffect:p4=0.0, 1.0, 60.0, 0.0
+ 
+ antenna{
+ 
+ azimuth{
+ angleHalfSens:r=1.8
+ sideLobesSensitivity:r=-35.0
+ }
+ 
+ elevation{
+ angleHalfSens:r=2.7
+ sideLobesSensitivity:r=-35.0
+ }
+ }
+ }
+ 
+ hprf{
+ sideLobesAttenuation:r=-20.0
+ power:r=1000.0
+ band:i=8
+ rcs:r=5.0
+ range:r=120000.0
+ rangeMax:r=170000.0
+ multipathEffect:p4=0.0, 1.0, 60.0, 0.0
+ 
+ antenna{
+ 
+ azimuth{
+ angleHalfSens:r=1.8
+ sideLobesSensitivity:r=-35.0
+ }
+ 
+ elevation{
+ angleHalfSens:r=2.7
+ sideLobesSensitivity:r=-35.0
+ }
+ }
+ }
+ 
+ GTM{
+ sideLobesAttenuation:r=-20.0
+ power:r=1000.0
+ band:i=8
+ rcs:r=40.0
+ range:r=30000.0
+ rangeMax:r=150000.0
+ multipathEffect:p4=0.0, 1.0, 60.0, 0.0
+ 
+ antenna{
+ 
+ azimuth{
+ angleHalfSens:r=1.8
+ sideLobesSensitivity:r=-50.0
+ }
+ 
+ elevation{
+ angleHalfSens:r=2.7
+ sideLobesSensitivity:r=-50.0
+ }
+ }
+ }
+ }
+ 
+ signals{
+ track:b=yes
+ 
+ mprfSearch{
+ groundClutter:b=no
+ aircraftAsTarget:b=yes
+ friendFoeId:b=yes
+ mainBeamNotchWidth:r=100.0
+ 
+ distance{
+ presents:b=yes
+ minValue:r=500.0
+ maxValue:r=150000.0
+ width:r=500.0
+ }
+ 
+ dopplerSpeed{
+ presents:b=yes
+ minValue:r=-900.0
+ maxValue:r=900.0
+ signalWidthMin:r=2.0
+ width:r=38.0
+ }
+ }
+ 
+ hprfSearch{
+ groundClutter:b=no
+ aircraftAsTarget:b=yes
+ friendFoeId:b=yes
+ mainBeamDopplerSpeed:b=yes
+ 
+ distance{
+ presents:b=yes
+ minValue:r=9000.0
+ maxValue:r=170000.0
+ width:r=3000.0
+ }
+ 
+ dopplerSpeed{
+ presents:b=yes
+ minValue:r=50.0
+ maxValue:r=1200.0
+ signalWidthMin:r=5.0
+ width:r=150.0
+ }
+ }
+ 
+ mprfTrack{
+ groundClutter:b=no
+ aircraftAsTarget:b=yes
+ angularAccuracy:r=0.05
+ distanceAccuracy:r=15.0
+ mainBeamNotchWidth:r=40.0
+ mainBeamNotchMaxElevation:r=3.5
+ track:b=yes
+ 
+ distance{
+ presents:b=yes
+ minValue:r=500.0
+ maxValue:r=150000.0
+ width:r=500.0
+ }
+ 
+ dopplerSpeed{
+ presents:b=yes
+ minValue:r=-900.0
+ maxValue:r=900.0
+ signalWidthMin:r=2.0
+ width:r=24.0
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
+ maxValue:r=170000.0
+ width:r=500.0
+ }
+ 
+ dopplerSpeed{
+ presents:b=yes
+ minValue:r=-1200.0
+ maxValue:r=1200.0
+ signalWidthMin:r=2.0
+ width:r=24.0
+ }
+ }
+ 
+ acmLock{
+ groundClutter:b=no
+ aircraftAsTarget:b=yes
+ angularAccuracy:r=0.05
+ distanceAccuracy:r=15.0
+ mainBeamNotchWidth:r=40.0
+ 
+ distance{
+ presents:b=yes
+ minValue:r=250.0
+ maxValue:r=200000.0
+ width:r=250.0
+ }
+ 
+ dopplerSpeed{
+ presents:b=yes
+ minValue:r=-900.0
+ maxValue:r=900.0
+ signalWidthMin:r=2.0
+ width:r=24.0
+ }
+ }
+ 
+ acmTrack{
+ groundClutter:b=no
+ aircraftAsTarget:b=yes
+ angularAccuracy:r=0.05
+ distanceAccuracy:r=15.0
+ mainBeamNotchWidth:r=40.0
+ mainBeamNotchMaxElevation:r=3.5
+ track:b=yes
+ 
+ distance{
+ presents:b=yes
+ minValue:r=250.0
+ maxValue:r=20000.0
+ width:r=250.0
+ }
+ 
+ dopplerSpeed{
+ presents:b=yes
+ minValue:r=-900.0
+ maxValue:r=900.0
+ signalWidthMin:r=2.0
+ width:r=24.0
+ }
+ }
+ 
+ GTMSearch{
+ groundClutter:b=no
+ aircraftAsTarget:b=no
+ groundVehiclesAsTarget:b=yes
+ angularAccuracy:r=0.0
+ distanceAccuracy:r=1.0
+ absDopplerSpeed:b=yes
+ mainBeamDopplerSpeed:b=yes
+ 
+ distance{
+ presents:b=yes
+ minValue:r=500.0
+ maxValue:r=200000.0
+ width:r=15.0
+ }
+ 
+ dopplerSpeed{
+ presents:b=yes
+ minValue:r=2.5
+ maxValue:r=1000.0
+ signalWidthMin:r=2.5
+ width:r=0.0
+ }
+ }
+ 
+ GTMTrack{
+ groundClutter:b=no
+ aircraftAsTarget:b=no
+ groundVehiclesAsTarget:b=yes
+ angularAccuracy:r=0.0
+ distanceAccuracy:r=1.0
+ absDopplerSpeed:b=yes
+ mainBeamDopplerSpeed:b=yes
+ 
+ distance{
+ presents:b=yes
+ minValue:r=500.0
+ maxValue:r=200000.0
+ width:r=15.0
+ }
+ 
+ dopplerSpeed{
+ presents:b=yes
+ minValue:r=1.5
+ maxValue:r=1000.0
+ signalWidthMin:r=2.5
+ width:r=0.0
+ }
+ }
+ }
+ 
+ illuminationTransmitter{
+ power:r=200.0
+ 
+ antenna{
+ angleHalfSens:r=10.0
+ sideLobesSensitivity:r=-30.0
+ }
+ }
+ 
+ scanPatterns{
+ 
+ searchAutoNarrow{
+ type:t="pyramide"
+ azimuthLimits:p2=-70.0, 70.0
+ elevationLimits:p2=-70.0, 70.0
+ rollStabLimit:r=90.0
+ pitchStabLimit:r=70.0
+ period:r=1.1432
+ width:r=10.0
+ barHeight:r=2.5
+ barsCount:i=8
+ rowMajor:b=yes
+ preciseMinor:b=yes
+ }
+ 
+ searchAutoMedium{
+ type:t="pyramide"
+ azimuthLimits:p2=-70.0, 70.0
+ elevationLimits:p2=-70.0, 70.0
+ rollStabLimit:r=90.0
+ pitchStabLimit:r=70.0
+ period:r=2.2047
+ width:r=20.0
+ barHeight:r=2.5
+ barsCount:i=8
+ rowMajor:b=yes
+ preciseMinor:b=yes
+ }
+ 
+ searchAutoWide{
+ type:t="pyramide"
+ azimuthLimits:p2=-70.0, 70.0
+ elevationLimits:p2=-70.0, 70.0
+ rollStabLimit:r=90.0
+ pitchStabLimit:r=70.0
+ period:r=3.8378
+ width:r=35.0
+ barHeight:r=2.5
+ barsCount:i=8
+ rowMajor:b=yes
+ preciseMinor:b=yes
+ }
+ 
+ bvrLockSearch{
+ type:t="pyramide"
+ azimuthLimits:p2=-70.0, 70.0
+ elevationLimits:p2=-70.0, 70.0
+ rollStabLimit:r=90.0
+ pitchStabLimit:r=70.0
+ period:r=0.1
+ width:r=2.0
+ barHeight:r=2.5
+ barsCount:i=6
+ rowMajor:b=yes
+ indicate:b=yes
+ }
+ 
+ bvrLockTws{
+ type:t="pyramide"
+ azimuthLimits:p2=-70.0, 70.0
+ elevationLimits:p2=-70.0, 70.0
+ rollStabLimit:r=90.0
+ pitchStabLimit:r=70.0
+ period:r=0.1
+ width:r=2.0
+ barHeight:r=2.5
+ barsCount:i=2
+ rowMajor:b=yes
+ indicate:b=yes
+ }
+ 
+ verticalLock{
+ type:t="pyramide"
+ azimuthLimits:p2=-70.0, 70.0
+ elevationLimits:p2=-70.0, 70.0
+ period:r=0.2
+ width:r=25.0
+ barHeight:r=1.5
+ barsCount:i=4
+ rowMajor:b=no
+ centerElevation:r=12.5
+ indicate:b=yes
+ }
+ 
+ boresightLock{
+ type:t="cone"
+ azimuthLimits:p2=-70.0, 70.0
+ elevationLimits:p2=-70.0, 70.0
+ period:r=0.1
+ width:r=1.5
+ indicate:b=yes
+ }
+ 
+ track{
+ type:t="no"
+ azimuthLimits:p2=-70.0, 70.0
+ elevationLimits:p2=-70.0, 70.0
+ }
+ 
+ hmdLock{
+ type:t="pyramide"
+ azimuthLimits:p2=-70.0, 70.0
+ elevationLimits:p2=-70.0, 70.0
+ period:r=0.2
+ width:r=0.75
+ barHeight:r=1.5
+ barsCount:i=2
+ rowMajor:b=yes
+ indicate:b=yes
+ hmd:b=yes
+ }
+ 
+ hmdTrack{
+ type:t="no"
+ azimuthLimits:p2=-70.0, 70.0
+ elevationLimits:p2=-70.0, 70.0
+ hmd:b=yes
+ }
+ }
+ 
+ scanPatternSets{
+ 
+ search{
+ scanPattern1:t="searchAutoMedium"
+ scanPattern2:t="searchAutoWide"
+ scanPattern3:t="searchAutoNarrow"
+ }
+ 
+ tws{
+ scanPattern1:t="searchAutoMedium"
+ scanPattern2:t="searchAutoWide"
+ scanPattern3:t="searchAutoNarrow"
+ }
+ 
+ acmLock{
+ scanPattern1:t="boresightLock"
+ scanPattern2:t="verticalLock"
+ }
+ 
+ hmdLock{
+ scanPattern1:t="hmdLock"
+ }
+ }
+ 
+ scopeRangeSets{
+ 
+ common{
+ range1:r=40000.0
+ range2:r=100000.0
+ range3:r=200000.0
+ range4:r=20000.0
+ }
+ 
+ gtm{
+ range1:r=20000.0
+ range2:r=40000.0
+ range3:r=100000.0
+ range4:r=200000.0
+ }
+ 
+ acm{
+ range1:r=20000.0
+ }
+ }
+ 
+ fsms{
+ 
+ main{
+ stateInit:t="init"
+ 
+ actionsTemplates{
+ 
+ init{
+ 
+ setEnabled{
+ value:b=no
+ }
+ 
+ setTargetDesignationRange{
+ azimuthRange:p2=-70.0, 70.0
+ azimuthWidth:r=5.0
+ elevationLimits:p2=-70.0, 70.0
+ distanceRange:p2=0.0, 170000.0
+ distanceWidth:r=2000.0
+ distanceRelWidthMin:r=0.05
+ }
+ 
+ setFsmActive{
+ fsm:t="searchModes"
+ active:b=yes
+ }
+ }
+ 
+ setStandbySearchModeCommon{
+ 
+ setCenterAzimuth{
+ source:t="constant"
+ value:r=0.0
+ }
+ 
+ setCenterElevation{
+ source:t="constant"
+ value:r=0.0
+ }
+ 
+ setScopeRangeSet{
+ scopeRangeSet:t="common"
+ }
+ 
+ setFsmActive{
+ fsm:t="searchModes"
+ active:b=yes
+ }
+ }
+ 
+ setStandbyModeCommon{
+ 
+ setStandbySearchModeCommon{
+ }
+ 
+ setEnabled{
+ value:b=no
+ }
+ }
+ 
+ resetStandbyMode{
+ 
+ setFsmActive{
+ fsm:t="searchModes"
+ active:b=no
+ }
+ }
+ 
+ resetSearchMode{
+ 
+ clearTargets{
+ }
+ 
+ setFsmActive{
+ fsm:t="search"
+ active:b=no
+ }
+ 
+ setFsmActive{
+ fsm:t="searchModes"
+ active:b=no
+ }
+ 
+ setCueEnabled{
+ value:b=no
+ }
+ }
+ 
+ setBvrLockModeCommon{
+ 
+ setEnabled{
+ value:b=yes
+ }
+ 
+ setScanPatternSet{
+ }
+ 
+ resetScanPhase{
+ }
+ }
+ 
+ setBvrLockMode{
+ 
+ setBvrLockModeCommon{
+ }
+ 
+ setFsmActive{
+ fsm:t="bvrLock"
+ active:b=yes
+ }
+ 
+ setDistGatePos{
+ source:t="targetDesignation"
+ width:r=2000.0
+ }
+ 
+ setRelSpeedGatePos{
+ source:t="constRange"
+ pos:r=0.0
+ width:r=3000.0
+ }
+ 
+ setScanPattern{
+ scanPattern:t="bvrLockSearch"
+ }
+ 
+ setCenterAzimuth{
+ source:t="targetDesignation"
+ }
+ }
+ 
+ designatedTargetSearch{
+ 
+ designateTargetUnderCue{
+ type:i=0
+ self:b=yes
+ sensorIndex:i=0
+ }
+ 
+ designateActiveDetectedTarget{
+ type:i=0
+ self:b=yes
+ sensorIndex:i=0
+ }
+ }
+ 
+ resetBvrLockMode{
+ 
+ setFsmActive{
+ fsm:t="bvrLock"
+ active:b=no
+ }
+ }
+ 
+ setTrackMode{
+ 
+ setEnabled{
+ value:b=yes
+ }
+ 
+ setScanPatternSet{
+ }
+ 
+ setScanPattern{
+ scanPattern:t="track"
+ }
+ 
+ addTargetOfInterest{
+ }
+ 
+ setLastTargetOfInterestActive{
+ }
+ 
+ updateActiveTargetOfInterest{
+ }
+ 
+ setCenterAzimuth{
+ source:t="activeTargetOfInterest"
+ }
+ 
+ setCenterElevation{
+ source:t="activeTargetOfInterest"
+ }
+ 
+ setDistGatePos{
+ source:t="activeTargetOfInterest"
+ width:r=0.0
+ }
+ 
+ setRelSpeedGatePos{
+ source:t="activeTargetOfInterest"
+ width:r=0.0
+ }
+ 
+ setFsmActive{
+ fsm:t="track"
+ active:b=yes
+ }
+ 
+ setFsmActive{
+ fsm:t="illumination"
+ active:b=yes
+ }
+ }
+ 
+ resetTrackMode{
+ 
+ clearTargetsOfInterest{
+ }
+ 
+ setFsmActive{
+ fsm:t="track"
+ active:b=no
+ }
+ 
+ setFsmActive{
+ fsm:t="illumination"
+ active:b=no
+ }
+ }
+ 
+ setAcmLockMode{
+ 
+ setEnabled{
+ value:b=yes
+ }
+ 
+ resetScanPhase{
+ }
+ 
+ setScanPatternSet{
+ scanPatternSet:t="acmLock"
+ }
+ 
+ setCenterAzimuth{
+ source:t="constant"
+ value:r=0.0
+ }
+ 
+ setCenterElevation{
+ source:t="constant"
+ value:r=0.0
+ }
+ 
+ setFsmActive{
+ fsm:t="acmLock"
+ active:b=yes
+ }
+ 
+ setDistGatePos{
+ source:t="constRange"
+ pos:r=10000.0
+ width:r=20000.0
+ }
+ 
+ setRelSpeedGatePos{
+ source:t="constRange"
+ pos:r=0.0
+ width:r=3000.0
+ }
+ 
+ setScopeRangeSet{
+ scopeRangeSet:t="acm"
+ }
+ 
+ setTransiver{
+ transiver:t="mprf"
+ }
+ 
+ setSignal{
+ signal:t="acmLock"
+ }
+ 
+ setModeName{
+ name:t="PD ACM"
+ }
+ }
+ 
+ resetAcmLockMode{
+ 
+ setFsmActive{
+ fsm:t="acmLock"
+ active:b=no
+ }
+ }
+ 
+ setHmdStandbyMode{
+ 
+ setEnabled{
+ value:b=no
+ }
+ 
+ clearTargetsOfInterest{
+ }
+ 
+ setScanPatternSet{
+ }
+ 
+ setScanPattern{
+ scanPattern:t="hmdLock"
+ }
+ 
+ resetScanPhase{
+ }
+ 
+ setDistGatePos{
+ source:t="constRange"
+ pos:r=10000.0
+ width:r=20000.0
+ }
+ 
+ setRelSpeedGatePos{
+ source:t="constRange"
+ pos:r=0.0
+ width:r=3000.0
+ }
+ 
+ setScopeRangeSet{
+ scopeRangeSet:t="acm"
+ }
+ 
+ setFsmActive{
+ fsm:t="helmetDesignation"
+ active:b=yes
+ }
+ 
+ setTransiver{
+ transiver:t="mprf"
+ }
+ 
+ setSignal{
+ signal:t="acmLock"
+ }
+ 
+ setModeName{
+ name:t="PD HMD"
+ }
+ }
+ 
+ resetHmdStandbyMode{
+ 
+ resetStandbyMode{
+ }
+ 
+ setFsmActive{
+ fsm:t="helmetDesignation"
+ active:b=no
+ }
+ }
+ 
+ setHmdLockMode{
+ 
+ setEnabled{
+ value:b=yes
+ }
+ 
+ clearTargetsOfInterest{
+ }
+ 
+ setScanPatternSet{
+ }
+ 
+ setScanPattern{
+ scanPattern:t="hmdLock"
+ }
+ 
+ resetScanPhase{
+ }
+ 
+ setDistGatePos{
+ source:t="constRange"
+ pos:r=10000.0
+ width:r=20000.0
+ }
+ 
+ setRelSpeedGatePos{
+ source:t="constRange"
+ pos:r=0.0
+ width:r=3000.0
+ }
+ 
+ setFsmActive{
+ fsm:t="acmLock"
+ active:b=yes
+ }
+ 
+ setFsmActive{
+ fsm:t="helmetDesignation"
+ active:b=yes
+ }
+ 
+ setScopeRangeSet{
+ scopeRangeSet:t="acm"
+ }
+ 
+ setTransiver{
+ transiver:t="mprf"
+ }
+ 
+ setSignal{
+ signal:t="acmLock"
+ }
+ 
+ setModeName{
+ name:t="PD HMD"
+ }
+ }
+ 
+ resetHmdLockMode{
+ 
+ resetAcmLockMode{
+ }
+ 
+ setFsmActive{
+ fsm:t="helmetDesignation"
+ active:b=no
+ }
+ }
+ 
+ setHmdTrackMode{
+ 
+ setTrackMode{
+ }
+ 
+ setScanPattern{
+ scanPattern:t="hmdTrack"
+ }
+ }
+ 
+ resetHmdTrackMode{
+ 
+ resetTrackMode{
+ }
+ }
+ 
+ setSearchStandbyModeCommon{
+ 
+ setStandbyModeCommon{
+ }
+ 
+ setScanPatternSet{
+ scanPatternSet:t="search"
+ }
+ }
+ 
+ setTwsStandbyModeCommon{
+ 
+ setStandbyModeCommon{
+ }
+ 
+ setScanPatternSet{
+ scanPatternSet:t="tws"
+ }
+ }
+ 
+ setSearchModeCommon{
+ 
+ setStandbySearchModeCommon{
+ }
+ 
+ setEnabled{
+ value:b=yes
+ }
+ 
+ setCueEnabled{
+ value:b=yes
+ updateActiveTargetUnderCue:b=no
+ }
+ 
+ setScanPatternSet{
+ scanPatternSet:t="search"
+ }
+ 
+ setFsmActive{
+ fsm:t="search"
+ active:b=yes
+ }
+ }
+ 
+ setTwsSearchModeCommon{
+ 
+ setStandbySearchModeCommon{
+ }
+ 
+ setEnabled{
+ value:b=yes
+ }
+ 
+ setCueEnabled{
+ value:b=yes
+ updateActiveTargetUnderCue:b=yes
+ }
+ 
+ setScanPatternSet{
+ scanPatternSet:t="tws"
+ }
+ 
+ setFsmActive{
+ fsm:t="tws"
+ active:b=yes
+ }
+ }
+ 
+ resetTwsMode{
+ 
+ clearTargets{
+ }
+ 
+ clearTargetsOfInterest{
+ }
+ 
+ setFsmActive{
+ fsm:t="tws"
+ active:b=no
+ }
+ 
+ setFsmActive{
+ fsm:t="searchModes"
+ active:b=no
+ }
+ 
+ setCueEnabled{
+ value:b=no
+ }
+ }
+ 
+ designatedTargetTws{
+ 
+ designateActiveDetectedTarget{
+ type:i=0
+ self:b=yes
+ sensorIndex:i=0
+ }
+ }
+ 
+ setTwsBvrLockMode{
+ 
+ setBvrLockModeCommon{
+ }
+ 
+ setFsmActive{
+ fsm:t="bvrLock"
+ active:b=yes
+ }
+ 
+ setDistGatePos{
+ source:t="targetDesignation"
+ }
+ 
+ setRelSpeedGatePos{
+ source:t="targetDesignation"
+ }
+ 
+ setScanPattern{
+ scanPattern:t="bvrLockTws"
+ }
+ 
+ setCenterAzimuth{
+ source:t="targetDesignation"
+ }
+ 
+ setCenterElevation{
+ source:t="targetDesignation"
+ }
+ 
+ setModeName{
+ name:t="TWS acquisition"
+ }
+ }
+ 
+ setMprfStandbyMode{
+ 
+ setSearchStandbyModeCommon{
+ }
+ 
+ setTransiver{
+ transiver:t="mprf"
+ }
+ 
+ setSignal{
+ signal:t="mprfSearch"
+ }
+ 
+ setModeName{
+ name:t="PD standby"
+ }
+ }
+ 
+ setHprfStandbyMode{
+ 
+ setSearchStandbyModeCommon{
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
+ setMprfTwsStandbyMode{
+ 
+ setTwsStandbyModeCommon{
+ }
+ 
+ setTransiver{
+ transiver:t="mprf"
+ }
+ 
+ setSignal{
+ signal:t="mprfSearch"
+ }
+ 
+ setModeName{
+ name:t="TWS standby"
+ }
+ }
+ 
+ setHprfTwsStandbyMode{
+ 
+ setSearchStandbyModeCommon{
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
+ setGtmStandbyMode{
+ 
+ setSearchStandbyModeCommon{
+ }
+ 
+ setTransiver{
+ transiver:t="GTM"
+ }
+ 
+ setSignal{
+ signal:t="GTMSearch"
+ }
+ 
+ setScopeRangeSet{
+ scopeRangeSet:t="gtm"
+ }
+ 
+ setModeName{
+ name:t="GTM standby"
+ }
+ }
+ 
+ setGtmTwsStandbyMode{
+ 
+ setSearchStandbyModeCommon{
+ }
+ 
+ setTransiver{
+ transiver:t="GTM"
+ }
+ 
+ setSignal{
+ signal:t="GTMSearch"
+ }
+ 
+ setScopeRangeSet{
+ scopeRangeSet:t="gtm"
+ }
+ 
+ setModeName{
+ name:t="GTM standby"
+ }
+ }
+ 
+ setMprfSearchMode{
+ 
+ setSearchModeCommon{
+ }
+ 
+ setTransiver{
+ transiver:t="mprf"
+ }
+ 
+ setSignal{
+ signal:t="mprfSearch"
+ }
+ 
+ setModeName{
+ name:t="PD search"
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
+ setMprfTwsSearchMode{
+ 
+ setTwsSearchModeCommon{
+ }
+ 
+ setTransiver{
+ transiver:t="mprf"
+ }
+ 
+ setSignal{
+ signal:t="mprfSearch"
+ }
+ 
+ setModeName{
+ name:t="TWS search"
+ }
+ }
+ 
+ setHprfTwsSearchMode{
+ 
+ setTwsSearchModeCommon{
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
+ name:t="TWS HDN search"
+ }
+ }
+ 
+ setGtmSearchMode{
+ 
+ setSearchModeCommon{
+ }
+ 
+ setTransiver{
+ transiver:t="GTM"
+ }
+ 
+ setSignal{
+ signal:t="GTMSearch"
+ }
+ 
+ setScopeRangeSet{
+ scopeRangeSet:t="gtm"
+ }
+ 
+ setModeName{
+ name:t="GTM search"
+ }
+ }
+ 
+ setGtmTwsSearchMode{
+ 
+ setTwsSearchModeCommon{
+ }
+ 
+ setTransiver{
+ transiver:t="GTM"
+ }
+ 
+ setSignal{
+ signal:t="GTMSearch"
+ }
+ 
+ setScopeRangeSet{
+ scopeRangeSet:t="gtm"
+ }
+ 
+ setModeName{
+ name:t="TWS GTM search"
+ }
+ }
+ 
+ setMprfBvrLockMode{
+ 
+ setBvrLockMode{
+ }
+ 
+ setModeName{
+ name:t="PD acquisition"
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
+ setGtmBvrLockMode{
+ 
+ setBvrLockModeCommon{
+ }
+ 
+ setFsmActive{
+ fsm:t="lock"
+ active:b=yes
+ }
+ 
+ setScanPattern{
+ scanPattern:t="bvrLockSearch"
+ }
+ 
+ setTransiver{
+ transiver:t="GTM"
+ }
+ 
+ setSignal{
+ signal:t="GTMSearch"
+ }
+ 
+ setDistGatePos{
+ source:t="targetDesignation"
+ width:r=2000.0
+ }
+ 
+ setRelSpeedGatePos{
+ source:t="constRange"
+ pos:r=0.0
+ width:r=3000.0
+ }
+ 
+ setModeName{
+ name:t="GTM acquisition"
+ }
+ }
+ 
+ setGtmTwsBvrLockMode{
+ 
+ setGtmBvrLockMode{
+ }
+ 
+ setModeName{
+ name:t="TWS GTM acquisition"
+ }
+ }
+ 
+ resetGtmBvrLockMode{
+ 
+ setFsmActive{
+ fsm:t="lock"
+ active:b=no
+ }
+ }
+ 
+ setGtmBvrTrackMode{
+ 
+ setTrackMode{
+ }
+ 
+ setTransiver{
+ transiver:t="GTM"
+ }
+ 
+ setSignal{
+ signal:t="GTMTrack"
+ }
+ }
+ 
+ setAcmTrackMode{
+ 
+ setTrackMode{
+ }
+ 
+ setTransiver{
+ transiver:t="mprf"
+ }
+ 
+ setSignal{
+ signal:t="acmTrack"
+ }
+ }
+ }
+ 
+ transitions{
+ 
+ init{
+ stateFrom:t="init"
+ event:t="init"
+ stateTo:t="standby"
+ 
+ actions{
+ 
+ init{
+ }
+ }
+ }
+ 
+ standbyToSearch{
+ stateFrom:t="standby"
+ command:t="switch"
+ event:t="enable"
+ stateTo:t="search"
+ 
+ actions{
+ 
+ doCustomActionTemplate{
+ fsm:t="main"
+ name:t="resetStandbyMode"
+ }
+ 
+ doCustomActionTemplate{
+ fsm:t="main"
+ name:t="setSearchMode"
+ }
+ }
+ }
+ 
+ searchToStandby{
+ stateFrom:t="search"
+ command:t="switch"
+ event:t="disable"
+ stateTo:t="standby"
+ 
+ actions{
+ 
+ doCustomActionTemplate{
+ fsm:t="main"
+ name:t="resetSearchMode"
+ }
+ 
+ doCustomActionTemplate{
+ fsm:t="main"
+ name:t="setStandbyMode"
+ }
+ }
+ }
+ 
+ bvrLock{
+ stateFrom:t="search"
+ command:t="selectTarget"
+ 
+ actions{
+ 
+ doCustomActionTemplate{
+ fsm:t="main"
+ name:t="designateTarget"
+ }
+ }
+ }
+ 
+ checkDesignationType0{
+ stateFrom:t="search"
+ command:t="designateTarget"
+ stateTo:t="checkDesignationType0"
+ 
+ actions{
+ 
+ checkDesignationTypeEquals{
+ value:i=0
+ }
+ }
+ }
+ 
+ bvrLockResponce{
+ stateFrom:t="checkDesignationType0"
+ event:t="designationTypeEquals"
+ stateTo:t="bvrLock"
+ 
+ actions{
+ 
+ doCustomActionTemplate{
+ fsm:t="main"
+ name:t="resetSearchMode"
+ }
+ 
+ doCustomActionTemplate{
+ fsm:t="main"
+ name:t="setBvrLockMode"
+ }
+ }
+ }
+ 
+ returnToSearchMode{
+ stateFrom:t="checkDesignationType0"
+ event:t="designationTypeNotEquals"
+ stateTo:t="search"
+ }
+ 
+ bvrLockToBvrTrack{
+ stateFrom:t="bvrLock"
+ event:t="targetDetected"
+ stateTo:t="bvrTrack"
+ 
+ actions{
+ 
+ doCustomActionTemplate{
+ fsm:t="main"
+ name:t="resetBvrLockMode"
+ }
+ 
+ doCustomActionTemplate{
+ fsm:t="main"
+ name:t="setBvrTrackMode"
+ }
+ }
+ }
+ 
+ failedBvrLock{
+ stateFrom:t="bvrLock"
+ event:t="scanFinished"
+ stateTo:t="search"
+ 
+ actions{
+ 
+ doCustomActionTemplate{
+ fsm:t="main"
+ name:t="resetBvrLockMode"
+ }
+ 
+ doCustomActionTemplate{
+ fsm:t="main"
+ name:t="setSearchMode"
+ }
+ }
+ }
+ 
+ finishedBvrTrack{
+ stateFrom:t="bvrTrack"
+ event:t="targetsOfInterestCleanup"
+ command:t="selectTarget"
+ command:t="switch"
+ stateTo:t="search"
+ 
+ actions{
+ 
+ doCustomActionTemplate{
+ fsm:t="main"
+ name:t="resetBvrTrackMode"
+ }
+ 
+ doCustomActionTemplate{
+ fsm:t="main"
+ name:t="setSearchMode"
+ }
+ }
+ }
+ 
+ finishBvrTrackAndSwitchOff{
+ stateFrom:t="bvrTrack"
+ event:t="disable"
+ stateTo:t="standby"
+ 
+ actions{
+ 
+ doCustomActionTemplate{
+ fsm:t="main"
+ name:t="resetBvrTrackMode"
+ }
+ 
+ doCustomActionTemplate{
+ fsm:t="main"
+ name:t="setStandbyMode"
+ }
+ }
+ }
+ 
+ updateStandbyMode{
+ stateFrom:t="standby"
+ event:t="fsmActivate"
+ 
+ actions{
+ 
+ doCustomActionTemplate{
+ fsm:t="main"
+ name:t="resetStandbyMode"
+ }
+ 
+ doCustomActionTemplate{
+ fsm:t="main"
+ name:t="setStandbyMode"
+ }
+ }
+ }
+ 
+ updateSearchMode{
+ stateFrom:t="search"
+ event:t="fsmActivate"
+ 
+ actions{
+ 
+ doCustomActionTemplate{
+ fsm:t="main"
+ name:t="resetSearchMode"
+ }
+ 
+ doCustomActionTemplate{
+ fsm:t="main"
+ name:t="setSearchMode"
+ }
+ }
+ }
+ 
+ switchScanPattern{
+ stateFrom:t="standby"
+ stateFrom:t="search"
+ stateFrom:t="acmLock"
+ command:t="scanPatternSwitch"
+ 
+ actions{
+ 
+ setNextScanPattern{
+ }
+ }
+ }
+ 
+ switchScopeRange{
+ command:t="rangeSwitch"
+ 
+ actions{
+ 
+ setNextScopeRange{
+ }
+ }
+ }
+ 
+ searchToAcmLock{
+ stateFrom:t="search"
+ command:t="acmSwitch"
+ stateTo:t="acmLock"
+ 
+ actions{
+ 
+ doCustomActionTemplate{
+ fsm:t="main"
+ name:t="resetSearchMode"
+ }
+ 
+ doCustomActionTemplate{
+ fsm:t="main"
+ name:t="setAcmLockMode"
+ }
+ }
+ }
+ 
+ acmLockToAcmTrack{
+ stateFrom:t="acmLock"
+ event:t="targetDetected"
+ stateTo:t="acmTrack"
+ 
+ actions{
+ 
+ doCustomActionTemplate{
+ fsm:t="main"
+ name:t="resetAcmLockMode"
+ }
+ 
+ doCustomActionTemplate{
+ fsm:t="main"
+ name:t="setAcmTrackMode"
+ }
+ }
+ }
+ 
+ acmLockToStandby{
+ stateFrom:t="acmLock"
+ command:t="selectTarget"
+ event:t="disable"
+ stateTo:t="standby"
+ 
+ actions{
+ 
+ doCustomActionTemplate{
+ fsm:t="main"
+ name:t="resetAcmLockMode"
+ }
+ 
+ doCustomActionTemplate{
+ fsm:t="main"
+ name:t="setStandbyMode"
+ }
+ }
+ }
+ 
+ acmTrackToAcmLock{
+ stateFrom:t="acmTrack"
+ event:t="targetsOfInterestCleanup"
+ stateTo:t="acmLock"
+ 
+ actions{
+ 
+ doCustomActionTemplate{
+ fsm:t="main"
+ name:t="resetAcmTrackMode"
+ }
+ 
+ doCustomActionTemplate{
+ fsm:t="main"
+ name:t="setAcmLockMode"
+ }
+ }
+ }
+ 
+ acmTrackToStandby{
+ stateFrom:t="acmTrack"
+ command:t="selectTarget"
+ event:t="disable"
+ stateTo:t="standby"
+ 
+ actions{
+ 
+ doCustomActionTemplate{
+ fsm:t="main"
+ name:t="resetAcmTrackMode"
+ }
+ 
+ doCustomActionTemplate{
+ fsm:t="main"
+ name:t="setStandbyMode"
+ }
+ }
+ }
+ 
+ acmTrackToSearch{
+ stateFrom:t="acmTrack"
+ command:t="acmSwitch"
+ command:t="switch"
+ stateTo:t="search"
+ 
+ actions{
+ 
+ doCustomActionTemplate{
+ fsm:t="main"
+ name:t="resetAcmTrackMode"
+ }
+ 
+ doCustomActionTemplate{
+ fsm:t="main"
+ name:t="setSearchMode"
+ }
+ }
+ }
+ 
+ standbyToAcmLock{
+ stateFrom:t="standby"
+ command:t="acmSwitch"
+ stateTo:t="acmLock"
+ 
+ actions{
+ 
+ doCustomActionTemplate{
+ fsm:t="main"
+ name:t="resetStandbyMode"
+ }
+ 
+ doCustomActionTemplate{
+ fsm:t="main"
+ name:t="setAcmLockMode"
+ }
+ }
+ }
+ 
+ standbyToHmdStandby{
+ stateFrom:t="standby"
+ command:t="selectTarget"
+ stateTo:t="hmdLock"
+ 
+ actions{
+ 
+ doCustomActionTemplate{
+ fsm:t="main"
+ name:t="resetStandbyMode"
+ }
+ 
+ doCustomActionTemplate{
+ fsm:t="main"
+ name:t="setHmdLockMode"
+ }
+ }
+ }
+ 
+ acmLockToHmdStandby{
+ stateFrom:t="acmLock"
+ command:t="acmSwitch"
+ stateTo:t="hmdStandby"
+ 
+ actions{
+ 
+ doCustomActionTemplate{
+ fsm:t="main"
+ name:t="resetAcmLockMode"
+ }
+ 
+ doCustomActionTemplate{
+ fsm:t="main"
+ name:t="setHmdStandbyMode"
+ }
+ }
+ }
+ 
+ hmdStandbyToSearch{
+ stateFrom:t="hmdStandby"
+ command:t="acmSwitch"
+ stateTo:t="search"
+ 
+ actions{
+ 
+ doCustomActionTemplate{
+ fsm:t="main"
+ name:t="resetHmdStandbyMode"
+ }
+ 
+ doCustomActionTemplate{
+ fsm:t="main"
+ name:t="setSearchMode"
+ }
+ }
+ }
+ 
+ hmdStandbyToHmdLock{
+ stateFrom:t="hmdStandby"
+ command:t="selectTarget"
+ stateTo:t="hmdLock"
+ 
+ actions{
+ 
+ doCustomActionTemplate{
+ fsm:t="main"
+ name:t="resetHmdStandbyMode"
+ }
+ 
+ doCustomActionTemplate{
+ fsm:t="main"
+ name:t="setHmdLockMode"
+ }
+ }
+ }
+ 
+ hmdLockToHmdTrack{
+ stateFrom:t="hmdLock"
+ event:t="targetDetected"
+ stateTo:t="hmdTrack"
+ 
+ actions{
+ 
+ doCustomActionTemplate{
+ fsm:t="main"
+ name:t="resetHmdLockMode"
+ }
+ 
+ doCustomActionTemplate{
+ fsm:t="main"
+ name:t="setHmdTrackMode"
+ }
+ }
+ }
+ 
+ hmdLockToHmdStandby{
+ stateFrom:t="hmdLock"
+ event:t="scanFinished"
+ stateTo:t="hmdStandby"
+ 
+ actions{
+ 
+ doCustomActionTemplate{
+ fsm:t="main"
+ name:t="resetHmdLockMode"
+ }
+ 
+ doCustomActionTemplate{
+ fsm:t="main"
+ name:t="setHmdStandbyMode"
+ }
+ }
+ }
+ 
+ hmdTrackToHmdStandby{
+ stateFrom:t="hmdTrack"
+ event:t="targetsOfInterestCleanup"
+ command:t="selectTarget"
+ command:t="switch"
+ stateTo:t="hmdStandby"
+ 
+ actions{
+ 
+ doCustomActionTemplate{
+ fsm:t="main"
+ name:t="resetHmdTrackMode"
+ }
+ 
+ doCustomActionTemplate{
+ fsm:t="main"
+ name:t="setHmdStandbyMode"
+ }
+ }
+ }
+ 
+ hmdTrackToStandby{
+ stateFrom:t="hmdTrack"
+ event:t="disable"
+ stateTo:t="standby"
+ 
+ actions{
+ 
+ doCustomActionTemplate{
+ fsm:t="main"
+ name:t="resetHmdTrackMode"
+ }
+ 
+ doCustomActionTemplate{
+ fsm:t="main"
+ name:t="setStandbyMode"
+ }
+ }
+ }
+ }
+ }
+ 
+ searchModes{
+ stateInit:t="init"
+ 
+ transitions{
+ 
+ initToMprf{
+ stateFrom:t="init"
+ event:t="fsmActivate"
+ stateTo:t="mprf"
+ 
+ actions{
+ 
+ setCustomActionTemplate{
+ fsm:t="main"
+ name:t="setHmdStandbyMode"
+ actionTemplateName:t="setHmdStandbyMode"
+ }
+ 
+ setCustomActionTemplate{
+ fsm:t="main"
+ name:t="resetHmdStandbyMode"
+ actionTemplateName:t="resetHmdStandbyMode"
+ }
+ 
+ setCustomActionTemplate{
+ fsm:t="main"
+ name:t="setHmdLockMode"
+ actionTemplateName:t="setHmdLockMode"
+ }
+ 
+ setCustomActionTemplate{
+ fsm:t="main"
+ name:t="resetHmdLockMode"
+ actionTemplateName:t="resetHmdLockMode"
+ }
+ 
+ setCustomActionTemplate{
+ fsm:t="main"
+ name:t="setHmdTrackMode"
+ actionTemplateName:t="setHmdTrackMode"
+ }
+ 
+ setCustomActionTemplate{
+ fsm:t="main"
+ name:t="resetHmdTrackMode"
+ actionTemplateName:t="resetHmdTrackMode"
+ }
+ 
+ setCustomActionTemplate{
+ fsm:t="main"
+ name:t="setStandbyMode"
+ actionTemplateName:t="setMprfStandbyMode"
+ }
+ 
+ setCustomActionTemplate{
+ fsm:t="main"
+ name:t="resetStandbyMode"
+ actionTemplateName:t="resetStandbyMode"
+ }
+ 
+ setCustomActionTemplate{
+ fsm:t="main"
+ name:t="setSearchMode"
+ actionTemplateName:t="setMprfSearchMode"
+ }
+ 
+ setCustomActionTemplate{
+ fsm:t="main"
+ name:t="resetSearchMode"
+ actionTemplateName:t="resetSearchMode"
+ }
+ 
+ setCustomActionTemplate{
+ fsm:t="main"
+ name:t="setBvrLockMode"
+ actionTemplateName:t="setBvrLockMode"
+ }
+ 
+ setCustomActionTemplate{
+ fsm:t="main"
+ name:t="resetBvrLockMode"
+ actionTemplateName:t="resetBvrLockMode"
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
+ name:t="setAcmLockMode"
+ actionTemplateName:t="setAcmLockMode"
+ }
+ 
+ setCustomActionTemplate{
+ fsm:t="main"
+ name:t="resetAcmLockMode"
+ actionTemplateName:t="resetAcmLockMode"
+ }
+ 
+ setCustomActionTemplate{
+ fsm:t="main"
+ name:t="setBvrTrackMode"
+ actionTemplateName:t="setTrackMode"
+ }
+ 
+ setCustomActionTemplate{
+ fsm:t="main"
+ name:t="resetBvrTrackMode"
+ actionTemplateName:t="resetTrackMode"
+ }
+ 
+ setCustomActionTemplate{
+ fsm:t="main"
+ name:t="setAcmTrackMode"
+ actionTemplateName:t="setAcmTrackMode"
+ }
+ 
+ setCustomActionTemplate{
+ fsm:t="main"
+ name:t="resetAcmTrackMode"
+ actionTemplateName:t="resetTrackMode"
+ }
+ }
+ }
+ 
+ mprfToMprfTws{
+ stateFrom:t="mprf"
+ command:t="modeSwitch"
+ stateTo:t="mprfTws"
+ 
+ actions{
+ 
+ setCustomActionTemplate{
+ fsm:t="main"
+ name:t="setStandbyMode"
+ actionTemplateName:t="setMprfTwsStandbyMode"
+ }
+ 
+ setCustomActionTemplate{
+ fsm:t="main"
+ name:t="setSearchMode"
+ actionTemplateName:t="setMprfTwsSearchMode"
+ }
+ 
+ setCustomActionTemplate{
+ fsm:t="main"
+ name:t="setBvrLockMode"
+ actionTemplateName:t="setTwsBvrLockMode"
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
+ actionTemplateName:t="resetTwsMode"
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
+ mprfTwsToHprf{
+ stateFrom:t="mprfTws"
+ command:t="modeSwitch"
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
+ actionTemplateName:t="setBvrLockMode"
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
+ hprfToHprfTws{
+ stateFrom:t="hprf"
+ command:t="modeSwitch"
+ stateTo:t="hprfTws"
+ 
+ actions{
+ 
+ setCustomActionTemplate{
+ fsm:t="main"
+ name:t="setStandbyMode"
+ actionTemplateName:t="setHprfTwsStandbyMode"
+ }
+ 
+ setCustomActionTemplate{
+ fsm:t="main"
+ name:t="setSearchMode"
+ actionTemplateName:t="setHprfTwsSearchMode"
+ }
+ 
+ setCustomActionTemplate{
+ fsm:t="main"
+ name:t="setBvrLockMode"
+ actionTemplateName:t="setTwsBvrLockMode"
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
+ actionTemplateName:t="resetTwsMode"
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
+ hprfTwsToGtm{
+ stateFrom:t="hprfTws"
+ command:t="modeSwitch"
+ stateTo:t="gtm"
+ 
+ actions{
+ 
+ setCustomActionTemplate{
+ fsm:t="main"
+ name:t="setStandbyMode"
+ actionTemplateName:t="setGtmStandbyMode"
+ }
+ 
+ setCustomActionTemplate{
+ fsm:t="main"
+ name:t="setSearchMode"
+ actionTemplateName:t="setGtmSearchMode"
+ }
+ 
+ setCustomActionTemplate{
+ fsm:t="main"
+ name:t="setBvrLockMode"
+ actionTemplateName:t="setGtmBvrLockMode"
+ }
+ 
+ setCustomActionTemplate{
+ fsm:t="main"
+ name:t="resetBvrLockMode"
+ actionTemplateName:t="resetGtmBvrLockMode"
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
+ name:t="setBvrTrackMode"
+ actionTemplateName:t="setGtmBvrTrackMode"
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
+ gtmToGtmTws{
+ stateFrom:t="gtm"
+ command:t="modeSwitch"
+ stateTo:t="gtmTws"
+ 
+ actions{
+ 
+ setCustomActionTemplate{
+ fsm:t="main"
+ name:t="setStandbyMode"
+ actionTemplateName:t="setGtmTwsStandbyMode"
+ }
+ 
+ setCustomActionTemplate{
+ fsm:t="main"
+ name:t="setSearchMode"
+ actionTemplateName:t="setGtmTwsSearchMode"
+ }
+ 
+ setCustomActionTemplate{
+ fsm:t="main"
+ name:t="setBvrLockMode"
+ actionTemplateName:t="setGtmTwsBvrLockMode"
+ }
+ 
+ setCustomActionTemplate{
+ fsm:t="main"
+ name:t="resetBvrLockMode"
+ actionTemplateName:t="resetGtmBvrLockMode"
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
+ name:t="setBvrTrackMode"
+ actionTemplateName:t="setGtmBvrTrackMode"
+ }
+ 
+ setCustomActionTemplate{
+ fsm:t="main"
+ name:t="resetSearchMode"
+ actionTemplateName:t="resetTwsMode"
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
+ gtmTwsToMprf{
+ stateFrom:t="gtmTws"
+ command:t="modeSwitch"
+ stateTo:t="mprf"
+ 
+ actions{
+ 
+ setCustomActionTemplate{
+ fsm:t="main"
+ name:t="setStandbyMode"
+ actionTemplateName:t="setMprfStandbyMode"
+ }
+ 
+ setCustomActionTemplate{
+ fsm:t="main"
+ name:t="setSearchMode"
+ actionTemplateName:t="setMprfSearchMode"
+ }
+ 
+ setCustomActionTemplate{
+ fsm:t="main"
+ name:t="setBvrLockMode"
+ actionTemplateName:t="setBvrLockMode"
+ }
+ 
+ setCustomActionTemplate{
+ fsm:t="main"
+ name:t="resetBvrLockMode"
+ actionTemplateName:t="resetBvrLockMode"
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
+ name:t="setBvrTrackMode"
+ actionTemplateName:t="setTrackMode"
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
+ }
+ }
+ 
+ search{
+ stateInit:t="search"
+ 
+ transitions{
+ 
+ scan{
+ event:t="update"
+ 
+ actions{
+ 
+ scan{
+ }
+ 
+ setCenterAzimuth{
+ source:t="constant"
+ value:r=0.0
+ }
+ 
+ setCenterAzimuth{
+ source:t="designationCue"
+ }
+ 
+ setCenterElevation{
+ source:t="constant"
+ value:r=0.0
+ }
+ 
+ setCenterElevation{
+ source:t="designationCue"
+ }
+ }
+ }
+ 
+ detect{
+ event:t="targetInSight"
+ 
+ actions{
+ 
+ setDistGatePos{
+ source:t="continuousScale"
+ width:r=0.0
+ }
+ 
+ setRelSpeedGatePos{
+ source:t="continuousScale"
+ width:r=0.0
+ }
+ 
+ detectTarget{
+ }
+ }
+ }
+ 
+ addTarget{
+ event:t="targetDetected"
+ 
+ actions{
+ 
+ addTarget{
+ }
+ 
+ updateActiveDetectedTarget{
+ }
+ }
+ }
+ 
+ switchSelectedTarget{
+ command:t="switchTarget"
+ 
+ actions{
+ 
+ setNextDetectedTargetActive{
+ }
+ }
+ }
+ 
+ setCueAzimuth{
+ command:t="cueAxisX"
+ 
+ actions{
+ 
+ setCueAzimuth{
+ }
+ }
+ }
+ 
+ setCueDist{
+ command:t="cueAxisY"
+ 
+ actions{
+ 
+ setCueDist{
+ }
+ 
+ setCueDopplerSpeed{
+ }
+ }
+ }
+ 
+ setCueElevation{
+ command:t="cueAxisZ"
+ 
+ actions{
+ 
+ setCueElevation{
+ }
+ }
+ }
+ 
+ setSelectedTarget{
+ command:t="switchToTarget"
+ 
+ actions{
+ 
+ setDetectedTargetActive{
+ }
+ }
+ }
+ }
+ }
+ 
+ tws{
+ stateInit:t="search"
+ 
+ transitions{
+ 
+ scan{
+ event:t="update"
+ stateFrom:t="track"
+ stateTo:t="search"
+ 
+ actions{
+ 
+ scan{
+ }
+ 
+ extrapolateTargetsOfInterest{
+ }
+ 
+ clearTargetsOfInterest{
+ timeOut:r=4.0
+ }
+ 
+ setCueToActiveTargetOfInterest{
+ }
+ 
+ setCenterAzimuth{
+ source:t="constant"
+ value:r=0.0
+ }
+ 
+ setCenterAzimuth{
+ source:t="designationCue"
+ }
+ 
+ setCenterAzimuth{
+ source:t="activeTargetOfInterest"
+ }
+ 
+ setCenterElevation{
+ source:t="constant"
+ value:r=0.0
+ }
+ 
+ setCenterElevation{
+ source:t="designationCue"
+ }
+ 
+ setCenterElevation{
+ source:t="activeTargetOfInterest"
+ }
+ }
+ }
+ 
+ detect{
+ event:t="targetInSight"
+ 
+ actions{
+ 
+ setDistGatePos{
+ source:t="continuousScale"
+ width:r=0.0
+ }
+ 
+ setRelSpeedGatePos{
+ source:t="continuousScale"
+ width:r=0.0
+ }
+ 
+ detectTarget{
+ }
+ }
+ }
+ 
+ addTarget{
+ event:t="targetDetected"
+ stateFrom:t="search"
+ 
+ actions{
+ 
+ updateTargetOfInterest{
+ limit:i=10
+ radius:r=1000.0
+ dopplerSpeedGateMaxTime:r=8.0
+ }
+ 
+ updateActiveDetectedTarget{
+ }
+ 
+ setCueToActiveTargetOfInterest{
+ }
+ }
+ }
+ 
+ switchSelectedTarget{
+ command:t="switchTarget"
+ 
+ actions{
+ 
+ setNextDetectedTargetActive{
+ }
+ }
+ }
+ 
+ setCueAzimuth{
+ command:t="cueAxisX"
+ 
+ actions{
+ 
+ setCueAzimuth{
+ }
+ }
+ }
+ 
+ setCueDist{
+ command:t="cueAxisY"
+ 
+ actions{
+ 
+ setCueDist{
+ }
+ 
+ setCueDopplerSpeed{
+ }
+ }
+ }
+ 
+ setCueElevation{
+ command:t="cueAxisZ"
+ 
+ actions{
+ 
+ setCueElevation{
+ }
+ }
+ }
+ 
+ setSelectedTarget{
+ command:t="switchToTarget"
+ 
+ actions{
+ 
+ setDetectedTargetActive{
+ }
+ }
+ }
+ 
+ designateTarget{
+ command:t="selectTarget"
+ 
+ actions{
+ 
+ designateActiveDetectedTarget{
+ type:i=0
+ sensorIndex:i=1
+ }
+ 
+ designateTargetUnderCue{
+ type:i=0
+ sensorIndex:i=1
+ }
+ }
+ }
+ 
+ scanTrack{
+ stateFrom:t="search"
+ event:t="update"
+ stateTo:t="track"
+ 
+ actions{
+ 
+ scan{
+ periodMult:r=0.01
+ }
+ 
+ extrapolateTargetsOfInterest{
+ }
+ 
+ clearTargetsOfInterest{
+ timeOut:r=4.0
+ }
+ 
+ setCueToActiveTargetOfInterest{
+ }
+ }
+ }
+ 
+ addTargetTrack{
+ stateFrom:t="track"
+ event:t="targetDetected"
+ 
+ actions{
+ 
+ updateTargetOfInterest{
+ limit:i=10
+ onlyExisting:b=yes
+ radius:r=1000.0
+ dopplerSpeedGateMaxTime:r=8.0
+ }
+ 
+ updateActiveDetectedTarget{
+ }
+ 
+ setCueToActiveTargetOfInterest{
+ }
+ }
+ }
+ }
+ }
+ 
+ helmetDesignation{
+ stateInit:t="helmetDesignation"
+ 
+ actionsTemplates{
+ 
+ designateHelmetTargetDir{
+ 
+ designateHelmetTarget{
+ self:b=yes
+ }
+ 
+ setCenterAzimuth{
+ source:t="targetDesignation"
+ }
+ 
+ setCenterElevation{
+ source:t="targetDesignation"
+ }
+ }
+ }
+ 
+ transitions{
+ 
+ activate{
+ event:t="fsmActivate"
+ 
+ actions{
+ 
+ designateHelmetTargetDir{
+ }
+ }
+ }
+ 
+ updateDesignation{
+ event:t="update"
+ 
+ actions{
+ 
+ designateHelmetTargetDir{
+ }
+ }
+ }
+ }
+ }
+ 
+ bvrLock{
+ stateInit:t="lock"
+ 
+ transitions{
+ 
+ scan{
+ event:t="update"
+ 
+ actions{
+ 
+ scan{
+ }
+ }
+ }
+ 
+ detect{
+ event:t="targetInSight"
+ 
+ actions{
+ 
+ detectTarget{
+ ignoreOwnWeapon:b=yes
+ rangeMult:r=1.0
+ }
+ }
+ }
+ }
+ }
+ 
+ lock{
+ stateInit:t="lock"
+ 
+ transitions{
+ 
+ scan{
+ event:t="update"
+ 
+ actions{
+ 
+ scan{
+ }
+ }
+ }
+ 
+ detect{
+ event:t="targetInSight"
+ 
+ actions{
+ 
+ detectTarget{
+ ignoreOwnWeapon:b=yes
+ rangeMult:r=1.0
+ }
+ }
+ }
+ }
+ }
+ 
+ acmLock{
+ stateInit:t="lock"
+ 
+ transitions{
+ 
+ scan{
+ event:t="update"
+ 
+ actions{
+ 
+ scan{
+ }
+ }
+ }
+ 
+ detect{
+ event:t="targetInSight"
+ 
+ actions{
+ 
+ detectTarget{
+ ignoreOwnWeapon:b=yes
+ rangeMult:r=1.0
+ }
+ }
+ }
+ }
+ }
+ 
+ track{
+ stateInit:t="init"
+ 
+ actionsTemplates{
+ 
+ setMprfTrack{
+ 
+ setTransiver{
+ transiver:t="mprf"
+ }
+ 
+ setSignal{
+ signal:t="mprfTrack"
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
+ track{
+ 
+ updateActiveTargetOfInterest{
+ 
+ dirFilter{
+ }
+ 
+ distFilter{
+ }
+ 
+ dopplerSpeedFilter{
+ }
+ }
+ 
+ setCenterAzimuth{
+ source:t="activeTargetOfInterest"
+ }
+ 
+ setCenterElevation{
+ source:t="activeTargetOfInterest"
+ }
+ 
+ setDistGatePos{
+ source:t="activeTargetOfInterest"
+ width:r=0.0
+ }
+ 
+ setRelSpeedGatePos{
+ source:t="activeTargetOfInterest"
+ width:r=0.0
+ }
+ }
+ 
+ extrapolate{
+ 
+ extrapolateTargetsOfInterest{
+ }
+ 
+ clearTargetsOfInterest{
+ timeOut:r=3.0
+ dirRateLim:r=1.0
+ }
+ 
+ setCenterAzimuth{
+ source:t="activeTargetOfInterest"
+ }
+ 
+ setCenterElevation{
+ source:t="activeTargetOfInterest"
+ }
+ 
+ setDistGatePos{
+ source:t="activeTargetOfInterest"
+ width:r=0.0
+ }
+ 
+ setRelSpeedGatePos{
+ source:t="activeTargetOfInterest"
+ width:r=0.0
+ }
+ }
+ }
+ 
+ transitions{
+ 
+ start{
+ event:t="fsmActivate"
+ stateTo:t="mprf"
+ 
+ actions{
+ 
+ setMprfTrack{
+ }
+ 
+ setModeName{
+ name:t="PD track"
+ }
+ }
+ }
+ 
+ tryDetectMprf{
+ stateFrom:t="mprfTry"
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
+ detect{
+ event:t="update"
+ 
+ actions{
+ 
+ detectTarget{
+ ignoreOwnWeapon:b=yes
+ rangeMult:r=1.0
+ }
+ }
+ }
+ 
+ trackMprf{
+ stateFrom:t="mprf"
+ event:t="targetDetected"
+ 
+ actions{
+ 
+ track{
+ }
+ }
+ }
+ 
+ startTrackMprf{
+ stateFrom:t="mprfTry"
+ stateFrom:t="hprfOkMprfTry"
+ event:t="targetDetected"
+ stateTo:t="mprf"
+ 
+ actions{
+ 
+ setMprfTrack{
+ }
+ 
+ track{
+ }
+ 
+ setModeName{
+ name:t="PD track"
+ }
+ }
+ }
+ 
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
+ trackHprf{
+ stateFrom:t="hprf"
+ event:t="targetDetected"
+ stateTo:t="mprfTry"
+ 
+ actions{
+ 
+ track{
+ }
+ 
+ setMprfTrack{
+ }
+ }
+ }
+ 
+ startTrackHprf{
+ stateFrom:t="hprfTry"
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
+ mprfToHprf{
+ stateFrom:t="mprf"
+ stateFrom:t="mprfTry"
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
+ hprfToMprf{
+ stateFrom:t="hprf"
+ event:t="targetNotDetected"
+ stateTo:t="mprfTry"
+ 
+ actions{
+ 
+ extrapolate{
+ }
+ }
+ }
+ 
+ hprfTryToMprf{
+ stateFrom:t="hprfTry"
+ event:t="targetNotDetected"
+ stateTo:t="mprfTry"
+ 
+ actions{
+ 
+ extrapolate{
+ }
+ 
+ setModeName{
+ name:t="track memory"
+ }
+ }
+ }
+ }
+ }
+ 
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
+ }
```

  **Removed**:
```diff
```


- **aces.vromfs.bin_u/gamedata/sensors/su_kopio.blkx**:

  **Added**:
```diff
+ width:r=3.0
+ barsCount:i=3
+ rowMajor:b=no
+ period:r=0.5
+ width:r=3.0
+ barsCount:i=3
+ rowMajor:b=no
```

  **Removed**:
```diff
- width:r=4.0
- barsCount:i=4
- rowMajor:b=yes
- period:r=0.25
- width:r=4.0
- barsCount:i=2
- rowMajor:b=yes
```


- **aces.vromfs.bin_u/gamedata/sensors/su_kopio_25.blkx**:

  **Added**:
```diff
+ width:r=3.0
+ barsCount:i=3
+ rowMajor:b=no
+ period:r=0.5
+ width:r=3.0
+ barsCount:i=3
+ rowMajor:b=no
```

  **Removed**:
```diff
- width:r=4.0
- barsCount:i=4
- rowMajor:b=yes
- period:r=0.25
- width:r=4.0
- barsCount:i=2
- rowMajor:b=yes
```


- **aces.vromfs.bin_u/gamedata/sensors/uk_captor_m_pirate.blkx**:

  **Added**:
```diff
+ distanceAccuracy:r=100.0
+ period:r=3.0
+ barHeight:r=1.5
+ barsCount:i=42
+ barsOneWay:b=yes
+ barHeight:r=1.5
+ barsCount:i=20
+ barsOneWay:b=yes
+ barHeight:r=2.0
+ barsCount:i=2
```

  **Removed**:
```diff
- distanceAccuracy:r=10.0
- period:r=2.5
- barHeight:r=4.0
- barsCount:i=16
- barsOneWay:b=no
- rollStabLimit:r=90.0
- pitchStabLimit:r=60.0
- barHeight:r=3.75
- barsCount:i=8
- barsOneWay:b=no
- rollStabLimit:r=90.0
- pitchStabLimit:r=60.0
- rollStabLimit:r=90.0
- pitchStabLimit:r=60.0
- barHeight:r=4.0
- barsCount:i=1
```


- **aces.vromfs.bin_u/gamedata/units/ships/germ_battlecruiser_ersatz_yorck.blkx**:

  **Added**:
```diff
+ hp:r=2982.0
+ hp:r=3465.0
+ hp:r=2846.0
+ hp:r=645.0
+ hp:r=3969.0
+ hp:r=3500.0
+ hp:r=3500.0
+ 
+ ammunition_storage_shells_05_dm{
+ hp:r=3584.0
+ }
+ hp:r=5600.0
+ 
+ ammunition_storage_charges_05_dm{
+ hp:r=7259.0
+ }
+ hp:r=2461.0
+ hp:r=2461.0
+ }
+ 
+ ammunition_storage_aux_03_dm{
+ hp:r=2200.0
+ }
+ 
+ ammunition_storage_aux_04_dm{
+ hp:r=2200.0
+ }
+ 
+ ammunition_storage_aux_05_dm{
+ hp:r=2543.0
+ }
+ 
+ ammunition_storage_aux_06_dm{
+ hp:r=2543.0
+ }
+ 
+ ammunition_storage_aux_07_dm{
+ hp:r=2200.0
+ }
+ 
+ ammunition_storage_aux_08_dm{
+ hp:r=2200.0
+ }
+ 
+ ammunition_storage_aux_09_dm{
+ hp:r=2200.0
+ hp:r=15238.0
+ hp:r=12433.0
+ hp:r=12462.0
+ hp:r=10439.0
+ armor_cit_07_dm{
+ armorClass:t="ship_RGA"
+ armorThickness:r=100.0
+ hp:r=10000.0
+ }
+ 
+ armorThickness:r=20.0
+ armorThickness:r=20.0
+ armor_cit_03_dm{
+ armorThickness:r=60.0
+ hp:r=10000.0
+ }
+ 
+ armor_cit_19_dm{
+ armor_cit_25_dm{
+ armorThickness:r=50.0
+ armor_cit_26_dm{
+ armor_cit_27_dm{
+ armorThickness:r=40.0
+ hp:r=10000.0
+ }
+ 
+ armor_cit_28_dm{
+ armorThickness:r=60.0
+ hp:r=10000.0
+ }
+ 
+ armor_cit_22_dm{
+ armorThickness:r=25.0
+ hp:r=10000.0
+ }
+ 
+ 
+ armor_cit_24_dm{
+ armorClass:t="ship_RGA"
+ armorThickness:r=100.0
+ hp:r=10000.0
+ }
+ 
+ armor_cit_29_dm{
+ armorThickness:r=50.0
+ hp:r=10000.0
+ }
+ 
+ armor_cit_30_dm{
+ armorClass:t="ship_RGA"
+ armorThickness:r=100.0
+ hp:r=10000.0
+ }
+ 
+ armor_cit_31_dm{
+ armorClass:t="ship_RGA"
+ armorThickness:r=180.0
+ hp:r=10000.0
+ }
+ 
+ armor_cit_32_dm{
+ armorClass:t="ship_RGA"
+ armorThickness:r=150.0
+ hp:r=10000.0
+ }
+ armor_cit_l_03_dm{
+ hidableInViewer:b=no
+ armorThickness:r=60.0
+ hp:r=8500.0
+ }
+ 
+ armor_cit_l_04_dm{
+ hidableInViewer:b=no
+ armorThickness:r=60.0
+ hp:r=8500.0
+ }
+ 
+ armorThickness:r=70.0
+ armorThickness:r=70.0
+ 
+ fuel_tank_03_dm{
+ hp:r=5927.0
+ }
+ 
+ fuel_tank_04_dm{
+ hp:r=5944.0
+ }
+ 
+ fuel_tank_05_dm{
+ hp:r=6000.0
+ }
+ 
+ fuel_tank_06_dm{
+ hp:r=6000.0
+ }
+ 
+ coal_bunker_05_dm{
+ hp:r=3000.0
+ }
+ 
+ coal_bunker_06_dm{
+ hp:r=3000.0
+ }
+ crew:i=9
+ crew:i=62
+ crew:i=69
+ crew:i=88
+ crew:i=88
+ crew:i=69
+ crew:i=85
+ crew:i=101
+ crew:i=87
+ crew:i=81
+ count:i=90
+ }
+ }
+ 
+ shells{
+ entityMunition:t="shells"
+ fatalFire:b=no
+ fatalExplosion:b=no
+ damageEffect:t="ammunition_storage_shells"
+ 
+ ammunition_storage_shells_02_dm{
+ count:i=90
+ count:i=90
+ }
+ }
+ 
+ charges{
+ entityMunition:t="charges"
+ fatalFire:b=yes
+ damageEffect:t="ammunition_storage_charges"
+ 
+ ammunition_storage_charges_02_dm{
+ count:i=90
+ ammunition_storage_shells_03_dm{
+ ammunition_storage_charges_03_dm{
+ ammunition_storage_shells_04_dm{
+ ammunition_storage_charges_04_dm{
+ ammunition_storage_shells_05_dm{
+ ammunition_storage_charges_05_dm{
+ weaponTrigger:t="gunner10"
+ weaponTrigger:t="gunner12"
+ weaponTrigger:t="gunner14"
+ elevator:t="elevator_12_dm"
+ elevator:t="elevator_14_dm"
+ ammunition_storage_aux_07_dm{
+ count:i=900
+ weaponTrigger:t="gunner5"
+ weaponTrigger:t="gunner7"
+ weaponTrigger:t="gunner9"
+ entityMunition:t="aux"
+ fatalExplosion:b=no
+ fatalFire:b=no
+ fireParamsPreset:t="ship_ammo_fire_aux"
+ explosionEvent:t="ammo_aux_explosion_3"
+ fireEvent:t="ammo_aux_fire_3"
+ elevator:t="elevator_07_dm"
+ elevator:t="elevator_09_dm"
+ elevator:t="elevator_11_dm"
+ elevator:t="elevator_13_dm"
+ dstrElevatorDisablesShooting:b=no
+ splashRadiusConstraint:r=10.0
+ splashDamageConstraint:r=3000.0
+ shatterRadiusConstraint:r=1.0
+ 
+ gunpowderMassToSplashParams{
+ 
+ gunpowderMassToInnerRadius{
+ p1:p2=100.0, 1.0
+ p2:p2=10000.0, 2.0
+ }
+ 
+ gunpowderMassToOuterRadius{
+ p1:p2=100.0, 2.0
+ p2:p2=10000.0, 10.0
+ }
+ 
+ gunpowderMassToPenetration{
+ p1:p2=100.0, 13.5
+ p2:p2=500.0, 15.0
+ p3:p2=2000.0, 20.0
+ p4:p2=5000.0, 30.0
+ }
+ 
+ gunpowderMassToDamage{
+ p1:p2=100.0, 1000.0
+ p3:p2=10000.0, 5000.0
+ }
+ }
+ 
+ shells{
+ damageEffect:t="ammunition_storage_aux"
+ 
+ ammunition_storage_aux_08_dm{
+ count:i=900
+ }
+ }
+ }
+ 
+ ammo7{
+ weaponTrigger:t="gunner16"
+ weaponTrigger:t="gunner18"
+ entityMunition:t="aux"
+ fatalExplosion:b=no
+ fatalFire:b=no
+ fireParamsPreset:t="ship_ammo_fire_aux"
+ explosionEvent:t="ammo_aux_explosion_2"
+ fireEvent:t="ammo_aux_fire_2"
+ elevator:t="elevator_06_dm"
+ dstrElevatorDisablesShooting:b=no
+ splashRadiusConstraint:r=10.0
+ splashDamageConstraint:r=3000.0
+ shatterRadiusConstraint:r=1.0
+ 
+ gunpowderMassToSplashParams{
+ 
+ gunpowderMassToInnerRadius{
+ p1:p2=100.0, 1.0
+ p2:p2=10000.0, 2.0
+ }
+ 
+ gunpowderMassToOuterRadius{
+ p1:p2=100.0, 2.0
+ p2:p2=10000.0, 10.0
+ }
+ 
+ gunpowderMassToPenetration{
+ p1:p2=100.0, 13.5
+ p2:p2=500.0, 15.0
+ p3:p2=2000.0, 20.0
+ p4:p2=5000.0, 30.0
+ }
+ 
+ gunpowderMassToDamage{
+ p1:p2=100.0, 1000.0
+ p3:p2=10000.0, 5000.0
+ }
+ }
+ 
+ shells{
+ damageEffect:t="ammunition_storage_aux"
+ 
+ ammunition_storage_aux_01_dm{
+ count:i=100
+ }
+ }
+ 
+ shells{
+ damageEffect:t="ammunition_storage_aux"
+ 
+ ammunition_storage_aux_03_dm{
+ count:i=100
+ }
+ }
+ 
+ shells{
+ damageEffect:t="ammunition_storage_aux"
+ 
+ ammunition_storage_aux_05_dm{
+ count:i=100
+ }
+ }
+ }
+ 
+ ammo8{
+ weaponTrigger:t="gunner17"
+ weaponTrigger:t="gunner19"
+ entityMunition:t="aux"
+ fatalExplosion:b=no
+ fatalFire:b=no
+ fireParamsPreset:t="ship_ammo_fire_aux"
+ explosionEvent:t="ammo_aux_explosion_2"
+ fireEvent:t="ammo_aux_fire_2"
+ elevator:t="elevator_05_dm"
+ dstrElevatorDisablesShooting:b=no
+ splashRadiusConstraint:r=10.0
+ splashDamageConstraint:r=3000.0
+ shatterRadiusConstraint:r=1.0
+ 
+ gunpowderMassToSplashParams{
+ 
+ gunpowderMassToInnerRadius{
+ p1:p2=100.0, 1.0
+ p2:p2=10000.0, 2.0
+ }
+ 
+ gunpowderMassToOuterRadius{
+ p1:p2=100.0, 2.0
+ p2:p2=10000.0, 10.0
+ }
+ 
+ gunpowderMassToPenetration{
+ p1:p2=100.0, 13.5
+ p2:p2=500.0, 15.0
+ p3:p2=2000.0, 20.0
+ p4:p2=5000.0, 30.0
+ }
+ 
+ gunpowderMassToDamage{
+ p1:p2=100.0, 1000.0
+ p3:p2=10000.0, 5000.0
+ }
+ }
+ 
+ shells{
+ damageEffect:t="ammunition_storage_aux"
+ 
+ ammunition_storage_aux_02_dm{
+ count:i=100
+ }
+ }
+ 
+ shells{
+ damageEffect:t="ammunition_storage_aux"
+ 
+ ammunition_storage_aux_04_dm{
+ count:i=100
+ }
+ }
+ 
+ shells{
+ damageEffect:t="ammunition_storage_aux"
+ 
+ ammunition_storage_aux_06_dm{
+ count:i=100
+ }
+ }
+ }
+ 
+ ammo9{
+ ammunition_storage_aux_09_dm{
+ count:i=600
+ ammo10{
+ ammo11{
+ ammo12{
+ part{
+ partNo:t="ammunition_storage_charges_03_dm"
+ critWaterLevel:r=0.65
+ }
+ 
+ 
+ part{
+ partNo:t="ammunition_storage_shells_03_dm"
+ critWaterLevel:r=0.8
+ }
+ partNo:t="ammunition_storage_charges_04_dm"
+ partNo:t="ammunition_storage_shells_04_dm"
+ partNo:t="ammunition_storage_shells_05_dm"
+ partNo:t="ammunition_storage_charges_05_dm"
```

  **Removed**:
```diff
- hp:r=3226.0
- hp:r=3500.0
- hp:r=3037.0
- hp:r=750.0
- hp:r=4600.0
- hp:r=4600.0
- hp:r=4600.0
- hp:r=7300.0
- hp:r=2200.0
- hp:r=2265.0
- hp:r=15225.0
- hp:r=12431.0
- hp:r=12459.0
- hp:r=10710.0
- armor_cit_22_dm{
- armorThickness:r=25.0
- hp:r=10000.0
- }
- 
- armorThickness:r=60.0
- armorThickness:r=25.0
- armor_cit_07_dm{
- hidableInViewer:b=yes
- armor_cit_03_dm{
- armorThickness:r=60.0
- armor_cit_19_dm{
- armor_cit_l_20_dm{
- armorClass:t="ship_structural_steel"
- armorThickness:r=30.0
- hp:r=8500.0
- }
- 
- armor_cit_l_21_dm{
- armorClass:t="ship_structural_steel"
- armorThickness:r=30.0
- hp:r=8500.0
- }
- 
- armor_cit_l_22_dm{
- armorClass:t="ship_structural_steel"
- armorThickness:r=30.0
- hp:r=8500.0
- }
- 
- armor_cit_l_23_dm{
- armorClass:t="ship_structural_steel"
- armorThickness:r=30.0
- hp:r=8500.0
- }
- 
- armor_cit_l_24_dm{
- armorClass:t="ship_structural_steel"
- armorThickness:r=30.0
- hp:r=8500.0
- }
- 
- armor_cit_l_25_dm{
- armorClass:t="ship_structural_steel"
- armorThickness:r=30.0
- hp:r=8500.0
- }
- 
- armor_cit_r_20_dm{
- armorClass:t="ship_structural_steel"
- armorThickness:r=30.0
- hp:r=8500.0
- }
- 
- armor_cit_r_21_dm{
- armorClass:t="ship_structural_steel"
- armorThickness:r=30.0
- hp:r=8500.0
- }
- 
- armor_cit_r_22_dm{
- armorClass:t="ship_structural_steel"
- armorThickness:r=30.0
- hp:r=8500.0
- }
- 
- armor_cit_r_23_dm{
- armorClass:t="ship_structural_steel"
- armorThickness:r=30.0
- hp:r=8500.0
- }
- 
- armor_cit_r_24_dm{
- armorClass:t="ship_structural_steel"
- armorThickness:r=30.0
- hp:r=8500.0
- }
- 
- armor_cit_r_25_dm{
- armorClass:t="ship_structural_steel"
- armorThickness:r=30.0
- hp:r=8500.0
- }
- 
- armorThickness:r=100.0
- armorThickness:r=100.0
- armor_cit_l_14_dm{
- armorThickness:r=15.0
- hp:r=8500.0
- }
- 
- armor_cit_l_15_dm{
- armorThickness:r=15.0
- hp:r=8500.0
- }
- 
- armor_cit_l_16_dm{
- armorThickness:r=15.0
- hp:r=8500.0
- }
- 
- armor_cit_l_17_dm{
- armorThickness:r=15.0
- hp:r=8500.0
- }
- 
- armor_cit_l_18_dm{
- armorThickness:r=15.0
- hp:r=8500.0
- }
- 
- armor_cit_l_19_dm{
- armorThickness:r=15.0
- hp:r=8500.0
- }
- 
- armor_cit_r_14_dm{
- armorThickness:r=15.0
- hp:r=8500.0
- }
- 
- armor_cit_r_15_dm{
- armorThickness:r=15.0
- hp:r=8500.0
- }
- 
- armor_cit_r_16_dm{
- armorThickness:r=15.0
- hp:r=8500.0
- }
- 
- armor_cit_r_17_dm{
- armorThickness:r=15.0
- hp:r=8500.0
- }
- 
- armor_cit_r_18_dm{
- armorThickness:r=15.0
- hp:r=8500.0
- }
- 
- armor_cit_r_19_dm{
- armorThickness:r=15.0
- hp:r=8500.0
- }
- 
- crew:i=10
- crew:i=61
- crew:i=67
- crew:i=85
- crew:i=85
- crew:i=67
- crew:i=92
- crew:i=100
- crew:i=86
- crew:i=86
- count:i=180
- count:i=180
- ammunition_storage_shells_02_dm{
- ammunition_storage_charges_02_dm{
- ammunition_storage_shells_03_dm{
- ammunition_storage_charges_03_dm{
- ammunition_storage_shells_04_dm{
- ammunition_storage_charges_04_dm{
- weaponTrigger:t="gunner5"
- weaponTrigger:t="gunner7"
- weaponTrigger:t="gunner9"
- weaponTrigger:t="gunner16"
- weaponTrigger:t="gunner17"
- weaponTrigger:t="gunner18"
- weaponTrigger:t="gunner19"
- elevator:t="elevator_05_dm"
- elevator:t="elevator_06_dm"
- elevator:t="elevator_07_dm"
- elevator:t="elevator_09_dm"
- ammunition_storage_aux_01_dm{
- count:i=1500
- weaponTrigger:t="gunner10"
- weaponTrigger:t="gunner12"
- weaponTrigger:t="gunner14"
- elevator:t="elevator_11_dm"
- elevator:t="elevator_12_dm"
- elevator:t="elevator_15_dm"
- elevator:t="elevator_16_dm"
- ammunition_storage_aux_02_dm{
- count:i=1500
- ammo7{
- ammo8{
- ammo9{
- partNo:t="ammunition_storage_charges_03_dm"
- partNo:t="ammunition_storage_shells_03_dm"
- partNo:t="ammunition_storage_shells_04_dm"
- partNo:t="ammunition_storage_charges_04_dm"
```


- **aces.vromfs.bin_u/gamedata/units/ships/uk_battleship_rodney.blkx**:

  **Added**:
```diff
+ hp:r=6432.0
+ hp:r=5200.0
+ hp:r=5499.0
+ hp:r=1000.0
+ hp:r=872.0
+ hp:r=10338.0
+ hp:r=9905.0
+ hp:r=10231.0
+ hp:r=3000.0
+ hp:r=2520.0
+ hp:r=3000.0
+ hp:r=500.0
+ hp:r=500.0
+ hp:r=17900.0
+ hp:r=17900.0
+ hp:r=17900.0
+ hp:r=17900.0
+ hp:r=14470.0
+ hp:r=17900.0
+ hp:r=17900.0
+ hp:r=15332.0
+ armor_cit_25_dm{
+ armorThickness:r=228.6
+ hidableInViewer:b=yes
+ armorThickness:r=19.05
+ armorThickness:r=158.75
+ armorClass:t="ship_RGA"
+ armorClass:t="ship_RGA"
+ armorClass:t="ship_RGA"
+ armorThickness:r=381.0
+ armorThickness:r=330.2
+ armorThickness:r=317.5
+ armorThickness:r=304.8
+ armor_cit_01_dm{
+ armorThickness:r=25.4
+ armor_cit_02_dm{
+ armorThickness:r=25.4
+ hp:r=10000.0
+ }
+ 
+ armor_cit_12_dm{
+ armorThickness:r=101.6
+ hp:r=10000.0
+ }
+ 
+ armor_cit_13_dm{
+ armorThickness:r=19.05
+ hp:r=10000.0
+ }
+ 
+ armorThickness:r=107.95
+ armorThickness:r=107.95
+ armorThickness:r=25.4
+ armorThickness:r=25.4
+ armorThickness:r=25.4
+ armorThickness:r=25.4
+ armorThickness:r=25.4
+ armorThickness:r=25.4
+ armorThickness:r=25.0
+ fireProtectionHp:r=30.0
+ hp:r=1000.0
+ crew:i=12
+ crew:i=10
+ crew:i=91
+ crew:i=96
+ crew:i=121
+ crew:i=91
+ maxSpeed:r=11.85
+ row:p2=11.85, 32.5
```

  **Removed**:
```diff
- hp:r=6800.0
- hp:r=6800.0
- hp:r=5835.0
- hp:r=637.0
- hp:r=860.0
- hp:r=10800.0
- hp:r=10800.0
- hp:r=10800.0
- hp:r=2300.0
- hp:r=2300.0
- hp:r=2300.0
- 
- ammunition_storage_aux_06_dm{
- hp:r=2300.0
- }
- 
- ammunition_storage_aux_07_dm{
- hp:r=2300.0
- }
- hp:r=543.0
- hp:r=543.0
- hp:r=11800.0
- hp:r=12959.0
- hp:r=11800.0
- hp:r=11800.0
- hp:r=11800.0
- hp:r=12326.0
- hp:r=12786.0
- hp:r=11800.0
- armor_cit_13_dm{
- armorThickness:r=101.6
- armorClass:t="ship_RHA"
- armorClass:t="ship_RHA"
- armorClass:t="ship_RHA"
- armorClass:t="ship_RHA"
- hp:r=10000.0
- }
- 
- armor_cit_01_dm{
- armorThickness:r=61.5
- hp:r=10000.0
- }
- 
- armor_cit_02_dm{
- armorThickness:r=76.2
- armorThickness:r=101.6
- armorThickness:r=177.8
- armorClass:t="ship_RHA"
- armorClass:t="ship_RHA"
- armorClass:t="ship_RHA"
- armorClass:t="ship_RHA"
- hp:r=10000.0
- }
- 
- armor_cit_12_dm{
- armorThickness:r=101.6
- armorClass:t="ship_RHA"
- armorClass:t="ship_RHA"
- armorThickness:r=304.8
- armorThickness:r=381.0
- armorThickness:r=304.8
- armorThickness:r=330.2
- armor_cit_25_dm{
- armorThickness:r=317.5
- armorThickness:r=38.1
- armorThickness:r=38.1
- armorThickness:r=38.1
- armorThickness:r=38.1
- armorThickness:r=38.1
- armorThickness:r=38.1
- armorThickness:r=38.1
- armorThickness:r=38.1
- fireProtectionHp:r=5.0
- genericDamageMult:r=1.0
- explosionDamageMult:r=1.5
- armorThickness:r=20.0
- hp:r=700.0
- crew:i=6
- crew:i=6
- crew:i=113
- crew:i=97
- crew:i=113
- crew:i=86
- maxSpeed:r=11.8
- row:p2=11.8, 32.5
```


- **aces.vromfs.bin_u/gamedata/units/ships/ussr_battleship_arhangelsk.blkx**:

  **Added**:
```diff
+ 
+ ammunition_storage_aux_02_dm{
+ hp:r=3000.0
+ }
+ 
+ ammunition_storage_aux_03_dm{
+ hp:r=3000.0
+ }
+ 
+ ammunition_storage_aux_04_dm{
+ hp:r=2639.0
+ }
+ 
+ ammunition_storage_aux_05_dm{
+ hp:r=3000.0
+ }
+ armorThickness:r=76.0
+ armorThickness:r=25.0
+ armor_cit_69_dm{
+ armorClass:t="ship_RGA"
+ armorThickness:r=101.0
+ hp:r=10000.0
+ }
+ 
+ armorThickness:r=152.0
+ armorThickness:r=152.0
+ armorThickness:r=38.0
+ armorThickness:r=31.0
+ armorThickness:r=25.0
+ armor_cit_70_dm{
+ armorThickness:r=7.0
+ hp:r=10000.0
+ }
+ 
+ armorThickness:r=50.0
+ armorThickness:r=152.0
+ 
+ armor_cit_l_16_dm{
+ hidableInViewer:b=no
+ armorThickness:r=25.0
+ hp:r=8500.0
+ }
+ 
+ armor_cit_l_17_dm{
+ hidableInViewer:b=no
+ armorThickness:r=25.0
+ hp:r=8500.0
+ }
+ 
+ armor_cit_l_18_dm{
+ hidableInViewer:b=no
+ armorThickness:r=25.0
+ hp:r=8500.0
+ }
+ 
+ armor_cit_l_19_dm{
+ hidableInViewer:b=no
+ armorThickness:r=25.0
+ hp:r=8500.0
+ }
+ 
+ armor_cit_l_20_dm{
+ hidableInViewer:b=no
+ armorThickness:r=25.0
+ hp:r=8500.0
+ }
+ 
+ armor_cit_r_16_dm{
+ hidableInViewer:b=no
+ armorThickness:r=25.0
+ hp:r=8500.0
+ }
+ 
+ armor_cit_r_17_dm{
+ hidableInViewer:b=no
+ armorThickness:r=25.0
+ hp:r=8500.0
+ }
+ 
+ armor_cit_r_18_dm{
+ hidableInViewer:b=no
+ armorThickness:r=25.0
+ hp:r=8500.0
+ }
+ 
+ armor_cit_r_19_dm{
+ hidableInViewer:b=no
+ armorThickness:r=25.0
+ hp:r=8500.0
+ }
+ 
+ armor_cit_r_20_dm{
+ hidableInViewer:b=no
+ armorThickness:r=25.0
+ hp:r=8500.0
+ }
+ 
+ armor_cit_l_21_dm{
+ hidableInViewer:b=no
+ armorThickness:r=25.0
+ hp:r=8500.0
+ }
+ 
+ armor_cit_l_22_dm{
+ hidableInViewer:b=no
+ armorThickness:r=25.0
+ hp:r=8500.0
+ }
+ 
+ armor_cit_l_23_dm{
+ hidableInViewer:b=no
+ armorThickness:r=25.0
+ hp:r=8500.0
+ }
+ 
+ armor_cit_l_24_dm{
+ hidableInViewer:b=no
+ armorThickness:r=25.0
+ hp:r=8500.0
+ }
+ 
+ armor_cit_l_25_dm{
+ hidableInViewer:b=no
+ armorThickness:r=25.0
+ hp:r=8500.0
+ }
+ 
+ armor_cit_r_21_dm{
+ hidableInViewer:b=no
+ armorThickness:r=25.0
+ hp:r=8500.0
+ }
+ 
+ armor_cit_r_22_dm{
+ hidableInViewer:b=no
+ armorThickness:r=25.0
+ hp:r=8500.0
+ }
+ 
+ armor_cit_r_23_dm{
+ hidableInViewer:b=no
+ armorThickness:r=25.0
+ hp:r=8500.0
+ }
+ 
+ armor_cit_r_24_dm{
+ hidableInViewer:b=no
+ armorThickness:r=25.0
+ hp:r=8500.0
+ }
+ 
+ armor_cit_r_25_dm{
+ hidableInViewer:b=no
+ armorThickness:r=25.0
+ hp:r=8500.0
+ }
+ armorClass:t="ship_RHA"
```

  **Removed**:
```diff
- armorThickness:r=279.0
- armorClass:t="ship_RGA"
- armorThickness:r=76.0
- rmorThickness:r=152.0
- rmorThickness:r=152.0
- armorThickness:r=60.0
- armorThickness:r=50.0
- armorThickness:r=32.0
- hidableInViewer:b=yes
- armorThickness:r=51.0
- armorThickness:r=102.0
- armorClass:t="ship_RGA"
```


- **aces.vromfs.bin_u/gamedata/units/tankmodels/fr_vbci.blkx**:

  **Added**:
```diff
+ Weapon{
+ trigger:t="gunner2"
+ triggerGroup:t="commander"
+ blk:t="gameData/Weapons/dummy_weapon.blk"
+ emitter:t="bone_commander_sight_v"
+ defaultYaw:r=0.0
+ defaultPitch:r=0.0
+ parkInDeadzone:b=no
+ speedYaw:r=120.0
+ speedPitch:r=90.0
+ 
+ turret{
+ head:t="bone_commander_sight_h"
+ gun:t="bone_commander_sight_v"
+ gunnerDm:t="commander_dm"
+ verDriveDm:t="commander_panoramic_sight_dm"
+ horDriveDm:t="commander_panoramic_sight_dm"
+ }
+ 
+ gunStabilizer{
+ hasVerticalGunFreeMode:b=no
+ forceEnabled:b=yes
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
+ row:p2=45.0, 0.00015
+ row:p2=80.0, 0.0002
+ }
+ }
+ 
+ limits{
+ yaw:p2=-180.0, 180.0
+ pitch:p2=-9.0, 65.0
+ }
+ }
+ 
+ Weapon{
+ trigger:t="gunner2"
+ triggerGroup:t="commander"
+ blk:t="gameData/Weapons/dummy_weapon.blk"
+ emitter:t="bone_commander_sight_v"
+ defaultYaw:r=0.0
+ defaultPitch:r=0.0
+ parkInDeadzone:b=no
+ speedYaw:r=120.0
+ speedPitch:r=90.0
+ 
+ turret{
+ head:t="bone_commander_sight_h"
+ gun:t="bone_commander_sight_v"
+ gunnerDm:t="commander_dm"
+ verDriveDm:t="commander_panoramic_sight_dm"
+ horDriveDm:t="commander_panoramic_sight_dm"
+ }
+ 
+ gunStabilizer{
+ hasVerticalGunFreeMode:b=no
+ forceEnabled:b=yes
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
+ row:p2=45.0, 0.00015
+ row:p2=80.0, 0.0002
+ }
+ }
+ 
+ limits{
+ yaw:p2=-180.0, 180.0
+ pitch:p2=-9.0, 65.0
+ }
+ }
+ 
```

  **Removed**:
```diff
```


- **aces.vromfs.bin_u/gamedata/units/tankmodels/germ_panzerjager_nashorn.blkx**:

  **Added**:
```diff
+ maxAdditionalPitch:r=0.0
```

  **Removed**:
```diff
```


- **aces.vromfs.bin_u/gamedata/units/tankmodels/germ_pzh_2000.blkx**:

  **Added**:
```diff
+ drowningCheckHeightMultiplier:r=0.8075
+ dmgAngles{
+ hatch_06:p2=10.0, 65.0
+ hatch_07:p2=10.0, 65.0
+ }
+ 
+ topGearRadius:r=0.12
```

  **Removed**:
```diff
```


- **aces.vromfs.bin_u/gamedata/units/tankmodels/it_pzh_2000_hu.blkx**:

  **Added**:
```diff
+ drowningCheckHeightMultiplier:r=0.8075
+ 
+ turret_05_back_dm{
+ }
+ 
+ turret_05_bottom_dm{
+ }
+ 
+ turret_05_side_dm{
+ }
+ 
+ turret_05_top_dm{
+ }
+ 
+ turret_06_top_dm{
+ }
+ 
+ turret_06_side_dm{
+ }
+ 
+ turret_06_bottom_dm{
+ }
+ 
+ turret_06_back_dm{
+ }
+ 
+ ex_armor_r_07_dm{
+ }
+ 
+ ex_armor_r_08_dm{
+ }
+ 
+ ex_armor_r_09_dm{
+ }
+ 
+ ex_armor_r_10_dm{
+ }
+ 
+ ex_armor_l_07_dm{
+ }
+ 
+ ex_armor_l_08_dm{
+ }
+ 
+ ex_armor_l_09_dm{
+ }
+ 
+ ex_armor_l_10_dm{
+ }
+ dmgAngles{
+ hatch_06:p2=10.0, 65.0
+ hatch_07:p2=10.0, 65.0
+ }
+ 
+ topGearRadius:r=0.12
+ 
+ hideNodes{
+ node:t="ex_armor_r_02"
+ node:t="ex_armor_r_03"
+ node:t="ex_armor_r_04"
+ node:t="ex_armor_r_05"
+ node:t="ex_armor_l_02"
+ node:t="ex_armor_l_03"
+ node:t="ex_armor_l_04"
+ node:t="ex_armor_l_05"
+ }
+ node:t="ex_decor_07_net"
+ node:t="ex_decor_18_net"
+ node:t="ex_armor_l_07"
+ node:t="ex_armor_l_08"
+ node:t="ex_armor_l_09"
+ node:t="ex_armor_l_10"
+ node:t="ex_armor_r_07"
+ node:t="ex_armor_r_08"
+ node:t="ex_armor_r_09"
+ node:t="ex_armor_r_10"
+ node:t="turret_05_back"
+ node:t="turret_05_bottom"
+ node:t="turret_05_side"
+ node:t="turret_05_top"
+ node:t="turret_06_back"
+ node:t="turret_06_bottom"
+ node:t="turret_06_side"
+ node:t="turret_06_top"
```

  **Removed**:
```diff
```


- **aces.vromfs.bin_u/gamedata/units/tankmodels/us_rdf_lt.blkx**:

  **Added**:
```diff
+ EngineName:t="engine_m3_bradley"
```

  **Removed**:
```diff
- EngineName:t="engine_hstvl"
```


- **aces.vromfs.bin_u/gamedata/weapons/bombguns/su_fab_3000m_54.blkx**:

  **Added**:
```diff
+ bulletName:t="su_fab_3000m_54"
```

  **Removed**:
```diff
- bulletName:t="su_fab_3000_m54"
```


- **aces.vromfs.bin_u/gamedata/weapons/bombguns/su_grom_2.blkx**:

  **Added**:
```diff
+ bulletName:t="su_grom_2"
```

  **Removed**:
```diff
- bulletName:t="grom_2"
```


- **aces.vromfs.bin_u/gamedata/weapons/containers/pylon_kfir_central_us_3000lb_m118.blkx**:

  **Added**:
```diff
+ container:b=yes
+ mesh:t="pylon_kfir_central_3000lb"
+ useEmitter:b=yes
+ emitter:t="bomb2"
+ blk:t="gameData/Weapons/BombGuns/us_3000lb_m118.blk"
+ bullets:i=1
+ amountPerTier:i=1
```

  **Removed**:
```diff
```


- **aces.vromfs.bin_u/gamedata/weapons/groundmodels_weapons/152mm_mim146.blkx**:

  **Added**:
```diff
+ loadFactorMax:r=42.0
+ reqAccelMax:r=42.0
```

  **Removed**:
```diff
- loadFactorMax:r=35.0
- reqAccelMax:r=35.0
```


- **aces.vromfs.bin_u/gamedata/weapons/groundmodels_weapons/152mm_mim146_launcher_user_cannon.blkx**:

  **Added**:
```diff
+ loadFactorMax:r=42.0
+ reqAccelMax:r=42.0
+ loadFactorMax:r=42.0
+ reqAccelMax:r=42.0
```

  **Removed**:
```diff
- loadFactorMax:r=35.0
- reqAccelMax:r=35.0
- loadFactorMax:r=35.0
- reqAccelMax:r=35.0
```


---
