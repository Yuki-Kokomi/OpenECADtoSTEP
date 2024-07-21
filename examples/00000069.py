SketchPlane0 = add_sketchplane(
origin= [0., 0., 0.], normal= [ 0., -1.,  0.], x_axis= [ 1.,  0., -0.], y_axis= [0., 0., 1.])
Loops0 = []
Curves0_0 = []
Arc0_0_0 = add_arc(start= [128., 128.], end= [147., 109.], mid= [133.565, 114.565])
Curves0_0.append(Arc0_0_0)
Line0_0_1 = add_line(start= [147., 109.], end= [223., 109.])
Curves0_0.append(Line0_0_1)
Line0_0_2 = add_line(start= [223., 109.], end= [223., 128.])
Curves0_0.append(Line0_0_2)
Line0_0_3 = add_line(start= [223., 128.], end= [213.5, 128. ])
Curves0_0.append(Line0_0_3)
Line0_0_4 = add_line(start= [213.5, 128. ], end= [213.5, 204. ])
Curves0_0.append(Line0_0_4)
Line0_0_5 = add_line(start= [213.5, 204. ], end= [223., 204.])
Curves0_0.append(Line0_0_5)
Line0_0_6 = add_line(start= [223., 204.], end= [223., 223.])
Curves0_0.append(Line0_0_6)
Line0_0_7 = add_line(start= [223., 223.], end= [147., 223.])
Curves0_0.append(Line0_0_7)
Arc0_0_8 = add_arc(start= [147., 223.], end= [128., 204.], mid= [133.565, 217.435])
Curves0_0.append(Arc0_0_8)
Line0_0_9 = add_line(start= [128., 204.], end= [128., 128.])
Curves0_0.append(Line0_0_9)
Loop0_0 = add_loop(Curves0_0)
Loops0.append(Loop0_0)
Curves0_1 = []
Circle0_1_0 = add_circle(center= [156.5, 166. ], radius= 9.652)
Curves0_1.append(Circle0_1_0)
Loop0_1 = add_loop(Curves0_1)
Loops0.append(Loop0_1)
Profile0 = add_profile(Loops0)
Sketch0 = add_sketch(sketch_plane= SketchPlane0, profile= Profile0,
        sketch_position= [-0.75  , -0.    , -0.2308], sketch_size= 0.5769)
Extrude0 = add_extrude(sketch= Sketch0,
        operation= 0, type= 0, extent_one= 0.0462, extent_two= 0.)
SketchPlane1 = add_sketchplane(
        origin= [0., 0., 0.], normal= [ 0., -1.,  0.], x_axis= [ 1.,  0., -0.], y_axis= [0., 0., 1.])
Loops1 = []
Curves1_0 = []
Line1_0_0 = add_line(start= [128., 128.], end= [223., 128.])
Curves1_0.append(Line1_0_0)
Line1_0_1 = add_line(start= [223., 128.], end= [223.    , 159.6667])
Curves1_0.append(Line1_0_1)
Line1_0_2 = add_line(start= [223.    , 159.6667], end= [128.    , 159.6667])
Curves1_0.append(Line1_0_2)
Line1_0_3 = add_line(start= [128.    , 159.6667], end= [128., 128.])
Curves1_0.append(Line1_0_3)
Loop1_0 = add_loop(Curves1_0)
Loops1.append(Loop1_0)
Profile1 = add_profile(Loops1)
Sketch1 = add_sketch(sketch_plane= SketchPlane1, profile= Profile1,
        sketch_position= [-0.1731, -0.    , -0.3462], sketch_size= 0.3462)
Extrude1 = add_extrude(sketch= Sketch1,
        operation= 1, type= 0, extent_one= 0.0462, extent_two= 0.)
SketchPlane2 = add_sketchplane(
        origin= [0., 0., 0.], normal= [ 0., -1.,  0.], x_axis= [ 1.,  0., -0.], y_axis= [0., 0., 1.])
