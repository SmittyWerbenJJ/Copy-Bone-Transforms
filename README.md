# Copy-Bone-Transforms
A blender plugin to copy bone transforms of one armature to another armature having same bone names.

## Installation
- Download the latest plugin from the releases.
- In Blender, go to Edit > Preferences > Add-ons.
- Click Install and select the downloaded zip file.
- Check the box next to "Copy Bone Transforms Plugin" to enable the plugin.

## Usage:
- Open a Blender project containing two armatures with bones having the same name.
- Go to the "3D View" workspace.
- Press N to open the Sidebar panel.
-  Scroll down to the "Rigging" tab and expand it.
- Selec the Source Armature-Object (The Armature that we want to copy the transforms **from**) 
- Selec the Target Armature-Object (The Armature that we want to copy the transforms **to**) 
- Click on "Add Copy Transform Constraints" to copy the bone transforms from the source armature to the target armature.- 
- Click on "Remove Copy Transform Constraints" to remove the Copy Transform constraints that were created using the addon

## Demo:
![blender_Zc6ZihkpUH](https://user-images.githubusercontent.com/35438764/233882878-6a465463-29c2-46b4-91a2-310982c2c8b2.gif)

# Note:
    Source and Target must be Armatures,otherwise the tool will not work
    Both Armatures must have the same bone names.
    If the addon does not show up, read the Installation instruction.

