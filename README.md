# Kraut Salad
Proof of concept implementation of a cyber threat intelligence and incident handling platform

## Current Status
Currently, the basic database design is complete and a first parser for MITRE' [stix](https://stix.mitre.org) and [cybox](https://cybox.mitre.org) cyber threat intelligence exchange formats is written. Kraut Salad is supposed to be a proof of concept implementation to determine if a relational database model is feasible or not. Therefore, Kraut Salad only implements a subset of the MITRE standard and still requires some cybox objects to be implemented.

We also test the [django REST framework](http://www.django-rest-framework.org) to see if the capabilities suffice our needs. So far there is no graphical interface or website implemented, thus only the import of stix XML works at the moment.

## Requirements
Please refer to requirements.txt for an updated list of required packages.

## Test Documents
Kraut Salad has been tested with:
* Mandiant APT1 Report
* FireEye Poison Ivy Report

Both available at https://stix.mitre.org/language/version1.0.1/samples.html

## Usage
To load a stix documents into the database either point at a particular file directly or just at the directory containing several documents:

```python
python manage.py load_stix report.xml
```

The output will be something like this
```
--> performing version check ... found 1.1.1 ... [DONE]
--> extracting stix package information ... [DONE]
--> extracting observable information ... [DONE]
------
Missing references for: object_2_object
namespace:File-01d04d81-697c-489c-8340-e1b93332b87c -> {'id': u'namespace:HTTPSession-9765c645-8cdd-43e2-9df3-af6a66eb97ba', 'relationship': u'Connected_To'} 
------
Missing stix elements:
Missing stix element implementation: timestamp
------
Missing Object Types:
Missing object type implementation: HTTPSessionObjectType
Missing object type implementation: WindowsExecutableFileObjectType
------
```

The Kraut parser will tell you about missing object references, stix elements, and cybox objects at the end of the run.


## Roadmap
The following items describe what is still planned but has no particular order:

* add more cybox objects (e.g. ProcessObject, HTTPSessionObject, ...)
* add support for IOC format
* create a webinterface to browse and modify threat intelligence data
* create an interface to neo4js graph database
* create a webinterface to track and handle incidents
* associate threat intelligence data with assets detected during an incident