Loops2 = []
Curves2_0 = []
Line2_0_0 = add_line(start= [128., 128.], end= [191.3333, 128.    ])
Curves2_0.append(Line2_0_0)
Arc2_0_1 = add_arc(start= [191.3333, 128.    ], end= [207.1667, 143.8333], mid= [202.5292, 132.6375])
Curves2_0.append(Arc2_0_1)
Line2_0_2 = add_line(start= [207.1667, 143.8333], end= [207.1667, 207.1667])
Curves2_0.append(Line2_0_2)
Arc2_0_3 = add_arc(start= [207.1667, 207.1667], end= [191.3333, 223.    ], mid= [202.5292, 218.3625])
Curves2_0.append(Arc2_0_3)
Line2_0_4 = add_line(start= [191.3333, 223.    ], end= [128., 223.])
Curves2_0.append(Line2_0_4)
Line2_0_5 = add_line(start= [128., 223.], end= [128.    , 207.1667])
Curves2_0.append(Line2_0_5)
Line2_0_6 = add_line(start= [128.    , 207.1667], end= [135.9167, 207.1667])
Curves2_0.append(Line2_0_6)
Line2_0_7 = add_line(start= [135.9167, 207.1667], end= [135.9167, 143.8333])
Curves2_0.append(Line2_0_7)
Line2_0_8 = add_line(start= [135.9167, 143.8333], end= [128.    , 143.8333])
Curves2_0.append(Line2_0_8)
Line2_0_9 = add_line(start= [128.    , 143.8333], end= [128., 128.])
Curves2_0.append(Line2_0_9)
Loop2_0 = add_loop(Curves2_0)
Loops2.append(Loop2_0)
Curves2_1 = []
Circle2_1_0 = add_circle(center= [183.4167, 175.5   ], radius= 8.0433)
Curves2_1.append(Circle2_1_0)
Loop2_1 = add_loop(Curves2_1)
Loops2.append(Loop2_1)
Profile2 = add_profile(Loops2)
Sketch2 = add_sketch(sketch_plane= SketchPlane2, profile= Profile2,
        sketch_position= [ 0.1731,  0.    , -0.3462], sketch_size= 0.6923)
Extrude2 = add_extrude(sketch= Sketch2,
        operation= 1, type= 0, extent_one= 0.0462, extent_two= 0.)
SketchPlane3 = add_sketchplane(
        origin= [0., 0., 0.], normal= [ 0., -1.,  0.], x_axis= [ 1.,  0., -0.], y_axis= [0., 0., 1.])
Loops3 = []
Curves3_0 = []
Line3_0_0 = add_line(start= [128., 128.], end= [139.875, 128.   ])
Curves3_0.append(Line3_0_0)
Line3_0_1 = add_line(start= [139.875, 128.   ], end= [139.875, 223.   ])
Curves3_0.append(Line3_0_1)
Line3_0_2 = add_line(start= [139.875, 223.   ], end= [128., 223.])
Curves3_0.append(Line3_0_2)
Line3_0_3 = add_line(start= [128., 223.], end= [128.   , 211.125])
Curves3_0.append(Line3_0_3)
Line3_0_4 = add_line(start= [128.   , 211.125], end= [128.   , 139.875])
Curves3_0.append(Line3_0_4)
Line3_0_5 = add_line(start= [128.   , 139.875], end= [128., 128.])
Curves3_0.append(Line3_0_5)
Loop3_0 = add_loop(Curves3_0)
Loops3.append(Loop3_0)
Profile3 = add_profile(Loops3)
Sketch3 = add_sketch(sketch_plane= SketchPlane3, profile= Profile3,
        sketch_position= [ 0.1731,  0.    , -0.2308], sketch_size= 0.4615)
Extrude3 = add_extrude(sketch= Sketch3,
        operation= 1, type= 0, extent_one= 0.0462, extent_two= 0.)
SketchPlane4 = add_sketchplane(
        origin= [0., 0., 0.], normal= [ 0., -1.,  0.], x_axis= [ 1.,  0., -0.], y_axis= [0., 0., 1.])
