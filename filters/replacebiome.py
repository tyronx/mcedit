#  ReplaceBiome Filter by TyronX, based on SethBling's SetBiome Filter
# Directions: Just select a region and use this filter, it will apply the
# biome to all columns within the selected region. It can be used on regions
# of any size, they need not correspond to chunks.
#
# If you modify and redistribute this code, please credit SethBling

from pymclevel import MCSchematic
from pymclevel import TAG_Compound
from pymclevel import TAG_Short
from pymclevel import TAG_Byte
from pymclevel import TAG_Byte_Array
from pymclevel import TAG_String
from numpy import zeros

inputs = (
    ("Search for Biome", (
        "Beach",
        "Birch Forest",
        "Birch Forest Hills",
        "Birch Forest Hills M",
        "Birch Forest M",
        "Cold Beach",
        "Cold Taiga",
        "Cold Taiga Hills",
        "Cold Taiga M",
        "Deep Ocean",
        "Desert",
        "Desert M",
        "Desert Hills",
        "Extreme Hills",
        "Extreme Hills Edge",
        "Extreme Hills M",
        "Extreme Hills+",
        "Extreme Hills+ M",
        "Flower Forest",
        "Forest",
        "ForestHills",
        "FrozenOcean",
        "FrozenRiver",
        "Ice Mountains",
        "Ice Plains",
        "Ice Plains Spikes",
        "Jungle",
        "Jungle M",
        "Jungle Edge",
        "Jungle Edge M",
        "Jungle Hills",
        "Mega Spruce Taiga",
        "Mega Spruce Taiga Hills",
        "Mega Taiga",
        "Mega Taiga Hills",
        "Mesa",
        "Mesa (Bryce)",
        "Mesa Plateau",
        "Mesa Plateau F",
        "Mesa Plateau F M",
        "Mesa Plateau M",
        "Mushroom Island",
        "Mushroom Island Shore",
        "Nether",
        "Ocean",
        "Plains",
        "River",
        "Roofed Forest",
        "Roofed Forest M",
        "Savanna",
        "Savanna M",
        "Savanna Plateau",
        "Savanna Plateau M",
        "Stone Beach",
        "Sunflower Plains",
        "Swampland",
        "Swampland M",
        "Taiga",
        "Taiga M",
        "Taiga Hills",
        "End"
    )),
    ("Replace with", (
        "Beach",
        "Birch Forest",
        "Birch Forest Hills",
        "Birch Forest Hills M",
        "Birch Forest M",
        "Cold Beach",
        "Cold Taiga",
        "Cold Taiga Hills",
        "Cold Taiga M",
        "Deep Ocean",
        "Desert",
        "Desert M",
        "Desert Hills",
        "Extreme Hills",
        "Extreme Hills Edge",
        "Extreme Hills M",
        "Extreme Hills+",
        "Extreme Hills+ M",
        "Flower Forest",
        "Forest",
        "ForestHills",
        "FrozenOcean",
        "FrozenRiver",
        "Ice Mountains",
        "Ice Plains",
        "Ice Plains Spikes",
        "Jungle",
        "Jungle M",
        "Jungle Edge",
        "Jungle Edge M",
        "Jungle Hills",
        "Mega Spruce Taiga",
        "Mega Spruce Taiga Hills",
        "Mega Taiga",
        "Mega Taiga Hills",
        "Mesa",
        "Mesa (Bryce)",
        "Mesa Plateau",
        "Mesa Plateau F",
        "Mesa Plateau F M",
        "Mesa Plateau M",
        "Mushroom Island",
        "Mushroom Island Shore",
        "Nether",
        "Ocean",
        "Plains",
        "River",
        "Roofed Forest",
        "Roofed Forest M",
        "Savanna",
        "Savanna M",
        "Savanna Plateau",
        "Savanna Plateau M",
        "Stone Beach",
        "Sunflower Plains",
        "Swampland",
        "Swampland M",
        "Taiga",
        "Taiga M",
        "Taiga Hills",
        "End"
    )),
)

biomeids = {
    "Ocean":0,
    "Plains":1,
    "Desert":2,
    "Extreme Hills":3,
    "Forest":4,
    "Taiga":5,
    "Swampland":6,
    "River":7,
    "Nether":8,
    "End":9,
    "Frozen Ocean":10,
    "Frozen River":11,
    "Ice Plains":12,
    "Ice Mountains":13,
    "Mushroom Island":14,
    "Mushroom Island Shore":15,
    "Beach":16,
    "Desert Hills":17,
    "Forest Hills":18,
    "Taiga Hills":19,
    "Extreme Hills Edge":20,
    "Jungle":21,
    "Jungle Hills":22,
    "Jungle Edge":23,
    "Deep Ocean":24,
    "Stone Beach":25,
    "Cold Beach":26,
    "Birch Forest":27,
    "Birch Forest Hills":28,
    "Roofed Forest":29,
    "Cold Taiga":30,
    "Cold Taiga Hills":31,
    "Mega Taiga":32,
    "Mega Taiga Hills":33,
    "Extreme Hills+":34,
    "Savanna":35,
    "Savanna Plateau":36,
    "Mesa":37,
    "Mesa Plateau F":38,
    "Mesa Plateau":39,
    "Sunflower Plains":129,
    "Desert M":130,
    "Extreme Hills M":131,
    "Flower Forest":132,
    "Taiga M":133,
    "Swampland M":134,
    "Ice Plains Spikes":140,
    "Jungle M":149,
    "JungleEdge M":151,
    "Birch Forest M":155,
    "Birch Forest Hills M":156,
    "Roofed Forest M":157,
    "Cold Taiga M":158,
    "Mega Spruce Taiga":160,
    "Mega Spruce Taiga Hills":161,
    "Extreme Hills+ M":162,
    "Savanna M":163,
    "Savanna Plateau M":164,
    "Mesa (Bryce)":165,
    "Mesa Plateau F M":166,
    "Mesa Plateau M":167,
}

def perform(level, box, options):
    searchbiome = biomeids[options["Search for Biome"]]
    replacebiome = biomeids[options["Replace with"]]

    minx = int(box.minx/16)*16
    minz = int(box.minz/16)*16

    for x in xrange(minx, box.maxx, 16):
        for z in xrange(minz, box.maxz, 16):
            chunk = level.getChunk(x / 16, z / 16)
            #chunk.decompress()
            chunk.dirty = True
            biomearray = chunk.root_tag["Level"]["Biomes"].value

            chunkx = int(x/16)*16
            chunkz = int(z/16)*16

            for bx in xrange(max(box.minx, chunkx), min(box.maxx, chunkx+16)):
                for bz in xrange(max(box.minz, chunkz), min(box.maxz, chunkz+16)):
                    idx = 16*(bz-chunkz)+(bx-chunkx)
                    if biomearray[idx] == searchbiome:
                        biomearray[idx] = replacebiome

            chunk.root_tag["Level"]["Biomes"].value = biomearray
