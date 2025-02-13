# -*- coding: utf-8 -*-
import heimdall
from heimdall.decorators import create_database
from rdflib import Graph, Literal, URIRef
from urllib.parse import quote_plus


@create_database([
    'rdf:hext',
    'rdf:json-ld',
    'rdf:nt',
    'rdf:pretty-xml',
    'rdf:trig',
    'rdf:turtle',
    ])
def createDatabase(tree, url, **options):
    r"""Serializes a HERA elements tree into an RDF file

    :param tree: (:py:class:`xml.etree.ElementTree.Element`) HERA elements tree
    :param url: (:py:class:`str`) Path of the file to create
    :param format: (:py:class:`str`, default: ``rdf:turtle``) One of the following: ``rdf:turtle``, ``rdf:nt``, ``rdf:pretty-xml``, ``rdf:trig``, ``rdf:json-ld``, ``rdf:hext``
    :return: None
    :rtype: :py:class:`NoneType`

    Usage example: ::
      >>> import heimdall
      >>> tree = heimdall.getDatabase(...)
      >>> # ... do stuff ...
      >>> heimdall.createDatabase(tree, format='rdf:turtle', url='output.xml')
    """  # nopep8: E501
    g = tree2graph(tree)
    format = options.get('format', 'rdf:turtle')[len('rdf:'):]
    with open(url, 'w') as f:
        # NOTE: g.serialize is /not/ idempotent !
        #       even if data is the same, specific file content can change
        f.write(g.serialize(format=format))


def tree2graph(tree):
    graph = Graph()
    for item in heimdall.getItems(tree):
        try:
            node = item2uri(item)
        except KeyError:
            continue  # no equivalent URI: we can't do anything with this item
        entity = _get_entity(tree, item)
        for metadata in heimdall.getMetadata(item):
            triples = metadata2triples(tree, entity, node, metadata)
            for triple in triples:
                graph.add(triple)
    return graph


def _get_entity(tree, item):
    """Retieve ``item``'s entity, if any"""
    eid = item.attrib.get('eid', None)
    if eid is None:
        return None
    return heimdall.getEntity(tree, lambda e: e.get('id', None) == eid)


def item2uri(item, url_prefix='http://example.org'):
    value = heimdall.getValue(item, pid='uri')
    if value is not None:
        return URIRef(value)
    value = heimdall.getValue(item, pid='id')
    if value is not None:
        return URIRef(f'{url_prefix}/{value}')
    raise KeyError("No equivalent URI found in item")


def metadata2triples(tree, entity, node, metadata):
    uris = list()
    if entity is not None:
        aid = metadata.attrib.get('aid', None)
        if aid is not None:
            a = heimdall.getAttribute(
                    entity,
                    lambda a: a.attrib.get('id', None) == aid
                    )
            uris = a.uri
    if len(uris) < 1:
        pid = metadata.attrib.get('pid', None)
        if pid is not None:
            p = heimdall.getProperty(
                    tree,
                    lambda p: p.attrib.get('id', None) == pid
                    )
            uris = p.uri

    triples = list()
    for uri in uris:
        triples.append((node, URIRef(uri), Literal(metadata.text)))
    return triples


__version__ = '1.0.0'
__all__ = ['createDatabase', '__version__']