Loops4 = []
Curves4_0 = []
Line4_0_0 = add_line(start= [128., 128.], end= [139.875, 128.   ])
Curves4_0.append(Line4_0_0)
Line4_0_1 = add_line(start= [139.875, 128.   ], end= [139.875, 139.875])
Curves4_0.append(Line4_0_1)
Line4_0_2 = add_line(start= [139.875, 139.875], end= [139.875, 211.125])
Curves4_0.append(Line4_0_2)
Line4_0_3 = add_line(start= [139.875, 211.125], end= [139.875, 223.   ])
Curves4_0.append(Line4_0_3)
Line4_0_4 = add_line(start= [139.875, 223.   ], end= [128., 223.])
Curves4_0.append(Line4_0_4)
Line4_0_5 = add_line(start= [128., 223.], end= [128., 128.])
Curves4_0.append(Line4_0_5)
Loop4_0 = add_loop(Curves4_0)
Loops4.append(Loop4_0)
Profile4 = add_profile(Loops4)
Sketch4 = add_sketch(sketch_plane= SketchPlane4, profile= Profile4,
        sketch_position= [-0.2308, -0.    , -0.2308], sketch_size= 0.4615)
Extrude4 = add_extrude(sketch= Sketch4,
        operation= 1, type= 0, extent_one= 0.0462, extent_two= 0.)
SketchPlane5 = add_sketchplane(
        origin= [0., 0., 0.], normal= [ 0., -1.,  0.], x_axis= [ 1.,  0., -0.], y_axis= [0., 0., 1.])
Loops5 = []
Curves5_0 = []
Line5_0_0 = add_line(start= [128., 128.], end= [223., 128.])
Curves5_0.append(Line5_0_0)
Line5_0_1 = add_line(start= [223., 128.], end= [223.    , 143.8333])
Curves5_0.append(Line5_0_1)
Line5_0_2 = add_line(start= [223.    , 143.8333], end= [128.    , 143.8333])
Curves5_0.append(Line5_0_2)
Line5_0_3 = add_line(start= [128.    , 143.8333], end= [128., 128.])
Curves5_0.append(Line5_0_3)
Loop5_0 = add_loop(Curves5_0)
Loops5.append(Loop5_0)
Profile5 = add_profile(Loops5)
Sketch5 = add_sketch(sketch_plane= SketchPlane5, profile= Profile5,
        sketch_position= [-0.1731, -0.    , -0.2308], sketch_size= 0.3462)
Extrude5 = add_extrude(sketch= Sketch5,
        operation= 1, type= 0, extent_one= 0.0462, extent_two= 0.)
SketchPlane6 = add_sketchplane(
        origin= [0., 0., 0.], normal= [ 0., -1.,  0.], x_axis= [ 1.,  0., -0.], y_axis= [0., 0., 1.])
Loops6 = []
Curves6_0 = []
Arc6_0_0 = add_arc(start= [128., 128.], end= [147., 109.], mid= [133.565, 114.565])
Curves6_0.append(Arc6_0_0)
Line6_0_1 = add_line(start= [147., 109.], end= [223., 109.])
Curves6_0.append(Line6_0_1)
Line6_0_2 = add_line(start= [223., 109.], end= [223., 128.])
Curves6_0.append(Line6_0_2)
Line6_0_3 = add_line(start= [223., 128.], end= [213.5, 128. ])
Curves6_0.append(Line6_0_3)
Line6_0_4 = add_line(start= [213.5, 128. ], end= [213.5, 204. ])
Curves6_0.append(Line6_0_4)
Line6_0_5 = add_line(start= [213.5, 204. ], end= [223., 204.])
Curves6_0.append(Line6_0_5)
Line6_0_6 = add_line(start= [223., 204.], end= [223., 223.])
Curves6_0.append(Line6_0_6)
Line6_0_7 = add_line(start= [223., 223.], end= [147., 223.])
Curves6_0.append(Line6_0_7)
Arc6_0_8 = add_arc(start= [147., 223.], end= [128., 204.], mid= [133.565, 217.435])
Curves6_0.append(Arc6_0_8)
Line6_0_9 = add_line(start= [128., 204.], end= [128., 128.])
Curves6_0.append(Line6_0_9)
Loop6_0 = add_loop(Curves6_0)
Loops6.append(Loop6_0)
Curves6_1 = []
Circle6_1_0 = add_circle(center= [156.5, 166. ], radius= 9.652)
Curves6_1.append(Circle6_1_0)
Loop6_1 = add_loop(Curves6_1)
Loops6.append(Loop6_1)
Profile6 = add_profile(Loops6)
Sketch6 = add_sketch(sketch_plane= SketchPlane6, profile= Profile6,
        sketch_position= [-0.75  , -0.    , -0.2308], sketch_size= 0.5769)
