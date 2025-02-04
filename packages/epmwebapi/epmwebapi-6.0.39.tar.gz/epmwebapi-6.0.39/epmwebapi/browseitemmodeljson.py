﻿from epmwebapi.browsedirection import BrowseDirection


class BrowseItemModelJSON(object):
  
  def __init__(self, path, nodeClassMask, referenceTypes, browseDirection = BrowseDirection.Forward.value):
    self._path = path
    self._nodeClassMask = nodeClassMask
    self._referenceTypes = referenceTypes
    self._browseDirection = browseDirection

  def toDict(self):

    referenceTypes = []
    for item in self._referenceTypes:
        referenceTypes.append(item)

    return { 'path': self._path.toDict(), 
             'nodeClassMask': self._nodeClassMask, 
             'referenceTypes': referenceTypes,
             'direction': self._browseDirection}

