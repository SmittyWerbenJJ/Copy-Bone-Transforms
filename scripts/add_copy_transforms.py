
"""
serpens variables

source_armature
target_armature
constraint_id
"""
bones_to_add_modifiers=[]
cpt_constraint_name="Copy Transforms "+ constraint_id
target_names=[bone.name for bone in target_armature.pose.bones]
for bone in source_armature.pose.bones:
    if bone.name not in target_names:
        continue
    add_constraint=True
    for constraint in target_armature.pose.bones[bone.name].constraints:
        if constraint.name in cpt_constraint_name :
            add_constraint=False
          
    if add_constraint:
        bones_to_add_modifiers.append(target_armature.pose.bones[bone.name])
       
for bone in bones_to_add_modifiers:
    constraint=bone.constraints.new(type='COPY_TRANSFORMS')
    constraint.name=cpt_constraint_name
    constraint.target=bpy.data.objects[source_armature.name]
    constraint.subtarget=bone.name
