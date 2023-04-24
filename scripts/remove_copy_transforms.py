
"""
serpens variables

source_armature
target_armature
constraint_id
"""

if target_armature is not None and target_armature.type=="ARMATURE":
    for bone in target_armature.pose.bones:
        for constraint in bone.constraints:
            constraint.name="Copy Transforms "+constraint_id
            bone.constraints.remove(constraint)
            pass
   