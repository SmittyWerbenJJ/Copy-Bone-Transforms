"""
serpens variables:
target_object
source_object
"""

if target_object is None or source_object is None:
    canRun=False
else: 
    canRun= target_object.type =="ARMATURE" and source_object.type=="ARMATURE"

row=self.layout.row()
row.enabled=canRun
row.operator("sna.add_copy_transforms_constraints_2f97b")
        