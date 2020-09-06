# groundwater potential zonation
 repository for GW potential zonation

Title: A comparative study of machine learning and MCDM Fuzzy-AHP technique to Groundwater potential mapping in the data-scarce region.

data guide:

Ahp_accu_check.csv ---   contains the true and predicted classes by weighted overlay analysis, 		    for accuracy assesment.

Data_unlabeled.csv ---- data for classification after modetraining.

Train_Data.csv---------- Data for training
		*Every row represents a features (cell 90m*90m).
		*Columns represents the different parameters as stated below.
	
		1. FID  	=  Feature ID (dtype= Int)
		2. Shape	=  Shape of the Feature.
		3. Join_count	=  value=1, represents that there is at least one 					parameter for the respected feature.
			 	  value=0, otherwise.
		4. Target_FID   =  geospatial ID of shape file.
		5. join_cou_1	=  value=0, for no well yield potential data.
			   value=1, otherwise.
		7. x		=  Easting of the centroid of respective cell.
		8. y		=  Northing of the centriod of respective cell.
		9. Aspect	=  Aspect of cell.
		10.DFR		=  Distance from River.
		11.DFF		=  Distance from fault.
		12.Altitude	=  Elevation of cells.
		13.Geomorph	=  Geomorphological category.
		14.Draw_D	=  GroundWater Fluctuation (premonsoon-						postmonsoon)
		15.Drain_D	=  Drainage Density (Km/sqKm)
		16.LS		=  LS- Factor
		17.Litho	=  Lithology Category.
		18.Lineam_D	=  Lineament density.
		19.MRVBF	=  Multi Resolution index of Valley Bottom Flatness.
		20.MRRTF	=  Multi Resolution Ridge Top Flatness.
		21.LULC		=  Land Use Land Cover Category.
		22.SCA		=  Specific Catchment Area.
		23.Profile_C	=  Profile Curveture
		24.Plan_C	=  Plan Curveture
		25.SPI		=  Specific Precipitation Index
		26.Slope	=  Slope of each feature.
		27.TWI		=  Topographic wetness index.
		28.TRI		=  Topographic Ruggedness index
		29.TPI		=  Topographic position Index.
		30.WellYield	=  wells potential yeilds in Lps. 0 value represent no data.( total 208 well data is available for training and testing)


Train_Data_agm.csv------ Augmented dataset with above mentioned parameters.

python Code for notebooks: (in .ipynb)(raw-- trained with 208 well data, agm -- trained with augmented dataset)

GWP_01_KNN_agm
GWP_01_KNN_raw
GWP_01_RandomForest_agm
GWP_01_RandomForest_raw
GWP_template
GWP01_RF_regressor
GWP01_SVM_agm
GWP01_SVM_raw
