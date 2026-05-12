import arcpy
import sys

# -------------------------------------------------------------------------------
# Project: CA Stream Flow Compliance Tool
# Description: Automates the identification of Water Right Points of Diversion (POD)
#              located within Fully Appropriated Stream Systems (FASS).
# Developer: Reetu Sharma, PhD - Senior Chemist & Data Scientist
# -------------------------------------------------------------------------------

def run_compliance_check(pod_layer, fass_layer, output_gdb):
    try:
        arcpy.env.overwriteOutput = True
        arcpy.AddMessage("Initiating Spatial Analysis for Water Rights Compliance...")

        # 1. Spatial Join: Identify PODs located within restricted stream boundaries
        # Target: PODs, Join: FASS Streams
        temp_join = f"{output_gdb}\\POD_FASS_SpatialJoin"
        arcpy.analysis.SpatialJoin(pod_layer, fass_layer, temp_join, "JOIN_ONE_TO_ONE", "KEEP_COMMON", match_option="COMPLETELY_WITHIN")

        # 2. Data Science Logic: Filter for 'Fully Appropriated' status in Summer seasons
        # This demonstrates handling of regulatory 'seasonality' constraints
        compliance_query = "FASS_STATUS = 'Fully Appropriated' AND RESTRICT_SEASON = 'Summer'"
        
        output_alerts = f"{output_gdb}\\Compliance_Alerts_Summer_2026"
        arcpy.analysis.Select(temp_join, output_alerts, compliance_query)

        # 3. Summary Statistics for Reporting
        match_count = int(arcpy.management.GetCount(output_alerts)[0])
        
        if match_count > 0:
            arcpy.AddWarning(f"ALERT: {match_count} diversion points flagged for potential non-compliance.")
        else:
            arcpy.AddMessage("SUCCESS: All diversion points are in compliance with current FASS status.")

    except arcpy.ExecuteError:
        arcpy.AddError(arcpy.GetMessages(2))
    except Exception as e:
        arcpy.AddError(str(e))

if __name__ == "__main__":
    # Define paths (In a real scenario, these would be your local or SDE paths)
    # These match the eWRIMS and FASS datasets from the CA State Water Board
    POD_DATA = "Water_Rights_Points_of_Diversion"
    FASS_DATA = "Fully_Appropriated_Stream_Systems"
    WORKSPACE = arcpy.env.scratchGDB 

    run_compliance_check(POD_DATA, FASS_DATA, WORKSPACE)
