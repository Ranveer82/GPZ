# groundwater potential zonation
 repository for GW potential zonation

Title: A comparative study of machine learning and MCDM Fuzzy-AHP technique to Groundwater potential mapping in the data-scarce region.

data guide:

Ahp_accu_check.csv ---   contains the true and predicted classes by weighted overlay analysis, 		    for accuracy assesment.

Data_unlabeled.csv ---- data for classification after modetraining.

Train_Data.csv---------- Data for training
		*Every row represents a features (cell 90m*90m).
		*Columns represents the different parameters as stated below.
	
		1. x		=  Easting of the centroid of respective cell.
		2. y		=  Northing of the centriod of respective cell.
		
		3.DFR		=  Distance from River.
		4.DFF		=  Distance from fault.
		5.Altitude	=  Elevation of cells.
		6.Geomorph	=  Geomorphological category.
		7.Draw_D	=  GroundWater Fluctuation (premonsoon-postmonsoon)
		8.Drain_D	=  Drainage Density (Km/sqKm)
		9.LS		=  LS- Factor
		10.Litho	=  Lithology Category.
		11.Lineam_D	=  Lineament density.
		12.MRVBF	=  Multi Resolution index of Valley Bottom Flatness.
		13.MRRTF	=  Multi Resolution Ridge Top Flatness.
		14.LULC		=  Land Use Land Cover Category.
		15.SCA		=  Specific Catchment Area.
		16.Profile_C	=  Profile Curveture
		17.Plan_C	=  Plan Curveture
		18.SPI		=  Specific Precipitation Index
		19.Slope	=  Slope of each feature.
		20.TWI		=  Topographic wetness index.
		21.TRI		=  Topographic Ruggedness index
		22.TPI		=  Topographic position Index.
		23.WellYield	=  wells potential yeilds in Lps. 0 value represent no data.( total 208 well data is available for training and testing)


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
