#!/bin/env python
"""Merge mutiple glTF 2.0 animations into one."""
import json
import sys

def merge(gltf):
    # Maps (node, path) to (input, output, interpolation)
    target_to_sampler = {}
    for animation in gltf.get('animations', []):
        for channel in animation['channels']:
            target_json = channel['target']
            if 'node' not in target_json:
                continue
            target = (target_json['node'], target_json['path'])
            if target in target_to_sampler:
                raise Exception("Can't merge; multiple channels have the same target")
            sampler_json = animation['samplers'][channel['sampler']]
            sampler = (
                sampler_json['input'],
                sampler_json['output'],
                sampler_json.get('interpolation', 'LINEAR')
            )
            target_to_sampler[target] = sampler

    channels = []
    samplers = []
    for i, (target, sampler) in enumerate(target_to_sampler.items()):
        new_channel = {
            'sampler': i,
            'target': {
                'node': target[0],
                'path': target[1]
            }
        }
        new_sampler = {
            'input': sampler[0],
            'output': sampler[1],
        }
        if sampler[2] != 'LINEAR':
            new_sampler['interpolation'] = sampler[2]
        channels.append(new_channel)
        samplers.append(new_sampler)

    animations = [{
        'channels': channels,
        'samplers': samplers
    }]
    gltf['animations'] = animations


def convert(infile, outfile):
    with open(infile, "rb") as f:
        gltf = json.load(f)
    merge(gltf)
    with open(outfile, "w+") as f:
        json.dump(gltf, f, indent=4)


convert(sys.argv[1], sys.argv[2])
