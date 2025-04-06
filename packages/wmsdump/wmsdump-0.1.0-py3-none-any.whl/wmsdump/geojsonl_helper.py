import json
import numpy as np
from geoindex_rs import rtree as rt
from shapely.geometry import shape

def fix_if_required(p):
    if p.is_valid:
        return p
    p = p.buffer(0)
    if not p.is_valid:
        print('found invalid polygon')
    return p

def get_shape(feat):
    geom = feat['geometry']
    s = shape(geom)
    s = fix_if_required(s)
    return s


class FileReader:
    def __init__(self, fname,
                 maintain_map=True,
                 use_offset=False,
                 filter_fn=lambda x:True,
                 index_val_fn=lambda x:x,
                 index_key_fn=lambda x:x):
        self.file = fname
        self.count = 0
        self.maintain_map = maintain_map
        self.use_offset = use_offset
        self.filter_fn = filter_fn
        self.index_key_fn = index_key_fn
        self.index_val_fn = index_val_fn
        self.idx_map = {}
        self.tree = None

    def iter_features(self, f):
        while True:
            line = f.readline()
            if line == '':
                break
            feat = json.loads(line)
            if self.filter_fn(feat):
                yield feat, f.tell()

    def iter_for_idx(self):
        with open(self.file, 'r') as f:
            if self.maintain_map and self.use_offset:
                self.idx_map[self.count] = 0

            for feat, pos in self.iter_features(f):

                self.count += 1
                if not self.maintain_map:
                    yield feat

                if self.use_offset:
                    self.idx_map[self.count] = pos
                else:
                    self.idx_map[self.count - 1] = self.index_val_fn(feat)
                yield feat

    def __iter__(self):
        with open(self.file, 'r') as f:
            for feat, _ in self.iter_features(f):
                yield feat

    def populate_spatial_index(self):
        xmin = []
        ymin = []
        xmax = []
        ymax = []
        for feat in self.iter_for_idx():
            s = get_shape(feat)
            b = s.bounds
            xmin.append(b[0])
            ymin.append(b[1])
            xmax.append(b[2])
            ymax.append(b[3])
        
        xmin = np.array(xmin, dtype=np.float32)
        ymin = np.array(ymin, dtype=np.float32)
        xmax = np.array(xmax, dtype=np.float32)
        ymax = np.array(ymax, dtype=np.float32)
        
        builder = rt.RTreeBuilder(num_items=len(xmin))
        builder.add(xmin, ymin, xmax, ymax)
        tree = builder.finish()
        self.tree = tree

    def get_intersecting_feats(self, s):
        if self.tree is None:
            raise Exception('index not built')

        b = s.bounds
        results = rt.search(self.tree, *b)
        results = results.to_pylist()
        out = []
        for i in results:
            feat = self.get(i)
            c = get_shape(feat)
            if c.intersects(s):
                out.append(feat)
        return out

    def get(self, n, *args):
        if n >= self.count:
            return None

        if not self.maintain_map:
            return None

        key = self.index_key_fn(n, *args)
        if not self.use_offset:
            return self.idx_map[key]

        with open(self.file, 'r') as f:
            f.seek(self.idx_map[n])
            line = f.readline()
            feat = json.loads(line)
            return feat


