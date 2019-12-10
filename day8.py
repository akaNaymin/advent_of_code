
def sif_to_layers(sif, width, height):
    layer_ranges = list(range(0, len(sif), width*height)) + [len(sif)]
    layers = []
    for i, r in enumerate(layer_ranges[:-1]):
        layer = sif[r:layer_ranges[i+1]]
        layer = [int(p) for p in layer]
        layers.append(layer)
    return layers

with open('inputs/day8.sif') as f:
    sif = f.read()

img = sif_to_layers(sif, 25, 6)
print(len(img))

def count_occ(layers):
    min_count = len(layers[0])
    min_layer = layers[0]
    for layer in layers:
        count = layer.count(0)
        if count < min_count:
            min_count = count
            min_layer = layer
    count_1 = min_layer.count(1)
    count_2 = min_layer.count(2)
    return(count_1 * count_2)

print(count_occ(img))

def print_sif(layers, width):
    final_image = [2] * len(layers[0])
    for layer in layers:
        for i in range(len(final_image)):
            if final_image[i] == 2 and layer[i] != 2:
                final_image[i] = layer[i]

    layer_ranges = list(range(0, len(final_image), width)) + [len(final_image)]
    for i, r in enumerate(layer_ranges[:-1]):
        row = final_image[r:layer_ranges[i+1]]
        row = [(' ','X')[h] for h in row]
        print(''.join(row))

print_sif(img, 25)