Extrude6 = add_extrude(sketch= Sketch6,
        operation= 0, type= 0, extent_one= -0.0462, extent_two= 0.)
SketchPlane7 = add_sketchplane(
        origin= [0., 0., 0.], normal= [ 0., -1.,  0.], x_axis= [ 1.,  0., -0.], y_axis= [0., 0., 1.])
Loops7 = []
Curves7_0 = []
Line7_0_0 = add_line(start= [128., 128.], end= [223., 128.])
Curves7_0.append(Line7_0_0)
Line7_0_1 = add_line(start= [223., 128.], end= [223.    , 159.6667])
Curves7_0.append(Line7_0_1)
Line7_0_2 = add_line(start= [223.    , 159.6667], end= [128.    , 159.6667])
Curves7_0.append(Line7_0_2)
Line7_0_3 = add_line(start= [128.    , 159.6667], end= [128., 128.])
Curves7_0.append(Line7_0_3)
Loop7_0 = add_loop(Curves7_0)
Loops7.append(Loop7_0)
Profile7 = add_profile(Loops7)
Sketch7 = add_sketch(sketch_plane= SketchPlane7, profile= Profile7,
        sketch_position= [-0.1731, -0.    ,  0.2308], sketch_size= 0.3462)
Extrude7 = add_extrude(sketch= Sketch7,
        operation= 1, type= 0, extent_one= -0.0462, extent_two= 0.)
SketchPlane8 = add_sketchplane(
        origin= [0., 0., 0.], normal= [ 0., -1.,  0.], x_axis= [ 1.,  0., -0.], y_axis= [0., 0., 1.])
Loops8 = []
Curves8_0 = []
Line8_0_0 = add_line(start= [128., 128.], end= [191.3333, 128.    ])
Curves8_0.append(Line8_0_0)
Arc8_0_1 = add_arc(start= [191.3333, 128.    ], end= [207.1667, 143.8333], mid= [202.5292, 132.6375])
Curves8_0.append(Arc8_0_1)
Line8_0_2 = add_line(start= [207.1667, 143.8333], end= [207.1667, 207.1667])
Curves8_0.append(Line8_0_2)
Arc8_0_3 = add_arc(start= [207.1667, 207.1667], end= [191.3333, 223.    ], mid= [202.5292, 218.3625])
Curves8_0.append(Arc8_0_3)
Line8_0_4 = add_line(start= [191.3333, 223.    ], end= [128., 223.])
Curves8_0.append(Line8_0_4)
Line8_0_5 = add_line(start= [128., 223.], end= [128.    , 207.1667])
Curves8_0.append(Line8_0_5)
Line8_0_6 = add_line(start= [128.    , 207.1667], end= [135.9167, 207.1667])
Curves8_0.append(Line8_0_6)
Line8_0_7 = add_line(start= [135.9167, 207.1667], end= [135.9167, 143.8333])
Curves8_0.append(Line8_0_7)
Line8_0_8 = add_line(start= [135.9167, 143.8333], end= [128.    , 143.8333])
Curves8_0.append(Line8_0_8)
Line8_0_9 = add_line(start= [128.    , 143.8333], end= [128., 128.])
Curves8_0.append(Line8_0_9)
Loop8_0 = add_loop(Curves8_0)
Loops8.append(Loop8_0)
Curves8_1 = []
Circle8_1_0 = add_circle(center= [183.4167, 175.5   ], radius= 8.0433)
Curves8_1.append(Circle8_1_0)
Loop8_1 = add_loop(Curves8_1)
Loops8.append(Loop8_1)
Profile8 = add_profile(Loops8)
Sketch8 = add_sketch(sketch_plane= SketchPlane8, profile= Profile8,
        sketch_position= [ 0.1731,  0.    , -0.3462], sketch_size= 0.6923)
Extrude8 = add_extrude(sketch= Sketch8,
        operation= 1, type= 0, extent_one= -0.0462, extent_two= 0.)