from .models import Hotspot

def resolve_hotspots(*_, interactive_part_id=None): # city=None
    print("interactive_part_id: " + str(interactive_part_id))
    if interactive_part_id:
        return Hotspot.objects.filter(interactive_part=interactive_part_id)
    return Hotspot.objects.all()

# def resolve_hotspots(*_, interactive_id=None): # city=None
#     print("interactive_id: " + str(interactive_id))
#     if interactive_id:
#         return Hotspot.objects.filter(interactive=interactive_id)
#     return Hotspot.objects.all()
