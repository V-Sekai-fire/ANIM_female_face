[input gltf binary | hard code path] -> [check | blender| has one skeleton | has at least one animation]
[check] -> [merge all merges into one mesh| blender]
[merge all merges into one mesh| blender] -> [export fbx with zero animations and correct ?? scale | blender]
[export fbx with zero animations and correct ?? scale | blender] -> [dem bones]
[merge all merges into one mesh| blender] -> [export alembic animation at 60 fps | blender]
[export alembic animation at 60 fps | blender] -> [dem bones]
[dem bones] -> [fbx]
[fbx ] -> [gltf| blender]


